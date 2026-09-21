<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import FullCalendar from '@fullcalendar/vue3'
import dayGridPlugin from '@fullcalendar/daygrid'
import interactionPlugin from '@fullcalendar/interaction'
import AdminLayout from '@/layouts/AdminLayout.vue'
import PageBreadcrumb from '@/layouts/common/PageBreadcrumb.vue'

import {
  getWorkingDays,
  createWorkingDay,
  updateWorkingDay,
  getOverrides,
  createOverride,
  updateOverride,
  type Period,
  type WorkingDayPayload,
  type OverridePayload,
} from '@/api/workingDaysService'

/* ================= STATE ================= */
const workingDays = ref<any[]>([])
const overrides = ref<any[]>([])
const activeTab = ref<'weekly' | 'override'>('weekly')
const today = new Date().toISOString().split('T')[0]

// حالات الـ Edit والـ Drawer
const isDrawerOpen = ref(false)
const editingId = ref<number | null>(null)

const form = reactive({
  day: 'monday' as WorkingDayPayload['day'],
  date: '',
  period: 'morning' as Period,
  start_time: '',
  end_time: '',
  max_patients: 15,
  is_closed: false,
})

const errors = reactive({
  date: '',
  start_time: '',
  end_time: '',
  general: '',
})

/* ================= CALENDAR SETTINGS ================= */
const calendarEvents = ref<any[]>([])
const calendarOptions = reactive({
  plugins: [dayGridPlugin, interactionPlugin],
  initialView: 'dayGridMonth',
  events: calendarEvents,
  headerToolbar: { left: 'prev,next today', center: 'title', right: '' },
  locale: 'fr',
  height: 'auto',
  eventDisplay: 'block',
})

/* ================= FETCH DATA ================= */
const dayMap = (d: string) =>
  ({ sunday: 0, monday: 1, tuesday: 2, wednesday: 3, thursday: 4, friday: 5, saturday: 6 })[d] || 0

const fetchData = async () => {
  try {
    const [wd, ov] = await Promise.all([getWorkingDays(), getOverrides()])
    workingDays.value = wd
    overrides.value = ov

    const weekly = wd.map((item: any) => ({
      title: `Fixe: ${item.max_patients} pts`,
      daysOfWeek: [dayMap(item.day)],
      startTime: item.start_time,
      endTime: item.end_time,
      backgroundColor: item.period === 'morning' ? '#dbeafe' : '#ffedd5',
      textColor: item.period === 'morning' ? '#1e40af' : '#9a3412',
      borderColor: 'transparent',
    }))

    const exceptions = ov.map((item: any) => ({
      title: item.is_closed ? '❌ FERMÉ' : `EXC: ${item.max_patients} pts`,
      start: item.date,
      allDay: true,
      backgroundColor: item.is_closed ? '#fee2e2' : '#dcfce7',
      textColor: item.is_closed ? '#b91c1c' : '#15803d',
      borderColor: 'transparent',
    }))

    calendarEvents.value = [...weekly, ...exceptions]
  } catch (e) {
    console.error('FETCH ERROR:', e)
  }
}

/* ================= EDIT LOGIC ================= */
const startEdit = (item: any, type: 'weekly' | 'override') => {
  activeTab.value = type
  editingId.value = item.id

  form.day = item.day || 'monday'
  form.date = item.date || ''
  form.period = item.period
  form.start_time = item.start_time?.substring(0, 5) || ''
  form.end_time = item.end_time?.substring(0, 5) || ''
  form.max_patients = item.max_patients
  form.is_closed = item.is_closed || false

  isDrawerOpen.value = true
}

const closeDrawer = () => {
  isDrawerOpen.value = false
  editingId.value = null
  // إعادة تصفير الفورم
  form.date = ''
  form.start_time = ''
  form.end_time = ''
  form.is_closed = false
}

/* ================= VALIDATION LOGIC ================= */
const validateForm = () => {
  errors.date = ''
  errors.start_time = ''
  errors.end_time = ''
  errors.general = ''
  let isValid = true

  if (activeTab.value === 'override' && !form.date) {
    errors.date = 'La date est obligatoire.'
    isValid = false
  }

  if (!form.is_closed) {
    if (!form.start_time) {
      errors.start_time = 'Requis.'
      isValid = false
    }
    if (!form.end_time) {
      errors.end_time = 'Requis.'
      isValid = false
    }
    if (form.start_time && form.end_time && form.start_time >= form.end_time) {
      errors.end_time = "L'heure de fin doit être après le début."
      isValid = false
    }
  }
  return isValid
}

/* ================= SUBMIT HANDLER ================= */
const submitHandler = async () => {
  if (!validateForm()) return

  try {
    const start = form.start_time.length === 5 ? form.start_time + ':00' : form.start_time
    const end = form.end_time.length === 5 ? form.end_time + ':00' : form.end_time

    const payload: any = {
      period: form.period,
      start_time: form.is_closed ? null : start,
      end_time: form.is_closed ? null : end,
      max_patients: form.max_patients,
    }

    if (activeTab.value === 'weekly') {
      payload.day = form.day
      if (editingId.value) {
        await updateWorkingDay(editingId.value, payload)
      } else {
        await createWorkingDay(payload)
      }
    } else {
      payload.date = form.date
      payload.is_closed = form.is_closed
      if (editingId.value) {
        await updateOverride(editingId.value, payload)
      } else {
        await createOverride(payload)
      }
    }

    await fetchData()
    closeDrawer()
  } catch (e: any) {
    errors.general = "Erreur lors de l'enregistrement. Vérifiez les données."
  }
}

onMounted(fetchData)
</script>

<template>
  <AdminLayout>
    <PageBreadcrumb pageTitle="Planning & Exceptions" />

    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 w-full relative pb-20">
      <!-- CALENDAR -->
      <div
        class="lg:col-span-8 bg-white dark:bg-zinc-950 p-6 lg:p-8 rounded-3xl shadow-sm border border-slate-200 dark:border-zinc-800"
      >
        <FullCalendar :options="calendarOptions" />
      </div>

      <!-- SIDEBAR: FORM & LIST -->
      <div class="lg:col-span-4 flex flex-col space-y-6">
        <!-- FORM (For Adding New) -->
        <div
          class="bg-white dark:bg-zinc-950 p-6 lg:p-8 rounded-3xl shadow-sm border border-slate-200 dark:border-zinc-800"
        >
          <div
            class="flex bg-slate-100 dark:bg-zinc-900 p-1.5 rounded-xl mb-8 border border-slate-200 dark:border-zinc-800 shadow-inner"
          >
            <button
              type="button"
              @click="
                activeTab = 'weekly'
                editingId = null
              "
              :class="
                activeTab === 'weekly' && !editingId
                  ? 'bg-white dark:bg-zinc-800 shadow-sm text-brand-600 dark:text-brand-400'
                  : 'text-slate-500 hover:text-slate-700 dark:hover:text-slate-300'
              "
              class="flex-1 py-2 text-xs font-bold rounded-lg transition-all"
            >
              Prog. Fixe
            </button>
            <button
              type="button"
              @click="
                activeTab = 'override'
                editingId = null
              "
              :class="
                activeTab === 'override' && !editingId
                  ? 'bg-white dark:bg-zinc-800 shadow-sm text-brand-600 dark:text-brand-400'
                  : 'text-slate-500 hover:text-slate-700 dark:hover:text-slate-300'
              "
              class="flex-1 py-2 text-xs font-bold rounded-lg transition-all"
            >
              Exception
            </button>
          </div>

          <!-- FORM INPUTS (Dynamic based on activeTab) -->
          <div class="space-y-5">
            <div v-if="activeTab === 'weekly'">
              <label
                class="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider ml-1"
                >Jour</label
              >
              <select
                v-model="form.day"
                class="w-full mt-2 bg-slate-50 dark:bg-zinc-900 border border-slate-200 dark:border-zinc-700 text-slate-800 dark:text-white rounded-xl p-3 text-sm focus:ring-2 focus:ring-brand-500 outline-none transition-all"
              >
                <option value="monday">Lundi</option>
                <option value="tuesday">Mardi</option>
                <option value="wednesday">Mercredi</option>
                <option value="thursday">Jeudi</option>
                <option value="friday">Vendredi</option>
                <option value="saturday">Samedi</option>
                <option value="sunday">Dimanche</option>
              </select>
            </div>
            <div v-else>
              <label
                class="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider ml-1"
                >Date spécifique</label
              >
              <input
                v-model="form.date"
                type="date"
                :min="today"
                class="w-full mt-2 bg-slate-50 dark:bg-zinc-900 border border-slate-200 dark:border-zinc-700 text-slate-800 dark:text-white rounded-xl p-3 text-sm focus:ring-2 focus:ring-brand-500 outline-none transition-all"
              />
            </div>

            <div>
              <label
                class="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider ml-1"
                >Période</label
              >
              <select
                v-model="form.period"
                class="w-full mt-2 bg-slate-50 dark:bg-zinc-900 border border-slate-200 dark:border-zinc-700 text-slate-800 dark:text-white rounded-xl p-3 text-sm focus:ring-2 focus:ring-brand-500 outline-none transition-all"
              >
                <option value="morning">Matin</option>
                <option value="afternoon">Après-midi</option>
              </select>
            </div>

            <div
              v-if="activeTab === 'override'"
              class="flex items-center gap-3 p-4 bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800 rounded-xl"
            >
              <input
                v-model="form.is_closed"
                type="checkbox"
                id="closed"
                class="w-5 h-5 accent-red-600 rounded"
              />
              <label
                for="closed"
                class="text-sm font-bold text-red-700 dark:text-red-400 uppercase cursor-pointer"
                >Fermé ce jour-là</label
              >
            </div>

            <template v-if="!form.is_closed">
              <div class="grid grid-cols-2 gap-4">
                <div>
                  <label
                    class="text-[10px] font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider ml-1"
                    >Début</label
                  >
                  <input
                    v-model="form.start_time"
                    type="time"
                    class="w-full mt-1 bg-slate-50 dark:bg-zinc-900 border border-slate-200 dark:border-zinc-700 text-slate-800 dark:text-white rounded-xl p-3 text-sm focus:ring-2 focus:ring-brand-500 outline-none transition-all"
                  />
                </div>
                <div>
                  <label
                    class="text-[10px] font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider ml-1"
                    >Fin</label
                  >
                  <input
                    v-model="form.end_time"
                    type="time"
                    class="w-full mt-1 bg-slate-50 dark:bg-zinc-900 border border-slate-200 dark:border-zinc-700 text-slate-800 dark:text-white rounded-xl p-3 text-sm focus:ring-2 focus:ring-brand-500 outline-none transition-all"
                  />
                </div>
              </div>
              <div>
                <label
                  class="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider ml-1"
                  >Capacité (Max Patients)</label
                >
                <input
                  v-model="form.max_patients"
                  type="number"
                  placeholder="Ex: 15"
                  class="w-full mt-2 bg-slate-50 dark:bg-zinc-900 border border-slate-200 dark:border-zinc-700 text-slate-800 dark:text-white rounded-xl p-3 text-sm focus:ring-2 focus:ring-brand-500 outline-none transition-all"
                />
              </div>
            </template>

            <button
              type="button"
              @click="submitHandler"
              class="w-full bg-brand-600 text-white font-bold py-3.5 mt-2 rounded-xl shadow-md shadow-brand-500/20 hover:bg-brand-700 active:scale-95 transition-all flex items-center justify-center gap-2"
            >
              {{ editingId ? 'Mettre à jour' : 'Ajouter au programme' }}
            </button>
          </div>
        </div>

        <!-- RECAP LIST (WITH EDIT BUTTONS) -->
        <div
          class="bg-white dark:bg-zinc-950 rounded-3xl shadow-sm border border-slate-200 dark:border-zinc-800 overflow-hidden flex flex-col h-full"
        >
          <div
            class="p-4 bg-slate-50 dark:bg-zinc-900 border-b border-slate-200 dark:border-zinc-800 font-bold text-[10px] text-slate-500 dark:text-slate-400 uppercase text-center tracking-widest"
          >
            Résumé des Plages Horaires
          </div>
          <div
            class="flex-1 overflow-y-auto max-h-[400px] divide-y divide-slate-100 dark:divide-zinc-800 custom-scrollbar"
          >
            <div
              v-if="workingDays.length === 0 && overrides.length === 0"
              class="p-8 text-center text-sm text-slate-500 italic"
            >
              Aucun créneau configuré.
            </div>

            <div
              v-for="wd in workingDays"
              :key="'wd' + wd.id"
              class="p-4 flex justify-between items-center text-sm group hover:bg-slate-50 dark:hover:bg-zinc-900 transition-colors"
            >
              <span class="capitalize font-bold text-slate-800 dark:text-slate-200"
                >{{ wd.day }}
                <span class="text-slate-500 dark:text-slate-400 font-medium"
                  >({{ wd.period === 'morning' ? 'Matin' : 'Après-midi' }})</span
                ></span
              >
              <button
                type="button"
                @click="startEdit(wd, 'weekly')"
                class="opacity-0 group-hover:opacity-100 bg-brand-50 dark:bg-brand-900/30 text-brand-600 dark:text-brand-400 px-3 py-1.5 rounded-lg text-xs font-bold transition-all hover:bg-brand-100 dark:hover:bg-brand-900/50"
              >
                Modifier
              </button>
            </div>
            <div
              v-for="ov in overrides"
              :key="'ov' + ov.id"
              class="p-4 flex justify-between items-center text-sm group hover:bg-slate-50 dark:hover:bg-zinc-900 transition-colors"
            >
              <span class="text-slate-600 dark:text-slate-300 font-medium"
                ><span
                  class="bg-amber-100 dark:bg-amber-900/30 text-amber-700 dark:text-amber-400 text-[10px] uppercase font-bold px-2 py-0.5 rounded-md mr-2"
                  >Exc</span
                >{{ ov.date }}</span
              >
              <button
                type="button"
                @click="startEdit(ov, 'override')"
                class="opacity-0 group-hover:opacity-100 bg-amber-50 dark:bg-amber-900/30 text-amber-700 dark:text-amber-400 px-3 py-1.5 rounded-lg text-xs font-bold transition-all hover:bg-amber-100 dark:hover:bg-amber-900/50"
              >
                Modifier
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- EDIT DRAWER -->
      <Teleport to="body">
        <Transition name="slide">
          <div
            v-if="isDrawerOpen"
            class="fixed right-0 top-0 h-full w-full sm:w-[420px] bg-white dark:bg-zinc-950 shadow-2xl z-[100] border-l border-slate-200 dark:border-zinc-800 flex flex-col"
          >
            <div
              class="flex justify-between items-center p-6 border-b border-slate-100 dark:border-zinc-800"
            >
              <h3 class="font-bold text-lg text-slate-800 dark:text-white">Modifier Créneau</h3>
              <button
                type="button"
                @click="closeDrawer"
                class="w-8 h-8 flex items-center justify-center rounded-full bg-slate-100 dark:bg-zinc-800 text-slate-500 hover:text-slate-800 dark:hover:text-white transition-colors"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    fill-rule="evenodd"
                    d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                    clip-rule="evenodd"
                  />
                </svg>
              </button>
            </div>

            <!-- Form Content inside Drawer -->
            <div class="p-6 space-y-6 flex-1 overflow-y-auto">
              <div>
                <label
                  class="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider mb-3 block"
                  >Période</label
                >
                <div class="grid grid-cols-2 gap-3">
                  <button
                    type="button"
                    @click="form.period = 'morning'"
                    :class="
                      form.period === 'morning'
                        ? 'bg-brand-600 text-white ring-2 ring-brand-600 ring-offset-2 dark:ring-offset-zinc-950'
                        : 'bg-slate-100 dark:bg-zinc-900 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-zinc-800'
                    "
                    class="py-3 rounded-xl text-sm font-bold transition-all"
                  >
                    Matin ☀️
                  </button>
                  <button
                    type="button"
                    @click="form.period = 'afternoon'"
                    :class="
                      form.period === 'afternoon'
                        ? 'bg-brand-600 text-white ring-2 ring-brand-600 ring-offset-2 dark:ring-offset-zinc-950'
                        : 'bg-slate-100 dark:bg-zinc-900 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-zinc-800'
                    "
                    class="py-3 rounded-xl text-sm font-bold transition-all"
                  >
                    Après-midi 🌙
                  </button>
                </div>
              </div>

              <div v-if="!form.is_closed" class="grid grid-cols-2 gap-4">
                <div>
                  <label
                    class="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider block mb-1"
                    >Début</label
                  >
                  <input
                    v-model="form.start_time"
                    type="time"
                    class="w-full bg-slate-50 dark:bg-zinc-900 border border-slate-200 dark:border-zinc-700 text-slate-800 dark:text-white rounded-xl p-3 text-sm focus:ring-2 focus:ring-brand-500 outline-none transition-all"
                  />
                </div>
                <div>
                  <label
                    class="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider block mb-1"
                    >Fin</label
                  >
                  <input
                    v-model="form.end_time"
                    type="time"
                    class="w-full bg-slate-50 dark:bg-zinc-900 border border-slate-200 dark:border-zinc-700 text-slate-800 dark:text-white rounded-xl p-3 text-sm focus:ring-2 focus:ring-brand-500 outline-none transition-all"
                  />
                </div>
              </div>

              <div>
                <label
                  class="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider block mb-1"
                  >Max Patients</label
                >
                <input
                  v-model="form.max_patients"
                  type="number"
                  class="w-full bg-slate-50 dark:bg-zinc-900 border border-slate-200 dark:border-zinc-700 text-slate-800 dark:text-white rounded-xl p-3 text-sm focus:ring-2 focus:ring-brand-500 outline-none transition-all"
                />
              </div>
            </div>

            <!-- Drawer Footer -->
            <div
              class="p-6 border-t border-slate-100 dark:border-zinc-800 bg-slate-50 dark:bg-zinc-900/50 flex gap-3"
            >
              <button
                type="button"
                @click="closeDrawer"
                class="flex-1 px-4 py-3 rounded-xl text-slate-600 dark:text-slate-300 font-bold hover:bg-slate-200 dark:hover:bg-zinc-800 transition-colors text-sm"
              >
                Annuler
              </button>
              <button
                type="button"
                @click="submitHandler"
                class="flex-1 bg-brand-600 text-white font-bold py-3 rounded-xl shadow-md shadow-brand-500/20 hover:bg-brand-700 transition-colors text-sm flex justify-center items-center"
              >
                Enregistrer
              </button>
            </div>
          </div>
        </Transition>

        <!-- Overlay for Drawer -->
        <Transition name="fade">
          <div
            v-if="isDrawerOpen"
            @click="closeDrawer"
            class="fixed inset-0 bg-slate-900/40 backdrop-blur-sm z-[99]"
          ></div>
        </Transition>
      </Teleport>
    </div>
  </AdminLayout>
</template>

<style scoped>
.slide-enter-active,
.slide-leave-active {
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}
.slide-enter-from,
.slide-leave-to {
  transform: translateX(100%);
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* FullCalendar Pro Max Theme Overrides */
:deep(.fc) {
  --fc-border-color: transparent;
  --fc-daygrid-event-dot-width: 8px;
  --fc-today-bg-color: rgba(79, 70, 229, 0.05); /* brand-50 */
  --fc-event-border-color: transparent;
}
:deep(.fc-theme-standard td),
:deep(.fc-theme-standard th) {
  border-color: #f1f5f9; /* slate-100 */
}
:deep(.dark .fc-theme-standard td),
:deep(.dark .fc-theme-standard th) {
  border-color: #27272a; /* zinc-800 */
}
:deep(.fc-col-header-cell-cushion) {
  padding: 12px 8px;
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  color: #64748b; /* slate-500 */
  letter-spacing: 0.05em;
}
:deep(.fc-daygrid-day-number) {
  font-size: 0.875rem;
  font-weight: 600;
  padding: 8px;
  color: #334155; /* slate-700 */
}
:deep(.dark .fc-daygrid-day-number) {
  color: #e2e8f0; /* slate-200 */
}
:deep(.fc-event) {
  border-radius: 8px;
  padding: 2px 6px;
  font-size: 0.7rem;
  font-weight: 700;
  border: none;
  box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  margin-bottom: 4px;
}
:deep(.fc-toolbar-title) {
  font-size: 1.25rem !important;
  font-weight: 800 !important;
  text-transform: capitalize;
}
:deep(.fc-button-primary) {
  background-color: transparent !important;
  border-color: #e2e8f0 !important;
  color: #64748b !important;
  border-radius: 12px !important;
  font-weight: 600 !important;
  text-transform: capitalize !important;
  box-shadow: none !important;
  transition: all 0.2s ease !important;
}
:deep(.dark .fc-button-primary) {
  border-color: #3f3f46 !important; /* zinc-700 */
  color: #a1a1aa !important; /* zinc-400 */
}
:deep(.fc-button-primary:hover) {
  background-color: #f8fafc !important; /* slate-50 */
  color: #4f46e5 !important; /* brand-600 */
}
:deep(.dark .fc-button-primary:hover) {
  background-color: #27272a !important; /* zinc-800 */
}
:deep(.fc-button-primary:not(:disabled).fc-button-active),
:deep(.fc-button-primary:not(:disabled):active) {
  background-color: #4f46e5 !important;
  border-color: #4f46e5 !important;
  color: white !important;
}
</style>
