<template>
  <div
    class="rounded-2xl border border-gray-200 bg-white p-6 dark:border-gray-800 dark:bg-gray-900"
  >
    <p class="mt-2 mb-8 text-sm text-gray-500">
      Modifiez votre mot de passe pour sécuriser votre compte.
    </p>

    <form @submit.prevent="saveProfile">
      <div class="grid grid-cols-1 gap-6 lg:grid-cols-2">
        <div>
          <label class="mb-2 block text-sm font-medium"> Nom d'utilisateur </label>

          <input
            :value="securityForm.username"
            disabled
            class="h-11 w-full rounded-lg border border-gray-300 bg-gray-100 px-4 text-gray-500 cursor-not-allowed dark:bg-gray-800 dark:border-gray-700"
          />

          <p class="mt-2 text-xs text-gray-500">
            Ce nom d'utilisateur est fixe et ne peut pas être modifié.
          </p>
        </div>

        <div>
          <label class="mb-2 block text-sm font-medium">
            Mot de passe actuel <span class="text-red-500">*</span>
          </label>

          <input
            type="password"
            v-model="securityForm.current_password"
            class="w-full rounded-lg border px-4 h-11"
          />
        </div>

        <div>
          <label class="mb-2 block text-sm font-medium">
            Nouveau mot de passe <span class="text-red-500">*</span>
          </label>

          <input
            type="password"
            v-model="securityForm.new_password"
            @input="validateField('new_password')"
            class="w-full rounded-lg border px-4 h-11"
            :class="{ 'border-red-500': errors.new_password }"
          />
          <p v-if="errors.new_password" class="text-red-500 text-xs mt-1">
            {{ errors.new_password }}
          </p>
        </div>
        <div>
          <label class="mb-2 block text-sm font-medium">
            Confirmer le mot de passe <span class="text-red-500">*</span>
          </label>

          <input
            type="password"
            v-model="securityForm.confirm_password"
            @input="validateField('confirm_password')"
            class="w-full rounded-lg border px-4 h-11"
            :class="{ 'border-red-500': errors.confirm_password }"
          />
          <p v-if="errors.confirm_password" class="text-red-500 text-xs mt-1">
            {{ errors.confirm_password }}
          </p>
        </div>
      </div>

      <div class="mt-8 flex justify-end">
        <button
          type="submit"
          class="rounded-lg bg-brand-500 px-6 py-3 text-white hover:bg-brand-600"
        >
          Enregistrer
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { updateAccountSecurity } from '@/api/accountService'
import { getDoctorProfile } from '@/api/doctorService'
import Swal from 'sweetalert2'

const errors = ref({
  current_password: '',
  new_password: '',
  confirm_password: '',
})

const validateField = (field) => {
  errors.value[field] = ''

  if (
    field === 'new_password' &&
    securityForm.value.new_password &&
    securityForm.value.new_password.length < 8
  ) {
    errors.value.new_password = 'Minimum 8 caractères requis'
  }

  if (
    field === 'confirm_password' &&
    securityForm.value.confirm_password &&
    securityForm.value.confirm_password !== securityForm.value.new_password
  ) {
    errors.value.confirm_password = 'Les mots de passe ne correspondent pas'
  }
}
const doctor = ref({})
const securityForm = ref({
  username: '',
  current_password: '',
  new_password: '',
  confirm_password: '',
})

onMounted(async () => {
  try {
    doctor.value = await getDoctorProfile()
    securityForm.value.username = localStorage.getItem('username') || doctor.value.username || ''
  } catch (e) {
    console.error('Erreur chargement profil:', e)
  }
})

const saveProfile = async () => {
  const form = securityForm.value

  // Username obligatoire
  if (!form.username.trim()) {
    return Swal.fire({
      icon: 'warning',
      title: "Nom d'utilisateur obligatoire",
    })
  }

  // Mot de passe actuel obligatoire
  if (!form.current_password.trim()) {
    return Swal.fire({
      icon: 'warning',
      title: 'Veuillez entrer votre mot de passe actuel',
    })
  }

  // Si l'utilisateur veut changer le mot de passe
  if (form.new_password || form.confirm_password) {
    if (form.new_password.length < 8) {
      return Swal.fire({
        icon: 'warning',
        title: 'Mot de passe trop court',
        text: 'Minimum 8 caractères requis',
      })
    }

    if (form.new_password !== form.confirm_password) {
      return Swal.fire({
        icon: 'error',
        title: 'Confirmation incorrecte',
        text: 'Les deux mots de passe doivent être identiques',
      })
    }

    if (form.new_password === form.current_password) {
      return Swal.fire({
        icon: 'warning',
        title: 'Mot de passe identique',
        text: "Le nouveau mot de passe doit être différent de l'ancien",
      })
    }
  }

  // Confirmation avant sauvegarde
  const confirm = await Swal.fire({
    title: "Confirmer l'enregistrement ?",
    text: 'Les modifications de sécurité seront appliquées.',
    icon: 'question',
    showCancelButton: true,
    confirmButtonText: 'Oui, enregistrer',
    cancelButtonText: 'Annuler',
  })

  if (!confirm.isConfirmed) {
    return
  }

  try {
    const response = await updateAccountSecurity(form)

    Swal.fire({
      icon: 'success',
      title: 'Succès',
      text: response.message,
      timer: 1800,
      showConfirmButton: false,
    })

    // vider les champs password après succès
    securityForm.value.current_password = ''
    securityForm.value.new_password = ''
    securityForm.value.confirm_password = ''
  } catch (e) {
    console.log('ERROR:', e.response?.data)

    let message = 'Une erreur est survenue'

    if (e.response?.data?.current_password) {
      message = e.response.data.current_password[0]
    } else if (e.response?.data?.confirm_password) {
      message = e.response.data.confirm_password
    } else if (e.response?.data?.detail) {
      message = e.response.data.detail
    }

    Swal.fire({
      icon: 'error',
      title: 'Erreur',
      text: message,
    })
  }
}
</script>
