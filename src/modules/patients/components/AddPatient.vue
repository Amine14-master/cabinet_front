<template>
  <div class="space-y-4">
    <div
      class="overflow-hidden rounded-xl border border-gray-200 bg-white dark:border-gray-800 dark:bg-white/[0.03]"
    >
      <div class="max-w-full overflow-x-auto custom-scrollbar">
        <form @submit.prevent="handleFormSubmit" class="grid grid-cols-1 gap-6 p-4">
          <!-- Card 1: Informations Personnelles (Inchangé) -->
          <div
            class="bg-white dark:bg-white/[0.03] rounded-3xl border border-gray-100 dark:border-gray-800 p-8 shadow-sm"
          >
            <div class="flex items-center gap-3 mb-6">
              <div
                class="w-10 h-10 rounded-xl bg-blue-50 dark:bg-blue-500/10 flex items-center justify-center text-blue-600"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-6 w-6"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                  />
                </svg>
              </div>
              <h2 class="text-lg font-bold dark:text-white">Informations Personnelles</h2>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div class="space-y-2">
                <label class="text-xs font-bold text-gray-400 uppercase ml-1">Prénom</label>
                <input
                  v-model="formData.first_name"
                  type="text"
                  required
                  class="w-full px-4 py-3.5 rounded-2xl border border-gray-200 dark:border-gray-700 dark:bg-gray-900 focus:ring-2 focus:ring-blue-500 outline-none dark:text-white"
                  placeholder="Prénom"
                />
              </div>
              <div class="space-y-2">
                <label class="text-xs font-bold text-gray-400 uppercase ml-1">Nom</label>
                <input
                  v-model="formData.last_name"
                  type="text"
                  required
                  class="w-full px-4 py-3.5 rounded-2xl border border-gray-200 dark:border-gray-700 dark:bg-gray-900 focus:ring-2 focus:ring-blue-500 outline-none dark:text-white"
                  placeholder="Nom"
                />
              </div>
              <div class="space-y-2">
                <label class="text-xs font-bold text-gray-400 uppercase ml-1"
                  >Date de naissance</label
                >
                <input
                  v-model="formData.date_of_birth"
                  type="date"
                  required
                  class="w-full px-4 py-3.5 rounded-2xl border border-gray-200 dark:border-gray-700 dark:bg-gray-900 focus:ring-2 focus:ring-blue-500 outline-none dark:text-white"
                />
              </div>
              <div class="space-y-2">
                <label class="text-xs font-bold text-gray-400 uppercase ml-1">Genre</label>
                <select
                  v-model="formData.gender"
                  class="w-full px-4 py-3.5 rounded-2xl border border-gray-200 dark:border-gray-700 dark:bg-gray-900 focus:ring-2 focus:ring-blue-500 outline-none dark:text-white"
                >
                  <option value="M">Homme</option>
                  <option value="F">Femme</option>
                </select>
              </div>
            </div>
          </div>

          <!-- Card 2: Contact (Simplifié) -->
          <div
            class="bg-white dark:bg-white/[0.03] rounded-3xl border border-gray-100 dark:border-gray-800 p-8 shadow-sm"
          >
            <div class="flex items-center gap-3 mb-6">
              <div
                class="w-10 h-10 rounded-xl bg-pink-50 dark:bg-pink-500/10 flex items-center justify-center text-pink-600"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-6 w-6"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"
                  />
                </svg>
              </div>
              <h2 class="text-lg font-bold dark:text-white">Contact & Groupe Sanguin</h2>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
              <div class="space-y-2">
                <label class="text-xs font-bold text-gray-400 uppercase ml-1">Téléphone</label>
                <input
                  v-model="formData.phone"
                  type="tel"
                  required
                  class="w-full px-4 py-3.5 rounded-2xl border border-gray-200 dark:border-gray-700 dark:bg-gray-900 focus:ring-2 focus:ring-blue-500 outline-none dark:text-white"
                  placeholder="05/06/07..."
                />
              </div>
              <div class="space-y-2">
                <label class="text-xs font-bold text-gray-400 uppercase ml-1">Email</label>
                <input
                  v-model="formData.email"
                  type="email"
                  class="w-full px-4 py-3.5 rounded-2xl border border-gray-200 dark:border-gray-700 dark:bg-gray-900 focus:ring-2 focus:ring-blue-500 outline-none dark:text-white"
                  placeholder="email@exemple.com"
                />
              </div>
              <div class="space-y-2">
                <label class="text-xs font-bold text-gray-400 uppercase ml-1">Groupe Sanguin</label>
                <select
                  v-model="formData.blood_group"
                  class="w-full px-4 py-3.5 rounded-2xl border border-gray-200 dark:border-gray-700 dark:bg-gray-900 focus:ring-2 focus:ring-blue-500 outline-none dark:text-white"
                >
                  <option
                    v-for="bg in ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']"
                    :key="bg"
                    :value="bg"
                  >
                    {{ bg }}
                  </option>
                </select>
              </div>
            </div>
          </div>

          <!-- Card 3: NOUVEAU - Détails de la Consultation -->
          <div
            class="bg-white dark:bg-white/[0.03] rounded-3xl border border-gray-100 dark:border-gray-800 p-8 shadow-sm"
          >
            <div class="flex items-center gap-3 mb-6">
              <div
                class="w-10 h-10 rounded-xl bg-amber-50 dark:bg-amber-500/10 flex items-center justify-center text-amber-600"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-6 w-6"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"
                  />
                </svg>
              </div>
              <h2 class="text-lg font-bold dark:text-white">Première Consultation</h2>
            </div>

            <div class="space-y-6">
              <div class="space-y-2">
                <label class="text-xs font-bold text-gray-400 uppercase ml-1"
                  >Symptômes & Motif de visite</label
                >
                <textarea
                  v-model="formData.symptoms"
                  rows="3"
                  class="w-full px-4 py-3.5 rounded-2xl border border-gray-200 dark:border-gray-700 dark:bg-gray-900 focus:ring-2 focus:ring-blue-500 outline-none dark:text-white"
                  placeholder="Quels sont les symptômes décrits ?"
                ></textarea>
              </div>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="space-y-2">
                  <label class="text-xs font-bold text-gray-400 uppercase ml-1">Diagnostic</label>
                  <textarea
                    v-model="formData.diagnosis"
                    rows="4"
                    class="w-full px-4 py-3.5 rounded-2xl border border-gray-200 dark:border-gray-700 dark:bg-gray-900 focus:ring-2 focus:ring-blue-500 outline-none dark:text-white"
                    placeholder="Votre analyse médicale..."
                  ></textarea>
                </div>
                <div class="space-y-2">
                  <label class="text-xs font-bold text-gray-400 uppercase ml-1">Prescription</label>
                  <textarea
                    v-model="formData.prescription"
                    rows="4"
                    class="w-full px-4 py-3.5 rounded-2xl border border-gray-200 dark:border-gray-700 dark:bg-gray-900 focus:ring-2 focus:ring-blue-500 outline-none dark:text-white"
                    placeholder="Médicaments et posologie..."
                  ></textarea>
                </div>
              </div>
            </div>
          </div>

          <div class="mb-10">
            <h2
              class="text-xl font-bold text-gray-900 dark:text-white flex items-center gap-3 mb-6"
            >
              <span
                class="w-8 h-8 rounded-xl bg-purple-500/10 flex items-center justify-center text-purple-600"
                >📁</span
              >
              Dossier Médical (Antécédents)
            </h2>
            <div
              class="grid grid-cols-1 md:grid-cols-2 gap-6 bg-purple-50/50 dark:bg-purple-900/10 p-6 rounded-3xl border border-purple-100 dark:border-purple-900/30"
            >
              <div class="space-y-2">
                <label class="text-xs font-bold text-gray-400 uppercase ml-1">Allergies</label>
                <textarea
                  v-model="formData.allergies"
                  rows="2"
                  class="w-full px-4 py-3.5 rounded-2xl border border-gray-200 dark:border-gray-700 dark:bg-gray-900 focus:ring-2 focus:ring-purple-500 outline-none dark:text-white"
                  placeholder="Pénicilline, arachides... (laisser vide si aucune)"
                ></textarea>
              </div>
              <div class="space-y-2">
                <label class="text-xs font-bold text-gray-400 uppercase ml-1"
                  >Maladies Chroniques</label
                >
                <textarea
                  v-model="formData.chronic_diseases"
                  rows="2"
                  class="w-full px-4 py-3.5 rounded-2xl border border-gray-200 dark:border-gray-700 dark:bg-gray-900 focus:ring-2 focus:ring-purple-500 outline-none dark:text-white"
                  placeholder="Diabète, HTA, Asthme..."
                ></textarea>
              </div>
              <div class="space-y-2">
                <label class="text-xs font-bold text-gray-400 uppercase ml-1"
                  >Antécédents Chirurgicaux</label
                >
                <textarea
                  v-model="formData.surgical_history"
                  rows="2"
                  class="w-full px-4 py-3.5 rounded-2xl border border-gray-200 dark:border-gray-700 dark:bg-gray-900 focus:ring-2 focus:ring-purple-500 outline-none dark:text-white"
                  placeholder="Opération de l'appendicite (2015)..."
                ></textarea>
              </div>
              <div class="space-y-2">
                <label class="text-xs font-bold text-gray-400 uppercase ml-1"
                  >Antécédents Familiaux</label
                >
                <textarea
                  v-model="formData.family_history"
                  rows="2"
                  class="w-full px-4 py-3.5 rounded-2xl border border-gray-200 dark:border-gray-700 dark:bg-gray-900 focus:ring-2 focus:ring-purple-500 outline-none dark:text-white"
                  placeholder="Cancer, maladies génétiques..."
                ></textarea>
              </div>
            </div>
          </div>

          <!-- Footer Actions -->
          <div class="flex items-center justify-end gap-4 mt-4 px-8 pb-8">
            <button
              type="button"
              @click="$router.back()"
              class="px-8 py-3.5 rounded-2xl text-gray-500 font-bold hover:bg-gray-100 dark:hover:bg-gray-800 transition-all"
            >
              Annuler
            </button>
            <button
              type="submit"
              :disabled="isSubmitting"
              class="px-10 py-3.5 rounded-2xl bg-blue-600 text-white font-bold hover:bg-blue-700 shadow-xl shadow-blue-500/25 transition-all active:scale-95 disabled:opacity-50"
            >
              <span v-if="isSubmitting">Traitement...</span>
              <span v-else>Enregistrer Patient & Consultation</span>
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { createPatientManual } from '@/api/patientsService'

const router = useRouter()
const isSubmitting = ref(false)
const errors = ref({})

const formData = reactive({
  first_name: '',
  last_name: '',
  email: '',
  phone: '',
  gender: 'M',
  date_of_birth: '',
  blood_group: 'A+',
  allergies: '',
  chronic_diseases: '',
  surgical_history: '',
  family_history: '',
})

const handleFormSubmit = async () => {
  errors.value = {}
  isSubmitting.value = true

  try {
    await createPatientManual(formData)
    router.push({ path: '/patients', query: { success: 'true' } })
  } catch (err) {
    if (typeof err === 'object') {
      errors.value = err
    }
    console.error("Détails de l'erreur:", err)
  } finally {
    isSubmitting.value = false
  }
}
</script>
