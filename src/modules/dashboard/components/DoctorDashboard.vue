<template>
  <div class="space-y-8 text-gray-900 font-sans w-full">
    
    <!-- Top Action Banner (Current & Next) -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
      
      <!-- Current Patient Card -->
      <div class="bg-gradient-to-br from-brand-600 to-brand-800 text-white rounded-[24px] p-8 shadow-xl shadow-brand-900/10 relative overflow-hidden flex flex-col justify-between min-h-[280px]">
        <div class="absolute -right-10 -top-10 w-48 h-48 rounded-full bg-white/10 blur-3xl"></div>
        <div class="absolute -left-10 -bottom-10 w-40 h-40 rounded-full bg-brand-400/20 blur-2xl"></div>
        
        <div class="relative z-10">
          <div class="flex items-center gap-3 mb-6">
            <span class="relative flex h-3 w-3">
              <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-red-400 opacity-75"></span>
              <span class="relative inline-flex rounded-full h-3 w-3 bg-red-500"></span>
            </span>
            <span class="text-sm font-bold text-brand-100 uppercase tracking-widest">En Consultation</span>
          </div>
          
          <div v-if="queue.current" class="space-y-4">
            <div>
              <h2 class="text-3xl font-bold tracking-tight text-white">{{ queue.current.patient_name }}</h2>
              <p class="text-sm text-brand-200 font-mono mt-1 opacity-80">Dossier: {{ queue.current.code }}</p>
            </div>
            
            <div class="flex gap-4 pt-4 mt-auto">
              <button
                @click="resumeConsultation(queue.current)"
                class="flex-1 py-3.5 px-5 bg-white/10 hover:bg-white/20 text-white rounded-xl text-sm font-bold transition-all backdrop-blur-sm border border-white/10"
              >
                Ouvrir Dossier
              </button>
              <button
                @click="completeConsultation"
                :disabled="actionLoading"
                class="flex-1 py-3.5 px-5 bg-white text-brand-700 hover:bg-brand-50 disabled:opacity-50 rounded-xl text-sm font-bold transition-all shadow-md"
              >
                Terminer
              </button>
            </div>
          </div>
          
          <div v-else class="py-8 flex flex-col items-center justify-center text-center opacity-80 mt-4">
            <div class="w-16 h-16 rounded-full bg-white/10 flex items-center justify-center mb-4">
              <svg class="w-8 h-8 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4" />
              </svg>
            </div>
            <p class="text-brand-100 font-medium text-lg">Salle de consultation libre.</p>
          </div>
        </div>
      </div>

      <!-- Next Patient Card -->
      <div class="bg-white rounded-[24px] border border-gray-100 p-8 shadow-[0_4px_24px_rgba(0,0,0,0.02)] flex flex-col justify-between min-h-[280px]">
        <div class="flex items-center justify-between mb-6">
          <span class="text-sm font-bold text-gray-400 uppercase tracking-widest">Prochain Patient</span>
          <span class="text-xs font-bold text-brand-700 bg-brand-50 px-3 py-1.5 rounded-full ring-1 ring-brand-100">
            {{ queue.waiting_count }} en attente
          </span>
        </div>
        
        <div v-if="queue.waiting && queue.waiting.length > 0" class="flex-1 flex flex-col justify-between">
          <div class="flex items-center gap-5">
            <div class="w-16 h-16 rounded-full bg-brand-50 text-brand-600 flex items-center justify-center text-2xl font-bold ring-4 ring-white shadow-sm">
              {{ queue.waiting[0].patient_name.charAt(0).toUpperCase() }}
            </div>
            <div>
              <h2 class="text-2xl font-bold text-gray-900 tracking-tight">{{ queue.waiting[0].patient_name }}</h2>
              <div class="flex items-center gap-3 mt-1.5">
                <span class="text-sm text-gray-500 font-mono">{{ queue.waiting[0].code }}</span>
                <span class="w-1 h-1 rounded-full bg-gray-300"></span>
                <span class="text-xs font-semibold text-gray-400 uppercase tracking-wider">{{ periodLabel(queue.waiting[0].period) }}</span>
              </div>
            </div>
          </div>
          
          <button
            @click="callNext"
            :disabled="actionLoading || !!queue.current"
            class="w-full mt-8 py-3.5 px-4 bg-brand-600 hover:bg-brand-700 disabled:bg-gray-100 disabled:text-gray-400 text-white rounded-xl text-sm font-bold transition-all shadow-md shadow-brand-500/20 flex items-center justify-center gap-2 group"
          >
            <svg class="w-5 h-5 transition-transform group-hover:scale-110" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M11 5.882V19.24a1.76 1.76 0 01-3.417.592l-2.147-6.15M18 13a3 3 0 100-6M5.436 13.683A4.001 4.001 0 017 6h1.832c4.1 0 7.625-1.234 9.168-3v14c-1.543-1.766-5.067-3-9.168-3H7a3.988 3.988 0 01-1.564-.317z" /></svg>
            Appeler en salle
          </button>
        </div>
        
        <div v-else class="flex-1 flex flex-col items-center justify-center text-center opacity-70">
          <div class="w-16 h-16 bg-gray-50 rounded-full flex items-center justify-center mb-4">
            <svg class="w-8 h-8 text-gray-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
          </div>
          <h3 class="font-bold text-gray-600 text-lg">Salle d'attente vide</h3>
          <p class="text-sm text-gray-400 mt-1">Aucun patient en attente.</p>
        </div>
      </div>
    </div>

    <!-- Quick Stats -->
    <div class="grid grid-cols-2 md:grid-cols-4 gap-4 lg:gap-6">
      <div class="bg-white rounded-2xl border border-gray-100 p-6 shadow-sm hover:shadow-md transition-shadow">
        <p class="text-xs text-gray-400 font-bold uppercase tracking-widest mb-2">Total Prévu</p>
        <h3 class="text-3xl font-black text-gray-900">{{ dashboardStats?.today_total || todayPatients.length }}</h3>
      </div>
      <div class="bg-white rounded-2xl border border-gray-100 p-6 shadow-sm hover:shadow-md transition-shadow">
        <p class="text-xs text-brand-600 font-bold uppercase tracking-widest mb-2">En Attente</p>
        <h3 class="text-3xl font-black text-brand-600">{{ dashboardStats?.today_waiting || queue.waiting_count }}</h3>
      </div>
      <div class="bg-white rounded-2xl border border-gray-100 p-6 shadow-sm hover:shadow-md transition-shadow">
        <p class="text-xs text-emerald-600 font-bold uppercase tracking-widest mb-2">Terminés</p>
        <h3 class="text-3xl font-black text-emerald-600">{{ dashboardStats?.today_completed || (todayPatients.length - queue.waiting_count - (queue.current ? 1 : 0)) }}</h3>
      </div>
      <!-- Quick link to view all today's appointments -->
      <router-link to="/queue/today" class="bg-gray-900 hover:bg-gray-800 text-white rounded-2xl p-6 flex flex-col justify-center items-center text-center transition-all group shadow-lg shadow-gray-900/10">
        <div class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center mb-3 group-hover:scale-110 transition-transform">
          <svg class="w-5 h-5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3" />
          </svg>
        </div>
        <span class="text-sm font-bold tracking-wide">Gérer la file du jour</span>
      </router-link>
    </div>

    <!-- Today's Patients Recap -->
    <div class="bg-white rounded-3xl border border-gray-100 p-8 shadow-sm">
      <div class="flex items-center justify-between mb-8">
        <div>
          <h3 class="text-xl font-bold text-gray-900">Aperçu de la journée</h3>
          <p class="text-sm text-gray-400 mt-1">Tous les patients enregistrés pour aujourd'hui</p>
        </div>
        <router-link to="/patients" class="text-sm font-bold text-brand-600 hover:text-brand-700 bg-brand-50 px-4 py-2 rounded-xl transition-colors">Voir tout</router-link>
      </div>
      
      <div class="overflow-x-auto">
        <table class="w-full text-left border-collapse min-w-[600px]">
          <thead>
            <tr class="border-b border-gray-100 text-gray-400 text-xs font-bold uppercase tracking-widest">
              <th class="pb-4 px-4 w-24">Ordre</th>
              <th class="pb-4">Patient</th>
              <th class="pb-4">Période</th>
              <th class="pb-4 text-right px-4">Action</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-50 text-sm">
            <tr v-for="(pat, idx) in todayPatients.slice(0, 5)" :key="pat.code" class="group hover:bg-gray-50 transition-colors">
              <td class="py-5 px-4">
                <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gray-100 text-gray-500 font-mono font-bold text-xs">
                  {{ (idx + 1).toString().padStart(2, '0') }}
                </span>
              </td>
              <td class="py-5">
                <p class="font-bold text-gray-900 text-base">{{ pat.patient_name }}</p>
                <p class="text-xs text-gray-400 font-mono mt-1">{{ pat.code }}</p>
              </td>
              <td class="py-5">
                <span 
                  class="px-3 py-1.5 rounded-lg text-xs font-bold tracking-wider uppercase inline-block border" 
                  :class="pat.period === 'morning' ? 'bg-amber-50 text-amber-700 border-amber-100' : 'bg-indigo-50 text-indigo-700 border-indigo-100'"
                >
                  {{ periodLabel(pat.period) }}
                </span>
              </td>
              <td class="py-5 text-right px-4">
                <router-link :to="`/consultations/create?patient=${pat.code}`" class="inline-flex items-center gap-1 text-brand-600 hover:text-brand-800 font-bold text-sm transition-colors group-hover:underline">
                  Consulter
                  <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" /></svg>
                </router-link>
              </td>
            </tr>
            <tr v-if="loadingTodayPatients">
              <td colspan="4" class="py-12 text-center">
                <div class="flex flex-col items-center justify-center space-y-3">
                  <div class="w-8 h-8 border-4 border-gray-200 border-t-brand-600 rounded-full animate-spin"></div>
                  <span class="text-sm font-medium text-gray-400">Chargement des données...</span>
                </div>
              </td>
            </tr>
            <tr v-else-if="todayPatients.length === 0">
              <td colspan="4" class="py-12 text-center">
                <div class="flex flex-col items-center justify-center text-gray-400">
                  <svg class="w-12 h-12 mb-3 opacity-20" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                  <span class="font-medium">Aucun patient prévu aujourd'hui.</span>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from "vue";
import { useRouter } from "vue-router";
import api from "@/api/axios";

const router = useRouter();

// State
const doctorName = ref("");
const queue = ref({
  current: null,
  waiting: [],
  waiting_count: 0,
});
const actionLoading = ref(false);
const queueError = ref("");
const ticketData = ref(null);
const dashboardStats = ref(null);

const imprimerTicket = (patientName, code, period) => {
  ticketData.value = {
    patientName,
    code,
    period: periodLabel(period),
    date: new Date().toLocaleDateString("fr-DZ"),
    time: new Date().toLocaleTimeString("fr-DZ", { hour: '2-digit', minute: '2-digit' }),
  }
  setTimeout(() => {
    window.print();
  }, 100);
}

let pollTimer = null;
const POLL_INTERVAL_MS = 10000;

const todayPatients = ref([]);
const loadingTodayPatients = ref(true);

async function fetchTodayPatients() {
  loadingTodayPatients.value = true;
  try {
    const todayStr = new Date().toISOString().split('T')[0];
    const { data } = await api.get("appointments/doctor-appointments/", { params: { date: todayStr } });
    todayPatients.value = data;
  } catch (err) {
    console.error("Erreur API:", err);
    todayPatients.value = [];
  } finally {
    loadingTodayPatients.value = false;
  }
}

async function fetchStats() {
  try {
    // The web app uses api/axios which maps to base URL. Mobile API is /api/mobile.
    // Assuming we can call the dashboard_stats route. Let's make sure the URL is correct.
    const { data } = await api.get("mobile/dashboard/stats/");
    if (data && data.stats) {
      dashboardStats.value = data.stats;
    }
  } catch (err) {
    console.error("Erreur stats:", err);
  }
}

function periodLabel(period) {
  return period === "morning" ? "Matin" : period === "afternoon" ? "Après-midi" : period;
}

// API methods
async function fetchQueue() {
  try {
    const { data } = await api.get("appointments/doctor/queue/today/");
    queue.value = data;
    queueError.value = "";
  } catch (err) {
    console.error(err);
    queueError.value = err.response?.data?.error || "Erreur lors du chargement de la file";
  }
}

async function callNext() {
  actionLoading.value = true;
  try {
    await api.post("appointments/doctor/queue/call-next/");
    await fetchQueue();
  } catch (err) {
    console.error(err);
    queueError.value = err.response?.data?.error || "Erreur de l'appel";
  } finally {
    actionLoading.value = false;
  }
}

async function completeConsultation() {
  if (!queue.value.current) return;
  actionLoading.value = true;
  try {
    await api.post(`appointments/doctor/queue/${queue.value.current.code}/complete/`);
    await fetchQueue();
  } catch (err) {
    console.error(err);
    queueError.value = err.response?.data?.error || "Erreur de clôture";
  } finally {
    actionLoading.value = false;
  }
}

function resumeConsultation(patient) {
  if (!patient) return;
  router.push(`/consultations/create?patient=${patient.code}`);
}

async function fetchDoctorProfile() {
  try {
    const { data } = await api.get("users/update-security/"); 
    doctorName.value = data.first_name || data.username || "Daniel Leon";
  } catch (e) {}
}

onMounted(() => {
  fetchQueue();
  fetchDoctorProfile();
  fetchTodayPatients();
  fetchStats();
  pollTimer = setInterval(() => {
    fetchQueue();
    fetchStats();
  }, POLL_INTERVAL_MS);
});

onUnmounted(() => {
  if (pollTimer) clearInterval(pollTimer);
});
</script>

<style scoped>
@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.animate-spin {
  animation: spin 1s linear infinite;
}

.slide-enter-active, .slide-leave-active { 
  transition: transform 0.3s ease; 
}
.slide-enter-from, .slide-leave-to { 
  transform: translateX(100%); 
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
.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background: #94a3b8;
}

@media print {
  body * {
    visibility: hidden;
  }
  .print-ticket, .print-ticket * {
    visibility: visible;
  }
  .print-ticket {
    position: absolute;
    left: 50%;
    top: 50px;
    transform: translateX(-50%);
    width: 80mm;
    border: none;
    box-shadow: none;
    background: white;
  }
  aside, header, footer, main {
    border: none !important;
    box-shadow: none !important;
    background: transparent !important;
  }
}
</style>