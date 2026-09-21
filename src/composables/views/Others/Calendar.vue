<template>
  <AdminLayout>
    <PageBreadcrumb :pageTitle="currentPageTitle" />

    <div class="grid grid-cols-1 xl:grid-cols-3 gap-6">
      <!-- GAUCHE : Calendrier -->
      <div
        class="xl:col-span-2 rounded-2xl border border-gray-200 bg-white dark:border-gray-800 dark:bg-white/[0.03]"
      >
        <div class="p-4 border-b border-gray-100 dark:border-gray-800">
          <h2 class="text-xl font-semibold text-gray-800 dark:text-white">Planning du Médecin</h2>
          <p class="text-sm text-gray-500 mt-1">Gérez les disponibilités et rendez-vous</p>
        </div>

        <div class="custom-calendar p-4">
          <FullCalendar ref="calendarRef" class="min-h-screen" :options="calendarOptions" />
        </div>
      </div>

      <!-- DROITE : Disponibilité -->
      <div
        class="rounded-2xl border border-gray-200 bg-white p-5 dark:border-gray-800 dark:bg-white/[0.03]"
      >
        <div class="flex items-center justify-between mb-5">
          <div>
            <h3 class="text-lg font-semibold text-gray-800 dark:text-white">Disponibilité</h3>
            <p class="text-sm text-gray-500">Ajouter les créneaux disponibles</p>
          </div>
        </div>

        <!-- Date -->
        <div class="mb-4">
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
            Date
          </label>
          <input
            v-model="slotDate"
            type="date"
            class="h-11 w-full rounded-xl border border-gray-300 px-4 text-sm dark:border-gray-700 dark:bg-gray-900 dark:text-white"
          />
        </div>

        <!-- Heure début -->
        <div class="mb-4">
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
            Heure de début
          </label>
          <input
            v-model="slotStart"
            type="time"
            class="h-11 w-full rounded-xl border border-gray-300 px-4 text-sm dark:border-gray-700 dark:bg-gray-900 dark:text-white"
          />
        </div>

        <!-- Heure fin -->
        <div class="mb-4">
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
            Heure de fin
          </label>
          <input
            v-model="slotEnd"
            type="time"
            class="h-11 w-full rounded-xl border border-gray-300 px-4 text-sm dark:border-gray-700 dark:bg-gray-900 dark:text-white"
          />
        </div>

        <!-- Durée -->
        <div class="mb-4">
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
            Durée du créneau
          </label>

          <select
            v-model="slotDuration"
            class="h-11 w-full rounded-xl border border-gray-300 px-4 text-sm dark:border-gray-700 dark:bg-gray-900 dark:text-white"
          >
            <option value="15">15 min</option>
            <option value="20">20 min</option>
            <option value="30">30 min</option>
            <option value="45">45 min</option>
            <option value="60">60 min</option>
          </select>
        </div>

        <!-- Patients max -->
        <div class="mb-6">
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
            Patients max / créneau
          </label>

          <input
            v-model="maxPatients"
            type="number"
            min="1"
            class="h-11 w-full rounded-xl border border-gray-300 px-4 text-sm dark:border-gray-700 dark:bg-gray-900 dark:text-white"
          />
        </div>

        <!-- Bouton -->
        <button
          @click="addAvailability"
          class="w-full rounded-xl bg-brand-500 px-4 py-3 text-sm font-medium text-white hover:bg-brand-600"
        >
          Ajouter disponibilité
        </button>

        <!-- Liste -->
        <div class="mt-6">
          <h4 class="text-sm font-semibold text-gray-700 dark:text-gray-300 mb-3">
            Créneaux du jour
          </h4>

          <div
            v-for="(item, index) in availabilities"
            :key="index"
            class="mb-3 rounded-xl border border-gray-200 p-3 dark:border-gray-700"
          >
            <div class="flex items-center justify-between">
              <div>
                <p class="font-medium text-gray-800 dark:text-white">
                  {{ item.date }}
                </p>
                <p class="text-sm text-gray-500">{{ item.start }} - {{ item.end }}</p>
              </div>

              <span class="rounded-full bg-green-100 px-3 py-1 text-xs font-medium text-green-700">
                {{ item.max }} Patients
              </span>
            </div>
          </div>

          <div v-if="availabilities.length === 0" class="text-sm text-gray-400">
            Aucune disponibilité ajoutée
          </div>
        </div>
      </div>
    </div>
  </AdminLayout>
</template>

<script setup>
import { ref, reactive } from 'vue'
import FullCalendar from '@fullcalendar/vue3'
import dayGridPlugin from '@fullcalendar/daygrid'
import interactionPlugin from '@fullcalendar/interaction'

import AdminLayout from '@/layouts/AdminLayout.vue'
import PageBreadcrumb from '@/layouts/common/PageBreadcrumb.vue'

const currentPageTitle = ref('Calendrier Médecin')
const calendarRef = ref(null)

const slotDate = ref('')
const slotStart = ref('')
const slotEnd = ref('')
const slotDuration = ref('30')
const maxPatients = ref(2)

const availabilities = ref([])
const events = ref([])

const addAvailability = () => {
  if (!slotDate.value || !slotStart.value || !slotEnd.value) return

  availabilities.value.push({
    date: slotDate.value,
    start: slotStart.value,
    end: slotEnd.value,
    duration: slotDuration.value,
    max: maxPatients.value,
  })

  events.value.push({
    title: 'Disponible',
    start: slotDate.value,
    color: '#22c55e',
  })

  slotDate.value = ''
  slotStart.value = ''
  slotEnd.value = ''
}

const calendarOptions = reactive({
  plugins: [dayGridPlugin, interactionPlugin],
  initialView: 'dayGridMonth',
  selectable: true,
  events: events,
  headerToolbar: {
    left: 'prev,next today',
    center: 'title',
    right: 'dayGridMonth',
  },
})
</script>
