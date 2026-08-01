<template>
  <div class="space-y-4">
    <!-- Header/Toolbar: Search & Filter -->
    <div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between mb-6">
      <div class="relative flex-1 max-w-md">
        <span class="absolute inset-y-0 left-0 flex items-center pl-3.5 text-gray-400 pointer-events-none">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
        </span>
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Rechercher par nom, UID, téléphone, groupe..."
          class="w-full rounded-lg border border-gray-200/80 bg-white py-2 pl-10 pr-4 text-sm text-gray-900 outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500/20 dark:border-gray-800 dark:bg-zinc-900 dark:text-white transition-all placeholder:text-gray-400"
        />
      </div>

      <div class="flex items-center gap-2">
        <select 
          v-model="statusFilter"
          class="rounded-lg border border-gray-200/80 bg-white px-3 py-2 text-sm font-medium text-gray-600 outline-none focus:border-blue-500 dark:border-gray-800 dark:bg-zinc-900 dark:text-gray-300 cursor-pointer transition-all appearance-none pr-8 relative bg-[url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%2371717a%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E')] bg-[length:0.65rem_auto] bg-[right_0.75rem_center] bg-no-repeat"
        >
          <option value="All">Tous les statuts</option>
          <option value="Stable">Stable</option>
          <option value="Urgent">Urgent</option>
          <option value="Pending">En attente</option>
        </select>

        <button 
          @click="resetFilters"
          class="p-2 rounded-lg border border-gray-200/80 bg-white text-gray-500 hover:text-gray-700 hover:bg-gray-50 dark:border-gray-800 dark:bg-zinc-900 dark:text-gray-400 dark:hover:bg-zinc-800 transition-all"
          title="Réinitialiser"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
          </svg>
        </button>
      </div>
    </div>

    <!-- Modern Data Table Layout -->
    <div class="overflow-hidden rounded-xl border border-gray-100 bg-white dark:border-gray-800/80 dark:bg-zinc-950/40 backdrop-blur-sm">
      <div class="max-w-full overflow-x-auto custom-scrollbar">
        <table class="min-w-full table-fixed">
          <thead>
            <tr class="border-b border-gray-100 dark:border-gray-800/80 bg-gray-50/40 dark:bg-zinc-900/10">
              <th class="w-1/3 px-6 py-3.5 text-left text-xs font-semibold tracking-wider text-gray-400 uppercase">Patient</th>
              <th class="w-1/4 px-6 py-3.5 text-left text-xs font-semibold tracking-wider text-gray-400 uppercase">Dernière visite</th>
              <th class="w-1/5 px-6 py-3.5 text-left text-xs font-semibold tracking-wider text-gray-400 uppercase">Signes Vitaux</th>
              <th class="w-1/6 px-6 py-3.5 text-left text-xs font-semibold tracking-wider text-gray-400 uppercase">Statut</th>
              <th class="w-1/6 px-6 py-3.5 text-center text-xs font-semibold tracking-wider text-gray-400 uppercase">Action</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-100 dark:divide-gray-800/60">
            <!-- Loading State -->
            <tr v-if="isLoading">
              <td colspan="5" class="px-6 py-12 text-center">
                <div class="flex flex-col items-center justify-center gap-3">
                  <div class="h-6 w-6 animate-spin rounded-full border-2 border-solid border-blue-600 border-r-transparent"></div>
                  <p class="text-xs text-gray-400">Chargement des données...</p>
                </div>
              </td>
            </tr>

            <!-- Empty State -->
            <tr v-else-if="paginatedPatients.length === 0">
              <td colspan="5" class="px-6 py-16 text-center">
                <div class="flex flex-col items-center justify-center max-w-xs mx-auto">
                  <div class="p-3 bg-gray-50 dark:bg-zinc-900 rounded-xl text-gray-400 mb-3">
                    <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                    </svg>
                  </div>
                  <p class="text-sm font-medium text-gray-700 dark:text-zinc-300">Aucun patient trouvé</p>
                  <p class="text-xs text-gray-400 mt-0.5">Aucun dossier ne correspond à vos filtres actuels.</p>
                </div>
              </td>
            </tr>

            <!-- Table Rows -->
            <tr
              v-for="patient in paginatedPatients"
              :key="patient.id"
              class="hover:bg-gray-50/50 dark:hover:bg-zinc-900/10 transition-colors group"
            >
              <td class="px-6 py-3.5 whitespace-nowrap">
                <div class="flex items-center gap-3">
                  <div :class="[
                    'w-10 h-10 rounded-full flex items-center justify-center shadow-inner transition-transform group-hover:scale-[1.02]',
                    isMale(patient.gender) ? 'bg-blue-100 text-blue-600 dark:bg-blue-500/20' : 'bg-pink-100 text-pink-600 dark:bg-pink-500/20'
                  ]">
                    <svg v-if="isMale(patient.gender)" xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                    </svg>
                    <svg v-else xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                      <circle cx="12" cy="10" r="3" fill="currentColor" opacity="0.3"/>
                    </svg>
                  </div>
                  <div class="truncate">
                    <span class="block text-sm font-medium text-gray-800 dark:text-zinc-200 truncate">{{ patient.name }}</span>
                    <span class="block text-xs text-gray-400 font-mono tracking-tight mt-0.5">UID: {{ patient.id }}</span>
                  </div>
                </div>
              </td>

              <td class="px-6 py-3.5 whitespace-nowrap">
                <p class="text-xs font-medium text-gray-700 dark:text-zinc-300 truncate">{{ patient.lastVisitFormatted }}</p>
                <p class="text-[11px] text-gray-400 mt-0.5">Rejoint: {{ patient.dateJoined }}</p>
              </td>

              <td class="px-6 py-3.5 whitespace-nowrap">
                <div class="flex items-center gap-2.5 text-xs">
                  <div>
                    <span class="text-gray-400 font-medium mr-1">BP</span>
                    <span class="font-mono bg-gray-50 dark:bg-zinc-900 border border-gray-100 dark:border-zinc-800 px-1.5 py-0.5 rounded text-gray-700 dark:text-zinc-300">{{ patient.vitals.bp }}</span>
                  </div>
                  <div class="w-px h-3 bg-gray-200 dark:bg-zinc-800"></div>
                  <div>
                    <span class="text-gray-400 font-medium mr-1">HR</span>
                    <span class="font-mono bg-gray-50 dark:bg-zinc-900 border border-gray-100 dark:border-zinc-800 px-1.5 py-0.5 rounded text-gray-700 dark:text-zinc-300">{{ patient.vitals.hr }}</span>
                  </div>
                </div>
              </td>

              <td class="px-6 py-3.5 whitespace-nowrap">
                <span :class="['inline-flex items-center px-2.5 py-0.5 rounded-md text-[11px] font-medium border', statusClasses(patient.status)]">
                  {{ patient.status }}
                </span>
              </td>

              <td class="px-6 py-3.5 whitespace-nowrap text-center">
                <button 
                  @click.stop="openDetails(patient)" 
                  class="p-1.5 rounded-md text-gray-400 hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-zinc-900 transition-colors active:scale-95"
                  title="Voir Dossier"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                    <path stroke-linecap="round" stroke-linejoin="round" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                  </svg>
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Compact Pagination Bar -->
      <div v-if="filteredPatients.length > 0" class="flex items-center justify-between px-6 py-4 border-t border-gray-100 dark:border-gray-800/80 bg-gray-50/20 dark:bg-zinc-900/5">
        <div class="text-xs text-gray-400">
          Affichage de <span class="font-medium text-gray-700 dark:text-zinc-300">{{ startIndex + 1 }}</span> à 
          <span class="font-medium text-gray-700 dark:text-zinc-300">{{ Math.min(endIndex, filteredPatients.length) }}</span> sur 
          <span class="font-medium text-gray-700 dark:text-zinc-300">{{ filteredPatients.length }}</span> résultats
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

    <!-- Premium Slide Drawer: Patient Details -->
    <Transition name="slide">
      <div v-if="selectedPatient" class="fixed inset-0 z-50 overflow-hidden">
        <div class="absolute inset-0 bg-zinc-950/40 backdrop-blur-sm transition-opacity" @click="closeDetails"></div>
        <div class="absolute inset-y-0 right-0 max-w-sm w-full bg-white dark:bg-zinc-950 border-l border-gray-100 dark:border-zinc-900 shadow-xl flex flex-col">
          <!-- Drawer Header -->
          <div class="p-5 border-b border-gray-100 dark:border-zinc-900 flex justify-between items-center">
            <div>
              <h2 class="text-base font-semibold text-gray-900 dark:text-white">Dossier Patient</h2>
              <p class="text-xs font-mono text-gray-400 mt-0.5">ID: {{ selectedPatient.id }}</p>
            </div>
            <button @click="closeDetails" class="p-1.5 rounded-lg text-gray-400 hover:bg-gray-50 dark:hover:bg-zinc-900 transition-colors">
              <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
          
          <!-- Drawer Content -->
          <div class="p-5 space-y-6 flex-1 overflow-y-auto">
            <!-- Profile Info: Drawer Avatar (♂ / ♀) -->
            <div class="flex flex-col items-center text-center p-4 rounded-xl bg-gray-50/50 dark:bg-zinc-900/30 border border-gray-100/50 dark:border-zinc-900">
              <div :class="[
                'w-16 h-16 rounded-xl flex items-center justify-center text-2xl font-semibold mb-3 border shadow-sm',
                isMale(selectedPatient.gender) ? 'bg-blue-50 text-blue-600 border-blue-100' : 'bg-rose-50 text-rose-600 border-rose-100'
              ]">
                {{ isMale(selectedPatient.gender) ? '♂' : '♀' }}
              </div>
              <h3 class="text-base font-medium text-gray-900 dark:text-white">{{ selectedPatient.name }}</h3>
              <p class="text-xs text-blue-600 font-medium mt-0.5">{{ selectedPatient.email }}</p>
              
              <button 
                @click="goToPatient"
                class="mt-3 inline-flex items-center gap-1 text-xs text-gray-400 hover:text-blue-600 transition-colors font-medium"
              >
                Voir tous les détails 
                <svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
                </svg>
              </button>
            </div>

            <!-- Health Grid -->
            <div class="grid grid-cols-3 gap-3">
              <div class="p-3 rounded-xl bg-gray-50/50 dark:bg-zinc-900/20 border border-gray-100 dark:border-zinc-900/60 text-center">
                <p class="text-[10px] uppercase font-bold text-gray-400 mb-0.5">Sexe</p>
                <p class="text-xs font-semibold dark:text-white">{{ isMale(selectedPatient.gender) ? 'Homme' : 'Femme' }}</p>
              </div>
              <div class="p-3 rounded-xl bg-gray-50/50 dark:bg-zinc-900/20 border border-gray-100 dark:border-zinc-900/60 text-center">
                <p class="text-[10px] uppercase font-bold text-gray-400 mb-0.5">Groupe</p>
                <p class="text-xs font-bold text-rose-600 dark:text-rose-400">{{ selectedPatient.bloodType || '—' }}</p>
              </div>
              <div class="p-3 rounded-xl bg-gray-50/50 dark:bg-zinc-900/20 border border-gray-100 dark:border-zinc-900/60 text-center">
                <p class="text-[10px] uppercase font-bold text-gray-400 mb-0.5">Âge</p>
                <p class="text-xs font-semibold dark:text-white">{{ calculateAge(selectedPatient.dob) }} ans</p>
              </div>
            </div>

            <!-- Contact Info -->
            <div class="space-y-2.5">
              <h4 class="text-[11px] font-semibold uppercase tracking-wider text-gray-400">Coordonnées</h4>
              <div class="flex items-center justify-between p-3 rounded-lg border border-gray-100 dark:border-zinc-900">
                <span class="text-xs text-gray-400">Téléphone</span>
                <span class="text-xs font-medium text-gray-800 dark:text-zinc-200 font-mono">{{ selectedPatient.phone || '—' }}</span>
              </div>
              <div class="flex items-center justify-between p-3 rounded-lg border border-gray-100 dark:border-zinc-900">
                <span class="text-xs text-gray-400">Email</span>
                <span class="text-xs font-medium text-gray-800 dark:text-zinc-200 truncate max-w-[180px]">{{ selectedPatient.email || '—' }}</span>
              </div>
            </div>
          </div>

          <!-- Bottom Action -->
          <div class="p-5 border-t border-gray-100 dark:border-zinc-900">
            <button
              @click="handleCreateFollowUp"
              class="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2.5 rounded-lg text-sm transition-all active:scale-[0.98] shadow-sm hover:shadow shadow-blue-500/10 flex items-center justify-center gap-1.5"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4" />
              </svg>
              Nouveau Rendez-vous
            </button>
          </div>
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from "vue"
import { useRouter } from "vue-router"
import { getDoctorPatients } from "@/api/patientsService"

const router = useRouter()
const searchQuery = ref("")
const statusFilter = ref("All")
const selectedPatient = ref(null)

const patients = ref([])
const isLoading = ref(true)

// Local Client-side Pagination State
const currentPage = ref(1)
const itemsPerPage = ref(8)

const page = ref(1)
const pageSize = ref(100)
const total = ref(0)

const fetchPatients = async () => {
  try {
    isLoading.value = true
    const res = await getDoctorPatients({
      page: page.value,
      page_size: pageSize.value
    })

    const rows = res.results || []
    total.value = res.count || 0

    patients.value = rows.map((item) => ({
      id: item.patient_details?.code || "-",
      name: item.patient_details?.full_name || "-",
      email: item.patient_details?.email || "-",
      phone: item.patient_details?.phone || "-",
      gender: item.patient_details?.gender || "",
      lastVisitFormatted: item.last_consultation
        ? new Date(item.last_consultation).toLocaleDateString("fr-FR")
        : "Pas de visite",
      dateJoined: item.added_at
        ? new Date(item.added_at).toLocaleDateString("fr-FR")
        : "-",
      status: "Stable",
      bloodType: item.patient_details?.blood_group || "-",
      dob: item.patient_details?.date_of_birth || null,
      vitals: {
        bp: "12/8",
        hr: "72"
      }
    }))
  } catch (error) {
    console.error(error)
    patients.value = []
  } finally {
    isLoading.value = false
  }
}

onMounted(fetchPatients)

const filteredPatients = computed(() => {
  return patients.value.filter((p) => {
    const q = searchQuery.value.toLowerCase().trim()
    const matchesStatus = statusFilter.value === "All" || p.status === statusFilter.value
    
    if (!matchesStatus) return false
    if (!q) return true

    return (
      p.name.toLowerCase().includes(q) ||
      p.id.toLowerCase().includes(q) ||
      p.phone.toLowerCase().includes(q) ||
      p.bloodType.toLowerCase().includes(q)
    )
  })
})

const totalPages = computed(() => {
  return Math.ceil(filteredPatients.value.length / itemsPerPage.value) || 1
})

const startIndex = computed(() => (currentPage.value - 1) * itemsPerPage.value)
const endIndex = computed(() => startIndex.value + itemsPerPage.value)

const paginatedPatients = computed(() => {
  return filteredPatients.value.slice(startIndex.value, endIndex.value)
})

const nextPage = () => {
  if (currentPage.value < totalPages.value) currentPage.value++
}

const prevPage = () => {
  if (currentPage.value > 1) currentPage.value--
}

watch([searchQuery, statusFilter], () => {
  currentPage.value = 1
})

const isMale = (gender) => gender === "M" || gender === "Male"
const openDetails = (patient) => { selectedPatient.value = patient }
const closeDetails = () => { selectedPatient.value = null }

const statusClasses = (status) => {
  switch (status) {
    case 'Stable': 
      return 'bg-emerald-50/60 text-emerald-700 border-emerald-100 dark:bg-emerald-500/5 dark:text-emerald-400 dark:border-emerald-500/10'
    case 'Pending': 
      return 'bg-amber-50/50 text-amber-700 border-amber-100 dark:bg-amber-500/5 dark:text-amber-400 dark:border-amber-500/10'
    case 'Urgent': 
      return 'bg-rose-50/60 text-rose-700 border-rose-100 dark:bg-rose-500/5 dark:text-rose-400 dark:border-rose-500/10'
    default: 
      return 'bg-gray-50 text-gray-700 border-gray-200 dark:bg-zinc-900 dark:text-zinc-400 dark:border-zinc-800'
  }
}

function calculateAge(dob) {
  if (!dob) return "—"
  const birthDate = new Date(dob)
  const diff = Date.now() - birthDate.getTime()
  const ageDate = new Date(diff)
  return Math.abs(ageDate.getUTCFullYear() - 1970)
}

const resetFilters = () => {
  searchQuery.value = ""
  statusFilter.value = "All"
  currentPage.value = 1
}

const handleCreateFollowUp = () => {
  if (!selectedPatient.value) return
  router.push({
    path: "/appointments/create",
    query: { patient_code: selectedPatient.value.id },
  })
  closeDetails()
}

const goToPatient = () => {
  if (!selectedPatient.value) return
  router.push({
    name: "patient-details",
    params: { code: selectedPatient.value.id }
  })
  closeDetails()
}
</script>

<script>
export default { name: "PatientTable" }
</script>

<style scoped>
.slide-enter-active, .slide-leave-active { 
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1); 
}
.slide-enter-from, .slide-leave-to { 
  transform: translateX(100%); 
}

.custom-scrollbar::-webkit-scrollbar {
  height: 5px;
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