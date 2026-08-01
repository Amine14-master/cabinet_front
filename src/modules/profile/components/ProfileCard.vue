<template>
  <div>
    <div class="p-5 mb-6 border border-gray-200 rounded-2xl dark:border-gray-800 lg:p-6">
      <div class="flex flex-col gap-5 xl:flex-row xl:items-center xl:justify-between">
        <div class="flex flex-col items-center w-full gap-6 xl:flex-row">
        <div class="relative w-20 h-20 overflow-hidden rounded-full border border-gray-200 dark:border-gray-800">
          <img
            :src="previewPhoto || doctor.photo || '/images/user/owner.jpg'"
            class="w-full h-full object-cover"
          />

     
        </div>
           <!-- Infos principales -->
          <div class="order-3 xl:order-2">
            <h4 class="mb-2 text-lg font-semibold text-center text-gray-800 dark:text-white/90 xl:text-left">
            Dr. {{ doctor?.first_name }} {{ doctor?.last_name }}
            </h4>
            <div class="flex flex-col items-center gap-1 text-center xl:flex-row xl:gap-3 xl:text-left">
              <p class="text-sm text-gray-500 dark:text-gray-400">{{ doctor.speciality?.name }}</p>
              <div class="hidden h-3.5 w-px bg-gray-300 dark:bg-gray-700 xl:block"></div>
              <p class="text-sm text-gray-500 dark:text-gray-400">{{ doctor?.cabinet?.wilaya }}</p>
            </div>
          </div>
          <div class="flex items-center order-2 gap-2 grow xl:order-3 xl:justify-end">
         
          <button
          class="edit-button"
          @click="isProfilePhotoModal = true"
        >
          <svg
            class="fill-current"
            width="18"
            height="18"
            viewBox="0 0 18 18"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              clip-rule="evenodd"
              d="M15.0911 2.78206C14.2125 1.90338 12.7878 1.90338 11.9092 2.78206L4.57524 10.116C4.26682 10.4244 4.0547 10.8158 3.96468 11.2426L3.31231 14.3352C3.25997 14.5833 3.33653 14.841 3.51583 15.0203C3.69512 15.1996 3.95286 15.2761 4.20096 15.2238L7.29355 14.5714C7.72031 14.4814 8.11172 14.2693 8.42013 13.9609L15.7541 6.62695C16.6327 5.74827 16.6327 4.32365 15.7541 3.44497L15.0911 2.78206ZM12.9698 3.84272C13.2627 3.54982 13.7376 3.54982 14.0305 3.84272L14.6934 4.50563C14.9863 4.79852 14.9863 5.2734 14.6934 5.56629L14.044 6.21573L12.3204 4.49215L12.9698 3.84272ZM11.2597 5.55281L5.6359 11.1766C5.53309 11.2794 5.46238 11.4099 5.43238 11.5522L5.01758 13.5185L6.98394 13.1037C7.1262 13.0737 7.25666 13.003 7.35947 12.9002L12.9833 7.27639L11.2597 5.55281Z"
              fill=""
            />
          </svg>
          Modifier
        </button>

          </div>
        </div>


      </div>
              <Modal
          v-if="isProfilePhotoModal"
          @close="isProfilePhotoModal = false"
        >
          <template #body>
            <div class="relative w-full max-w-md rounded-3xl bg-white p-6 dark:bg-gray-900">

              <button
                @click="isProfilePhotoModal = false"
                class="absolute right-5 top-5"
              >
                ✕
              </button>

              <h4 class="mb-6 text-xl font-semibold">
                Modifier la photo de profil
              </h4>

              <div class="flex flex-col items-center">

                <img
                  :src="previewPhoto || doctor.photo || '/images/user/owner.jpg'"
                  class="mb-5 h-36 w-36 rounded-full object-cover border"
                />

                <input
                  ref="photoInput"
                  type="file"
                  class="hidden"
                  accept="image/*"
                  @change="onSelectPhoto"
                />

                <button
                  type="button"
                  class="mb-6 rounded-lg border px-4 py-2"
                  @click="photoInput.click()"
                >
                  Choisir une photo
                </button>

                <div class="flex gap-3">
                  <button
                    type="button"
                    class="rounded-lg border px-4 py-2"
                    @click="isProfilePhotoModal = false"
                  >
                    Annuler
                  </button>

                  <button
                    type="button"
                    class="rounded-lg bg-brand-500 px-4 py-2 text-white"
                    @click="savePhoto"
                  >
                    Enregistrer
                  </button>
                </div>

              </div>

            </div>
          </template>
        </Modal>
    </div>

  </div>
</template>

<script setup>
import { ref } from "vue"
import Swal from "sweetalert2"
import { updateDoctorProfile } from "@/api/doctorService"
import Modal from "./Modal.vue" // Assure-toi que le composant Modal est importé

const props = defineProps({
  doctor: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['update:doctor'])

// Variables pour le modal photo
const isProfilePhotoModal = ref(false)
const photoInput = ref(null)
const selectedPhoto = ref(null)
const previewPhoto = ref(null)



const onSelectPhoto = (event) => {
  const file = event.target.files[0]
  if (!file) return
  selectedPhoto.value = file
  previewPhoto.value = URL.createObjectURL(file)
}

const savePhoto = async () => {
  if (!selectedPhoto.value) {
    return Swal.fire({
      icon: "warning",
      title: "Attention",
      text: "Veuillez choisir une photo."
    })
  }

  try {
    const response = await updateDoctorProfile({
      photo: selectedPhoto.value
    })

    props.doctor.photo = response.photo

    Swal.fire({
      icon: "success",
      title: "Succès",
      text: "Photo mise à jour.",
      timer: 1500,
      showConfirmButton: false
    })

    isProfilePhotoModal.value = false
    selectedPhoto.value = null
    previewPhoto.value = null

  } catch (e) {
    console.error(e)

    Swal.fire({
      icon: "error",
      title: "Erreur",
      text: "Impossible de mettre à jour la photo."
    })
  }
}
</script>