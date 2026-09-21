<template>
  <div class="space-y-4">
    <div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between mb-6">
      <div class="relative flex-1 max-w-md">
        <span
          class="absolute inset-y-0 left-0 flex items-center pl-3.5 text-gray-400 pointer-events-none"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="w-4 h-4"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            stroke-width="2"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
            />
          </svg>
        </span>
        <input
          v-model="searchQuery"
          @input="handleSearch"
          type="text"
          placeholder="Rechercher un patient ou code..."
          class="w-full rounded-lg border border-gray-200/80 bg-white py-2 pl-10 pr-4 text-sm text-gray-900 outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500/20 dark:border-gray-800 dark:bg-zinc-900 dark:text-white transition-all placeholder:text-gray-400"
        />
      </div>

      <div class="flex items-center gap-2">
        <div
          class="px-3 py-1.5 bg-blue-50 dark:bg-blue-500/10 border border-blue-100 dark:border-blue-500/20 rounded-lg text-xs font-semibold text-blue-600 dark:text-blue-400 uppercase tracking-wider"
        >
          {{ filteredData.length }} Consultations
        </div>
      </div>
    </div>

    <div
      class="overflow-hidden rounded-xl border border-gray-100 bg-white dark:border-gray-800/80 dark:bg-zinc-950/40 backdrop-blur-sm"
    >
      <div class="max-w-full overflow-x-auto custom-scrollbar">
        <table class="min-w-full table-fixed">
          <thead>
            <tr
              class="border-b border-gray-100 dark:border-gray-800/80 bg-gray-50/40 dark:bg-zinc-900/10"
            >
              <th
                class="w-1/3 px-6 py-3.5 text-left text-xs font-semibold tracking-wider text-gray-400 uppercase"
              >
                Patient
              </th>
              <th
                class="w-1/4 px-6 py-3.5 text-left text-xs font-semibold tracking-wider text-gray-400 uppercase"
              >
                Date RDV
              </th>
              <th
                class="w-1/4 px-6 py-3.5 text-left text-xs font-semibold tracking-wider text-gray-400 uppercase"
              >
                Diagnostic
              </th>
              <th
                class="w-1/4 px-6 py-3.5 text-left text-xs font-semibold tracking-wider text-gray-400 uppercase"
              >
                Prescription
              </th>
              <th
                class="w-1/6 px-6 py-3.5 text-center text-xs font-semibold tracking-wider text-gray-400 uppercase"
              >
                Action
              </th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-100 dark:divide-gray-800/60">
            <tr v-if="loading">
              <td colspan="5" class="px-6 py-12 text-center">
                <div class="flex flex-col items-center justify-center gap-3">
                  <div
                    class="h-6 w-6 animate-spin rounded-full border-2 border-solid border-blue-600 border-r-transparent"
                  ></div>
                  <p class="text-xs text-gray-400">Chargement des données médicales...</p>
                </div>
              </td>
            </tr>

            <tr v-else-if="paginatedData.length === 0">
              <td colspan="5" class="px-6 py-16 text-center">
                <div class="flex flex-col items-center justify-center max-w-xs mx-auto">
                  <div class="p-3 bg-gray-50 dark:bg-zinc-900 rounded-xl text-gray-400 mb-3">
                    <svg
                      class="w-5 h-5"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                      stroke-width="1.5"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                      />
                    </svg>
                  </div>
                  <p class="text-sm font-medium text-gray-700 dark:text-zinc-300">
                    Aucune consultation trouvée
                  </p>
                  <p class="text-xs text-gray-400 mt-0.5">Aucun dossier médical ne correspond.</p>
                </div>
              </td>
            </tr>

            <tr
              v-for="(item, index) in paginatedData"
              :key="index"
              class="hover:bg-gray-50/50 dark:hover:bg-zinc-900/10 transition-colors group"
            >
              <td class="px-6 py-3.5 whitespace-nowrap">
                <div class="flex items-center gap-3">
                  <div
                    class="w-10 h-10 rounded-full flex items-center justify-center shadow-inner transition-transform group-hover:scale-[1.02] bg-blue-100 text-blue-600 dark:bg-blue-500/20"
                  >
                    <span class="text-sm font-semibold">{{
                      item.patientName ? item.patientName.charAt(0).toUpperCase() : 'P'
                    }}</span>
                  </div>
                  <div class="truncate">
                    <span
                      class="block text-sm font-medium text-gray-800 dark:text-zinc-200 truncate"
                      >{{ item.patientName }}</span
                    >
                    <span class="block text-xs text-gray-400 font-mono tracking-tight mt-0.5"
                      >RDV: {{ item.appointmentCode }}</span
                    >
                  </div>
                </div>
              </td>

              <td class="px-6 py-3.5 whitespace-nowrap">
                <p class="text-sm font-medium text-gray-700 dark:text-zinc-300">{{ item.date }}</p>
              </td>

              <td class="px-6 py-3.5 max-w-[220px] truncate">
                <p
                  class="text-sm text-gray-800 dark:text-gray-200 truncate"
                  :title="item.diagnosis"
                >
                  {{ item.diagnosis || '---' }}
                </p>
              </td>

              <td class="px-6 py-3.5 max-w-[220px] truncate">
                <p
                  class="text-xs text-gray-500 dark:text-gray-400 italic truncate"
                  :title="item.prescription"
                >
                  {{ item.prescription || '---' }}
                </p>
              </td>

              <td class="px-6 py-3.5 whitespace-nowrap text-center">
                <button
                  @click.stop="openDetails(item)"
                  class="p-1.5 rounded-md text-gray-400 hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-zinc-900 transition-colors active:scale-95"
                  title="Voir Fiche"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="w-4 h-4"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    stroke-width="2"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                    />
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
                    />
                  </svg>
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <div
        v-if="filteredData.length > 0"
        class="flex items-center justify-between px-6 py-4 border-t border-gray-100 dark:border-gray-800/80 bg-gray-50/20 dark:bg-zinc-900/5"
      >
        <div class="text-xs text-gray-400">
          Affichage de
          <span class="font-medium text-gray-700 dark:text-zinc-300">{{ startIndex + 1 }}</span> à
          <span class="font-medium text-gray-700 dark:text-zinc-300">{{
            Math.min(endIndex, filteredData.length)
          }}</span>
          sur
          <span class="font-medium text-gray-700 dark:text-zinc-300">{{
            filteredData.length
          }}</span>
          résultats
        </div>
        <div class="flex items-center gap-2">
          <button
            @click="prevPage"
            :disabled="currentPage === 1"
            class="px-3 py-1.5 text-xs font-medium rounded-lg border border-gray-200 dark:border-zinc-800 bg-white dark:bg-zinc-900 text-gray-600 dark:text-zinc-400 hover:bg-gray-50 dark:hover:bg-zinc-800 transition-colors disabled:opacity-40 disabled:hover:bg-white dark:disabled:hover:bg-zinc-900 disabled:cursor-not-allowed"
          >
            Précédent
          </button>
          <span class="text-xs font-medium text-gray-500 dark:text-zinc-400 px-1">
            {{ currentPage }} / {{ totalPages }}
          </span>
          <button
            @click="nextPage"
            :disabled="currentPage === totalPages"
            class="px-3 py-1.5 text-xs font-medium rounded-lg border border-gray-200 dark:border-zinc-800 bg-white dark:bg-zinc-900 text-gray-600 dark:text-zinc-400 hover:bg-gray-50 dark:hover:bg-zinc-800 transition-colors disabled:opacity-40 disabled:hover:bg-white dark:disabled:hover:bg-zinc-900 disabled:cursor-not-allowed"
          >
            Suivant
          </button>
        </div>
      </div>
    </div>

    <Transition name="slide">
      <div v-if="selectedItem" class="fixed inset-0 z-50 overflow-hidden">
        <div
          class="absolute inset-0 bg-zinc-950/40 backdrop-blur-sm transition-opacity"
          @click="closeDetails"
        ></div>
        <div
          class="absolute inset-y-0 right-0 max-w-md w-full bg-white dark:bg-zinc-950 border-l border-gray-100 dark:border-zinc-900 shadow-xl flex flex-col"
        >
          <div
            class="p-5 border-b border-gray-100 dark:border-zinc-900 flex justify-between items-center"
          >
            <div>
              <h2 class="text-base font-semibold text-gray-900 dark:text-white">
                Fiche de Consultation
              </h2>
              <p class="text-xs font-mono text-gray-400 mt-0.5">
                Code RDV: {{ selectedItem.appointmentCode }}
              </p>
            </div>
            <button
              @click="closeDetails"
              class="p-1.5 rounded-lg text-gray-400 hover:bg-gray-50 dark:hover:bg-zinc-900 transition-colors"
            >
              <svg
                class="w-4 h-4"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                stroke-width="2"
              >
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>

          <div class="p-5 space-y-5 flex-1 overflow-y-auto custom-scrollbar">
            <div
              class="flex flex-col items-center text-center p-4 rounded-xl bg-gray-50/50 dark:bg-zinc-900/30 border border-gray-100/50 dark:border-zinc-900"
            >
              <div
                class="w-14 h-14 rounded-xl bg-blue-600 text-white flex items-center justify-center text-lg font-bold shadow-md shadow-blue-500/10 mb-3"
              >
                {{
                  selectedItem.patientName ? selectedItem.patientName.charAt(0).toUpperCase() : 'P'
                }}
              </div>
              <h3 class="text-base font-medium text-gray-900 dark:text-white">
                {{ selectedItem.patientName }}
              </h3>
              <p class="text-xs text-gray-400 font-mono mt-0.5">
                {{ selectedItem.patientPhone || 'Pas de téléphone' }}
              </p>
            </div>

            <div
              class="flex items-center justify-between p-3 rounded-xl border border-gray-100 dark:border-zinc-900 bg-gray-50/20"
            >
              <span class="text-xs text-gray-400 font-medium">Date d'enregistrement</span>
              <span class="text-xs font-semibold text-gray-800 dark:text-zinc-200">{{
                selectedItem.date
              }}</span>
            </div>

            <div class="space-y-1.5">
              <span class="text-[11px] font-semibold uppercase tracking-wider text-gray-400"
                >Symptômes signalés</span
              >
              <div
                class="text-xs text-gray-800 dark:text-zinc-300 bg-gray-50 dark:bg-zinc-900 border border-gray-100 dark:border-zinc-800/60 p-3.5 rounded-xl leading-relaxed whitespace-pre-line min-h-[70px]"
              >
                {{ selectedItem.symptoms || 'Aucun symptôme mentionné.' }}
              </div>
            </div>

            <div class="space-y-1.5">
              <span class="text-[11px] font-semibold uppercase tracking-wider text-gray-400"
                >Diagnostic Médical</span
              >
              <div
                class="text-xs font-medium text-emerald-700 dark:text-emerald-400 bg-emerald-50/40 dark:bg-emerald-500/[0.02] border border-emerald-100 dark:border-emerald-800/30 p-3.5 rounded-xl whitespace-pre-line"
              >
                {{ selectedItem.diagnosis || 'Aucun diagnostic posé.' }}
              </div>
            </div>

            <div class="space-y-1.5">
              <span class="text-[11px] font-semibold uppercase tracking-wider text-gray-400"
                >Ordonnance & Traitement</span
              >
              <div
                class="text-xs font-mono text-gray-800 dark:text-zinc-300 bg-blue-50/20 dark:bg-blue-500/[0.01] border border-blue-100/50 dark:border-zinc-800/40 p-4 rounded-xl leading-relaxed whitespace-pre-line"
              >
                <div
                  class="border-b border-blue-100/50 dark:border-blue-900/30 pb-1.5 mb-2.5 text-blue-600 dark:text-blue-400 font-bold uppercase tracking-wider text-[10px]"
                >
                  💊 Médicaments
                </div>
                {{ selectedItem.prescription || 'Aucun traitement généré.' }}
              </div>
            </div>
          </div>

          <div class="p-5 border-t border-gray-100 dark:border-zinc-900 bg-white dark:bg-zinc-950">
            <button
              @click="closeDetails"
              class="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2.5 rounded-xl text-sm transition-all active:scale-[0.98]"
            >
              Fermer le dossier
            </button>
          </div>
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { getDoctorConsultations } from '@/api/consultationService'

const searchQuery = ref('')
const combinedData = ref([])
const loading = ref(true)
const selectedItem = ref(null)

// --- AJOUT DE L'ÉTAT DE PAGINATION ---
const currentPage = ref(1)
const itemsPerPage = ref(8)

const fetchData = async () => {
  try {
    loading.value = true
    const response = await getDoctorConsultations(searchQuery.value)

    combinedData.value = response.map((con) => ({
      id: con.id,
      patientName: con.patient_name,
      patientPhone: con.patient_phone,
      patientCode: con.patient_code,
      appointmentCode: con.appointment_code || 'Direct',
      date: con.appointment_date,
      symptoms: con.symptoms,
      diagnosis: con.diagnosis,
      prescription: con.prescription,
      notes: con.notes,
    }))
  } catch (error) {
    console.error('Erreur:', error)
  } finally {
    loading.value = false
  }
}

// Filtrage local (si nécessaire en plus de l'API)
const filteredData = computed(() => {
  return combinedData.value.filter((item) => {
    const q = searchQuery.value.toLowerCase().trim()
    if (!q) return true
    return (
      item.patientName?.toLowerCase().includes(q) || item.appointmentCode?.toLowerCase().includes(q)
    )
  })
})

// --- LOGIQUE DE PAGINATION CALCULÉE ---
const totalPages = computed(() => {
  return Math.ceil(filteredData.value.length / itemsPerPage.value) || 1
})

const startIndex = computed(() => (currentPage.value - 1) * itemsPerPage.value)
const endIndex = computed(() => startIndex.value + itemsPerPage.value)

const paginatedData = computed(() => {
  return filteredData.value.slice(startIndex.value, endIndex.value)
})

const nextPage = () => {
  if (currentPage.value < totalPages.value) currentPage.value++
}

const prevPage = () => {
  if (currentPage.value > 1) currentPage.value--
}

// Reset de la page si l'utilisateur tape une recherche
watch(searchQuery, () => {
  currentPage.value = 1
})

const handleSearch = () => {
  fetchData()
}

onMounted(fetchData)

const openDetails = (item) => {
  selectedItem.value = item
}
const closeDetails = () => {
  selectedItem.value = null
}
</script>

<script>
export default { name: 'ConsultationTable' }
</script>

<style scoped>
/* Conserve tes styles d'animation et scrollbars */
.slide-enter-active,
.slide-leave-active {
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}
.slide-enter-from,
.slide-leave-to {
  transform: translateX(100%);
}
.custom-scrollbar::-webkit-scrollbar {
  height: 5px;
  width: 5px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: transparent;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background: #e4e4e7;
  border-radius: 10px;
}
.dark .custom-scrollbar::-webkit-scrollbar-thumb {
  background: #27272a;
}
</style>
