<template>
  <div class="w-full relative pb-20">
    <form @submit.prevent="handleSubmit" class="grid grid-cols-1 lg:grid-cols-12 gap-5 items-start">
      <!-- Column 1: Patient Selection & Period -->
      <div class="lg:col-span-4 flex flex-col space-y-5">
        <!-- Patient Search Card -->
        <div
          class="bg-white dark:bg-zinc-950 rounded-3xl border border-slate-200 dark:border-zinc-800 p-6 shadow-sm"
        >
          <div class="flex items-center gap-3 mb-6">
            <div
              class="w-10 h-10 rounded-xl bg-brand-50 dark:bg-brand-500/10 flex items-center justify-center text-brand-600"
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
            <h2 class="text-xl font-bold dark:text-white">Patient</h2>
          </div>

          <!-- Search Section -->
          <div v-if="!selectedPatient" class="space-y-4">
            <div class="relative">
              <div class="absolute inset-y-0 left-4 flex items-center pointer-events-none">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5 text-gray-400"
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
              </div>
              <input
                v-model="searchQuery"
                @input="handleSearch"
                type="text"
                placeholder="Rechercher par nom, téléphone..."
                class="w-full pl-12 pr-4 py-3 rounded-2xl border border-slate-200 dark:border-zinc-700 dark:bg-zinc-900 focus:ring-2 focus:ring-brand-500 outline-none dark:text-white shadow-sm"
              />
            </div>

            <!-- Loading State -->
            <div v-if="searching" class="text-center py-8">
              <div
                class="inline-block h-8 w-8 animate-spin rounded-full border-4 border-solid border-brand-600 border-r-transparent"
              ></div>
              <p class="text-sm text-gray-500 mt-2">Recherche...</p>
            </div>

            <!-- Search Results -->
            <div
              v-if="!searching && searchResults.length > 0"
              class="border border-slate-100 dark:border-zinc-800 rounded-2xl overflow-hidden divide-y divide-slate-50 dark:divide-zinc-800"
            >
              <div
                v-for="patient in searchResults"
                :key="patient.code"
                @click="selectPatient(patient)"
                class="p-4 hover:bg-brand-50 dark:hover:bg-brand-500/10 cursor-pointer transition-all flex justify-between items-center group"
              >
                <div class="flex-1">
                  <div class="flex items-center gap-2">
                    <span
                      class="text-xs font-mono bg-slate-100 dark:bg-zinc-800 px-2 py-1 rounded-lg text-slate-600 dark:text-slate-400 font-bold"
                    >
                      {{ patient.code }}
                    </span>
                    <p class="font-bold text-gray-900 dark:text-gray-100">
                      {{ patient.first_name }} {{ patient.last_name }}
                    </p>
                  </div>
                  <p class="text-sm text-gray-500 mt-1 flex items-center gap-1.5">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="h-3.5 w-3.5"
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
                    {{ patient.phone || 'Pas de téléphone' }}
                  </p>
                </div>
              </div>
            </div>

            <!-- No Results & New Patient Form -->
            <div
              v-if="!searching && searchQuery.length >= 2 && searchResults.length === 0"
              class="mt-6 p-5 bg-slate-50 dark:bg-zinc-900/30 rounded-2xl border-2 border-dashed border-slate-200 dark:border-zinc-700"
            >
              <div class="flex items-center gap-2 mb-4">
                <span
                  class="flex h-6 w-6 items-center justify-center rounded-full bg-brand-100 dark:bg-brand-900 text-xs text-brand-600 font-bold"
                  >+</span
                >
                <p class="text-xs font-bold text-slate-500 uppercase tracking-wider">
                  Nouveau Patient
                </p>
              </div>
              <div class="space-y-3">
                <div class="grid grid-cols-2 gap-3">
                  <input
                    v-model="form.patient_first_name"
                    type="text"
                    placeholder="Prénom *"
                    class="w-full px-4 py-2.5 rounded-xl border border-slate-200 dark:border-zinc-700 dark:bg-zinc-900 focus:ring-2 focus:ring-brand-500 outline-none shadow-sm text-sm"
                  />
                  <input
                    v-model="form.patient_last_name"
                    type="text"
                    placeholder="Nom *"
                    class="w-full px-4 py-2.5 rounded-xl border border-slate-200 dark:border-zinc-700 dark:bg-zinc-900 focus:ring-2 focus:ring-brand-500 outline-none shadow-sm text-sm"
                  />
                </div>
                <input
                  v-model="form.patient_phone"
                  type="tel"
                  placeholder="Numéro de téléphone *"
                  class="w-full px-4 py-2.5 rounded-xl border border-slate-200 dark:border-zinc-700 dark:bg-zinc-900 focus:ring-2 focus:ring-brand-500 outline-none shadow-sm text-sm"
                />
              </div>
            </div>
          </div>

          <!-- Selected Patient Card -->
          <div v-else class="relative overflow-hidden">
            <div
              class="bg-brand-50 border border-brand-100 dark:border-brand-900/30 dark:bg-brand-900/10 rounded-2xl p-5 shadow-sm"
            >
              <div class="flex items-start justify-between">
                <div>
                  <p class="text-[10px] font-bold text-brand-600 uppercase tracking-wider mb-2">
                    Patient sélectionné
                  </p>
                  <span
                    class="inline-block text-xs font-mono bg-white dark:bg-zinc-900 border border-brand-200 dark:border-brand-800 px-2 py-1 rounded-lg text-brand-700 dark:text-brand-400 font-bold mb-2"
                  >
                    {{ selectedPatient.code }}
                  </span>
                  <h3 class="text-lg font-bold text-gray-900 dark:text-white leading-tight mb-2">
                    {{ selectedPatient.first_name }} {{ selectedPatient.last_name }}
                  </h3>
                  <div class="space-y-1">
                    <p
                      v-if="selectedPatient.phone"
                      class="text-gray-500 dark:text-gray-400 text-xs flex items-center gap-1.5"
                    >
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        class="h-3.5 w-3.5"
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
                      {{ selectedPatient.phone }}
                    </p>
                  </div>
                </div>
                <button
                  @click="clearSelectedPatient"
                  type="button"
                  class="h-8 w-8 bg-white dark:bg-zinc-800 border border-slate-200 dark:border-zinc-700 hover:bg-slate-50 rounded-lg flex items-center justify-center text-gray-400 hover:text-gray-600 transition-all shadow-sm"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-4 w-4"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M6 18L18 6M6 6l12 12"
                    />
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Period Selection Card -->
        <div
          class="bg-white dark:bg-zinc-950 rounded-3xl border border-slate-200 dark:border-zinc-800 p-6 shadow-sm"
        >
          <div class="flex items-center gap-3 mb-5">
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
                  d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"
                />
              </svg>
            </div>
            <h2 class="text-xl font-bold dark:text-white">Période</h2>
          </div>

          <div class="grid grid-cols-2 gap-3">
            <label class="cursor-pointer relative">
              <input
                type="radio"
                v-model="form.period"
                value="morning"
                @change="onPeriodChange"
                class="peer sr-only"
              />
              <div
                class="p-4 rounded-2xl border-2 border-slate-100 dark:border-zinc-800 hover:border-brand-200 peer-checked:border-brand-600 peer-checked:bg-brand-50 dark:peer-checked:bg-brand-900/20 transition-all text-center"
              >
                <span class="block text-2xl mb-1">🌅</span>
                <span class="block text-sm font-bold text-gray-900 dark:text-white">Matin</span>
                <span class="block text-xs text-gray-500 mt-0.5">08:00 - 12:00</span>
              </div>
            </label>
            <label class="cursor-pointer relative">
              <input
                type="radio"
                v-model="form.period"
                value="afternoon"
                @change="onPeriodChange"
                class="peer sr-only"
              />
              <div
                class="p-4 rounded-2xl border-2 border-slate-100 dark:border-zinc-800 hover:border-brand-200 peer-checked:border-brand-600 peer-checked:bg-brand-50 dark:peer-checked:bg-brand-900/20 transition-all text-center"
              >
                <span class="block text-2xl mb-1">☀️</span>
                <span class="block text-sm font-bold text-gray-900 dark:text-white"
                  >Après-midi</span
                >
                <span class="block text-xs text-gray-500 mt-0.5">13:00 - 17:00</span>
              </div>
            </label>
          </div>
        </div>
      </div>

      <!-- Column 2: Interactive Calendar -->
      <div class="lg:col-span-8 flex flex-col">
        <!-- Constrain the calendar card itself so it doesn't stretch infinitely -->
        <div
          class="bg-white dark:bg-zinc-950 rounded-3xl border border-slate-200 dark:border-zinc-800 p-6 shadow-sm w-full flex flex-col relative overflow-hidden"
        >
          <div class="flex items-center justify-between mb-5">
            <div class="flex items-center gap-3">
              <div
                class="w-10 h-10 rounded-xl bg-indigo-50 dark:bg-indigo-500/10 flex items-center justify-center text-indigo-600"
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
                    d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
                  />
                </svg>
              </div>
              <div>
                <h2 class="text-xl font-bold dark:text-white">Calendrier</h2>
                <p class="text-sm text-gray-500">Sélectionnez une date avec des disponibilités</p>
              </div>
            </div>

            <!-- Month Navigation -->
            <div class="flex items-center gap-2">
              <button
                type="button"
                @click="prevMonth"
                class="p-2 text-slate-400 hover:text-brand-600 hover:bg-brand-50 rounded-full transition-all"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M15 19l-7-7 7-7"
                  />
                </svg>
              </button>
              <span
                class="font-bold text-slate-800 dark:text-white min-w-[120px] text-center capitalize text-sm"
                >{{ monthName }}</span
              >
              <button
                type="button"
                @click="nextMonth"
                class="p-2 text-slate-400 hover:text-brand-600 hover:bg-brand-50 rounded-full transition-all"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-4 w-4"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M9 5l7 7-7 7"
                  />
                </svg>
              </button>
            </div>
          </div>

          <!-- Calendar Grid -->
          <div class="flex-1 w-full mt-2">
            <!-- Days of Week -->
            <div class="grid grid-cols-7 gap-2 mb-2">
              <div
                v-for="day in weekDays"
                :key="day"
                class="text-center text-xs font-bold text-slate-400 uppercase tracking-wider py-2"
              >
                {{ day }}
              </div>
            </div>

            <!-- Dates Grid -->
            <div class="grid grid-cols-7 gap-1.5 relative min-h-[250px]">
              <!-- Loading Overlay -->
              <div
                v-if="loadingDates"
                class="absolute inset-0 bg-white/80 dark:bg-zinc-950/80 backdrop-blur-sm flex items-center justify-center z-10 rounded-xl"
              >
                <div
                  class="animate-spin h-6 w-6 border-4 border-brand-600 border-t-transparent rounded-full"
                ></div>
              </div>

              <template v-for="(day, index) in calendarDays" :key="index">
                <!-- Empty Cell -->
                <div v-if="day.empty" class="h-12 w-full bg-transparent"></div>

                <!-- Date Cell -->
                <button
                  v-else
                  type="button"
                  :disabled="!day.isAvailable || day.isPast"
                  @click="day.isAvailable ? selectDate(day.fullDate) : null"
                  :class="[
                    'relative flex flex-col items-center justify-center rounded-xl border transition-all h-12 w-full max-w-[3rem] mx-auto outline-none focus:ring-2 focus:ring-brand-500 focus:ring-offset-1',
                    day.isPast || !day.isAvailable
                      ? 'bg-slate-50/50 dark:bg-zinc-900/30 border-slate-100 dark:border-zinc-800/50 text-slate-300 dark:text-zinc-600 cursor-not-allowed'
                      : form.appointment_date === day.fullDate
                        ? 'bg-brand-50 dark:bg-brand-900/30 border-brand-600 text-brand-700 dark:text-brand-300 shadow-md ring-1 ring-brand-600 z-10 scale-[1.02]'
                        : 'bg-white dark:bg-zinc-950 border-slate-200 dark:border-zinc-800 text-slate-700 dark:text-slate-300 hover:border-brand-400 hover:shadow-sm cursor-pointer',
                  ]"
                >
                  <span
                    :class="[
                      'text-sm font-semibold',
                      form.appointment_date === day.fullDate
                        ? 'text-brand-700 dark:text-brand-300 font-bold'
                        : '',
                    ]"
                    >{{ day.date }}</span
                  >

                  <!-- Slots Text Indicator -->
                  <span
                    v-if="day.isAvailable"
                    :class="[
                      'text-[10px] mt-0.5 leading-none',
                      form.appointment_date === day.fullDate
                        ? 'text-brand-600 dark:text-brand-400 font-bold'
                        : 'text-brand-500 dark:text-brand-500 font-medium',
                    ]"
                  >
                    {{ day.availableSlots }} pl.
                  </span>
                </button>
              </template>
            </div>
          </div>

          <!-- Error Alert -->
          <transition name="fade">
            <div v-if="errorMessage" class="mt-6">
              <div
                class="p-4 bg-red-50 dark:bg-red-900/20 rounded-xl border border-red-100 dark:border-red-800"
              >
                <div class="flex items-center gap-3">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5 text-red-600 shrink-0"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                    />
                  </svg>
                  <p class="text-sm font-medium text-red-700 dark:text-red-400">
                    {{ errorMessage }}
                  </p>
                </div>
              </div>
            </div>
          </transition>

          <!-- Footer Actions -->
          <div
            class="flex flex-col-reverse sm:flex-row items-center justify-end gap-3 mt-8 pt-6 border-t border-slate-100 dark:border-zinc-800"
          >
            <button
              type="button"
              @click="resetForm"
              class="w-full sm:w-auto px-6 py-2.5 rounded-xl text-slate-500 font-bold hover:bg-slate-100 dark:hover:bg-zinc-800 transition-all text-sm"
            >
              Réinitialiser
            </button>
            <button
              type="button"
              @click="$router.back()"
              class="w-full sm:w-auto px-6 py-2.5 rounded-xl text-slate-500 font-bold hover:bg-slate-100 dark:hover:bg-zinc-800 transition-all text-sm"
            >
              Annuler
            </button>
            <button
              type="submit"
              :disabled="loading || !isFormValid"
              class="w-full sm:w-auto px-8 py-2.5 rounded-xl bg-brand-600 text-white font-bold hover:bg-brand-700 shadow-md shadow-brand-500/20 transition-all active:scale-95 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2 text-sm"
            >
              <svg
                v-if="loading"
                class="animate-spin h-4 w-4 text-white"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
              >
                <circle
                  class="opacity-25"
                  cx="12"
                  cy="12"
                  r="10"
                  stroke="currentColor"
                  stroke-width="4"
                ></circle>
                <path
                  class="opacity-75"
                  fill="currentColor"
                  d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                ></path>
              </svg>
              <span>{{ loading ? 'Enregistrement...' : 'Confirmer Rendez-vous' }}</span>
            </button>
          </div>
        </div>
      </div>
    </form>
  </div>
</template>

<script setup>
import { reactive, ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import {
  createDoctorAppointment,
  searchPatients,
  getAvailableSlots,
} from '@/api/appointmentService'
import { getPatientByCode } from '@/api/patientsService'

const router = useRouter()
const route = useRoute()

// State
const loading = ref(false)
const loadingDates = ref(false)
const searching = ref(false)
const errorMessage = ref('')
const searchQuery = ref('')
const searchResults = ref([])
const selectedPatient = ref(null)
const availableDates = ref([])

const today = new Date()
const minDate = today.toISOString().split('T')[0]

const form = reactive({
  appointment_date: '',
  period: 'morning',
  patient_first_name: '',
  patient_last_name: '',
  patient_phone: '',
})

// Validation
const isFormValid = computed(() => {
  if (!form.appointment_date) return false
  if (selectedPatient.value) return true
  return form.patient_first_name && form.patient_last_name && form.patient_phone
})

// Calendar Logic
const currentMonth = ref(today.getMonth())
const currentYear = ref(today.getFullYear())
const weekDays = ['Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim']

const calendarDays = computed(() => {
  const days = []
  let firstDay = new Date(currentYear.value, currentMonth.value, 1).getDay()
  let startDay = firstDay === 0 ? 6 : firstDay - 1

  const daysInMonth = new Date(currentYear.value, currentMonth.value + 1, 0).getDate()

  // Padding
  for (let i = 0; i < startDay; i++) {
    days.push({ empty: true })
  }

  // Days
  for (let i = 1; i <= daysInMonth; i++) {
    const dateStr = `${currentYear.value}-${String(currentMonth.value + 1).padStart(2, '0')}-${String(i).padStart(2, '0')}`
    const availableSlot = availableDates.value.find((slot) => slot.date === dateStr)
    const isPast = new Date(dateStr) < new Date(minDate)

    days.push({
      empty: false,
      date: i,
      fullDate: dateStr,
      isAvailable: !!availableSlot && !isPast,
      availableSlots: availableSlot ? availableSlot.available_slots : 0,
      totalSlots: availableSlot ? availableSlot.total_slots : 0,
      isPast,
    })
  }
  return days
})

const nextMonth = () => {
  if (currentMonth.value === 11) {
    currentMonth.value = 0
    currentYear.value++
  } else {
    currentMonth.value++
  }
}

const prevMonth = () => {
  if (currentMonth.value === 0) {
    currentMonth.value = 11
    currentYear.value--
  } else {
    currentMonth.value--
  }
}

const monthName = computed(() => {
  const name = new Date(currentYear.value, currentMonth.value).toLocaleString('fr-FR', {
    month: 'long',
    year: 'numeric',
  })
  return name.charAt(0).toUpperCase() + name.slice(1)
})

const loadAvailableDates = async () => {
  loadingDates.value = true
  try {
    const slots = await getAvailableSlots(form.period)
    availableDates.value = slots

    // Auto-select first available if empty
    if (slots.length > 0 && !form.appointment_date) {
      const firstValid = slots.find((s) => new Date(s.date) >= new Date(minDate))
      if (firstValid) form.appointment_date = firstValid.date
    }
  } catch (error) {
    console.error('Error loading dates:', error)
    availableDates.value = []
  } finally {
    loadingDates.value = false
  }
}

const onPeriodChange = () => {
  form.appointment_date = ''
  loadAvailableDates()
}

const selectDate = (date) => {
  form.appointment_date = date
}

// Patient Logic
const handleSearch = async () => {
  const query = searchQuery.value.trim()
  if (query.length < 2) {
    searchResults.value = []
    return
  }

  searching.value = true
  try {
    searchResults.value = await searchPatients(query)
  } catch (error) {
    console.error('Search error:', error)
    searchResults.value = []
  } finally {
    searching.value = false
  }
}

const selectPatient = (patient) => {
  selectedPatient.value = patient
  searchResults.value = []
  searchQuery.value = ''
  form.patient_first_name = ''
  form.patient_last_name = ''
  form.patient_phone = ''
}

const clearSelectedPatient = () => {
  selectedPatient.value = null
  searchQuery.value = ''
}

const resetForm = () => {
  form.appointment_date = ''
  form.period = 'morning'
  form.patient_first_name = ''
  form.patient_last_name = ''
  form.patient_phone = ''
  selectedPatient.value = null
  searchQuery.value = ''
  errorMessage.value = ''
  loadAvailableDates()
}

// Init & Submit
onMounted(async () => {
  if (route.query.patient_code) {
    try {
      selectedPatient.value = await getPatientByCode(route.query.patient_code)
    } catch (e) {
      console.error(e)
      errorMessage.value = 'Impossible de charger le patient.'
    }
  }
  loadAvailableDates()
})

const handleSubmit = async () => {
  if (!isFormValid.value) {
    errorMessage.value = 'Veuillez remplir tous les champs obligatoires'
    return
  }

  loading.value = true
  errorMessage.value = ''

  try {
    const payload = {
      appointment_date: form.appointment_date,
      period: form.period,
      patient_code: selectedPatient.value ? selectedPatient.value.code : null,
      patient_first_name: selectedPatient.value ? '' : form.patient_first_name,
      patient_last_name: selectedPatient.value ? '' : form.patient_last_name,
      patient_phone: selectedPatient.value ? '' : form.patient_phone,
    }

    await createDoctorAppointment(payload)
    router.push('/appointments')
  } catch (err) {
    errorMessage.value = err.response?.data?.detail || 'Erreur lors de la création du rendez-vous.'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
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
  background: #f1f5f9;
  border-radius: 3px;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background: #cbd5e1;
  border-radius: 3px;
}
.dark .custom-scrollbar::-webkit-scrollbar-track {
  background: #18181b;
}
.dark .custom-scrollbar::-webkit-scrollbar-thumb {
  background: #3f3f46;
}
</style>
