<template>
  <div class="space-y-4">
    <!-- Header/Toolbar: Search & Filter -->
    <div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between mb-6">
      <div class="relative flex-1 max-w-md">
        <span class="absolute inset-y-0 left-0 flex items-center pl-3.5 text-gray-400 pointer-events-none">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
        </span>
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Rechercher par nom, UID, téléphone, groupe..."
          class="w-full rounded-lg border border-gray-200/80 bg-white py-2 pl-10 pr-4 text-sm text-gray-900 outline-none focus:border-teal-500 focus:ring-1 focus:ring-teal-500/20 dark:border-gray-800 dark:bg-zinc-900 dark:text-white transition-all placeholder:text-gray-400"
        />
      </div>

      <div class="flex items-center gap-2">
        <select 
          v-model="statusFilter"
          class="rounded-lg border border-gray-200/80 bg-white px-3 py-2 text-sm font-medium text-gray-600 outline-none focus:border-teal-500 dark:border-gray-800 dark:bg-zinc-900 dark:text-gray-300 cursor-pointer transition-all appearance-none pr-8 relative bg-[url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%2371717a%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E')] bg-[length:0.65rem_auto] bg-[right_0.75rem_center] bg-no-repeat"
        >
          <option value="All">Tous les statuts</option>
          <option value="Stable">Stable</option>
          <option value="Urgent">Urgent</option>
          <option value="Pending">En attente</option>
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
              <th class="w-1/4 px-6 py-3.5 text-left text-xs font-semibold tracking-wider text-gray-400 uppercase">Dernière visite</th>
              <th class="w-1/5 px-6 py-3.5 text-left text-xs font-semibold tracking-wider text-gray-400 uppercase">Signes Vitaux</th>
              <th class="w-1/6 px-6 py-3.5 text-left text-xs font-semibold tracking-wider text-gray-400 uppercase">Statut</th>
              <th class="w-1/6 px-6 py-3.5 text-center text-xs font-semibold tracking-wider text-gray-400 uppercase">Action</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-100 dark:divide-gray-800/60">
            <!-- Loading State -->
            <tr v-if="isLoading">
              <td colspan="5" class="px-6 py-12 text-center">
                <div class="flex flex-col items-center justify-center gap-3">
                  <div class="h-6 w-6 animate-spin rounded-full border-2 border-solid border-teal-600 border-r-transparent"></div>
                  <p class="text-xs text-gray-400">Chargement des données...</p>
                </div>
              </td>
            </tr>

            <!-- Empty State -->
            <tr v-else-if="paginatedPatients.length === 0">
              <td colspan="5" class="px-6 py-16 text-center">
                <div class="flex flex-col items-center justify-center max-w-xs mx-auto">
                  <div class="p-3 bg-gray-50 dark:bg-zinc-900 rounded-xl text-gray-400 mb-3">
                    <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                    </svg>
                  </div>
                  <p class="text-sm font-medium text-gray-700 dark:text-zinc-300">Aucun patient trouvé</p>
                  <p class="text-xs text-gray-400 mt-0.5">Aucun dossier ne correspond à vos filtres actuels.</p>
                </div>
              </td>
            </tr>

            <!-- Table Rows -->
            <tr
              v-for="patient in paginatedPatients"
              :key="patient.id"
              class="hover:bg-gray-50/50 dark:hover:bg-zinc-900/10 transition-colors group"
            >
              <td class="px-6 py-3.5 whitespace-nowrap">
                <div class="flex items-center gap-3">
                  <div :class="[
                    'w-10 h-10 rounded-full flex items-center justify-center shadow-inner transition-transform group-hover:scale-[1.02]',
                    isMale(patient.gender) ? 'bg-teal-100 text-teal-600 dark:bg-teal-500/20' : 'bg-pink-100 text-pink-600 dark:bg-pink-500/20'
                  ]">
                    <svg v-if="isMale(patient.gender)" xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                    </svg>
                    <svg v-else xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                      <circle cx="12" cy="10" r="3" fill="currentColor" opacity="0.3"/>
                    </svg>
                  </div>
                  <div class="truncate">
                    <span class="block text-sm font-medium text-gray-800 dark:text-zinc-200 truncate">{{ patient.name }}</span>
                    <span class="block text-xs text-gray-400 font-mono tracking-tight mt-0.5">UID: {{ patient.id }}</span>
                  </div>
                </div>
              </td>

              <td class="px-6 py-3.5 whitespace-nowrap">
                <p class="text-xs font-medium text-gray-700 dark:text-zinc-300 truncate">{{ patient.lastVisitFormatted }}</p>
                <p class="text-[11px] text-gray-400 mt-0.5">Rejoint: {{ patient.dateJoined }}</p>
              </td>

              <td class="px-6 py-3.5 whitespace-nowrap">
                <div class="flex items-center gap-2.5 text-xs">
                  <div>
                    <span class="text-gray-400 font-medium mr-1">BP</span>
                    <span class="font-mono bg-gray-50 dark:bg-zinc-900 border border-gray-100 dark:border-zinc-800 px-1.5 py-0.5 rounded text-gray-700 dark:text-zinc-300">{{ patient.vitals.bp }}</span>
                  </div>
                  <div class="w-px h-3 bg-gray-200 dark:bg-zinc-800"></div>
                  <div>
                    <span class="text-gray-400 font-medium mr-1">HR</span>
                    <span class="font-mono bg-gray-50 dark:bg-zinc-900 border border-gray-100 dark:border-zinc-800 px-1.5 py-0.5 rounded text-gray-700 dark:text-zinc-300">{{ patient.vitals.hr }}</span>
                  </div>
                </div>
              </td>

              <td class="px-6 py-3.5 whitespace-nowrap">
                <span :class="['inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md text-[11px] font-bold border tracking-wider', statusClasses(patient.status)]">
                  <span :class="['w-1.5 h-1.5 rounded-full', statusDot(patient.status)]"></span>
                  {{ patient.status }}
                </span>
              </td>

              <td class="px-6 py-3.5 whitespace-nowrap text-center">
                <button 
                  @click.stop="openDetails(patient)" 
                  class="p-1.5 rounded-md text-gray-400 hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-zinc-900 transition-colors active:scale-95"
                  title="Voir Dossier"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                    <path stroke-linecap="round" stroke-linejoin="round" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                  </svg>
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Compact Pagination Bar -->
      <div v-if="filteredPatients.length > 0" class="flex items-center justify-between px-6 py-4 border-t border-gray-100 dark:border-gray-800/80 bg-gray-50/20 dark:bg-zinc-900/5">
        <div class="text-xs text-gray-400">
          Affichage de <span class="font-medium text-gray-700 dark:text-zinc-300">{{ startIndex + 1 }}</span> à 
          <span class="font-medium text-gray-700 dark:text-zinc-300">{{ Math.min(endIndex, filteredPatients.length) }}</span> sur 
          <span class="font-medium text-gray-700 dark:text-zinc-300">{{ filteredPatients.length }}</span> résultats
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

    <!-- Premium Slide Drawer: Patient Details -->
    <Teleport to="body">
      <Transition name="slide">
        <div v-if="selectedPatient" class="fixed inset-0 z-50 overflow-hidden">
          <div class="absolute inset-0 bg-slate-900/40 backdrop-blur-sm transition-opacity" @click="closeDetails"></div>
          <div class="absolute inset-y-0 right-0 max-w-sm w-full bg-white dark:bg-zinc-950 border-l border-gray-100 dark:border-zinc-900 shadow-xl flex flex-col">
          <!-- Drawer Header -->
          <div class="p-5 border-b border-gray-100 dark:border-zinc-900 flex justify-between items-center">
            <div>
              <h2 class="text-base font-semibold text-gray-900 dark:text-white">Dossier Patient</h2>
              <p class="text-xs font-mono text-gray-400 mt-0.5">ID: {{ selectedPatient.id }}</p>
            </div>
            <button @click="closeDetails" class="p-1.5 rounded-lg text-gray-400 hover:bg-gray-50 dark:hover:bg-zinc-900 transition-colors">
              <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
          
          <!-- Drawer Content -->
          <div class="flex-1 overflow-y-auto bg-gray-50/30 dark:bg-zinc-950/30 custom-scrollbar">
            <div class="p-5 space-y-6">
              <!-- Profile Info: Drawer Avatar (♂ / ♀) -->
              <div class="flex flex-col items-center text-center p-4 rounded-xl bg-white dark:bg-zinc-900 border border-gray-100 dark:border-zinc-800 shadow-sm">
                <div :class="[
                  'w-16 h-16 rounded-2xl flex items-center justify-center text-2xl font-semibold mb-3 border shadow-sm',
                  isMale(selectedPatient.gender) ? 'bg-gradient-to-br from-teal-50 to-teal-100 text-teal-600 border-teal-200' : 'bg-gradient-to-br from-rose-50 to-rose-100 text-rose-600 border-rose-200'
                ]">
                  {{ isMale(selectedPatient.gender) ? '♂' : '♀' }}
                </div>
                <h3 class="text-lg font-bold text-gray-900 dark:text-white">{{ selectedPatient.name }}</h3>
                <p class="text-xs text-gray-500 font-mono mt-1">{{ selectedPatient.phone || '—' }}</p>
                <div class="flex gap-2 mt-4">
                  <div class="px-3 py-1.5 rounded-lg bg-gray-50 dark:bg-zinc-800 border border-gray-100 dark:border-zinc-700">
                    <p class="text-[10px] uppercase font-bold text-gray-400 mb-0.5">Sexe</p>
                    <p class="text-xs font-semibold dark:text-white">{{ isMale(selectedPatient.gender) ? 'Homme' : 'Femme' }}</p>
                  </div>
                  <div class="px-3 py-1.5 rounded-lg bg-gray-50 dark:bg-zinc-800 border border-gray-100 dark:border-zinc-700">
                    <p class="text-[10px] uppercase font-bold text-gray-400 mb-0.5">Groupe</p>
                    <p class="text-xs font-bold text-rose-600 dark:text-rose-400">{{ selectedPatient.bloodType || '—' }}</p>
                  </div>
                  <div class="px-3 py-1.5 rounded-lg bg-gray-50 dark:bg-zinc-800 border border-gray-100 dark:border-zinc-700">
                    <p class="text-[10px] uppercase font-bold text-gray-400 mb-0.5">Âge</p>
                    <p class="text-xs font-semibold dark:text-white">{{ calculateAge(selectedPatient.dob) }} ans</p>
                  </div>
                </div>
              </div>

              <!-- Mobile App Claim Code Banner -->
              <div v-if="selectedPatient && !selectedPatient.is_claimed" class="bg-teal-50 dark:bg-teal-500/10 border border-teal-100 dark:border-teal-500/20 rounded-xl p-4 flex flex-col items-center text-center shadow-sm">
                <p class="text-xs font-bold text-teal-600 dark:text-teal-400 uppercase tracking-wider mb-1">Code Application Mobile</p>
                <p class="text-xs text-gray-500 dark:text-zinc-400 mb-3">Le patient doit saisir ce code lors de son inscription sur l'application mobile.</p>
                <div class="flex items-center gap-2">
                  <span class="text-xl font-black font-mono tracking-widest text-gray-900 dark:text-white px-4 py-1.5 bg-white dark:bg-zinc-900 border border-gray-200 dark:border-zinc-700 rounded-lg shadow-sm">
                    {{ selectedPatient.id }}
                  </span>
                </div>
              </div>
              <div v-else-if="selectedPatient && selectedPatient.is_claimed" class="bg-emerald-50 dark:bg-emerald-500/10 border border-emerald-100 dark:border-emerald-500/20 rounded-xl p-3 flex items-center justify-center gap-2 shadow-sm">
                <svg class="w-5 h-5 text-emerald-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                <span class="text-sm font-bold text-emerald-700 dark:text-emerald-400">Application Mobile Connectée</span>
              </div>

              <!-- Pro Tabs -->
              <div class="border-b border-gray-200 dark:border-zinc-800">
                <nav class="-mb-px flex gap-4" aria-label="Tabs">
                  <button v-if="!['secretary', 'assistant'].includes(role)" @click="activeTab = 'dossier'" :class="['whitespace-nowrap py-3 px-1 border-b-2 font-medium text-xs transition-colors', activeTab === 'dossier' ? 'border-rose-500 text-rose-600 dark:text-rose-400' : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300 dark:text-zinc-400 dark:hover:text-zinc-300']">
                    Dossier Médical
                  </button>
                  <button @click="activeTab = 'appointments'" :class="['whitespace-nowrap py-3 px-1 border-b-2 font-medium text-xs transition-colors', activeTab === 'appointments' ? 'border-teal-500 text-teal-600 dark:text-teal-400' : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300 dark:text-zinc-400 dark:hover:text-zinc-300']">
                    Rendez-vous ({{ patientHistory.appointments.length }})
                  </button>
                  <button v-if="!['secretary', 'assistant'].includes(role)" @click="activeTab = 'consultations'" :class="['whitespace-nowrap py-3 px-1 border-b-2 font-medium text-xs transition-colors', activeTab === 'consultations' ? 'border-emerald-500 text-emerald-600 dark:text-emerald-400' : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300 dark:text-zinc-400 dark:hover:text-zinc-300']">
                    Consultations ({{ patientHistory.consultations.length }})
                  </button>
                  <button v-if="!['secretary', 'assistant'].includes(role)" @click="activeTab = 'ordonnances'" :class="['whitespace-nowrap py-3 px-1 border-b-2 font-medium text-xs transition-colors', activeTab === 'ordonnances' ? 'border-purple-500 text-purple-600 dark:text-purple-400' : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300 dark:text-zinc-400 dark:hover:text-zinc-300']">
                    Ordonnances ({{ patientHistory.ordonnances.length }})
                  </button>
                </nav>
              </div>

              <!-- Loader -->
              <div v-if="loadingHistory" class="flex justify-center py-8">
                <div class="h-6 w-6 animate-spin rounded-full border-2 border-solid border-teal-600 border-r-transparent"></div>
              </div>

              <!-- Tab Contents -->
              <div v-else class="space-y-3 pb-6">
                
                <!-- Dossier Médical -->
                <div v-if="activeTab === 'dossier'" class="space-y-4">
                  <div class="p-4 bg-rose-50/50 dark:bg-rose-900/10 border border-rose-100 dark:border-rose-900/30 rounded-xl shadow-sm">
                    <h4 class="text-xs font-bold text-rose-500 uppercase tracking-wider flex items-center gap-2 mb-2">
                      <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                      </svg>
                      Allergies
                    </h4>
                    <p class="text-sm font-medium text-gray-900 dark:text-white whitespace-pre-line">{{ selectedPatient.allergies || 'Aucune allergie connue.' }}</p>
                  </div>
                  
                  <div class="p-4 bg-white dark:bg-zinc-900 border border-gray-100 dark:border-zinc-800 rounded-xl shadow-sm">
                    <h4 class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-2">Maladies Chroniques</h4>
                    <p class="text-sm font-medium text-gray-900 dark:text-white whitespace-pre-line">{{ selectedPatient.chronic_diseases || 'Non renseigné.' }}</p>
                  </div>
                  
                  <div class="p-4 bg-white dark:bg-zinc-900 border border-gray-100 dark:border-zinc-800 rounded-xl shadow-sm">
                    <h4 class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-2">Antécédents Chirurgicaux</h4>
                    <p class="text-sm font-medium text-gray-900 dark:text-white whitespace-pre-line">{{ selectedPatient.surgical_history || 'Non renseigné.' }}</p>
                  </div>
                  
                  <div class="p-4 bg-white dark:bg-zinc-900 border border-gray-100 dark:border-zinc-800 rounded-xl shadow-sm">
                    <h4 class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-2">Antécédents Familiaux</h4>
                    <p class="text-sm font-medium text-gray-900 dark:text-white whitespace-pre-line">{{ selectedPatient.family_history || 'Non renseigné.' }}</p>
                  </div>
                </div>

                <!-- Appointments -->
                <div v-if="activeTab === 'appointments'" class="space-y-3">
                  <div v-if="patientHistory.appointments.length === 0" class="text-center py-6 text-gray-400 text-xs">Aucun rendez-vous</div>
                  <div v-for="app in patientHistory.appointments" :key="app.code" class="p-3 bg-white dark:bg-zinc-900 border border-gray-100 dark:border-zinc-800 rounded-xl shadow-sm flex items-center justify-between group hover:border-teal-200 transition-colors">
                    <div>
                      <p class="text-sm font-semibold text-gray-900 dark:text-white">{{ app.appointment_date }}</p>
                      <p class="text-xs text-gray-500">{{ app.period === 'morning' ? 'Matin' : 'Après-midi' }}</p>
                    </div>
                    <div class="flex flex-col items-end gap-1.5">
                      <span :class="[
                        'text-[10px] font-bold px-2 py-1 rounded-md uppercase tracking-wider text-right',
                        app.status === 'scheduled' ? 'bg-amber-50 text-amber-600' : app.status === 'completed' ? 'bg-emerald-50 text-emerald-600' : 'bg-rose-50 text-rose-600'
                      ]">{{ app.status === 'scheduled' ? 'Programmé' : app.status === 'completed' ? 'Terminé (Présent)' : 'Annulé (Absent)' }}</span>
                      <button 
                        v-if="app.has_consultation && !['secretary', 'assistant'].includes(role)" 
                        @click.stop="openConsultationFromAppointment(app.consultation_id)"
                        class="text-[9px] text-emerald-600 bg-emerald-50 hover:bg-emerald-100 border border-emerald-100 px-1.5 py-0.5 rounded font-bold cursor-pointer transition-colors text-right flex items-center justify-end gap-1 w-full"
                      >
                        <span>✓ Consultation</span>
                        <svg xmlns="http://www.w3.org/2000/svg" class="w-2.5 h-2.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M9 5l7 7-7 7" />
                        </svg>
                      </button>
                      <span v-else-if="app.status === 'completed'" class="text-[9px] text-gray-500 bg-gray-50 border border-gray-200 px-1.5 py-0.5 rounded font-bold flex justify-end w-full">Pas de consultation</span>
                    </div>
                  </div>
                </div>

                <!-- Consultations -->
                <div v-if="activeTab === 'consultations'" class="space-y-3">
                  <div v-if="patientHistory.consultations.length === 0" class="text-center py-6 text-gray-400 text-xs">Aucune consultation</div>
                  <div v-for="cons in patientHistory.consultations" :key="cons.id" 
                       @click="toggleConsultation(cons.id)"
                       class="p-4 bg-white dark:bg-zinc-900 border border-gray-100 dark:border-zinc-800 rounded-xl shadow-sm hover:border-emerald-200 transition-colors cursor-pointer group">
                    <div class="flex justify-between items-center mb-1">
                      <p class="text-sm font-semibold text-gray-900 dark:text-white flex items-center gap-2">
                        📅 {{ new Date(cons.created_at).toLocaleDateString('fr-FR') }}
                      </p>
                      <svg :class="['w-4 h-4 text-gray-400 transition-transform duration-200', expandedConsultation === cons.id ? 'rotate-180' : '']" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                      </svg>
                    </div>
                    
                    <!-- Preview when collapsed -->
                    <div v-if="expandedConsultation !== cons.id" class="mt-2 flex items-center justify-between">
                      <p class="text-xs text-gray-500 line-clamp-1 flex-1 pr-4">
                        {{ cons.diagnosis || cons.symptoms || 'Dossier de consultation' }}
                      </p>
                      <span class="text-[10px] font-medium text-teal-600 bg-teal-50 dark:bg-teal-500/10 dark:text-teal-400 px-2 py-1 rounded-md opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap">
                        Afficher les détails
                      </span>
                    </div>

                    <!-- Expanded Details -->
                    <div v-if="expandedConsultation === cons.id" class="mt-4 space-y-4 border-t border-gray-100 dark:border-zinc-800 pt-4">
                      <div v-if="cons.symptoms">
                        <span class="text-[10px] text-gray-400 uppercase font-bold">Symptômes</span>
                        <p class="text-xs text-gray-700 dark:text-gray-300 mt-0.5">{{ cons.symptoms }}</p>
                      </div>
                      <div v-if="cons.diagnosis">
                        <span class="text-[10px] text-gray-400 uppercase font-bold">Diagnostic</span>
                        <p class="text-xs text-emerald-700 dark:text-emerald-400 mt-0.5 font-medium">{{ cons.diagnosis }}</p>
                      </div>
                      <div v-if="cons.prescription">
                        <span class="text-[10px] text-gray-400 uppercase font-bold">Prescription (Texte)</span>
                        <p class="text-xs text-gray-700 dark:text-gray-300 mt-0.5 whitespace-pre-wrap">{{ cons.prescription }}</p>
                      </div>
                      <div v-if="cons.notes">
                        <span class="text-[10px] text-gray-400 uppercase font-bold">Notes internes</span>
                        <p class="text-xs text-gray-500 italic mt-0.5 whitespace-pre-wrap">{{ cons.notes }}</p>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Ordonnances -->
                <div v-if="activeTab === 'ordonnances'" class="space-y-3">
                  <div v-if="patientHistory.ordonnances.length === 0" class="text-center py-6 text-gray-400 text-xs">Aucune ordonnance</div>
                  <div v-for="ord in patientHistory.ordonnances" :key="ord.code" class="p-3 bg-white dark:bg-zinc-900 border border-gray-100 dark:border-zinc-800 rounded-xl shadow-sm hover:border-purple-200 transition-colors flex items-center justify-between">
                    <div>
                      <p class="text-sm font-semibold text-gray-900 dark:text-white">Ordonnance</p>
                      <p class="text-xs text-gray-500 font-mono mt-0.5">{{ ord.code }}</p>
                    </div>
                    <a v-if="ord.pdf_file" :href="getPdfUrl(ord.pdf_file)" target="_blank" class="p-2 bg-purple-50 hover:bg-purple-100 dark:bg-purple-500/10 dark:hover:bg-purple-500/20 text-purple-600 rounded-lg transition-colors cursor-pointer" title="Voir l'ordonnance">
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                      </svg>
                    </a>
                  </div>
                </div>

              </div>
            </div>
          </div>

          <!-- Bottom Actions -->
          <div class="p-5 border-t border-gray-100 dark:border-zinc-900 flex gap-3">
            <button
              @click="handleCreateFollowUp"
              class="flex-1 bg-white hover:bg-gray-50 text-gray-700 border border-gray-200 dark:bg-zinc-900 dark:border-zinc-700 dark:text-zinc-300 dark:hover:bg-zinc-800 font-bold py-2.5 rounded-xl text-sm transition-all active:scale-[0.98] shadow-sm flex items-center justify-center gap-1.5"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
              </svg>
              Planifier RV
            </button>
            <button
              @click="handleImmediateConsultation"
              class="flex-1 bg-brand-600 hover:bg-brand-700 text-white font-bold py-2.5 rounded-xl text-sm transition-all active:scale-[0.98] shadow-md shadow-brand-500/20 flex items-center justify-center gap-1.5"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4" />
              </svg>
              Consulter
            </button>
          </div>
        </div>
      </div>
    </Transition>
    </Teleport>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from "vue"
import { useRouter } from "vue-router"
import { getDoctorPatients, getDoctorPatientProfile } from "@/api/patientsService"

const router = useRouter()
const role = localStorage.getItem('role') || 'doctor'
const searchQuery = ref("")
const statusFilter = ref("All")
const showDetails = ref(false)
const selectedPatient = ref(null)
const activeTab = ref('dossier')
const loadingHistory = ref(false)

const patients = ref([])
const isLoading = ref(true)

// Local Client-side Pagination State
const currentPage = ref(1)
const itemsPerPage = ref(8)

const page = ref(1)
const pageSize = ref(100)
const total = ref(0)

const fetchPatients = async () => {
  try {
    isLoading.value = true
    const res = await getDoctorPatients({
      page: page.value,
      page_size: pageSize.value
    })

    const rows = res.results || []
    total.value = res.count || 0

    patients.value = rows.map((item) => ({
      id: item.patient_details?.code || "-",
      name: item.patient_details?.full_name || "-",
      email: item.patient_details?.email || "-",
      phone: item.patient_details?.phone || "-",
      gender: item.patient_details?.gender || "",
      is_claimed: item.patient_details?.is_claimed || false,
      lastVisitFormatted: item.last_consultation
        ? new Date(item.last_consultation).toLocaleDateString("fr-FR")
        : "Pas de visite",
      dateJoined: item.added_at
        ? new Date(item.added_at).toLocaleDateString("fr-FR")
        : "-",
      status: "Stable",
      bloodType: item.patient_details?.blood_group || "-",
      dob: item.patient_details?.date_of_birth || null,
      allergies: item.patient_details?.allergies || "",
      chronic_diseases: item.patient_details?.chronic_diseases || "",
      surgical_history: item.patient_details?.surgical_history || "",
      family_history: item.patient_details?.family_history || "",
      vitals: {
        bp: "12/8",
        hr: "72"
      }
    }))
  } catch (error) {
    console.error(error)
    patients.value = []
  } finally {
    isLoading.value = false
  }
}

onMounted(fetchPatients)

const filteredPatients = computed(() => {
  return patients.value.filter((p) => {
    const q = searchQuery.value.toLowerCase().trim()
    const matchesStatus = statusFilter.value === "All" || p.status === statusFilter.value
    
    if (!matchesStatus) return false
    if (!q) return true

    return (
      p.name.toLowerCase().includes(q) ||
      p.id.toLowerCase().includes(q) ||
      p.phone.toLowerCase().includes(q) ||
      p.bloodType.toLowerCase().includes(q)
    )
  })
})

const totalPages = computed(() => {
  return Math.ceil(filteredPatients.value.length / itemsPerPage.value) || 1
})

const startIndex = computed(() => (currentPage.value - 1) * itemsPerPage.value)
const endIndex = computed(() => startIndex.value + itemsPerPage.value)

const paginatedPatients = computed(() => {
  return filteredPatients.value.slice(startIndex.value, endIndex.value)
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

const isMale = (gender) => gender === "M" || gender === "Male"

const expandedConsultation = ref(null)
const patientHistory = ref({
  appointments: [],
  consultations: [],
  ordonnances: []
})

const toggleConsultation = (id) => {
  expandedConsultation.value = expandedConsultation.value === id ? null : id
}

const openConsultationFromAppointment = (consultationId) => {
  if (!consultationId) return;
  activeTab.value = 'consultations';
  expandedConsultation.value = consultationId;
}

const openDetails = async (patient) => { 
  selectedPatient.value = patient 
  loadingHistory.value = true
  activeTab.value = 'appointments'
  
  try {
    const data = await getDoctorPatientProfile(patient.id)
    patientHistory.value = {
      appointments: data.appointments || [],
      consultations: data.consultations || [],
      ordonnances: data.ordonnances || []
    }
  } catch (error) {
    console.error("Erreur récupération historique:", error)
    patientHistory.value = { appointments: [], consultations: [], ordonnances: [] }
  } finally {
    loadingHistory.value = false
  }
}

const closeDetails = () => { 
  selectedPatient.value = null 
  expandedConsultation.value = null
  patientHistory.value = { appointments: [], consultations: [], ordonnances: [] }
}

const getPdfUrl = (url) => {
  if (!url) return "#";
  if (url.startsWith("http")) return url;
  return `http://127.0.0.1:8000${url}`;
}

const statusClasses = (status) => {
  switch (status) {
    case 'Stable': 
      return 'bg-emerald-50/60 text-emerald-700 border-emerald-100 dark:bg-emerald-500/5 dark:text-emerald-400 dark:border-emerald-500/10'
    case 'Pending': 
      return 'bg-amber-50/50 text-amber-700 border-amber-100 dark:bg-amber-500/5 dark:text-amber-400 dark:border-amber-500/10'
    case 'Urgent': 
      return 'bg-rose-50/60 text-rose-700 border-rose-100 dark:bg-rose-500/5 dark:text-rose-400 dark:border-rose-500/10'
    default: 
      return 'bg-gray-50 text-gray-700 border-gray-200 dark:bg-zinc-900 dark:text-zinc-400 dark:border-zinc-800'
  }
}

const statusDot = (status) => {
  switch (status) {
    case 'Stable': return 'bg-emerald-500'
    case 'Pending': return 'bg-amber-500'
    case 'Urgent': return 'bg-rose-500'
    default: return 'bg-gray-400'
  }
}

function calculateAge(dob) {
  if (!dob) return "—"
  const birthDate = new Date(dob)
  const diff = Date.now() - birthDate.getTime()
  const ageDate = new Date(diff)
  return Math.abs(ageDate.getUTCFullYear() - 1970)
}

const resetFilters = () => {
  searchQuery.value = ""
  statusFilter.value = "All"
  currentPage.value = 1
}

const handleCreateFollowUp = () => {
  if (!selectedPatient.value) return
  router.push({
    path: "/appointments/create",
    query: { patient_code: selectedPatient.value.id },
  })
  closeDetails()
}

const handleImmediateConsultation = () => {
  if (!selectedPatient.value) return
  router.push({
    path: "/consultations/create",
    query: { patient: selectedPatient.value.id },
  })
  closeDetails()
}

const goToPatient = () => {
  if (!selectedPatient.value) return
  router.push({
    name: "patient-details",
    params: { code: selectedPatient.value.id }
  })
  closeDetails()
}
</script>

<script>
export default { name: "PatientTable" }
</script>

<style scoped>
.slide-enter-active, .slide-leave-active { 
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1); 
}
.slide-enter-from, .slide-leave-to { 
  transform: translateX(100%); 
}

.custom-scrollbar::-webkit-scrollbar {
  height: 5px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: transparent;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background: #e4e4e7;
  border-radius: 10px;
}
.dark .custom-scrollbar::-webkit-scrollbar-thumb {
  background: #27272a;
}
</style>
