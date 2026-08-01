<template>
  <div class="space-y-4">
    <div class="overflow-hidden rounded-xl border border-gray-200 bg-white dark:border-gray-800 dark:bg-white/[0.03]">
      <div class="max-w-full overflow-x-auto custom-scrollbar">
        <form @submit.prevent="handleSubmit" class="grid grid-cols-1 gap-6 p-4">
          
          <!-- Card 1: Appointment Information (Read-only) -->
          <div class="bg-white dark:bg-white/[0.03] rounded-3xl border border-gray-100 dark:border-gray-800 p-8 shadow-sm">
            <div class="flex items-center gap-3 mb-6">
              <div class="w-10 h-10 rounded-xl bg-blue-50 dark:bg-blue-500/10 flex items-center justify-center text-blue-600">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                </svg>
              </div>
              <h2 class="text-lg font-bold dark:text-white">Informations du Rendez-vous</h2>
            </div>

            <div v-if="loadingAppointment" class="text-center py-8">
              <div class="inline-block h-8 w-8 animate-spin rounded-full border-4 border-solid border-blue-600 border-r-transparent"></div>
              <p class="text-sm text-gray-500 mt-2">Chargement du rendez-vous...</p>
            </div>

            <div v-else-if="appointmentError" class="text-center py-8">
              <div class="bg-red-50 dark:bg-red-900/20 text-red-600 dark:text-red-400 p-4 rounded-xl">
                {{ appointmentError }}
              </div>
            </div>

            <div v-else class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <!-- Patient Info -->
              <div class="space-y-2 md:col-span-2">
                <label class="text-xs font-bold text-gray-400 uppercase tracking-wider ml-1">Patient</label>
                <div class="relative overflow-hidden rounded-2xl bg-gradient-to-r from-blue-50 to-indigo-50 dark:from-blue-900/20 dark:to-indigo-900/20 p-4">
                  <div class="flex items-center gap-4">
                    <div class="w-14 h-14 rounded-xl bg-blue-600 flex items-center justify-center text-white text-xl font-bold shadow-lg">
                      {{ appointmentData?.patient_name?.charAt(0).toUpperCase() || '?' }}
                    </div>
                    <div>
                      <p class="font-bold text-gray-800 dark:text-white text-lg">{{ appointmentData?.patient_name }}</p>
                      <p class="text-sm text-gray-500 dark:text-gray-400">Code: {{ appointmentData?.patient_code }}</p>
                      <p class="text-sm text-gray-500 dark:text-gray-400">📞 {{ appointmentData?.patient_phone }}</p>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Appointment Code -->
              <div class="space-y-2">
                <label class="text-xs font-bold text-gray-400 uppercase tracking-wider ml-1">Code Rendez-vous</label>
                <div class="p-3.5 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700">
                  <p class="font-mono text-gray-700 dark:text-gray-300">{{ appointmentData?.code }}</p>
                </div>
              </div>

              <!-- Date -->
              <div class="space-y-2">
                <label class="text-xs font-bold text-gray-400 uppercase tracking-wider ml-1">Date</label>
                <div class="p-3.5 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700">
                  <p class="text-gray-700 dark:text-gray-300">{{ formatDate(appointmentData?.appointment_date) }}</p>
                </div>
              </div>

              <!-- Period -->
              <div class="space-y-2">
                <label class="text-xs font-bold text-gray-400 uppercase tracking-wider ml-1">Période</label>
                <div class="p-3.5 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700">
                  <span :class="[
                    'inline-flex items-center gap-1 text-xs px-2 py-1 rounded-full',
                    appointmentData?.period === 'morning' ? 'bg-amber-100 text-amber-700 dark:bg-amber-500/20 dark:text-amber-400' : 'bg-indigo-100 text-indigo-700 dark:bg-indigo-500/20 dark:text-indigo-400'
                  ]">
                    <span>{{ appointmentData?.period === 'morning' ? '🌅' : '☀️' }}</span>
                    <span class="capitalize">{{ appointmentData?.period === 'morning' ? 'Matin (08:00-12:00)' : 'Après-midi (13:00-17:00)' }}</span>
                  </span>
                </div>
              </div>

              <!-- Status -->
              <div class="space-y-2">
                <label class="text-xs font-bold text-gray-400 uppercase tracking-wider ml-1">Statut</label>
                <div class="p-3.5 rounded-2xl bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700">
                  <span class="inline-flex px-2 py-1 rounded-full text-xs font-bold bg-blue-100 text-blue-700 dark:bg-blue-500/20 dark:text-blue-400">
                    {{ appointmentData?.status === 'scheduled' ? '⏰ Programmé' : appointmentData?.status }}
                  </span>
                </div>
              </div>
            </div>
          </div>

          <!-- Card 2: Détails de la Consultation -->
          <div class="bg-white dark:bg-white/[0.03] rounded-3xl border border-gray-100 dark:border-gray-800 p-8 shadow-sm">
            <div class="flex items-center gap-3 mb-6">
              <div class="w-10 h-10 rounded-xl bg-amber-50 dark:bg-amber-500/10 flex items-center justify-center text-amber-600">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
                </svg>
              </div>
              <h2 class="text-lg font-bold dark:text-white">Détails de la Consultation</h2>
            </div>

            <div class="space-y-6">
              <!-- Symptoms -->
              <div class="space-y-2">
                <label class="text-xs font-bold text-gray-400 uppercase tracking-wider ml-1">Symptômes & Motif</label>
                <textarea 
                  v-model="formData.symptoms" 
                  rows="3" 
                  class="w-full px-4 py-3.5 rounded-2xl border border-gray-200 dark:border-gray-700 dark:bg-gray-900 focus:ring-2 focus:ring-blue-500 outline-none dark:text-white resize-none transition-all"
                  placeholder="Description des symptômes..."
                ></textarea>
              </div>

              <!-- Diagnosis & Prescription -->
              <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="space-y-2">
                  <label class="text-xs font-bold text-gray-400 uppercase tracking-wider ml-1">Diagnostic</label>
                  <textarea 
                    v-model="formData.diagnosis" 
                    rows="5" 
                    class="w-full px-4 py-3.5 rounded-2xl border border-gray-200 dark:border-gray-700 dark:bg-gray-900 focus:ring-2 focus:ring-blue-500 outline-none dark:text-white resize-none transition-all"
                    placeholder="Analyse médicale..."
                  ></textarea>
                </div>

                <div class="space-y-2">
                  <label class="text-xs font-bold text-gray-400 uppercase tracking-wider ml-1">Prescription</label>
                  <textarea 
                    v-model="formData.prescription" 
                    rows="5" 
                    class="w-full px-4 py-3.5 rounded-2xl border border-gray-200 dark:border-gray-700 dark:bg-gray-900 focus:ring-2 focus:ring-blue-500 outline-none dark:text-white resize-none transition-all"
                    placeholder="Médicaments et conseils..."
                  ></textarea>
                </div>
              </div>

              <!-- Notes -->
              <div class="space-y-2">
                <label class="text-xs font-bold text-gray-400 uppercase tracking-wider ml-1">Notes supplémentaires</label>
                <textarea 
                  v-model="formData.notes" 
                  rows="2" 
                  class="w-full px-4 py-3.5 rounded-2xl border border-gray-200 dark:border-gray-700 dark:bg-gray-900 focus:ring-2 focus:ring-blue-500 outline-none dark:text-white resize-none transition-all"
                  placeholder="Informations complémentaires..."
                ></textarea>
              </div>
            </div>
          </div>

          <!-- Error Alert -->
          <transition name="fade">
            <div v-if="Object.keys(errors).length > 0" class="mx-8">
              <div class="p-4 bg-red-50 dark:bg-red-900/20 rounded-2xl border border-red-100 dark:border-red-800">
                <div class="flex items-start gap-3">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-red-600 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                  <div class="flex-1">
                    <p class="text-sm font-semibold text-red-600 dark:text-red-400">Erreurs:</p>
                    <ul class="list-disc list-inside text-sm text-red-600 dark:text-red-400 mt-1">
                      <li v-for="(error, key) in errors" :key="key">{{ Array.isArray(error) ? error[0] : error }}</li>
                    </ul>
                  </div>
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
              :disabled="isSubmitting || loadingAppointment || !appointmentData" 
              class="px-10 py-3.5 rounded-2xl bg-blue-600 text-white font-bold hover:bg-blue-700 shadow-xl shadow-blue-500/25 transition-all active:scale-95 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
            >
              <svg v-if="isSubmitting" class="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              <span>{{ isSubmitting ? 'Enregistrement...' : 'Enregistrer la Consultation' }}</span>
            </button>
          </div>

        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { reactive, ref, onMounted } from "vue";
import { useRouter, useRoute } from "vue-router";
import { createConsultation, getAppointmentForConsultation } from "@/api/consultationService";

export default {
  name: 'ConsultationCreate',
  setup() {
    const router = useRouter();
    const route = useRoute();
    const isSubmitting = ref(false);
    const loadingAppointment = ref(true);
    const appointmentError = ref(null);
    const appointmentData = ref(null);
    const errors = ref({});

    const appointmentCode = ref(route.query.appointment_code || "");

    const formData = reactive({
      symptoms: '',
      diagnosis: '',
      prescription: '',
      notes: ''
    });

    // Fetch appointment details
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
      errors.value = {};
    };

    const handleSubmit = async () => {
      errors.value = {};
      
      // Validate at least one field is filled (optional - can remove if not needed)
      if (!formData.symptoms && !formData.diagnosis && !formData.prescription && !formData.notes) {
        errors.value.general = "Veuillez remplir au moins un champ de la consultation";
        return;
      }
      
      isSubmitting.value = true;

      try {
        const response = await createConsultation({
          appointment_code: appointmentCode.value,
          symptoms: formData.symptoms,
          diagnosis: formData.diagnosis,
          prescription: formData.prescription,
          notes: formData.notes
        });
        
        console.log('Success:', response);
        router.push({ path: '/consultations', query: { success: 'true' } });
      } catch (err) {
        console.error("Erreur lors de la création:", err);
        if (err.response && err.response.data) {
          errors.value = err.response.data;
        } else {
          errors.value = { general: "Une erreur est survenue. Veuillez réessayer." };
        }
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
      resetForm
    };
  }
};
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