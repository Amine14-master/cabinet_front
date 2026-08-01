<script setup lang="ts">
import { ref, reactive, onMounted } from "vue"
import FullCalendar from "@fullcalendar/vue3"
import dayGridPlugin from "@fullcalendar/daygrid"
import interactionPlugin from "@fullcalendar/interaction"
import AdminLayout from "@/layouts/AdminLayout.vue"
import PageBreadcrumb from "@/layouts/common/PageBreadcrumb.vue"

import {
  getWorkingDays, createWorkingDay, updateWorkingDay,
  getOverrides, createOverride, updateOverride,
  type Period, type WorkingDayPayload, type OverridePayload
} from "@/api/workingDaysService"

/* ================= STATE ================= */
const workingDays = ref<any[]>([])
const overrides = ref<any[]>([])
const activeTab = ref<"weekly" | "override">("weekly")
const today = new Date().toISOString().split('T')[0]

// حالات الـ Edit والـ Drawer
const isDrawerOpen = ref(false)
const editingId = ref<number | null>(null)

const form = reactive({
  day: "monday" as WorkingDayPayload["day"],
  date: "",
  period: "morning" as Period,
  start_time: "",
  end_time: "",
  max_patients: 15,
  is_closed: false
})

const errors = reactive({
  date: "", start_time: "", end_time: "", general: ""
})

/* ================= CALENDAR SETTINGS ================= */
const calendarEvents = ref<any[]>([])
const calendarOptions = reactive({
  plugins: [dayGridPlugin, interactionPlugin],
  initialView: "dayGridMonth",
  events: calendarEvents, 
  headerToolbar: { left: "prev,next today", center: "title", right: "" },
  locale: 'fr',
  height: 'auto',
  eventDisplay: 'block',
})

/* ================= FETCH DATA ================= */
const dayMap = (d: string) => ({ sunday: 0, monday: 1, tuesday: 2, wednesday: 3, thursday: 4, friday: 5, saturday: 6 }[d] || 0)

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
      backgroundColor: item.period === "morning" ? "#dbeafe" : "#ffedd5",
      textColor: item.period === "morning" ? "#1e40af" : "#9a3412",
      borderColor: "transparent"
    }))

    const exceptions = ov.map((item: any) => ({
      title: item.is_closed ? "❌ FERMÉ" : `EXC: ${item.max_patients} pts`,
      start: item.date,
      allDay: true,
      backgroundColor: item.is_closed ? "#fee2e2" : "#dcfce7",
      textColor: item.is_closed ? "#b91c1c" : "#15803d",
      borderColor: "transparent"
    }))

    calendarEvents.value = [...weekly, ...exceptions]
  } catch (e) {
    console.error("FETCH ERROR:", e)
  }
}

/* ================= EDIT LOGIC ================= */
const startEdit = (item: any, type: "weekly" | "override") => {
  activeTab.value = type
  editingId.value = item.id
  
  form.day = item.day || "monday"
  form.date = item.date || ""
  form.period = item.period
  form.start_time = item.start_time?.substring(0, 5) || ""
  form.end_time = item.end_time?.substring(0, 5) || ""
  form.max_patients = item.max_patients
  form.is_closed = item.is_closed || false
  
  isDrawerOpen.value = true
}

const closeDrawer = () => {
  isDrawerOpen.value = false
  editingId.value = null
  // إعادة تصفير الفورم
  form.date = ""; form.start_time = ""; form.end_time = ""; form.is_closed = false
}

/* ================= VALIDATION LOGIC ================= */
const validateForm = () => {
  errors.date = ""; errors.start_time = ""; errors.end_time = ""; errors.general = ""
  let isValid = true

  if (activeTab.value === 'override' && !form.date) {
    errors.date = "La date est obligatoire."
    isValid = false
  }

  if (!form.is_closed) {
    if (!form.start_time) { errors.start_time = "Requis."; isValid = false }
    if (!form.end_time) { errors.end_time = "Requis."; isValid = false }
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
    const start = form.start_time.length === 5 ? form.start_time + ":00" : form.start_time
    const end = form.end_time.length === 5 ? form.end_time + ":00" : form.end_time

    const payload: any = {
      period: form.period,
      start_time: form.is_closed ? null : start,
      end_time: form.is_closed ? null : end,
      max_patients: form.max_patients,
    }

    if (activeTab.value === "weekly") {
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

    <div class="grid grid-cols-12 gap-6 p-4 font-sans relative">
      <!-- CALENDAR -->
      <div class="col-span-12 lg:col-span-8 bg-white p-6 rounded-[24px] shadow-sm border border-gray-100">
        <FullCalendar :options="calendarOptions" />
      </div>

      <!-- SIDEBAR: FORM & LIST -->
      <div class="col-span-12 lg:col-span-4 space-y-6">
        
        <!-- FORM (For Adding New) -->
        <div class="bg-white p-6 rounded-[24px] shadow-sm border border-gray-100">
          <div class="flex bg-gray-100 p-1 rounded-xl mb-6">
            <button @click="activeTab = 'weekly'; editingId = null" 
              :class="activeTab === 'weekly' && !editingId ? 'bg-white shadow-sm text-blue-600' : 'text-gray-500'" 
              class="flex-1 py-2 text-[11px] font-black rounded-lg transition-all uppercase tracking-tight">
              Programme Fixe
            </button>
            <button @click="activeTab = 'override'; editingId = null" 
              :class="activeTab === 'override' && !editingId ? 'bg-white shadow-sm text-blue-600' : 'text-gray-500'" 
              class="flex-1 py-2 text-[11px] font-black rounded-lg transition-all uppercase tracking-tight">
              Exception (Date)
            </button>
          </div>

          <!-- FORM INPUTS (Dynamic based on activeTab) -->
          <div class="space-y-4">
             <!-- ... (نفس مدخلات الفورم اللي كانت عندك في الكود الأصلي) ... -->
             <div v-if="activeTab === 'weekly'">
               <label class="text-[11px] font-black text-gray-400 uppercase ml-1">Jour</label>
               <select v-model="form.day" class="w-full mt-1 bg-gray-50 border border-gray-200 rounded-xl p-3 text-sm">
                  <option value="monday">Lundi</option><option value="tuesday">Mardi</option><option value="wednesday">Mercredi</option>
                  <option value="thursday">Jeudi</option><option value="friday">Vendredi</option><option value="saturday">Samedi</option><option value="sunday">Dimanche</option>
               </select>
             </div>
             <div v-else>
               <label class="text-[11px] font-black text-gray-400 uppercase ml-1">Date spécifique</label>
               <input v-model="form.date" type="date" :min="today" class="w-full mt-1 bg-gray-50 border border-gray-200 rounded-xl p-3 text-sm" />
             </div>

             <div>
               <label class="text-[11px] font-black text-gray-400 uppercase ml-1">Période</label>
               <select v-model="form.period" class="w-full mt-1 bg-gray-50 border border-gray-200 rounded-xl p-3 text-sm">
                 <option value="morning">Matin</option>
                 <option value="afternoon">Après-midi</option>
               </select>
             </div>

             <div v-if="activeTab === 'override'" class="flex items-center gap-2 p-3 bg-red-50/50 border border-red-100 rounded-xl">
               <input v-model="form.is_closed" type="checkbox" id="closed" class="w-4 h-4 accent-red-600" />
               <label for="closed" class="text-xs font-bold text-red-700 uppercase">Fermé</label>
             </div>

             <template v-if="!form.is_closed">
               <div class="grid grid-cols-2 gap-3">
                 <input v-model="form.start_time" type="time" class="bg-gray-50 border border-gray-200 rounded-xl p-3 text-sm" />
                 <input v-model="form.end_time" type="time" class="bg-gray-50 border border-gray-200 rounded-xl p-3 text-sm" />
               </div>
               <input v-model="form.max_patients" type="number" placeholder="Max patients" class="w-full bg-gray-50 border border-gray-200 rounded-xl p-3 text-sm" />
             </template>

             <button @click="submitHandler" class="w-full bg-blue-600 text-white font-bold py-4 rounded-xl shadow-lg">
               {{ editingId ? 'Mettre à jour' : 'Ajouter au programme' }}
             </button>
          </div>
        </div>

        <!-- RECAP LIST (WITH EDIT BUTTONS) -->
        <div class="bg-white rounded-[24px] shadow-sm border border-gray-100 overflow-hidden">
          <div class="p-4 bg-gray-50/50 border-b font-bold text-[10px] text-gray-400 uppercase text-center tracking-widest">Résumé</div>
          <div class="max-h-[300px] overflow-y-auto divide-y divide-gray-50">
            <div v-for="wd in workingDays" :key="'wd'+wd.id" class="p-3 flex justify-between items-center text-sm group">
              <span class="capitalize font-bold text-gray-700">{{ wd.day }} <small class="text-gray-400">({{ wd.period }})</small></span>
              <button @click="startEdit(wd, 'weekly')" class="opacity-0 group-hover:opacity-100 bg-blue-50 text-blue-600 px-3 py-1 rounded-lg text-[10px] font-bold uppercase transition-all">Modifier</button>
            </div>
            <div v-for="ov in overrides" :key="'ov'+ov.id" class="p-3 flex justify-between items-center text-sm group">
              <span class="text-gray-500 font-medium">{{ ov.date }}</span>
              <button @click="startEdit(ov, 'override')" class="opacity-0 group-hover:opacity-100 bg-amber-50 text-amber-600 px-3 py-1 rounded-lg text-[10px] font-bold uppercase transition-all">Modifier</button>
            </div>
          </div>
        </div>
      </div>

      <!-- EDIT DRAWER (Yakhrej ghir ki tcliqui Edit) -->
      <Transition name="slide">
        <div v-if="isDrawerOpen" class="fixed right-0 top-0 h-full w-[380px] bg-white shadow-2xl z-[1000] p-6 border-l border-gray-100 overflow-y-auto">
            <div class="flex justify-between items-center mb-8">
                <h3 class="font-black text-lg text-gray-800 uppercase italic">Modifier Créneau</h3>
                <button @click="closeDrawer" class="text-gray-400 hover:text-red-500 text-2xl">&times;</button>
            </div>

            <!-- Copy of the Form inside Drawer for Editing -->
            <div class="space-y-5">
                <div>
                    <label class="text-[11px] font-black text-gray-400 uppercase">Période</label>
                    <div class="grid grid-cols-2 gap-2 mt-2">
                        <button @click="form.period = 'morning'" :class="form.period === 'morning' ? 'bg-blue-600 text-white' : 'bg-gray-100'" class="py-3 rounded-xl text-[10px] font-black uppercase transition-all">Matin ☀️</button>
                        <button @click="form.period = 'afternoon'" :class="form.period === 'afternoon' ? 'bg-orange-500 text-white' : 'bg-gray-100'" class="py-3 rounded-xl text-[10px] font-black uppercase transition-all">Soir 🌙</button>
                    </div>
                </div>

                <div v-if="!form.is_closed" class="grid grid-cols-2 gap-4">
                    <input v-model="form.start_time" type="time" class="bg-gray-50 border border-gray-200 rounded-xl p-4 text-sm font-bold" />
                    <input v-model="form.end_time" type="time" class="bg-gray-50 border border-gray-200 rounded-xl p-4 text-sm font-bold" />
                </div>

                <div>
                    <label class="text-[11px] font-black text-gray-400 uppercase">Max Patients</label>
                    <input v-model="form.max_patients" type="number" class="w-full bg-gray-50 border border-gray-200 rounded-xl p-4 text-sm font-bold mt-1" />
                </div>

                <button @click="submitHandler" class="w-full bg-blue-600 text-white font-black py-4 rounded-2xl shadow-xl mt-6">
                    Mettre à jour maintenant
                </button>
            </div>
        </div>
      </Transition>

      <!-- Overlay for Drawer -->
      <div v-if="isDrawerOpen" @click="closeDrawer" class="fixed inset-0 bg-black/10 backdrop-blur-[2px] z-[999]"></div>
    </div>
  </AdminLayout>
</template>

<style scoped>
.slide-enter-active, .slide-leave-active { transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1); }
.slide-enter-from, .slide-leave-to { transform: translateX(100%); }
</style>