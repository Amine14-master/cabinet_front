<template>
  <div class="space-y-8 p-1">


    <!-- Metrics Bento Grid -->
    <div class="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4">
      <!-- Total Card -->
      <div class="rounded-2xl border border-gray-100 bg-white p-5 dark:border-gray-800/60 dark:bg-zinc-900/40 backdrop-blur-sm">
        <div class="flex items-center justify-between">
          <p class="text-xs font-medium tracking-wider text-gray-400 uppercase">Total</p>
          <div class="h-8 w-8 rounded-lg bg-gray-50 dark:bg-zinc-800 flex items-center justify-center text-gray-500">
            <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
            </svg>
          </div>
        </div>
        <p class="text-3xl font-semibold tracking-tight text-gray-900 dark:text-white mt-2">{{ appointments.length }}</p>
      </div>

      <!-- Programmés Card -->
      <div class="rounded-2xl border border-gray-100 bg-white p-5 dark:border-gray-800/60 dark:bg-zinc-900/40 backdrop-blur-sm">
        <div class="flex items-center justify-between">
          <p class="text-xs font-medium tracking-wider text-gray-400 uppercase">Programmés</p>
          <div class="h-8 w-8 rounded-lg bg-teal-50/60 dark:bg-teal-500/10 flex items-center justify-center text-teal-600 dark:text-teal-400">
            <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
        </div>
        <p class="text-3xl font-semibold tracking-tight text-gray-900 dark:text-white mt-2">{{ getStatusCount('scheduled') }}</p>
      </div>

      <!-- Terminés Card -->
      <div class="rounded-2xl border border-gray-100 bg-white p-5 dark:border-gray-800/60 dark:bg-zinc-900/40 backdrop-blur-sm">
        <div class="flex items-center justify-between">
          <p class="text-xs font-medium tracking-wider text-gray-400 uppercase">Terminés</p>
          <div class="h-8 w-8 rounded-lg bg-emerald-50/60 dark:bg-emerald-500/10 flex items-center justify-center text-emerald-600 dark:text-emerald-400">
            <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
        </div>
        <p class="text-3xl font-semibold tracking-tight text-gray-900 dark:text-white mt-2">{{ getStatusCount('completed') }}</p>
      </div>

      <!-- Annulés Card -->
      <div class="rounded-2xl border border-gray-100 bg-white p-5 dark:border-gray-800/60 dark:bg-zinc-900/40 backdrop-blur-sm">
        <div class="flex items-center justify-between">
          <p class="text-xs font-medium tracking-wider text-gray-400 uppercase">Annulés</p>
          <div class="h-8 w-8 rounded-lg bg-rose-50/60 dark:bg-rose-500/10 flex items-center justify-center text-rose-600 dark:text-rose-400">
            <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </div>
        </div>
        <p class="text-3xl font-semibold tracking-tight text-gray-900 dark:text-white mt-2">{{ getStatusCount('cancelled') }}</p>
      </div>
    </div>

    <!-- Filters Toolbar -->
    <div class="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between bg-gray-50/50 dark:bg-zinc-900/20 p-2 rounded-xl">
      <div class="relative flex-1 max-w-md">
        <span class="absolute inset-y-0 left-0 flex items-center pl-3.5 text-gray-400 pointer-events-none">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
        </span>
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Rechercher par nom, téléphone, code, date..."
          class="w-full rounded-lg border border-gray-200/80 bg-white py-2 pl-10 pr-4 text-sm text-gray-900 outline-none focus:border-teal-500 focus:ring-1 focus:ring-teal-500/20 dark:border-gray-800 dark:bg-zinc-900 dark:text-white transition-all placeholder:text-gray-400"
        />
      </div>

      <div class="flex items-center gap-2">
        <select 
          v-model="statusFilter"
          class="rounded-lg border border-gray-200/80 bg-white px-3 py-2 text-sm font-medium text-gray-600 outline-none focus:border-teal-500 dark:border-gray-800 dark:bg-zinc-900 dark:text-gray-300 cursor-pointer transition-all appearance-none pr-8 relative bg-[url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%2371717a%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E')] bg-[length:0.65rem_auto] bg-[right_0.75rem_center] bg-no-repeat"
        >
          <option value="All">Tous les statuts</option>
          <option value="scheduled">Programmés</option>
          <option value="completed">Terminés</option>
          <option value="cancelled">Annulés</option>
        </select>

        <button 
          @click="resetFilters"
          class="p-2 rounded-lg border border-gray-200/80 bg-white text-gray-500 hover:text-gray-700 hover:bg-gray-50 dark:border-gray-800 dark:bg-zinc-900 dark:text-gray-400 dark:hover:bg-zinc-800 transition-all"
          title="Réinitialiser"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
          </svg>
        </button>
      </div>
    </div>

    <!-- Modern Data Table Layout -->
    <div class="overflow-hidden rounded-xl border border-gray-100 bg-white dark:border-gray-800/80 dark:bg-zinc-950/40 backdrop-blur-sm">
      <div class="max-w-full overflow-x-auto custom-scrollbar">
        <table class="min-w-full table-fixed">
          <thead>
            <tr class="border-b border-gray-100 dark:border-gray-800/80 bg-gray-50/40 dark:bg-zinc-900/10">
              <th class="w-1/3 px-6 py-3.5 text-left text-xs font-semibold tracking-wider text-gray-400 uppercase">Patient</th>
              <th class="w-1/4 px-6 py-3.5 text-left text-xs font-semibold tracking-wider text-gray-400 uppercase">Date & Période</th>
              <th class="w-1/6 px-6 py-3.5 text-left text-xs font-semibold tracking-wider text-gray-400 uppercase">Code</th>
              <th class="w-1/6 px-6 py-3.5 text-left text-xs font-semibold tracking-wider text-gray-400 uppercase">Statut</th>
              <th class="w-1/6 px-6 py-3.5 text-center text-xs font-semibold tracking-wider text-gray-400 uppercase">Actions</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-100 dark:divide-gray-800/60">
            <!-- Loading State -->
            <tr v-if="loading">
              <td colspan="5" class="px-6 py-12 text-center">
                <div class="flex flex-col items-center justify-center gap-3">
                  <div class="h-6 w-6 animate-spin rounded-full border-2 border-solid border-teal-600 border-r-transparent"></div>
                  <p class="text-xs text-gray-400">Chargement des données...</p>
                </div>
              </td>
            </tr>

            <!-- Empty State -->
            <tr v-else-if="paginatedAppointments.length === 0">
              <td colspan="5" class="px-6 py-16 text-center">
                <div class="flex flex-col items-center justify-center max-w-xs mx-auto">
                  <div class="p-3 bg-gray-50 dark:bg-zinc-900 rounded-xl text-gray-400 mb-3">
                    <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                    </svg>
                  </div>
                  <p class="text-sm font-medium text-gray-700 dark:text-zinc-300">Aucun rendez-vous</p>
                  <p class="text-xs text-gray-400 mt-0.5">Aucune donnée ne correspond à vos filtres actuels.</p>
                </div>
              </td>
            </tr>

            <!-- Table Rows -->
            <tr
              v-for="app in paginatedAppointments"
              :key="app.code"
              class="hover:bg-gray-50/50 dark:hover:bg-zinc-900/10 transition-colors group"
            >
              <td class="px-6 py-3.5 whitespace-nowrap">
                <div class="flex items-center gap-3">
                  <!-- Premium Minimal Avatar Frame with Gender SVG Icons -->
             <div :class="[
  'w-10 h-10 rounded-lg flex items-center justify-center shadow-inner transition-transform group-hover:scale-[1.02]',
  isMale(app.gender) 
    ? 'bg-teal-100 text-teal-600 dark:bg-teal-500/20' 
    : 'bg-pink-100 text-pink-600 dark:bg-pink-500/20'
]">
  <!-- Male Icon -->
  <svg v-if="isMale(app.gender)" xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
    <path stroke-linecap="round" stroke-linejoin="round" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
  </svg>
  <!-- Female Icon -->
  <svg v-else xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
    <path stroke-linecap="round" stroke-linejoin="round" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
    <circle cx="12" cy="10" r="2.5" fill="currentColor" opacity="0.25"/>
  </svg>
</div>
                  <div class="truncate">
                    <span class="block text-sm font-medium text-gray-800 dark:text-zinc-200 truncate">{{ app.patientName || 'Patient inconnu' }}</span>
                    <span class="block text-xs text-gray-400 font-mono tracking-tight mt-0.5">{{ app.patientPhone || '—' }}</span>
                  </div>
                </div>
              </td>

              <td class="px-6 py-3.5 whitespace-nowrap">
                <p class="text-xs font-medium text-gray-700 dark:text-zinc-300 truncate">{{ app.date }}</p>
                <div class="mt-1">
                  <span :class="[
                    'inline-flex items-center gap-1.5 text-[11px] font-medium px-2 py-0.5 rounded-md border',
                    app.period === 'morning' 
                      ? 'bg-amber-50/50 text-amber-700 border-amber-100 dark:bg-amber-500/5 dark:text-amber-400 dark:border-amber-500/10' 
                      : 'bg-indigo-50/50 text-indigo-700 border-indigo-100 dark:bg-indigo-500/5 dark:text-indigo-400 dark:border-indigo-500/10'
                  ]">
                    <span class="w-1.5 h-1.5 rounded-full" :class="app.period === 'morning' ? 'bg-amber-500' : 'bg-indigo-500'"></span>
                    {{ app.period === 'morning' ? 'Matin' : 'Après-midi' }}
                  </span>
                </div>
              </td>

              <td class="px-6 py-3.5 whitespace-nowrap">
                <span class="text-xs font-mono text-gray-500 dark:text-zinc-400 bg-gray-50 dark:bg-zinc-900 border border-gray-100 dark:border-zinc-800 px-2 py-0.5 rounded-md">
                  {{ app.code }}
                </span>
              </td>

              <td class="px-6 py-3.5 whitespace-nowrap">
                <div class="relative inline-block w-full max-w-[130px]">
                  <select 
                    v-model="app.status"
                    @change="handleStatusUpdate(app.code, app.status)"
                    :class="[
                      'w-full appearance-none rounded-lg px-2.5 py-1 text-xs font-medium border cursor-pointer outline-none transition-all pr-7 bg-[length:0.6rem_auto] bg-[right_0.5rem_center] bg-no-repeat',
                      statusClasses(app.status)
                    ]"
                  >
                    <option value="scheduled">Programmé</option>
                    <option value="completed">Terminé</option>
                    <option value="cancelled">Annulé</option>
                  </select>
                </div>
              </td>

              <td class="px-6 py-3.5 whitespace-nowrap text-center">
                <div class="flex items-center justify-center gap-1">
                  <button 
                    @click.stop="openDetails(app)" 
                    class="p-1.5 rounded-md text-gray-400 hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-zinc-900 transition-colors active:scale-95"
                    title="Détails"
                  >
                    <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                      <path stroke-linecap="round" stroke-linejoin="round" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                    </svg>
                  </button>
                  
                  <button 
                    v-if="app.status === 'scheduled' && !['secretary', 'assistant'].includes(role)"
                    @click="startConsultation(app)"
                    class="p-1.5 rounded-md text-gray-400 hover:text-teal-600 hover:bg-teal-50 dark:hover:bg-teal-500/10 transition-colors active:scale-95"
                    title="Consulter"
                  >
                    <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z" />
                      <path stroke-linecap="round" stroke-linejoin="round" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Compact Pagination Bar -->
      <div v-if="filteredAppointments.length > 0" class="flex items-center justify-between px-6 py-4 border-t border-gray-100 dark:border-gray-800/80 bg-gray-50/20 dark:bg-zinc-900/5">
        <div class="text-xs text-gray-400">
          Affichage de <span class="font-medium text-gray-700 dark:text-zinc-300">{{ startIndex + 1 }}</span> à 
          <span class="font-medium text-gray-700 dark:text-zinc-300">{{ Math.min(endIndex, filteredAppointments.length) }}</span> sur 
          <span class="font-medium text-gray-700 dark:text-zinc-300">{{ filteredAppointments.length }}</span> résultats
        </div>
        <div class="flex items-center gap-2">
          <button 
            @click="prevPage" 
            :disabled="currentPage === 1"
            class="px-3 py-1.5 text-xs font-medium rounded-lg border border-gray-200 dark:border-zinc-800 bg-white dark:bg-zinc-900 text-gray-600 dark:text-zinc-400 hover:bg-gray-50 dark:hover:bg-zinc-800 transition-colors disabled:opacity-40 disabled:hover:bg-white dark:disabled:hover:bg-zinc-900 disabled:cursor-not-allowed"
          >
            Précédent
          </button>
          <span class="text-xs font-medium text-gray-500 dark:text-zinc-400 px-1">
            {{ currentPage }} / {{ totalPages }}
          </span>
          <button 
            @click="nextPage" 
            :disabled="currentPage === totalPages"
            class="px-3 py-1.5 text-xs font-medium rounded-lg border border-gray-200 dark:border-zinc-800 bg-white dark:bg-zinc-900 text-gray-600 dark:text-zinc-400 hover:bg-gray-50 dark:hover:bg-zinc-800 transition-colors disabled:opacity-40 disabled:hover:bg-white dark:disabled:hover:bg-zinc-900 disabled:cursor-not-allowed"
          >
            Suivant
          </button>
        </div>
      </div>
    </div>

    <!-- Premium Slide Drawer -->
    <Transition name="slide">
      <div v-if="selectedAppointment" class="fixed inset-0 z-50 overflow-hidden">
        <div class="absolute inset-0 bg-zinc-950/40 backdrop-blur-sm transition-opacity" @click="closeDetails"></div>
        <div class="absolute inset-y-0 right-0 max-w-sm w-full bg-white dark:bg-zinc-950 border-l border-gray-100 dark:border-zinc-900 shadow-xl flex flex-col">
          <!-- Drawer Header -->
          <div class="p-5 border-b border-gray-100 dark:border-zinc-900 flex justify-between items-center">
            <div>
              <h2 class="text-base font-semibold text-gray-900 dark:text-white">Fiche Rendez-vous</h2>
              <p class="text-xs font-mono text-gray-400 mt-0.5">{{ selectedAppointment.code }}</p>
            </div>
            <button @click="closeDetails" class="p-1.5 rounded-lg text-gray-400 hover:bg-gray-50 dark:hover:bg-zinc-900 transition-colors">
              <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
          
          <!-- Drawer Content -->
          <div class="p-5 space-y-6 flex-1 overflow-y-auto">
            <!-- Profile Card with Adaptive Gender Icon -->
    <!-- Profile Card with Adaptive Gender Icon -->
<div class="flex flex-col items-center text-center p-4 rounded-xl bg-gray-50/50 dark:bg-zinc-900/30 border border-gray-100/50 dark:border-zinc-900">
  <div :class="[
    'w-16 h-16 rounded-xl flex items-center justify-center text-xl shadow-inner mb-3 border',
    isMale(selectedAppointment.gender) 
      ? 'bg-teal-100 text-teal-600 border-teal-200 dark:bg-teal-500/20 dark:text-teal-400 dark:border-teal-500/10' 
      : 'bg-pink-100 text-pink-600 border-pink-200 dark:bg-pink-500/20 dark:text-pink-400 dark:border-pink-500/10'
  ]">
    <svg v-if="isMale(selectedAppointment.gender)" xmlns="http://www.w3.org/2000/svg" class="w-7 h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
      <path stroke-linecap="round" stroke-linejoin="round" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
    </svg>
    <svg v-else xmlns="http://www.w3.org/2000/svg" class="w-7 h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
      <path stroke-linecap="round" stroke-linejoin="round" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
      <circle cx="12" cy="10" r="2.5" fill="currentColor" opacity="0.25"/>
    </svg>
  </div>
  <h3 class="text-base font-medium text-gray-900 dark:text-white">{{ selectedAppointment.patientName || 'Patient inconnu' }}</h3>
  <p class="text-xs text-gray-400 font-mono mt-0.5">{{ selectedAppointment.patientPhone || '—' }}</p>
  <p v-if="selectedAppointment.email" class="text-xs text-gray-400 font-mono mt-0.5">{{ selectedAppointment.email }}</p>
  
  <div class="flex gap-2 mt-3 flex-wrap justify-center">
    <span v-if="selectedAppointment.bloodGroup" class="text-[10px] px-2 py-0.5 bg-red-50 text-red-600 border border-red-100 rounded-md font-medium">Sang: {{ selectedAppointment.bloodGroup }}</span>
    <span v-if="selectedAppointment.dateOfBirth" class="text-[10px] px-2 py-0.5 bg-teal-50 text-teal-600 border border-teal-100 rounded-md font-medium">Né(e) le: {{ selectedAppointment.dateOfBirth }}</span>
  </div>
</div>

            <!-- Metadata Group -->
            <div class="space-y-2.5">
              <div class="flex items-center justify-between p-3 rounded-lg border border-gray-100 dark:border-zinc-900">
                <span class="text-xs text-gray-400">Date prévue</span>
                <span class="text-xs font-medium text-gray-800 dark:text-zinc-200">{{ selectedAppointment.date }}</span>
              </div>
              <div class="flex items-center justify-between p-3 rounded-lg border border-gray-100 dark:border-zinc-900">
                <span class="text-xs text-gray-400">Période</span>
                <span class="text-xs font-medium text-gray-800 dark:text-zinc-200">{{ selectedAppointment.period === 'morning' ? 'Matin (08:00 - 12:00)' : 'Après-midi (13:00 - 17:00)' }}</span>
              </div>
              <div class="flex items-center justify-between p-3 rounded-lg border border-gray-100 dark:border-zinc-900">
                <span class="text-xs text-gray-400">Statut du dossier</span>
                <span class="text-xs font-medium capitalize">
                  {{ selectedAppointment.status === 'scheduled' ? 'Programmé' : selectedAppointment.status === 'completed' ? 'Terminé' : 'Annulé' }}
                </span>
              </div>
            </div>
          </div>

          <!-- Drawer Footer -->
          <div class="p-5 border-t border-gray-100 dark:border-zinc-900 space-y-2">
            <button 
              v-if="selectedAppointment.status === 'scheduled'"
              @click="startConsultation(selectedAppointment)"  
              class="w-full bg-teal-600 hover:bg-teal-700 text-white font-medium py-2.5 rounded-lg text-sm transition-all active:scale-[0.98]"
            >
              Commencer la consultation
            </button>
            <button 
              @click="closeDetails"
              class="w-full bg-gray-50 hover:bg-gray-100 dark:bg-zinc-900 dark:hover:bg-zinc-800 text-gray-600 dark:text-zinc-400 font-medium py-2 rounded-lg text-xs transition-colors"
            >
              Fermer la fiche
            </button>
          </div>
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from "vue"
import { useRouter } from "vue-router"
import { getDoctorAppointments, updateAppointmentStatus } from "@/api/appointmentService"

const router = useRouter()
const role = localStorage.getItem('role') || 'doctor'
const searchQuery = ref("")
const statusFilter = ref("All")
const selectedAppointment = ref(null)
const appointments = ref([])
const loading = ref(true)

// Pagination State
const currentPage = ref(1)
const itemsPerPage = ref(8)

const fetchAppointments = async () => {
  try {
    loading.value = true
    const data = await getDoctorAppointments()
    
    
    appointments.value = data.map(item => {
      const patientGender = item.gender || item.patient?.gender || item.patient_details?.gender || "M";

      return {
        code: item.code || item.id || 'N/A',
        patientName: item.patient_name || item.patientName || item.patient?.full_name || "Anonyme",
        patientPhone: item.patient_phone || item.patientPhone || "N/A",
        gender: patientGender,
        email: item.patient_details?.email || "",
        bloodGroup: item.patient_details?.blood_group || "",
        dateOfBirth: item.patient_details?.date_of_birth || "",
        date: item.appointment_date ? new Date(item.appointment_date).toLocaleDateString('fr-FR', { 
          weekday: 'long', 
          year: 'numeric', 
          month: 'long', 
          day: 'numeric' 
        }) : "N/A",
        period: item.period || "N/A",
        status: item.status?.toLowerCase() || "scheduled",
      }
    })
  } catch (error) {
    console.error("Erreur API:", error)
  } finally {
    loading.value = false
  }
}

onMounted(fetchAppointments)

const filteredAppointments = computed(() => {
  return appointments.value.filter(app => {
    const query = searchQuery.value.toLowerCase().trim()
    
    const matchesStatus = statusFilter.value === "All" || app.status === statusFilter.value
    if (!matchesStatus) return false

    if (!query) return true

    return Object.values(app).some(value => 
      String(value).toLowerCase().includes(query)
    )
  })
})

// Pagination Logic
const totalPages = computed(() => {
  return Math.ceil(filteredAppointments.value.length / itemsPerPage.value) || 1
})

const startIndex = computed(() => (currentPage.value - 1) * itemsPerPage.value)
const endIndex = computed(() => startIndex.value + itemsPerPage.value)

const paginatedAppointments = computed(() => {
  return filteredAppointments.value.slice(startIndex.value, endIndex.value)
})

const nextPage = () => {
  if (currentPage.value < totalPages.value) currentPage.value++
}

const prevPage = () => {
  if (currentPage.value > 1) currentPage.value--
}

watch([searchQuery, statusFilter], () => {
  currentPage.value = 1
})

const getStatusCount = (status) => {
  return appointments.value.filter(app => app.status === status).length
}

const resetFilters = () => {
  searchQuery.value = ""
  statusFilter.value = "All"
  currentPage.value = 1
}

function openDetails(app) { 
  selectedAppointment.value = app 
}

function closeDetails() { 
  selectedAppointment.value = null 
}

async function handleStatusUpdate(code, newStatus) {
  try {
    await updateAppointmentStatus(code, newStatus)
  } catch (error) {
    alert("Erreur lors de la mise à jour du statut")
  }
}

function startConsultation(appointment) {
  if (appointment?.code) {
    router.push(`/consultations/create?appointment_code=${appointment.code}`)
  } else {
    alert('Erreur: Code de rendez-vous non trouvé')
  }
  closeDetails()
}

const isMale = (gender) => gender === "M" || gender === "Male" || gender === "homme"

function statusClasses(status) {
  const lightArrowColor = "%2371717a"
  
  switch (status?.toLowerCase()) {
    case 'completed': 
      return `bg-emerald-50/60 text-emerald-700 border-emerald-100/80 dark:bg-emerald-500/5 dark:text-emerald-400 dark:border-emerald-500/10 bg-[url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%23047857%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E')]`;
    case 'scheduled': 
      return `bg-teal-50/60 text-teal-700 border-teal-100/80 dark:bg-teal-500/5 dark:text-teal-400 dark:border-teal-500/10 bg-[url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%20%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%231d4ed8%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E')]`;
    case 'cancelled': 
      return `bg-rose-50/60 text-rose-700 border-rose-100/80 dark:bg-rose-500/5 dark:text-rose-400 dark:border-rose-500/10 bg-[url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%23be123c%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E')]`;
    default: 
      return `bg-gray-50 text-gray-700 border-gray-200 dark:bg-zinc-900 dark:text-zinc-400 dark:border-zinc-800 bg-[url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22${lightArrowColor}%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E')]`;
  }
}
</script>

<style scoped>
@keyframes spin { to { transform: rotate(360deg); } }
.animate-spin { animation: spin 1s linear infinite; }

.slide-enter-active, .slide-leave-active { 
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1); 
}
.slide-enter-from, .slide-leave-to { 
  transform: translateX(100%); 
}

.custom-scrollbar::-webkit-scrollbar { height: 5px; }
.custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
.custom-scrollbar::-webkit-scrollbar-thumb { background: #e4e4e7; border-radius: 10px; }
.dark .custom-scrollbar::-webkit-scrollbar-thumb { background: #27272a; }
</style>
