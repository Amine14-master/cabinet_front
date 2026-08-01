<template>
  <div class="space-y-6 p-4 max-w-7xl mx-auto text-gray-800 dark:text-gray-200 relative">
    
    <!-- Écran de chargement -->
    <div v-if="loading" class="flex flex-col items-center justify-center min-h-[400px] space-y-4">
      <div class="w-12 h-12 border-4 border-blue-600 border-t-transparent rounded-full animate-spin"></div>
      <p class="text-gray-500 font-medium text-sm">Chargement du dossier...</p>
    </div>

    <!-- Contenu Principal -->
    <div v-else-if="patient" class="space-y-6">
      
      <!-- ================= SECTION 1: TOP BAR & INFO PATIENT ================= -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <!-- Carte Identité Patient -->
        <div class="lg:col-span-2 bg-white dark:bg-white/[0.03] rounded-3xl border border-gray-100 dark:border-gray-800 p-6 shadow-sm flex flex-col justify-between">
          <div>
            <div class="flex items-center gap-4 mb-4">
              <div class="w-12 h-12 rounded-2xl bg-blue-50 dark:bg-blue-500/10 flex items-center justify-center text-blue-600 font-bold text-base tracking-wider">
                {{ patient.last_name[0] }}{{ patient.first_name[0] }}
              </div>
              <div>
                <h1 class="text-xl font-bold text-gray-900 dark:text-white">{{ patient.last_name }} {{ patient.first_name }}</h1>
                <span class="inline-flex items-center text-xs font-mono bg-blue-50 text-blue-600 dark:bg-blue-500/10 px-2.5 py-0.5 rounded-lg font-bold mt-1">
                  ID: {{ patient.code }}
                </span>
              </div>
            </div>
            
            <div class="grid grid-cols-2 sm:grid-cols-3 gap-6 pt-2">
              <div>
                <span class="block text-xs font-medium text-gray-400 mb-1">Date de naissance</span>
                <span class="text-sm font-semibold text-gray-700 dark:text-gray-300">{{ formatDate(patient.date_of_birth) }}</span>
              </div>
              <div>
                <span class="block text-xs font-medium text-gray-400 mb-1">Genre</span>
                <span class="text-sm font-semibold text-gray-700 dark:text-gray-300">{{ patient.gender === 'F' ? 'Féminin' : 'Masculin' }}</span>
              </div>
              <div>
                <span class="block text-xs font-medium text-gray-400 mb-1">Groupe Sanguin</span>
                <span class="inline-flex text-xs font-bold text-red-600 dark:text-red-400 bg-red-50 dark:bg-red-500/10 px-2.5 py-0.5 rounded-lg border border-red-100 dark:border-red-500/20">
                  {{ patient.blood_group }}
                </span>
              </div>
            </div>
          </div>
        </div>

        <!-- Carte Contact Rapide -->
        <div class="bg-white dark:bg-white/[0.03] rounded-3xl border border-gray-100 dark:border-gray-800 p-6 shadow-sm flex flex-col justify-center space-y-4">
          <h3 class="text-xs font-bold uppercase tracking-wider text-gray-400">Coordonnées</h3>
          <div class="flex items-center gap-3">
            <div class="w-8 h-8 rounded-lg bg-gray-50 dark:bg-white/[0.05] flex items-center justify-center text-gray-500 dark:text-gray-400">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" /></svg>
            </div>
            <a :href="'tel:' + patient.phone" class="text-sm font-semibold hover:text-blue-600 transition-colors">{{ patient.phone }}</a>
          </div>
          <div class="flex items-center gap-3">
            <div class="w-8 h-8 rounded-lg bg-gray-50 dark:bg-white/[0.05] flex items-center justify-center text-gray-500 dark:text-gray-400">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" /></svg>
            </div>
            <a :href="'mailto:' + patient.email" class="text-sm font-medium hover:text-blue-600 transition-colors truncate block max-w-[220px]">{{ patient.email }}</a>
          </div>
        </div>
      </div>

      <!-- ================= SECTION 2: TABLEAU OPTIMISÉ POUR DRAWER ================= -->
      <div class="bg-white dark:bg-white/[0.03] rounded-3xl border border-gray-100 dark:border-gray-800 shadow-sm overflow-hidden">
        <div class="p-6 border-b border-gray-100 dark:border-gray-800 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 bg-gray-50/50 dark:bg-white/[0.01]">
          <div>
            <h2 class="text-lg font-bold text-gray-900 dark:text-white">Dossier Clinique & Historique</h2>
            <p class="text-xs text-gray-400 mt-0.5">Cliquez sur une ligne pour ouvrir les détails de la consultation</p>
          </div>
          <div class="relative w-full sm:w-80">
            <span class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none text-gray-400">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
            </span>
            <input v-model="searchQuery" type="text" placeholder="Rechercher un diagnostic, code, date..." class="w-full pl-9 pr-4 py-2 text-xs rounded-xl border border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-900 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all"/>
          </div>
        </div>

        <div class="overflow-x-auto">
          <table class="w-full text-left border-collapse">
            <thead>
              <tr class="border-b border-gray-100 dark:border-gray-800 text-[11px] font-bold uppercase tracking-wider text-gray-400 bg-gray-50/50 dark:bg-transparent">
                <th class="py-4 px-6">Date de l'Acte</th>
                <th class="py-4 px-6">Identifiant / Code</th>
                <th class="py-4 px-6">Période</th>
                <th class="py-4 px-6">Statut RDV</th>
                <th class="py-4 px-6">Diagnostic Principal</th>
                <th class="py-4 px-6 text-center uppercase tracking-wider">Action</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-100 dark:divide-gray-800/60">
              <tr v-if="filteredRecords.length === 0">
                <td colspan="6" class="text-center py-12 text-xs text-gray-400">Aucun dossier trouvé.</td>
              </tr>
              <tr 
                v-for="record in filteredRecords" 
                :key="record.appointment_code"
                class="border-t border-gray-100 dark:border-gray-800 hover:bg-gray-50 dark:hover:bg-white/[0.02] transition-colors group"
              >
                <!-- Date de Consultation ou de RDV -->
                <td class="py-4 px-6 whitespace-nowrap font-semibold text-gray-900 dark:text-white">
                  {{ record.hasConsultation ? formatDateTime(record.consultation_date) : formatDate(record.date) }}
                </td>

                <!-- Codes -->
                <td class="py-4 px-6 whitespace-nowrap">
                  <div class="flex flex-col gap-0.5">
                    <span class="text-[10px] font-mono text-gray-400">RDV: {{ record.appointment_code }}</span>
                    <span v-if="record.hasConsultation" class="text-[10px] font-mono font-bold text-blue-600 dark:text-blue-400">CONS: #{{ record.consultation_id }}</span>
                  </div>
                </td>

                <!-- Période -->
                <td class="py-4 px-6 whitespace-nowrap text-gray-500 dark:text-gray-400 capitalize">
                  {{ record.period === 'morning' ? 'Matin' : 'Après-midi' }}
                </td>

                <!-- Statut -->
                <td class="py-4 px-6 whitespace-nowrap">
                  <span :class="['px-3 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider', getStatusClass(record.status)]">
                    {{ record.status === 'completed' ? 'Terminé' : 'Planifié' }}
                  </span>
                </td>

                <!-- Diagnostic léger -->
                <td class="py-4 px-6 max-w-xs truncate font-medium text-gray-700 dark:text-gray-300">
                  <span v-if="!record.hasConsultation" class="text-gray-300 dark:text-gray-700 italic font-normal">En attente</span>
                  <span v-else>{{ record.diagnosis }}</span>
                </td>

                <!-- Action avec l'icône de l'œil -->
                <td class="py-4 px-6 text-center">
                  <button 
                    @click.stop="openDrawer(record)" 
                    class="inline-flex items-center justify-center p-2 rounded-lg text-gray-400 hover:text-blue-600 hover:bg-blue-50 dark:hover:bg-blue-500/10 transition-all active:scale-90"
                    title="Voir Détails"
                  >
                    <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                    </svg>
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Footer Actions -->
      <div class="flex items-center justify-between pt-2">
        <p class="text-[11px] text-gray-400">Total: {{ filteredRecords.length }} ligne(s)</p>
        <button type="button" @click="$router.back()" class="px-5 py-2.5 rounded-xl border border-gray-200 dark:border-gray-700 text-gray-600 dark:text-gray-300 font-bold hover:bg-gray-50 dark:hover:bg-gray-800 transition-all text-xs shadow-sm">
          Retour à la liste
        </button>
      </div>
    </div>

<!-- =========================================================================
     SIDE DRAWER JUMEAU (PATIENT DETAILS STRUCTURE OPTIMISÉE)
     ========================================================================= -->
<Transition name="slide">
  <div v-if="isDrawerOpen" class="fixed inset-0 z-50 overflow-hidden">
    <div class="absolute inset-0 bg-gray-900/60 backdrop-blur-sm transition-opacity" @click="closeDrawer"></div>
    
    <div :class="[
      'absolute inset-y-0 right-0 w-full bg-white dark:bg-gray-950 shadow-2xl flex flex-col transform transition-all duration-300 border-l border-gray-100 dark:border-gray-800',
      selectedRecord?.hasConsultation ? 'max-w-3xl' : 'max-w-md'
    ]">
      
      <div class="p-6 border-b border-gray-100 dark:border-gray-800 flex justify-between items-center bg-gray-50/50 dark:bg-white/[0.02]">
        <div>
          <h2 class="text-lg font-bold text-gray-900 dark:text-white">Dossier Médical Acte</h2>
          <p class="text-xs text-gray-400 font-mono mt-0.5">Code RDV: {{ selectedRecord?.appointment_code }}</p>
        </div>
        <button @click="closeDrawer" class="p-2 rounded-full hover:bg-gray-200 dark:hover:bg-gray-800 transition-colors text-gray-500 dark:text-gray-400">✕</button>
      </div>
      
      <div class="p-8 space-y-6 flex-1 overflow-y-auto custom-scrollbar">
        
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 bg-gray-50 dark:bg-white/[0.01] p-4 rounded-2xl border border-gray-100 dark:border-gray-800/80">
          <div class="text-center sm:text-left">
            <span class="block text-[10px] uppercase font-bold text-gray-400 mb-0.5">Type d'acte</span>
            <span :class="['inline-flex px-2 py-0.5 rounded text-[10px] font-bold uppercase', selectedRecord?.hasConsultation ? 'bg-blue-50 text-blue-600 dark:bg-blue-500/10' : 'bg-amber-50 text-amber-600 dark:bg-amber-500/10']">
              {{ selectedRecord?.hasConsultation ? 'Consultation #' + selectedRecord.consultation_id : 'Rendez-vous Simple' }}
            </span>
          </div>
          <div class="text-center sm:border-l dark:border-gray-800 px-2">
            <span class="block text-[10px] uppercase font-bold text-gray-400 mb-0.5">Date & Heure</span>
            <span class="text-xs font-semibold dark:text-white">
              {{ selectedRecord?.hasConsultation ? formatDateTime(selectedRecord.consultation_date) : formatDate(selectedRecord?.date) }}
            </span>
          </div>
          <div class="text-center sm:border-l dark:border-gray-800 px-2">
            <span class="block text-[10px] uppercase font-bold text-gray-400 mb-0.5">Session</span>
            <span class="text-xs font-semibold dark:text-white capitalize">
              {{ selectedRecord?.period === 'morning' ? 'Matin' : 'Après-midi' }}
            </span>
          </div>
        </div>

        <div v-if="selectedRecord && !selectedRecord.hasConsultation" class="py-12 text-center border-2 border-dashed border-gray-100 dark:border-gray-800 rounded-2xl">
          <p class="text-sm text-gray-400">Aucune donnée clinique saisie pour le moment.</p>
        </div>

        <div v-else-if="selectedRecord" class="grid grid-cols-1 lg:grid-cols-2 gap-6">
          
          <div class="space-y-6">
            <div class="space-y-2">
              <h4 class="text-xs font-bold uppercase tracking-widest text-gray-400">Symptômes & Motifs</h4>
              <div class="text-sm font-medium text-gray-900 dark:text-white bg-gray-50 dark:bg-white/[0.02] p-5 rounded-2xl border border-gray-100 dark:border-gray-800 shadow-sm leading-relaxed min-h-[120px] whitespace-pre-line">
                {{ selectedRecord.symptoms || 'Aucun symptôme mentionné.' }}
              </div>
            </div>

            <div class="space-y-2">
              <h4 class="text-xs font-bold uppercase tracking-widest text-gray-400">Diagnostic Médical</h4>
              <div class="text-sm font-bold text-emerald-700 dark:text-emerald-400 bg-emerald-50/40 dark:bg-emerald-500/[0.02] p-5 rounded-2xl border border-emerald-100 dark:border-emerald-800/30 shadow-sm min-h-[80px] whitespace-pre-line">
                {{ selectedRecord.diagnosis || 'Aucun diagnostic posé.' }}
              </div>
            </div>
          </div>

          <div class="space-y-6">
            <div class="space-y-2">
              <h4 class="text-xs font-bold uppercase tracking-widest text-gray-400">Ordonnance & Traitement</h4>
              <div class="text-xs font-mono text-gray-800 dark:text-gray-200 bg-blue-50/30 dark:bg-blue-500/[0.01] p-5 rounded-2xl border border-blue-100/50 dark:border-blue-800/30 shadow-sm min-h-[230px] whitespace-pre-line leading-relaxed tracking-wide">
                <div class="border-b border-blue-100/50 dark:border-blue-900/30 pb-2 mb-3 text-blue-600 dark:text-blue-400 font-bold uppercase tracking-wider text-[10px]">
                  💊 Médicaments prescrits
                </div>
                {{ selectedRecord.prescription || 'Aucun traitement généré.' }}
              </div>
            </div>
          </div>

          <div v-if="selectedRecord.notes && selectedRecord.notes !== '...'" class="col-span-1 lg:col-span-2 space-y-2">
            <h4 class="text-xs font-bold uppercase tracking-widest text-gray-400">Notes & Remarques confidentielles</h4>
            <div class="p-4 rounded-2xl bg-gray-50/50 dark:bg-white/[0.01] border border-gray-100 dark:border-gray-800 text-xs text-gray-500 dark:text-gray-400 italic">
              {{ selectedRecord.notes }}
            </div>
          </div>

        </div>

      </div>

      <div class="p-6 border-t border-gray-100 dark:border-gray-800 bg-white dark:bg-gray-950 flex gap-3">
        <button
          @click="closeDrawer"
          class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3.5 rounded-2xl transition-all active:scale-[0.98] shadow-xl shadow-blue-500/25 text-sm"
        >
          Fermer le panneau
        </button>
      </div>

    </div>
  </div>
</Transition>

  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed, onUnmounted } from "vue";
import { useRoute } from "vue-router";
import { getDoctorPatientProfile } from "@/api/patientsService";

const route = useRoute();
const loading = ref(true);
const searchQuery = ref("");

// États pour le Drawer
const isDrawerOpen = ref(false);
const selectedRecord = ref<any>(null);

const patient = ref<any>(null);
const appointments = ref<any[]>([]);
const consultations = ref<any[]>([]);

const loadPatient = async () => {
  loading.value = true;
  try {
    const data = await getDoctorPatientProfile(route.params.code as string);
    patient.value = data.patient;
    appointments.value = data.appointments || [];
    consultations.value = data.consultations || [];
  } catch (err) {
    console.error(err);
  } finally {
    loading.value = false;
  }
};

// Fonctions de contrôle du Drawer
const openDrawer = (record: any) => {
  selectedRecord.value = record;
  isDrawerOpen.value = true;
  document.body.style.overflow = "hidden";
};

const closeDrawer = () => {
  isDrawerOpen.value = false;
  selectedRecord.value = null;
  document.body.style.overflow = "";
};

const handleKeyDown = (e: KeyboardEvent) => {
  if (e.key === "Escape" && isDrawerOpen.value) closeDrawer();
};

const combinedRecords = computed(() => {
  return appointments.value.map((app) => {
    const matchingConsultation = consultations.value.find(
      (c) => c.appointment_code === app.code
    );

    return {
      appointment_code: app.code,
      date: app.appointment_date,
      period: app.period,
      status: app.status,
      hasConsultation: !!matchingConsultation,
      consultation_id: matchingConsultation ? matchingConsultation.id : null,
      consultation_date: matchingConsultation ? matchingConsultation.created_at : null,
      symptoms: matchingConsultation ? matchingConsultation.symptoms : "",
      diagnosis: matchingConsultation ? matchingConsultation.diagnosis : "",
      prescription: matchingConsultation ? matchingConsultation.prescription : "",
      notes: matchingConsultation ? matchingConsultation.notes : "",
    };
  }).sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());
});

const filteredRecords = computed(() => {
  const query = searchQuery.value.toLowerCase().trim();
  if (!query) return combinedRecords.value;

  return combinedRecords.value.filter((r) => {
    return (
      r.appointment_code.toLowerCase().includes(query) ||
      r.date.includes(query) ||
      r.status.toLowerCase().includes(query) ||
      r.diagnosis.toLowerCase().includes(query) ||
      (r.consultation_id && String(r.consultation_id).includes(query))
    );
  });
});

const formatDate = (dateStr: string) => {
  if (!dateStr) return "";
  return new Date(dateStr).toLocaleDateString("fr-FR", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });
};

const formatDateTime = (dateTimeStr: string) => {
  if (!dateTimeStr) return "";
  return new Date(dateTimeStr).toLocaleDateString("fr-FR", {
    year: "numeric",
    month: "short",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
};

const getStatusClass = (status: string) => {
  return status === "completed"
    ? "bg-emerald-50 text-emerald-700 dark:bg-emerald-500/10 dark:text-emerald-400 border border-emerald-100/30 dark:border-emerald-500/20"
    : "bg-blue-50 text-blue-700 dark:bg-blue-500/10 dark:text-blue-400 border border-blue-100/30 dark:border-blue-500/20";
};

onMounted(() => {
  loadPatient();
  window.addEventListener("keydown", handleKeyDown);
});

onUnmounted(() => {
  window.removeEventListener("keydown", handleKeyDown);
  document.body.style.overflow = "";
});
</script>



