<template>
  <div class="space-y-4">
    <div class="overflow-hidden rounded-xl border border-gray-200 bg-white dark:border-gray-800 dark:bg-white/[0.03]">
      <div class="max-w-full overflow-x-auto custom-scrollbar">
        <form @submit.prevent="handleSubmit" class="grid grid-cols-1 gap-6 p-4">
          
          <!-- Card 1: Patient Selection -->
          <div class="bg-white dark:bg-white/[0.03] rounded-3xl border border-gray-100 dark:border-gray-800 p-8 shadow-sm">
            <div class="flex items-center gap-3 mb-6">
              <div class="w-10 h-10 rounded-xl bg-blue-50 dark:bg-blue-500/10 flex items-center justify-center text-blue-600">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                </svg>
              </div>
              <h2 class="text-lg font-bold dark:text-white">Patient</h2>
            </div>

            <!-- Search Section -->
            <div v-if="!selectedPatient" class="space-y-4">
              <div class="relative">
                <div class="absolute inset-y-0 left-4 flex items-center pointer-events-none">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                  </svg>
                </div>
                <input 
                  v-model="searchQuery" 
                  @input="handleSearch"
                  type="text"
                  placeholder="Rechercher par nom, téléphone ou code patient..."
                  class="w-full pl-12 pr-4 py-3.5 rounded-2xl border border-gray-200 dark:border-gray-700 dark:bg-gray-900 focus:ring-2 focus:ring-blue-500 outline-none dark:text-white"
                />
              </div>

              <!-- Loading State -->
              <div v-if="searching" class="text-center py-8">
                <div class="inline-block h-8 w-8 animate-spin rounded-full border-4 border-solid border-blue-600 border-r-transparent"></div>
                <p class="text-sm text-gray-500 mt-2">Recherche en cours...</p>
              </div>

              <!-- Search Results -->
              <div v-if="!searching && searchResults.length > 0" class="border border-gray-100 dark:border-gray-700 rounded-2xl overflow-hidden divide-y divide-gray-50 dark:divide-gray-800">
                <div 
                  v-for="patient in searchResults" 
                  :key="patient.code"
                  @click="selectPatient(patient)"
                  class="p-4 hover:bg-blue-50 dark:hover:bg-blue-500/10 cursor-pointer transition-all flex justify-between items-center group"
                >
                  <div class="flex-1">
                    <div class="flex items-center gap-2">
                      <span class="text-xs font-mono bg-gray-100 dark:bg-gray-800 px-2 py-1 rounded-lg text-gray-600 dark:text-gray-400">
                        {{ patient.code }}
                      </span>
                      <p class="font-semibold text-gray-800 dark:text-gray-100">
                        {{ patient.first_name }} {{ patient.last_name }}
                      </p>
                    </div>
                    <p class="text-sm text-gray-500 dark:text-gray-400 mt-1">
                      📞 {{ patient.phone || 'Pas de téléphone' }}
                    </p>
                    <p v-if="patient.email" class="text-xs text-gray-400 mt-1">
                      ✉️ {{ patient.email }}
                    </p>
                  </div>
                  <div class="opacity-0 group-hover:opacity-100 transition-all">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                    </svg>
                  </div>
                </div>
              </div>

              <!-- No Results & New Patient Form -->
              <div v-if="!searching && searchQuery.length >= 2 && searchResults.length === 0" 
                   class="mt-6 p-6 bg-gray-50 dark:bg-gray-900/30 rounded-2xl border-2 border-dashed border-gray-200 dark:border-gray-700">
                <div class="flex items-center gap-2 mb-4">
                  <span class="flex h-6 w-6 items-center justify-center rounded-full bg-blue-100 dark:bg-blue-900 text-xs text-blue-600 font-bold">+</span>
                  <p class="text-xs font-bold text-gray-500 uppercase tracking-wider">Nouveau Patient</p>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <input 
                    v-model="form.patient_first_name" 
                    type="text"
                    placeholder="Prénom *" 
                    class="w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-700 dark:bg-gray-900 focus:ring-2 focus:ring-blue-500 outline-none dark:text-white"
                  />
                  <input 
                    v-model="form.patient_last_name" 
                    type="text"
                    placeholder="Nom *" 
                    class="w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-700 dark:bg-gray-900 focus:ring-2 focus:ring-blue-500 outline-none dark:text-white"
                  />
                </div>
                <input 
                  v-model="form.patient_phone" 
                  type="tel"
                  placeholder="Numéro de téléphone *" 
                  class="mt-4 w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-700 dark:bg-gray-900 focus:ring-2 focus:ring-blue-500 outline-none dark:text-white"
                />
              </div>
            </div>

            <!-- Selected Patient Card -->
            <div v-else class="relative overflow-hidden">
              <div class="bg-gradient-to-r from-blue-600 to-blue-700 rounded-2xl p-6">
                <div class="relative z-10">
                  <div class="flex items-start justify-between">
                    <div>
                      <p class="text-xs font-bold text-blue-100 uppercase tracking-wider mb-2">Patient sélectionné</p>
                      <div class="flex items-center gap-2 mb-2">
                        <span class="text-xs font-mono bg-white/20 px-2 py-1 rounded-lg text-white">
                          {{ selectedPatient.code }}
                        </span>
                      </div>
                      <h3 class="text-xl font-bold text-white mb-1">{{ selectedPatient.first_name }} {{ selectedPatient.last_name }}</h3>
                      <div class="space-y-1 mt-2">
                        <p v-if="selectedPatient.phone" class="text-blue-100 text-sm flex items-center gap-2">
                          📞 {{ selectedPatient.phone }}
                        </p>
                        <p v-if="selectedPatient.email" class="text-blue-100 text-sm flex items-center gap-2">
                          ✉️ {{ selectedPatient.email }}
                        </p>
                      </div>
                    </div>
                    <button 
                      @click="clearSelectedPatient" 
                      type="button"
                      class="h-10 w-10 bg-white/10 hover:bg-white/20 rounded-xl flex items-center justify-center text-white transition-all"
                    >
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                      </svg>
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Card 2: Rendez-vous Details with Enhanced Date Selection -->
          <div class="bg-white dark:bg-white/[0.03] rounded-3xl border border-gray-100 dark:border-gray-800 p-8 shadow-sm">
            <div class="flex items-center gap-3 mb-6">
              <div class="w-10 h-10 rounded-xl bg-amber-50 dark:bg-amber-500/10 flex items-center justify-center text-amber-600">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                </svg>
              </div>
              <h2 class="text-lg font-bold dark:text-white">Détails du Rendez-vous</h2>
            </div>

            <!-- Period Selection + Date Search Row -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
              <!-- Period Selection -->
              <div class="space-y-2">
                <label class="text-xs font-bold text-gray-400 uppercase tracking-wider ml-1">Période *</label>
                <div class="relative">
                  <select 
                    v-model="form.period" 
                    @change="onPeriodChange"
                    class="w-full px-4 py-3.5 rounded-2xl border border-gray-200 dark:border-gray-700 dark:bg-gray-900 focus:ring-2 focus:ring-blue-500 outline-none appearance-none dark:text-white cursor-pointer"
                  >
                    <option value="morning">🌅 Matin (08:00 - 12:00)</option>
                    <option value="afternoon">☀️ Après-midi (13:00 - 17:00)</option>
                  </select>
                  <div class="absolute inset-y-0 right-4 flex items-center pointer-events-none">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                    </svg>
                  </div>
                </div>
              </div>

              <!-- Date Search Input -->
              <div class="space-y-2 md:col-span-2">
                <label class="text-xs font-bold text-gray-400 uppercase tracking-wider ml-1">
                  Rechercher une date spécifique
                </label>
                <div class="relative">
                  <div class="absolute inset-y-0 left-4 flex items-center pointer-events-none">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                    </svg>
                  </div>
                  <input 
                    type="date" 
                    v-model="dateSearchQuery"
                    @change="searchSpecificDate"
                    :min="minDate"
                    class="w-full pl-12 pr-4 py-3.5 rounded-2xl border border-gray-200 dark:border-gray-700 dark:bg-gray-900 focus:ring-2 focus:ring-blue-500 outline-none dark:text-white"
                  />
                  <button 
                    v-if="dateSearchQuery"
                    @click="clearDateSearch"
                    type="button"
                    class="absolute inset-y-0 right-4 flex items-center text-gray-400 hover:text-gray-600"
                  >
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                  </button>
                </div>
              </div>
            </div>

            <!-- Available Dates with Tabs/Filter -->
            <div class="space-y-4">
              <div class="flex items-center justify-between">
                <label class="text-xs font-bold text-gray-400 uppercase tracking-wider ml-1">
                  Dates disponibles
                  <span v-if="loadingDates" class="ml-2 text-blue-500">Chargement...</span>
                </label>
                
                <!-- Filter Buttons -->
                <div class="flex gap-2">
                  <button 
                    type="button"
                    @click="dateFilter = 'all'"
                    :class="[
                      'px-3 py-1 rounded-lg text-xs font-medium transition-all',
                      dateFilter === 'all' 
                        ? 'bg-blue-600 text-white' 
                        : 'bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-400 hover:bg-gray-200'
                    ]"
                  >
                    Toutes
                  </button>
                  <button 
                    type="button"
                    @click="dateFilter = 'week'"
                    :class="[
                      'px-3 py-1 rounded-lg text-xs font-medium transition-all',
                      dateFilter === 'week' 
                        ? 'bg-blue-600 text-white' 
                        : 'bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-400 hover:bg-gray-200'
                    ]"
                  >
                    Cette semaine
                  </button>
                  <button 
                    type="button"
                    @click="dateFilter = 'month'"
                    :class="[
                      'px-3 py-1 rounded-lg text-xs font-medium transition-all',
                      dateFilter === 'month' 
                        ? 'bg-blue-600 text-white' 
                        : 'bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-400 hover:bg-gray-200'
                    ]"
                  >
                    Ce mois
                  </button>
                </div>
              </div>
              
              <!-- Calendar/Grid View of Available Dates -->
              <div v-if="!loadingDates && filteredAvailableDates.length > 0" class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3">
                <div 
                  v-for="slot in filteredAvailableDates" 
                  :key="slot.date"
                  @click="selectDate(slot.date)"
                  :class="[
                    'p-4 rounded-2xl border-2 cursor-pointer transition-all transform hover:scale-105',
                    form.appointment_date === slot.date
                      ? 'border-blue-600 bg-blue-50 dark:bg-blue-900/20 shadow-md'
                      : 'border-gray-200 dark:border-gray-700 hover:border-blue-300 hover:shadow-sm'
                  ]"
                >
                  <div class="text-center">
                    <div class="text-sm font-bold text-gray-700 dark:text-gray-300">
                      {{ formatDateShort(slot.date) }}
                    </div>
                    <div class="text-xs text-gray-500 mt-1">
                      {{ slot.available_slots }} / {{ slot.total_slots }} places
                    </div>
                    <div class="mt-2">
                      <div class="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-1.5">
                        <div 
                          class="bg-blue-600 h-1.5 rounded-full transition-all"
                          :style="{ width: `${(slot.available_slots / slot.total_slots) * 100}%` }"
                        ></div>
                      </div>
                    </div>
                    <div v-if="slot.available_slots <= 3" class="mt-2">
                      <span class="text-xs text-orange-600 font-semibold">⚠️ Places limitées</span>
                    </div>
                  </div>
                </div>
              </div>

              <!-- No Results -->
              <div v-if="!loadingDates && filteredAvailableDates.length === 0 && availableDates.length > 0" 
                   class="text-center py-8 bg-gray-50 dark:bg-gray-900/30 rounded-2xl">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12 text-gray-400 mx-auto mb-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                <p class="text-gray-500 dark:text-gray-400">Aucune date ne correspond à votre filtre</p>
              </div>

              <!-- No Available Dates Message -->
              <div v-if="!loadingDates && availableDates.length === 0" 
                   class="text-center py-8 bg-amber-50 dark:bg-amber-900/20 rounded-2xl">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12 text-amber-600 mx-auto mb-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                <p class="text-amber-800 dark:text-amber-300 font-medium">Aucune date disponible pour cette période</p>
                <p class="text-sm text-amber-600 dark:text-amber-400 mt-1">
                  Essayez de changer de période ou contactez l'administrateur
                </p>
              </div>
            </div>

            <!-- Selected Date Summary -->
            <div v-if="form.appointment_date" class="mt-6 p-4 bg-gradient-to-r from-blue-50 to-indigo-50 dark:from-blue-900/20 dark:to-indigo-900/20 rounded-2xl">
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-blue-100 dark:bg-blue-900/50 flex items-center justify-center">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                  </svg>
                </div>
                <div>
                  <p class="text-xs text-gray-500 dark:text-gray-400">Rendez-vous sélectionné</p>
                  <p class="font-semibold text-gray-800 dark:text-white">
                    {{ formatDate(form.appointment_date) }} - {{ form.period === 'morning' ? 'Matin (08:00-12:00)' : 'Après-midi (13:00-17:00)' }}
                  </p>
                </div>
              </div>
            </div>
          </div>

          <!-- Error Alert -->
          <transition name="fade">
            <div v-if="errorMessage" class="mx-8">
              <div class="p-4 bg-red-50 dark:bg-red-900/20 rounded-2xl border border-red-100 dark:border-red-800">
                <div class="flex items-center gap-3">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-red-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                  <p class="text-sm text-red-600 dark:text-red-400">{{ errorMessage }}</p>
                </div>
              </div>
            </div>
          </transition>

          <!-- Footer Actions -->
          <div class="flex items-center justify-end gap-4 mt-4 px-8 pb-8">
            <button 
              type="button" 
              @click="resetForm" 
              class="px-8 py-3.5 rounded-2xl text-gray-500 font-bold hover:bg-gray-100 dark:hover:bg-gray-800 transition-all"
            >
              Réinitialiser
            </button>
            <button 
              type="button" 
              @click="$router.back()" 
              class="px-8 py-3.5 rounded-2xl text-gray-500 font-bold hover:bg-gray-100 dark:hover:bg-gray-800 transition-all"
            >
              Annuler
            </button>
            <button 
              type="submit" 
              :disabled="loading || !isFormValid" 
              class="px-10 py-3.5 rounded-2xl bg-blue-600 text-white font-bold hover:bg-blue-700 shadow-xl shadow-blue-500/25 transition-all active:scale-95 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
            >
              <svg v-if="loading" class="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              <span>{{ loading ? 'Enregistrement...' : 'Confirmer le Rendez-vous' }}</span>
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref, computed, onMounted } from "vue"
import { useRouter, useRoute } from "vue-router"
import { createDoctorAppointment, searchPatients, getAvailableSlots } from "@/api/appointmentService"
import { getPatientByCode } from "@/api/patientsService";
const router = useRouter();
const route = useRoute();
const patientCode = ref(route.query.patient_code || "");
const loading = ref(false)
const loadingDates = ref(false)
const searching = ref(false)
const errorMessage = ref("")
const searchQuery = ref("")
const searchResults = ref([])
const selectedPatient = ref(null)
const availableDates = ref([])
const dateSearchQuery = ref("")
const dateFilter = ref("all") // 'all', 'week', 'month'

const today = new Date()
const minDate = today.toISOString().split('T')[0]

const form = reactive({
  appointment_date: "",
  period: "morning",
  patient_first_name: "",
  patient_last_name: "",
  patient_phone: ""
})

const isFormValid = computed(() => {
  if (!form.appointment_date) return false
  if (selectedPatient.value) return true
  return form.patient_first_name && form.patient_last_name && form.patient_phone
})

// Filter available dates based on search and filter
const filteredAvailableDates = computed(() => {
  let filtered = [...availableDates.value]
  
  // Filter by date search
  if (dateSearchQuery.value) {
    filtered = filtered.filter(slot => slot.date === dateSearchQuery.value)
  }
  
  // Filter by week/month
  if (dateFilter.value === 'week') {
    const today = new Date()
    const nextWeek = new Date(today)
    nextWeek.setDate(today.getDate() + 7)
    filtered = filtered.filter(slot => {
      const slotDate = new Date(slot.date)
      return slotDate >= today && slotDate <= nextWeek
    })
  } else if (dateFilter.value === 'month') {
    const today = new Date()
    const nextMonth = new Date(today)
    nextMonth.setMonth(today.getMonth() + 1)
    filtered = filtered.filter(slot => {
      const slotDate = new Date(slot.date)
      return slotDate >= today && slotDate <= nextMonth
    })
  }
  
  return filtered
})

const loadAvailableDates = async () => {
  loadingDates.value = true
  
  try {
    const slots = await getAvailableSlots(form.period)
    availableDates.value = slots
    
    // Don't auto-select if there's a search query
    if (!dateSearchQuery.value && slots.length > 0 && !form.appointment_date) {
      form.appointment_date = slots[0].date
    }
  } catch (error) {
    console.error("Error loading dates:", error)
    availableDates.value = []
  } finally {
    loadingDates.value = false
  }
}

const onPeriodChange = () => {
  dateSearchQuery.value = ""
  dateFilter.value = "all"
  loadAvailableDates()
}

const searchSpecificDate = () => {
  if (dateSearchQuery.value) {
    // Check if the searched date is available
    const found = availableDates.value.find(slot => slot.date === dateSearchQuery.value)
    if (found) {
      form.appointment_date = found.date
      // Scroll to the selected date (optional)
    } else {
      errorMessage.value = "Cette date n'est pas disponible pour la période sélectionnée"
      setTimeout(() => {
        errorMessage.value = ""
      }, 3000)
    }
  }
}

const clearDateSearch = () => {
  dateSearchQuery.value = ""
  if (availableDates.value.length > 0 && !form.appointment_date) {
    form.appointment_date = availableDates.value[0].date
  }
}

const selectDate = (date) => {
  form.appointment_date = date
  dateSearchQuery.value = ""
}

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('fr-FR', { 
    weekday: 'long', 
    year: 'numeric', 
    month: 'long', 
    day: 'numeric' 
  })
}

const formatDateShort = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('fr-FR', { 
    weekday: 'short', 
    day: 'numeric', 
    month: 'short' 
  })
}

const handleSearch = async () => {
  const query = searchQuery.value.trim()
  
  if (query.length < 2) {
    searchResults.value = []
    return
  }
  
  searching.value = true
  
  try {
    const patients = await searchPatients(query)
    searchResults.value = patients
  } catch (error) {
    console.error("Search error:", error)
    searchResults.value = []
  } finally {
    searching.value = false
  }
}

const selectPatient = (patient) => {
  selectedPatient.value = patient
  searchResults.value = []
  searchQuery.value = ""
  form.patient_first_name = ""
  form.patient_last_name = ""
  form.patient_phone = ""
}

const clearSelectedPatient = () => {
  selectedPatient.value = null
  searchQuery.value = ""
}

const resetForm = () => {
  form.appointment_date = ""
  form.period = "morning"
  form.patient_first_name = ""
  form.patient_last_name = ""
  form.patient_phone = ""
  selectedPatient.value = null
  searchQuery.value = ""
  dateSearchQuery.value = ""
  dateFilter.value = "all"
  errorMessage.value = ""
  loadAvailableDates()
}

onMounted(async () => {
  if (route.query.patient_code) {
    try {
      selectedPatient.value = await getPatientByCode(
        route.query.patient_code
      );
    } catch (e) {
      console.error(e);
      errorMessage.value = "Impossible de charger le patient.";
    }
  }

  loadAvailableDates();
});

const handleSubmit = async () => {
  if (!isFormValid.value) {
    errorMessage.value = "Veuillez remplir tous les champs obligatoires"
    return
  }
  
  loading.value = true
  errorMessage.value = ""
  
  try {
    const payload = {
      appointment_date: form.appointment_date,
      period: form.period,
      patient_code: selectedPatient.value ? selectedPatient.value.code : null,
      patient_first_name: selectedPatient.value ? "" : form.patient_first_name,
      patient_last_name: selectedPatient.value ? "" : form.patient_last_name,
      patient_phone: selectedPatient.value ? "" : form.patient_phone
    }
    
    await createDoctorAppointment(payload)
    router.push("/appointments")
  } catch (err) {
    errorMessage.value = err.response?.data?.detail || "Erreur lors de la création du rendez-vous."
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: all 0.3s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.animate-spin {
  animation: spin 1s linear infinite;
}

.custom-scrollbar::-webkit-scrollbar {
  height: 6px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 3px;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background: #cbd5e1;
  border-radius: 3px;
}
</style>