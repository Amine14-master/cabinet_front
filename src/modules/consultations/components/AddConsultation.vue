<template>
  <div class="max-w-5xl mx-auto space-y-6 pb-12">
    
    <form @submit.prevent="handleSubmit" class="space-y-6">
      
      <div class="bg-white dark:bg-gray-950 rounded-2xl border border-gray-200 dark:border-gray-800 p-6 shadow-sm transition-all">
        <div class="flex items-center gap-3 mb-6 pb-4 border-b border-gray-100 dark:border-gray-800">
          <div class="w-10 h-10 rounded-xl bg-blue-50 dark:bg-blue-500/10 flex items-center justify-center text-blue-600 dark:text-blue-400">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
            </svg>
          </div>
          <div>
            <h2 class="text-base font-bold text-gray-900 dark:text-white">Informations du bénéficiaire</h2>
            <p class="text-xs text-gray-400">Vérification des détails du rendez-vous</p>
          </div>
        </div>

        <div v-if="loadingAppointment" class="text-center py-12">
          <div class="inline-block h-8 w-8 animate-spin rounded-full border-4 border-solid border-blue-600 border-r-transparent"></div>
          <p class="text-xs text-gray-400 font-medium mt-3">Synchronisation Doctolib en cours...</p>
        </div>

        <div v-else-if="appointmentError" class="p-4 bg-red-50 dark:bg-red-900/10 border border-red-100 dark:border-red-800/30 text-red-600 dark:text-red-400 rounded-xl text-sm">
          ⚠️ {{ appointmentError }}
        </div>

        <div v-else class="space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 p-4 rounded-xl bg-gray-50 dark:bg-white/[0.02] border border-gray-100 dark:border-gray-800/60">
            <div class="flex items-center gap-4">
              <div class="w-12 h-12 rounded-xl bg-blue-600 text-white flex items-center justify-center text-lg font-bold shadow-sm">
                {{ appointmentData?.patient_name?.charAt(0).toUpperCase() || 'P' }}
              </div>
              <div>
                <p class="font-bold text-gray-900 dark:text-white text-base">{{ appointmentData?.patient_name }}</p>
                <div class="flex flex-wrap items-center gap-x-3 gap-y-1 text-xs text-gray-500 dark:text-gray-400 mt-0.5">
                  <span class="font-mono">ID: {{ appointmentData?.patient_code }}</span>
                  <span class="text-gray-300 dark:text-gray-700">•</span>
                  <span>📞 {{ appointmentData?.patient_phone || 'Non renseigné' }}</span>
                </div>
              </div>
            </div>
            
            <div class="text-xs sm:text-right font-mono bg-white dark:bg-gray-900 px-3 py-2 rounded-lg border border-gray-200/60 dark:border-gray-800 shadow-2xs">
              <span class="text-gray-400 block text-[10px] uppercase font-sans font-bold tracking-wider mb-0.5">Code Consultation</span>
              <span class="text-gray-700 dark:text-gray-300 font-bold">{{ appointmentData?.code }}</span>
            </div>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
            <div class="p-3.5 rounded-xl border border-gray-100 dark:border-gray-800 bg-white dark:bg-transparent">
              <span class="text-[10px] font-bold text-gray-400 uppercase tracking-wider block mb-1">Date programmée</span>
              <p class="text-sm font-semibold text-gray-700 dark:text-gray-300">{{ formatDate(appointmentData?.appointment_date) }}</p>
            </div>
            
            <div class="p-3.5 rounded-xl border border-gray-100 dark:border-gray-800 bg-white dark:bg-transparent">
              <span class="text-[10px] font-bold text-gray-400 uppercase tracking-wider block mb-1">Créneau horaire</span>
              <div class="flex items-center gap-1.5 mt-0.5">
                <span>{{ appointmentData?.period === 'morning' ? '🌅' : '☀️' }}</span>
                <span class="text-sm font-semibold text-gray-700 dark:text-gray-300 capitalize">
                  {{ appointmentData?.period === 'morning' ? 'Matin (08:00 - 12:00)' : 'Après-midi (13:00 - 17:00)' }}
                </span>
              </div>
            </div>

            <div class="p-3.5 rounded-xl border border-gray-100 dark:border-gray-800 bg-white dark:bg-transparent">
              <span class="text-[10px] font-bold text-gray-400 uppercase tracking-wider block mb-1">Statut Doctolib</span>
              <span class="inline-flex mt-1 items-center px-2.5 py-0.5 rounded-md text-xs font-bold bg-blue-50 text-blue-700 dark:bg-blue-500/10 dark:text-blue-400 border border-blue-100 dark:border-blue-500/20">
                ● {{ appointmentData?.status === 'scheduled' ? 'Confirmé' : appointmentData?.status }}
              </span>
            </div>
          </div>
        </div>
      </div>

      <div class="bg-white dark:bg-gray-950 rounded-2xl border border-gray-200 dark:border-gray-800 p-6 shadow-sm">
        <div class="flex items-center gap-3 mb-6 pb-4 border-b border-gray-100 dark:border-gray-800">
          <div class="w-10 h-10 rounded-xl bg-amber-50 dark:bg-amber-500/10 flex items-center justify-center text-amber-600 dark:text-amber-400">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
          </div>
          <div>
            <h2 class="text-base font-bold text-gray-900 dark:text-white">Observations Cliniques</h2>
            <p class="text-xs text-gray-400">Données médicales récoltées durant l'examen</p>
          </div>
        </div>

        <div class="space-y-5">
          <div>
            <label class="text-xs font-bold text-gray-400 uppercase tracking-wider block mb-2">Symptômes & Motif principal</label>
            <textarea 
              v-model="formData.symptoms" 
              rows="2" 
              class="w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-800 dark:bg-gray-900/50 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none dark:text-white text-sm transition-all"
              placeholder="Ex: Céphalées aiguës depuis 48h, fièvre modérée..."
            ></textarea>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
            <div>
              <label class="text-xs font-bold text-gray-400 uppercase tracking-wider block mb-2">Diagnostic retenu</label>
              <textarea 
                v-model="formData.diagnosis" 
                rows="4" 
                class="w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-800 dark:bg-gray-900/50 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none dark:text-white text-sm transition-all"
                placeholder="Ex: Syndrome grippal précoce..."
              ></textarea>
            </div>

            <div>
              <label class="text-xs font-bold text-gray-400 uppercase tracking-wider block mb-2">Résumé libre de la prescription</label>
              <textarea 
                v-model="formData.prescription" 
                rows="4" 
                class="w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-800 dark:bg-gray-900/50 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none dark:text-white text-sm transition-all"
                placeholder="Ex: Repos strict, hydratation continue..."
              ></textarea>
            </div>
          </div>

          <div>
            <label class="text-xs font-bold text-gray-400 uppercase tracking-wider block mb-2">Notes confidentielles (Interne)</label>
            <textarea 
              v-model="formData.notes" 
              rows="2" 
              class="w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-800 dark:bg-gray-900/50 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none dark:text-white text-sm transition-all"
              placeholder="Observations secondaires ou antécédents notables..."
            ></textarea>
          </div>
        </div>
      </div>

      <div class="bg-white dark:bg-gray-950 rounded-2xl border border-gray-200 dark:border-gray-800 p-6 shadow-sm">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-6 pb-4 border-b border-gray-100 dark:border-gray-800">
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-emerald-50 dark:bg-emerald-500/10 flex items-center justify-center text-emerald-600 dark:text-emerald-400">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z" />
              </svg>
            </div>
            <div>
              <h2 class="text-base font-bold text-gray-900 dark:text-white">Lignes de Traitement médicaux</h2>
              <p class="text-xs text-gray-400">Ajout indexé sur la base pharmaceutique nationale</p>
            </div>
          </div>

          <button
            type="button"
            @click="addPrescriptionItem"
            class="inline-flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-semibold text-xs transition-all active:scale-95 shadow-sm shadow-emerald-500/20"
          >
            <span>＋</span> Ajouter un médicament
          </button>
        </div>

        <div v-if="prescriptionItems.length === 0" class="text-center py-10 border-2 border-dashed border-gray-100 dark:border-gray-800/80 rounded-xl">
          <p class="text-sm text-gray-400 font-medium">Aucun médicament ajouté à l'ordonnance électronique pour le moment.</p>
        </div>

        <div class="space-y-4">
          <div
            v-for="(item, index) in prescriptionItems"
            :key="index"
            class="group relative border border-gray-200 dark:border-gray-800 rounded-xl p-5 bg-gray-50/30 dark:bg-white/[0.01] hover:border-gray-300 dark:hover:border-gray-700 transition-all"
          >
            <div class="flex items-center justify-between mb-4">
              <span class="text-[10px] font-bold font-mono bg-gray-100 dark:bg-gray-800 text-gray-500 px-2 py-0.5 rounded-md">
                Ligne #{{ index + 1 }}
              </span>
              <button
                type="button"
                @click="removePrescriptionItem(index)"
                class="inline-flex items-center gap-1 text-xs text-red-500 hover:text-red-600 font-semibold opacity-80 hover:opacity-100 transition-opacity"
              >
                🗑️ Supprimer
              </button>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-5">
              
              <div class="lg:col-span-5 relative space-y-1.5">
                <label class="text-[10px] font-bold text-gray-400 uppercase tracking-wider block">Nom commercial ou DCI</label>
                <div class="relative">
                  <input
                    v-model="item.medicament_name"
                    @input="searchMedicaments(item)"
                    type="text"
                    autocomplete="off"
                    placeholder="Rechercher (ex: Paracétamol...)"
                    class="w-full text-sm rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 px-4 py-2.5 outline-none focus:border-blue-500 dark:text-white"
                  />
                </div>

                <div
                  v-if="item.results && item.results.length"
                  class="absolute left-0 right-0 z-50 mt-1 bg-white dark:bg-gray-900 border border-gray-200 dark:border-gray-700 rounded-xl shadow-xl max-h-56 overflow-y-auto custom-scrollbar"
                >
                  <table class="w-full text-xs text-left">
                    <thead class="bg-gray-50 dark:bg-gray-800/80 text-gray-400 sticky top-0 font-bold border-b border-gray-100 dark:border-gray-700">
                      <tr>
                        <th class="px-3 py-2">Spécialité</th>
                        <th class="px-3 py-2">Dosage</th>
                      </tr>
                    </thead>
                    <tbody class="divide-y divide-gray-100 dark:divide-gray-800">
                      <tr
                        v-for="med in item.results"
                        :key="med.id"
                        @click="selectMedicament(item, med)"
                        class="cursor-pointer hover:bg-blue-50 dark:hover:bg-blue-500/10 transition-colors"
                      >
                        <td class="px-3 py-2.5 font-bold text-gray-800 dark:text-gray-200">
                          {{ med.brand_name }}
                          <span class="block text-[10px] font-normal text-gray-400 font-mono">{{ med.dci_name }}</span>
                        </td>
                        <td class="px-3 py-2.5 text-gray-500 font-mono">{{ med.dosage }}</td>
                      </tr>
                    </tbody>
                  </table>
           
                </div>
                       <div class="p-2 border-t border-gray-100 dark:border-gray-700 bg-gray-50 dark:bg-gray-800/50">
                  <button 
                    type="button" 
                    @click="openCustomMedicamentModal(item)"
                    class="text-xs font-bold text-blue-600 dark:text-blue-400 hover:underline w-full text-center"
                  >
                    + Créer un médicament personnalisé
                  </button>
                </div>
              </div>

              <div class="lg:col-span-7 grid grid-cols-1 sm:grid-cols-3 gap-4">
                <div class="space-y-1.5">
                  <label class="text-[10px] font-bold text-gray-400 uppercase tracking-wider block">Dosage</label>
                  <input
                    v-model="item.dosage"
                    type="text"
                    placeholder="Ex: 1000 mg"
                    class="w-full text-sm rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 px-3 py-2.5 outline-none focus:border-blue-500 dark:text-white"
                  />
                </div>

                <div class="space-y-1.5">
                  <label class="text-[10px] font-bold text-gray-400 uppercase tracking-wider block">Fréquence</label>
                  <input
                    v-model="item.frequency"
                    type="text"
                    placeholder="Ex: 3 fois par jour"
                    class="w-full text-sm rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 px-3 py-2.5 outline-none focus:border-blue-500 dark:text-white"
                  />
                </div>

                <div class="space-y-1.5">
                  <label class="text-[10px] font-bold text-gray-400 uppercase tracking-wider block">Durée</label>
                  <input
                    v-model="item.duration"
                    type="text"
                    placeholder="Ex: 5 jours"
                    class="w-full text-sm rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 px-3 py-2.5 outline-none focus:border-blue-500 dark:text-white"
                  />
                </div>
              </div>

              <div class="lg:col-span-12 space-y-1.5">
                <label class="text-[10px] font-bold text-gray-400 uppercase tracking-wider block">Recommandation de prise</label>
                <input
                  v-model="item.instructions"
                  type="text"
                  placeholder="Ex: À prendre au milieu du repas avec un grand verre d'eau..."
                  class="w-full text-xs rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 px-4 py-2 outline-none focus:border-blue-500 dark:text-white italic"
                />
              </div>

            </div>
          </div>
        </div>
      </div>

      <transition name="fade">
        <div v-if="Object.keys(errors).length > 0" class="p-4 bg-red-50 dark:bg-red-900/10 border border-red-100 dark:border-red-800/30 rounded-xl">
          <div class="flex gap-3">
            <span class="text-red-500">⚠️</span>
            <div class="text-xs text-red-600 dark:text-red-400 font-medium">
              <p class="font-bold">Champs invalides :</p>
              <ul class="list-disc list-inside mt-1 space-y-0.5">
                <li v-for="(error, key) in errors" :key="key">{{ Array.isArray(error) ? error[0] : error }}</li>
              </ul>
            </div>
          </div>
        </div>
      </transition>

      <div class="flex items-center justify-end gap-3 pt-4 border-t border-gray-100 dark:border-gray-800">
        <button 
          type="button" 
          @click="resetForm" 
          class="px-5 py-3 rounded-xl text-xs text-gray-500 font-bold hover:bg-gray-100 dark:hover:bg-gray-900 transition-colors"
        >
          Réinitialiser el formulaire
        </button>
        <button 
          type="button" 
          @click="$router.back()" 
          class="px-5 py-3 rounded-xl text-xs text-gray-500 font-bold hover:bg-gray-100 dark:hover:bg-gray-900 transition-colors"
        >
          Annuler
        </button>
        <button 
          type="submit" 
          :disabled="isSubmitting || loadingAppointment || !appointmentData" 
          class="px-8 py-3 rounded-xl bg-blue-600 hover:bg-blue-700 disabled:opacity-40 disabled:cursor-not-allowed text-white text-xs font-bold shadow-md shadow-blue-500/10 transition-all active:scale-[0.98] flex items-center gap-2"
        >
          <svg v-if="isSubmitting" class="animate-spin h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
          <span>{{ isSubmitting ? 'Enregistrement...' : 'Valider la consultation Doctolib' }}</span>
        </button>
      </div>

    </form>
  </div>
  <div
  v-if="showCustomModal"
  class="fixed inset-0 z-50 flex items-center justify-center bg-black/40"
>
  <div class="bg-white dark:bg-gray-900 rounded-xl p-6 w-[500px] space-y-4">

    <h2 class="font-bold text-lg">
      Nouveau médicament
    </h2>

    <input
      v-model="customMedicament.brand_name"
      placeholder="Nom commercial"
      class="w-full border rounded-lg p-2"
    />

    <input
      v-model="customMedicament.dci_name"
      placeholder="DCI"
      class="w-full border rounded-lg p-2"
    />

    <input
      v-model="customMedicament.dosage"
      placeholder="Dosage"
      class="w-full border rounded-lg p-2"
    />

    <input
      v-model="customMedicament.form"
      placeholder="Forme"
      class="w-full border rounded-lg p-2"
    />

    <div class="flex justify-end gap-2">

      <button
        class="px-4 py-2 rounded border"
        @click="showCustomModal=false"
      >
        Annuler
      </button>

      <button
        class="px-4 py-2 rounded bg-blue-600 text-white"
        @click="saveCustomMedicament"
      >
        Enregistrer
      </button>

    </div>

  </div>
</div>
</template>

<script>
import { reactive, ref, onMounted } from "vue";
import { useRouter, useRoute } from "vue-router";
import { 
  createConsultation,
  getAppointmentForConsultation,
  searchMedicaments as searchMedicamentsApi ,

} from "@/api/consultationService";

import { 
createCustomMedicament
} from "@/api/ordonnaceService";

export default {
  name: 'ConsultationCreate',
  setup() {
    const medicamentSearch = ref("");
    const medicamentResults = ref([]);
    const searchLoading = ref(false);
    const prescriptionItems = ref([]);

    const router = useRouter();
    const route = useRoute();
    const isSubmitting = ref(false);
    const loadingAppointment = ref(true);
    const appointmentError = ref(null);
    const appointmentData = ref(null);
    const errors = ref({});
    const showCustomModal = ref(false);
    const currentItem = ref(null);
    const appointmentCode = ref(route.query.appointment_code || "");

    const customMedicament = reactive({
      brand_name: "",
      dci_name: "",
      dosage: "",
      form: ""
    });


    const openCustomMedicamentModal = (item) => {
      currentItem.value = item;

      customMedicament.brand_name = item.medicament_name || "";
      customMedicament.dci_name = "";
      customMedicament.dosage = "";
      customMedicament.form = "";

      showCustomModal.value = true;
    };

    const saveCustomMedicament = async () => {
      try {
        const med = await createCustomMedicament(customMedicament);

        currentItem.value.medicament = med.id;
        currentItem.value.medicament_name = med.brand_name;
        currentItem.value.dosage = med.dosage;
        currentItem.value.results = [];

        showCustomModal.value = false;
      } catch (e) {
        console.error(e);
        alert("Erreur lors de la création du médicament.");
      }
    };

    const formData = reactive({
      symptoms: '',
      diagnosis: '',
      prescription: '',
      notes: ''
    });

    const fetchAppointmentDetails = async () => {
      if (!appointmentCode.value) {
        appointmentError.value = "Aucun code de rendez-vous fourni";
        loadingAppointment.value = false;
        return;
      }
      
      try {
        const data = await getAppointmentForConsultation(appointmentCode.value);
        appointmentData.value = data;
      } catch (error) {
        console.error("Error fetching appointment:", error);
        if (error.response?.data?.error) {
          appointmentError.value = error.response.data.error;
          if (error.response.data.consultation_id) {
            appointmentError.value += " Redirection vers la consultation existante...";
            setTimeout(() => {
              router.push(`/consultations/${error.response.data.consultation_id}`);
            }, 2000);
          }
        } else {
          appointmentError.value = "Impossible de charger les informations du rendez-vous";
        }
      } finally {
        loadingAppointment.value = false;
      }
    };

    onMounted(() => {
      fetchAppointmentDetails();
    });

    const formatDate = (dateString) => {
      if (!dateString) return "N/A";
      const date = new Date(dateString);
      return date.toLocaleDateString('fr-FR', { 
        weekday: 'long', 
        year: 'numeric', 
        month: 'long', 
        day: 'numeric' 
      });
    };

    const resetForm = () => {
      formData.symptoms = '';
      formData.diagnosis = '';
      formData.prescription = '';
      formData.notes = '';
      prescriptionItems.value = [];
      errors.value = {};
    };

    const addPrescriptionItem = () => {
      prescriptionItems.value.push({
        medicament: null,
        medicament_name: "",
        dosage: "",
        frequency: "",
        duration: "",
        instructions: "",
        results: []
      });
    };

    const removePrescriptionItem = (index) => {
      prescriptionItems.value.splice(index, 1);
    };

    const searchMedicaments = async (item) => {
      if (!item.medicament_name || item.medicament_name.length < 2) {
        item.results = [];
        return;
      }
      // Debounce simple pour éviter de spammer le serveur
      clearTimeout(item.debounceTimer);
      item.debounceTimer = setTimeout(async () => {
        try {
          const data = await searchMedicamentsApi(item.medicament_name);
          item.results = data;
        } catch (e) { item.results = []; }
      }, 300);
    };

    const selectMedicament = (item, med) => {
      item.medicament = med.id;
      item.medicament_name = med.brand_name;
      item.dosage = med.dosage;
      item.results = [];
    };

const handleSubmit = async () => {
  // Validation simple
  if (prescriptionItems.value.some(i => !i.medicament_name)) {
    errors.value = { prescription: "Veuillez vérifier les noms des médicaments." };
    return;
  }
  
  isSubmitting.value = true;
  try {
    await createConsultation({
      appointment_code: appointmentCode.value,
      ...formData,
      items: prescriptionItems.value.map(i => ({
          medicament: i.medicament,
          dosage: i.dosage,
          frequency: i.frequency,
          duration: i.duration,
          instructions: i.instructions
      }))
    });
    router.push({ path: '/consultations', query: { success: 'true' } });
  } catch (err) {
    // Gestion propre des erreurs de validation venant du backend
    errors.value = err.response?.data || { general: "Erreur de connexion" };
  } finally {
    isSubmitting.value = false;
  }
};

    return {
      formData,
      isSubmitting,
      loadingAppointment,
      appointmentError,
      appointmentData,
      appointmentCode,
      errors,
      handleSubmit,
      formatDate,
      resetForm,
      medicamentSearch,
      medicamentResults,
      searchLoading,
      prescriptionItems,
      addPrescriptionItem,
      removePrescriptionItem,
      searchMedicaments,
      selectMedicament,
      showCustomModal,
      customMedicament,
      openCustomMedicamentModal,
      saveCustomMedicament,
    };
  }
};
</script>

<style scoped>
.fade-enter-active, .fade-leave-active { transition: all 0.2s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; transform: translateY(-4px); }
.custom-scrollbar::-webkit-scrollbar { width: 5px; height: 5px; }
.custom-scrollbar::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 4px; }
.dark .custom-scrollbar::-webkit-scrollbar-thumb { background: #334155; }
</style>