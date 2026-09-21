<template>
  <div class="space-y-4">
    <div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between mb-6">
      <div class="relative w-full max-w-sm">
        <span class="absolute inset-y-0 left-0 flex items-center pl-3 text-gray-400">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="w-5 h-5"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
            />
          </svg>
        </span>
        <input
          v-model="searchQuery"
          @input="handleSearch"
          type="text"
          placeholder="Rechercher un patient ou code..."
          class="w-full rounded-xl border border-gray-200 bg-white py-2.5 pl-10 pr-4 text-sm outline-none focus:border-blue-500 dark:border-gray-800 dark:bg-white/[0.03] dark:text-white transition-all"
        />
      </div>
      <div
        class="px-4 py-1.5 bg-blue-50 dark:bg-blue-500/10 border border-blue-100 dark:border-blue-500/20 rounded-full"
      >
        <span class="text-xs font-bold text-blue-600 dark:text-blue-400 uppercase">
          {{ combinedData.length }} Ordonnance{{ combinedData.length > 1 ? 's' : '' }}
        </span>
      </div>
    </div>

    <div
      class="overflow-hidden rounded-xl border border-gray-200 bg-white dark:border-gray-800 dark:bg-gray-950"
    >
      <div class="max-w-full overflow-x-auto custom-scrollbar">
        <table class="min-w-full">
          <thead>
            <tr
              class="border-b border-gray-200 dark:border-gray-800 bg-gray-50/50 dark:bg-white/[0.01]"
            >
              <th
                class="px-5 py-3 text-left font-bold text-gray-400 text-xs uppercase tracking-wider"
              >
                Patient
              </th>
              <th
                class="px-5 py-3 text-left font-bold text-gray-400 text-xs uppercase tracking-wider"
              >
                Code Ordonnance
              </th>
              <th
                class="px-5 py-3 text-left font-bold text-gray-400 text-xs uppercase tracking-wider"
              >
                Date Création
              </th>
              <th
                class="px-5 py-3 text-center font-bold text-gray-400 text-xs uppercase tracking-wider"
              >
                Médicaments
              </th>
              <th
                class="px-5 py-3 text-center font-bold text-gray-400 text-xs uppercase tracking-wider"
              >
                Action
              </th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-100 dark:divide-gray-800">
            <tr v-if="loading">
              <td colspan="5" class="px-5 py-12 text-center text-gray-400 text-sm">
                Chargement des ordonnances...
              </td>
            </tr>

            <tr v-else-if="combinedData.length === 0">
              <td colspan="5" class="px-5 py-12 text-center text-gray-400 text-sm">
                Aucune ordonnance trouvée.
              </td>
            </tr>

            <tr
              v-for="item in combinedData"
              :key="item.id"
              class="hover:bg-gray-50 dark:hover:bg-white/[0.01] transition-colors group"
            >
              <td class="px-5 py-4">
                <div class="flex items-center gap-3">
                  <div
                    class="w-9 h-9 rounded-xl bg-blue-50 dark:bg-blue-500/10 flex items-center justify-center font-bold text-blue-600 dark:text-blue-400"
                  >
                    {{ item.patientName ? item.patientName.charAt(0).toUpperCase() : 'P' }}
                  </div>
                  <div>
                    <p class="text-sm font-bold text-gray-800 dark:text-white">
                      {{ item.patientName }}
                    </p>
                    <p class="text-[10px] font-mono text-gray-400">
                      Patient: {{ item.patientCode }}
                    </p>
                  </div>
                </div>
              </td>

              <td class="px-5 py-4 text-sm font-mono text-gray-700 dark:text-gray-300">
                {{ item.code }}
              </td>

              <td class="px-5 py-4 text-sm text-gray-600 dark:text-gray-400">
                {{ formatDate(item.createdAt) }}
              </td>

              <td class="px-5 py-4 text-center">
                <span
                  class="px-2.5 py-1 text-xs font-bold rounded-md bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-300"
                >
                  {{ item.itemsCount }} dwe{{ item.itemsCount > 1 ? 's' : '' }}
                </span>
              </td>

              <td class="px-5 py-4 text-center">
                <button
                  @click="openDetails(item.code)"
                  :disabled="drawerLoading"
                  class="p-2 rounded-xl text-gray-400 hover:text-blue-600 hover:bg-blue-50 dark:hover:bg-blue-500/10 transition-all active:scale-95 disabled:opacity-50"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="w-5 h-5"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                    />
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
                    />
                  </svg>
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <Transition name="slide">
      <div v-if="selectedItem" class="fixed inset-0 z-50 overflow-hidden">
        <div
          class="absolute inset-0 bg-gray-900/40 backdrop-blur-sm transition-opacity"
          @click="closeDetails"
        ></div>

        <div
          class="absolute inset-y-0 right-0 max-w-2xl w-full bg-white dark:bg-gray-950 shadow-2xl flex flex-col border-l border-gray-200 dark:border-gray-800 transition-all duration-300"
        >
          <div
            class="p-6 border-b border-gray-100 dark:border-gray-800 flex justify-between items-center bg-gray-50/50 dark:bg-white/[0.01]"
          >
            <div class="flex items-center gap-3">
              <div
                class="p-2 bg-blue-50 dark:bg-blue-500/10 rounded-xl text-blue-600 dark:text-blue-400"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="w-6 h-6"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
                  />
                </svg>
              </div>
              <div>
                <h2 class="text-base font-bold text-gray-900 dark:text-white">
                  Détails de l'Ordonnance
                </h2>
                <p class="text-xs text-gray-400 font-mono mt-0.5">ID: {{ selectedItem.code }}</p>
              </div>
            </div>
            <button
              @click="closeDetails"
              class="p-2 rounded-xl hover:bg-gray-100 dark:hover:bg-gray-800 text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 transition-colors"
            >
              ✕
            </button>
          </div>

          <div
            class="p-6 space-y-6 flex-1 overflow-y-auto custom-scrollbar bg-gray-50/30 dark:bg-transparent"
          >
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div
                class="p-4 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 shadow-sm flex flex-col justify-between"
              >
                <div>
                  <span
                    class="text-[10px] font-bold text-gray-400 uppercase tracking-wider block mb-2"
                    >Patient</span
                  >
                  <div class="flex items-center gap-3">
                    <div
                      class="w-10 h-10 rounded-xl bg-blue-600 text-white flex items-center justify-center font-bold text-sm shadow-sm"
                    >
                      {{
                        selectedItem.patient_name
                          ? selectedItem.patient_name.charAt(0).toUpperCase()
                          : 'P'
                      }}
                    </div>
                    <div>
                      <h4 class="text-sm font-bold text-gray-900 dark:text-white">
                        {{ selectedItem.patient_name }}
                      </h4>
                      <p class="text-xs text-gray-400 font-mono mt-0.5">
                        {{ selectedItem.patient_phone || 'Pas de téléphone' }}
                      </p>
                    </div>
                  </div>
                </div>
              </div>

              <div
                class="p-4 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 shadow-sm"
              >
                <span
                  class="text-[10px] font-bold text-gray-400 uppercase tracking-wider block mb-2"
                  >Détails Consultation</span
                >
                <div class="space-y-1.5 text-xs text-gray-600 dark:text-gray-400">
                  <div class="flex justify-between">
                    <span>Rendez-vous :</span>
                    <span class="font-mono font-bold text-gray-900 dark:text-white">{{
                      selectedItem.appointment_code || 'Direct'
                    }}</span>
                  </div>
                  <div class="flex justify-between">
                    <span>Date d'émission :</span>
                    <span class="font-bold text-gray-800 dark:text-gray-200">{{
                      formatDate(selectedItem.created_at)
                    }}</span>
                  </div>
                  <div class="flex justify-between" v-if="selectedItem.created_at">
                    <span>Heure :</span>
                    <span class="font-mono text-gray-500">{{
                      formatTime(selectedItem.created_at)
                    }}</span>
                  </div>
                </div>
              </div>
            </div>

            <div
              class="p-4 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 shadow-sm space-y-4"
            >
              <div v-if="selectedItem.symptoms" class="space-y-1">
                <span class="text-[10px] font-bold text-gray-400 uppercase tracking-wider block"
                  >Symptômes relevés</span
                >
                <p
                  class="text-xs text-gray-700 dark:text-gray-300 leading-relaxed bg-gray-50 dark:bg-white/[0.02] p-2.5 rounded-lg border border-gray-100 dark:border-gray-800/50 whitespace-pre-line"
                >
                  {{ selectedItem.symptoms }}
                </p>
              </div>

              <div v-if="selectedItem.diagnosis" class="space-y-1">
                <span class="text-[10px] font-bold text-gray-400 uppercase tracking-wider block"
                  >Diagnostic Final</span
                >
                <p
                  class="text-xs font-bold text-emerald-700 dark:text-emerald-400 bg-emerald-50/50 dark:bg-emerald-500/[0.02] p-2.5 rounded-lg border border-emerald-100/50 dark:border-emerald-950/30 whitespace-pre-line"
                >
                  {{ selectedItem.diagnosis }}
                </p>
              </div>
            </div>

            <div class="space-y-2">
              <span class="text-[10px] font-bold text-gray-400 uppercase tracking-wider block px-1"
                >Médicaments Prescrits (Traitement)</span
              >

              <div v-if="selectedItem.items && selectedItem.items.length > 0" class="space-y-2.5">
                <div
                  v-for="(drug, index) in selectedItem.items"
                  :key="index"
                  class="p-4 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 shadow-sm flex flex-col md:flex-row md:items-center justify-between gap-3 hover:border-blue-200 dark:hover:border-blue-900/50 transition-colors"
                >
                  <div class="space-y-1">
                    <div class="flex items-center gap-2">
                      <span
                        class="w-5 h-5 bg-blue-50 dark:bg-blue-950 text-blue-600 dark:text-blue-400 font-mono text-[10px] font-bold rounded flex items-center justify-center"
                      >
                        {{ index + 1 }}
                      </span>
                      <h5 class="text-sm font-bold text-gray-900 dark:text-white">
                        {{
                          drug.medicament_name ||
                          drug.name ||
                          (drug.medicament && drug.medicament.name) ||
                          'Médicament'
                        }}
                      </h5>
                    </div>
                    <p v-if="drug.instructions" class="text-xs text-gray-400 italic pl-7">
                      “ {{ drug.instructions }} ”
                    </p>
                  </div>

                  <div class="flex flex-wrap items-center gap-1.5 md:justify-end pl-7 md:pl-0">
                    <span
                      v-if="drug.dosage"
                      class="px-2 py-0.5 text-[10px] font-medium bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-300 rounded-md"
                    >
                      Dosage: {{ drug.dosage }}
                    </span>
                    <span
                      v-if="drug.frequency"
                      class="px-2 py-0.5 text-[10px] font-bold bg-blue-50 dark:bg-blue-950 text-blue-600 dark:text-blue-400 rounded-md"
                    >
                      {{ drug.frequency }}
                    </span>
                    <span
                      v-if="drug.duration"
                      class="px-2 py-0.5 text-[10px] font-bold bg-emerald-50 dark:bg-emerald-950 text-emerald-600 dark:text-emerald-400 rounded-md"
                    >
                      Durée: {{ drug.duration }}
                    </span>
                  </div>
                </div>
              </div>

              <div
                v-else
                class="p-6 text-center border border-dashed border-gray-200 dark:border-gray-800 rounded-xl bg-white dark:bg-gray-900 text-gray-400 text-xs italic"
              >
                Aucun médicament n'a été rattaché à cette ordonnance.
              </div>
            </div>

            <div v-if="selectedItem.notes && selectedItem.notes !== '...'" class="space-y-1">
              <span class="text-[10px] font-bold text-gray-400 uppercase tracking-wider block px-1"
                >Notes d'observation</span
              >
              <div
                class="p-3 rounded-xl bg-amber-50/40 dark:bg-amber-500/[0.01] border border-amber-100/70 dark:border-amber-900/20 text-xs text-gray-600 dark:text-gray-400 italic"
              >
                {{ selectedItem.notes }}
              </div>
            </div>
          </div>

          <div
            class="p-4 border-t border-gray-100 dark:border-gray-800 bg-white dark:bg-gray-950 flex gap-3"
          >
            <a
              v-if="selectedItem.pdf_file"
              :href="getPdfUrl(selectedItem.pdf_file)"
              target="_blank"
              class="flex-1 bg-emerald-600 hover:bg-emerald-700 text-white font-bold py-2.5 rounded-xl transition-all active:scale-[0.98] shadow-sm text-xs flex items-center justify-center gap-2"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="w-4 h-4"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v2a2 2 0 002 2zm3-10V4a1 1 0 011-1h2a1 1 0 011 1v3m-3 7h.01"
                />
              </svg>
              Imprimer / Générer le PDF
            </a>
            <button
              @click="closeDetails"
              class="px-5 bg-gray-100 hover:bg-gray-200 dark:bg-gray-800 dark:hover:bg-gray-700 text-gray-700 dark:text-gray-300 font-bold py-2.5 rounded-xl transition-all active:scale-[0.98] text-xs"
            >
              Fermer
            </button>
          </div>
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getDoctorOrdonnances, getOrdonnanceDetail } from '@/api/ordonnaceService.ts'

const searchQuery = ref('')
const combinedData = ref([])
const loading = ref(true)
const drawerLoading = ref(false)
const selectedItem = ref(null)

const fetchData = async () => {
  try {
    loading.value = true
    const response = await getDoctorOrdonnances()

    const filtered = response.filter(
      (o) =>
        o.patient_name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
        o.code.toLowerCase().includes(searchQuery.value.toLowerCase()),
    )

    combinedData.value = filtered.map((con) => ({
      id: con.id,
      code: con.code,
      patientName: con.patient_name,
      patientCode: con.patient_code,
      appointmentCode: con.appointment_code || 'Direct',
      createdAt: con.created_at,
      itemsCount: con.items_count,
    }))
  } catch (error) {
    console.error('Erreur chargement liste ordonnances:', error)
  } finally {
    loading.value = false
  }
}

const handleSearch = () => {
  fetchData()
}

const openDetails = async (code) => {
  try {
    drawerLoading.value = true
    const details = await getOrdonnanceDetail(code)
    selectedItem.value = details
  } catch (error) {
    console.error('Erreur lors de la récupération des détails:', error)
  } finally {
    drawerLoading.value = false
  }
}

const closeDetails = () => {
  selectedItem.value = null
}

const getPdfUrl = (url) => {
  if (!url) return '#'
  if (url.startsWith('http')) return url
  return `http://127.0.0.1:8000${url}`
}
const formatDate = (dateString) => {
  if (!dateString) return '---'
  const date = new Date(dateString)
  return date.toLocaleDateString('fr-FR', { day: 'numeric', month: 'short', year: 'numeric' })
}

// Extraction de l'heure depuis created_at
const formatTime = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleTimeString('fr-FR', { hour: '2-digit', minute: '2-digit' })
}

onMounted(fetchData)
</script>

<style scoped>
.slide-enter-active,
.slide-leave-active {
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.slide-enter-from,
.slide-leave-to {
  transform: translateX(100%);
}
.custom-scrollbar::-webkit-scrollbar {
  height: 6px;
  width: 6px;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background: #e5e7eb;
  border-radius: 10px;
}
.dark .custom-scrollbar::-webkit-scrollbar-thumb {
  background: #374151;
}
</style>
