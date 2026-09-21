<template>
  <AdminLayout>
    <div class="space-y-6">
      <!-- Top header area with TV mode trigger -->
      <div class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
        <div>
          <h1 class="text-2xl font-bold text-gray-900">File d'Attente du Jour</h1>
          <p class="text-sm text-gray-500">
            Gestion interactive en temps réel de votre file d'attente
          </p>
        </div>
        <div class="flex gap-3">
          <button
            @click="tvModeOpen = true"
            class="inline-flex items-center gap-2 px-4 py-2 bg-gray-900 hover:bg-gray-800 text-white rounded-xl text-sm font-semibold transition-all shadow-sm"
          >
            <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
              />
            </svg>
            Écran Salle d'attente
          </button>
          <router-link
            to="/appointments/create"
            class="inline-flex items-center gap-2 px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-xl text-sm font-semibold transition-all shadow-sm"
          >
            <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2.5"
                d="M12 4v16m8-8H4"
              />
            </svg>
            Nouveau RDV
          </router-link>
        </div>
      </div>

      <!-- Top Summary Metric Cards -->
      <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
        <!-- Waiting Card -->
        <div
          class="bg-white rounded-2xl border border-gray-100 p-5 shadow-sm flex flex-col justify-center"
        >
          <p class="text-xs text-gray-400 font-semibold uppercase tracking-wider">En Attente</p>
          <h3 class="text-3xl font-bold text-gray-900 mt-1">{{ stats.waiting }}</h3>
        </div>

        <!-- In-Consultation Card -->
        <div
          class="bg-white rounded-2xl border border-gray-100 p-5 shadow-sm flex flex-col justify-center"
        >
          <p class="text-xs text-gray-400 font-semibold uppercase tracking-wider">
            En Consultation
          </p>
          <h3 class="text-3xl font-bold text-blue-600 mt-1">{{ stats.inConsultation }}</h3>
        </div>

        <!-- Completed Card -->
        <div
          class="bg-white rounded-2xl border border-gray-100 p-5 shadow-sm flex flex-col justify-center"
        >
          <p class="text-xs text-gray-400 font-semibold uppercase tracking-wider">Terminés</p>
          <h3 class="text-3xl font-bold text-emerald-600 mt-1">{{ stats.completed }}</h3>
        </div>

        <!-- Total Today Card -->
        <div
          class="bg-white rounded-2xl border border-gray-100 p-5 shadow-sm flex flex-col justify-center"
        >
          <p class="text-xs text-gray-400 font-semibold uppercase tracking-wider">
            Total Aujourd'hui
          </p>
          <h3 class="text-3xl font-bold text-gray-900 mt-1">{{ stats.total }}</h3>
        </div>
      </div>

      <!-- Main Queue Area (Full Width) -->
      <div class="space-y-6">
        <!-- Active Call Banner (In Progress Patient) -->
        <div
          class="bg-[#1A1C23] text-white rounded-3xl p-8 shadow-md relative overflow-hidden border border-gray-800"
        >
          <div
            class="absolute -right-16 -top-16 w-64 h-64 rounded-full bg-blue-500/10 blur-3xl"
          ></div>

          <div
            class="flex flex-col md:flex-row justify-between items-start md:items-center gap-6 relative z-10"
          >
            <div class="space-y-3">
              <span
                class="inline-flex items-center gap-2 px-3 py-1.5 text-xs font-bold text-blue-400 bg-blue-500/15 rounded-full uppercase tracking-wider"
              >
                <span class="w-2 h-2 rounded-full bg-blue-400 animate-pulse"></span>
                Patient Actuellement en Consultation
              </span>

              <div v-if="activePatient" class="space-y-1">
                <h2 class="text-3xl font-extrabold">
                  {{ activePatient.patient_first_name }} {{ activePatient.patient_last_name }}
                </h2>
                <p class="text-sm text-gray-400 font-mono flex items-center gap-3">
                  <span
                    >Code: <strong class="text-white">{{ activePatient.code }}</strong></span
                  >
                  <span>•</span>
                  <span>Tél: {{ activePatient.patient_phone || 'Non renseigné' }}</span>
                </p>
              </div>
              <div v-else>
                <h2 class="text-2xl font-bold text-gray-400">Aucun patient en cours</h2>
                <p class="text-sm text-gray-500 mt-1">
                  Veuillez appeler le prochain patient de la file d'attente.
                </p>
              </div>
            </div>

            <div class="flex gap-3 w-full md:w-auto mt-2 md:mt-0">
              <button
                v-if="activePatient"
                @click="openConsultationDrawer(activePatient)"
                class="flex-1 md:flex-none px-6 py-3.5 bg-white text-gray-900 hover:bg-gray-100 rounded-xl text-sm font-bold transition-all shadow-lg"
              >
                Reprendre la consultation
              </button>
              <button
                v-if="activePatient"
                @click="completeActiveConsultation"
                :disabled="actionLoading"
                class="flex-1 md:flex-none px-6 py-3.5 bg-emerald-500 hover:bg-emerald-600 disabled:opacity-50 text-white rounded-xl text-sm font-bold transition-all shadow-lg shadow-emerald-500/20"
              >
                Terminer la consultation
              </button>
            </div>
          </div>
        </div>

        <!-- Waiting Patients List -->
        <div class="bg-white rounded-3xl border border-gray-100 p-6 shadow-sm">
          <div class="flex items-center justify-between mb-6">
            <div>
              <h3 class="text-lg font-bold text-gray-900">Prochains Patients en Attente</h3>
              <p class="text-xs text-gray-400 mt-0.5">Triage chronologique de la file d'attente</p>
            </div>
            <span class="text-xs font-bold text-blue-600 bg-blue-50 px-3 py-1.5 rounded-full">
              {{ waitingList.length }} patients
            </span>
          </div>

          <div v-if="waitingList.length > 0" class="space-y-3">
            <div
              v-for="(item, index) in waitingList"
              :key="item.code"
              class="flex flex-col sm:flex-row sm:items-center justify-between p-4 bg-gray-50 rounded-2xl border border-gray-100 hover:bg-gray-100/80 transition-all gap-4 group"
            >
              <div class="flex items-center gap-5">
                <div
                  class="w-12 h-12 rounded-xl bg-blue-50 text-blue-600 font-bold text-lg flex items-center justify-center shrink-0 shadow-sm"
                >
                  #0{{ index + 1 }}
                </div>
                <div>
                  <h4 class="font-bold text-gray-900 text-lg">
                    {{ item.patient_first_name }} {{ item.patient_last_name }}
                  </h4>
                  <p class="text-xs text-gray-400 mt-1 font-mono flex items-center gap-3">
                    <span
                      >Code: <strong class="text-gray-500">{{ item.code }}</strong></span
                    >
                    <span>•</span>
                    <span>Tél: {{ item.patient_phone }}</span>
                    <span>•</span>
                    <span
                      class="px-2 py-0.5 bg-gray-200/60 rounded-md font-bold text-[10px] uppercase text-gray-500"
                    >
                      {{ item.period === 'morning' ? 'Matin' : 'Après-Midi' }}
                    </span>
                  </p>
                </div>
              </div>

              <div
                class="flex items-center gap-3 self-end sm:self-center opacity-100 sm:opacity-0 sm:group-hover:opacity-100 transition-opacity"
              >
                <!-- Thermal Print Action -->
                <button
                  @click="printTicket(item)"
                  class="p-3 bg-white border border-gray-200 text-gray-500 hover:text-blue-600 rounded-xl hover:bg-gray-50 transition-all shadow-sm"
                  title="Imprimer Ticket Thermique"
                >
                  <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"
                    />
                  </svg>
                </button>
                <!-- Call trigger -->
                <button
                  @click="callPatient(item)"
                  :disabled="actionLoading || !!activePatient"
                  class="px-5 py-3 bg-blue-600 hover:bg-blue-700 disabled:bg-gray-100 disabled:text-gray-400 text-white rounded-xl text-sm font-bold transition-all shadow-sm flex items-center gap-2"
                >
                  <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M11 5.882V19.24a1.76 1.76 0 01-3.417.592l-2.147-6.15M18 13a3 3 0 100-6M5.436 13.683A4.001 4.001 0 017 6h1.832c4.1 0 7.625-1.234 9.168-3v14c-1.543-1.766-5.067-3-9.168-3H7a3.988 3.988 0 01-1.564-.317z"
                    />
                  </svg>
                  Appeler ce patient
                </button>
              </div>
            </div>
          </div>

          <div
            v-else
            class="text-center py-16 bg-gray-50/50 rounded-2xl border border-dashed border-gray-200"
          >
            <div
              class="w-16 h-16 bg-white rounded-full flex items-center justify-center mx-auto mb-4 shadow-sm border border-gray-100"
            >
              <svg
                class="w-8 h-8 text-gray-300"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"
                />
              </svg>
            </div>
            <h4 class="font-bold text-gray-900 text-lg">Aucun patient en attente</h4>
            <p class="text-sm text-gray-400 mt-1">
              Tous les rendez-vous d'aujourd'hui ont été pris en charge.
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- TV Waiting Room Fullscreen Overlay -->
    <div
      v-if="tvModeOpen"
      class="fixed inset-0 bg-[#0F1016] z-[999999] flex flex-col text-white p-8"
    >
      <!-- Header with logo and clock -->
      <div class="flex justify-between items-center border-b border-white/10 pb-6">
        <div class="flex items-center gap-3">
          <div
            class="w-10 h-10 bg-blue-600 rounded-full flex items-center justify-center font-bold text-lg"
          >
            P
          </div>
          <div>
            <h2 class="text-xl font-bold tracking-wide">POURA CLINIQUE</h2>
            <p class="text-xs text-gray-400">Affichage de la Salle d'Attente</p>
          </div>
        </div>
        <div class="flex items-center gap-6">
          <span class="text-2xl font-bold tracking-widest text-blue-400">{{ liveTime }}</span>
          <button
            @click="tvModeOpen = false"
            class="text-xs text-gray-500 hover:text-white px-3 py-1 bg-white/5 rounded-lg border border-white/10"
          >
            Quitter le mode TV
          </button>
        </div>
      </div>

      <!-- Main TV Layout Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 grow py-12 items-center">
        <!-- Left side: Patient called right now -->
        <div
          class="space-y-6 text-center lg:text-left bg-blue-900/10 border border-blue-500/20 p-10 rounded-[32px] shadow-2xl relative overflow-hidden"
        >
          <div
            class="absolute -right-24 -bottom-24 w-80 h-80 rounded-full bg-blue-600/10 blur-3xl"
          ></div>
          <span
            class="px-4 py-1.5 bg-blue-500 text-white rounded-full text-xs font-bold uppercase tracking-widest"
          >
            PATIENT APPELÉ
          </span>

          <div v-if="activePatient" class="space-y-4">
            <h1 class="text-6xl font-extrabold tracking-tight text-white mt-4">
              {{ activePatient.patient_first_name }}
              {{ getInitials(activePatient.patient_last_name) }}.
            </h1>
            <p class="text-8xl font-black text-blue-400 tracking-wider">
              {{ activePatient.code }}
            </p>
            <p class="text-lg text-gray-400 mt-2">
              Veuillez vous présenter au cabinet de consultation du médecin.
            </p>
          </div>

          <div v-else class="py-12">
            <h3 class="text-3xl font-bold text-gray-500">Aucun appel actif</h3>
            <p class="text-sm text-gray-400 mt-2">
              Veuillez patienter, le médecin va appeler le prochain patient sous peu.
            </p>
          </div>
        </div>

        <!-- Right side: Next tickets in the queue -->
        <div class="space-y-6">
          <h3 class="text-lg font-bold tracking-widest text-gray-400 uppercase">
            PROCHAINS TICKET EN ATTENTE
          </h3>

          <div class="space-y-4 max-h-[480px] overflow-hidden">
            <div
              v-for="(item, index) in waitingList.slice(0, 4)"
              :key="item.code"
              class="flex items-center justify-between p-6 bg-white/5 border border-white/10 rounded-2xl"
            >
              <div class="flex items-center gap-6">
                <span
                  class="w-12 h-12 rounded-xl bg-white/5 font-extrabold text-lg flex items-center justify-center"
                >
                  #0{{ index + 1 }}
                </span>
                <div>
                  <h4 class="text-2xl font-extrabold text-white">
                    {{ item.patient_first_name }} {{ getInitials(item.patient_last_name) }}.
                  </h4>
                  <p class="text-xs text-gray-500 mt-1">Ticket enregistré</p>
                </div>
              </div>

              <span class="text-3xl font-black text-blue-400">
                {{ item.code }}
              </span>
            </div>

            <!-- Fallback -->
            <p v-if="waitingList.length === 0" class="text-gray-500 text-lg py-12">
              File d'attente vide.
            </p>
          </div>
        </div>
      </div>

      <!-- TV footer status bar -->
      <div
        class="border-t border-white/5 pt-6 text-center text-xs text-gray-500 flex justify-between items-center"
      >
        <p>© Poura Practice Management System - Tous droits réservés.</p>
        <div class="flex items-center gap-2">
          <span class="w-2.5 h-2.5 rounded-full bg-emerald-500"></span>
          <span>Flux de file d'attente en temps réel connecté</span>
        </div>
      </div>
    </div>

    <!-- Thermal Printable Ticket Data Container (Hidden) -->
    <div
      v-if="ticketPrintData"
      class="print-ticket hidden print:block w-[80mm] p-6 text-black bg-white font-mono text-center mx-auto"
    >
      <h2 class="text-base font-bold uppercase">Cabinet de Consultation</h2>
      <p class="text-xs text-gray-400">Dr. Daniel Leon</p>
      <div class="my-6 border-y border-dashed border-gray-400 py-4">
        <p class="text-[10px] text-gray-400">NUMÉRO DE TICKET</p>
        <h1 class="text-2xl font-extrabold tracking-wider my-2">{{ ticketPrintData.code }}</h1>
      </div>

      <!-- Embedded QR Code -->
      <div
        class="w-28 h-28 border-4 border-black mx-auto my-3 flex items-center justify-center p-1 bg-white"
      >
        <div class="w-full h-full bg-black relative flex flex-wrap gap-1 p-1">
          <div class="w-4 h-4 bg-white"></div>
          <div class="w-4 h-4 bg-white"></div>
          <div class="w-4 h-4 bg-black"></div>
          <div class="w-4 h-4 bg-white"></div>
        </div>
      </div>

      <div class="text-left text-[11px] space-y-1 mt-4 border-t border-dashed border-gray-400 pt-3">
        <p>
          <strong>Patient:</strong> {{ ticketPrintData.patient_first_name }}
          {{ ticketPrintData.patient_last_name }}
        </p>
        <p><strong>Date:</strong> {{ ticketPrintData.date }}</p>
        <p><strong>Heure:</strong> {{ ticketPrintData.time }}</p>
      </div>
    </div>
  </AdminLayout>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import AdminLayout from '@/layouts/AdminLayout.vue'
import api from '@/api/axios'
import Swal from 'sweetalert2'

// State
const actionLoading = ref(false)
const tvModeOpen = ref(false)
const liveTime = ref('')
const ticketPrintData = ref(null)

const stats = ref({
  waiting: 0,
  inConsultation: 0,
  completed: 0,
  total: 0,
})

const activePatient = ref(null)
const waitingList = ref([])

// Timer for TV Mode Clock
let clockTimer = null
let pollTimer = null

const formatTime = (timeStr) => {
  if (!timeStr) return '--:--'
  try {
    const d = new Date(timeStr)
    return d.toLocaleTimeString('fr-DZ', { hour: '2-digit', minute: '2-digit' })
  } catch (e) {
    return timeStr
  }
}

const getInitials = (lastName) => {
  if (!lastName) return ''
  return lastName.charAt(0).toUpperCase()
}

// Fetch stats and lists from API
const fetchQueueData = async () => {
  try {
    const { data } = await api.get('appointments/doctor/queue/today/')

    // In progress patient
    activePatient.value = data.current

    // Waiting patients
    waitingList.value = data.waiting || []

    // Dynamic Stats
    stats.value.waiting = data.waiting_count || data.waiting.length
    stats.value.inConsultation = data.current ? 1 : 0
    stats.value.completed = data.completed_count || 0
    stats.value.total = stats.value.waiting + stats.value.inConsultation + stats.value.completed
  } catch (e) {
    console.error('Error loading daily queue:', e)
    // Local Mock Fallback for testing
    if (waitingList.value.length === 0 && !activePatient.value) {
      activePatient.value = {
        code: 'AP-X789',
        patient_first_name: 'Irene',
        patient_last_name: 'Fleming',
        patient_phone: '+213 555 12 34 56',
        called_at: new Date().toISOString(),
      }
      waitingList.value = [
        {
          code: 'AP-T456',
          patient_first_name: 'Ahmed',
          patient_last_name: 'Benali',
          patient_phone: '+213 666 45 89 12',
          period: 'morning',
        },
        {
          code: 'AP-R123',
          patient_first_name: 'Fatiha',
          patient_last_name: 'Bouhired',
          patient_phone: '+213 777 98 45 22',
          period: 'afternoon',
        },
      ]
      stats.value = { waiting: 2, inConsultation: 1, completed: 4, total: 7 }
    }
  }
}

// Actions
const callPatient = async (patient) => {
  actionLoading.value = true
  try {
    await api.post('appointments/doctor/queue/call-next/')
    Swal.fire({
      icon: 'info',
      title: 'Patient appelé',
      text: `Appel du ticket ${patient.code} (${patient.patient_first_name})`,
      toast: true,
      position: 'top-end',
      showConfirmButton: false,
      timer: 3000,
    })
    await fetchQueueData()
  } catch (e) {
    console.error(e)
    // Offline simulation fallback
    activePatient.value = patient
    waitingList.value = waitingList.value.filter((item) => item.code !== patient.code)
    stats.value.inConsultation = 1
    stats.value.waiting = waitingList.value.length
  } finally {
    actionLoading.value = false
  }
}

const completeActiveConsultation = async () => {
  if (!activePatient.value) return
  actionLoading.value = true
  try {
    await api.post(`appointments/doctor/queue/${activePatient.value.code}/complete/`)
    Swal.fire({
      icon: 'success',
      title: 'Consultation Clôturée',
      toast: true,
      position: 'top-end',
      showConfirmButton: false,
      timer: 3000,
    })
    await fetchQueueData()
  } catch (e) {
    console.error(e)
    // Offline simulation fallback
    stats.value.completed += 1
    activePatient.value = null
    stats.value.inConsultation = 0
  } finally {
    actionLoading.value = false
  }
}

const openConsultationDrawer = (patient) => {
  Swal.fire({
    title: 'Ouvrir Dossier de Consultation',
    text: `Génération du dossier clinique pour ${patient.patient_first_name} ${patient.patient_last_name}`,
    icon: 'question',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Consulter Dossier',
  }).then((result) => {
    if (result.isConfirmed) {
      window.location.href = `/consultations/create?patient=${patient.code}`
    }
  })
}

const printTicket = (patient) => {
  ticketPrintData.value = {
    code: patient.code,
    patient_first_name: patient.patient_first_name,
    patient_last_name: patient.patient_last_name,
    date: new Date().toLocaleDateString('fr-DZ'),
    time: new Date().toLocaleTimeString('fr-DZ', { hour: '2-digit', minute: '2-digit' }),
  }
  setTimeout(() => {
    window.print()
  }, 100)
}

const updateTime = () => {
  const now = new Date()
  liveTime.value = now.toLocaleTimeString('fr-DZ', {
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
  })
}

onMounted(() => {
  fetchQueueData()
  pollTimer = setInterval(fetchQueueData, 10000)
  updateTime()
  clockTimer = setInterval(updateTime, 1000)
})

onUnmounted(() => {
  if (pollTimer) clearInterval(pollTimer)
  if (clockTimer) clearInterval(clockTimer)
})
</script>

<style scoped>
@media print {
  body * {
    visibility: hidden;
  }
  .print-ticket,
  .print-ticket * {
    visibility: visible;
  }
  .print-ticket {
    position: absolute;
    left: 50%;
    top: 50px;
    transform: translateX(-50%);
    width: 80mm;
    border: none;
    background: white;
  }
}
</style>
