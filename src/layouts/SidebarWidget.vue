<template>
  <div
    class="mx-auto mb-10 w-full max-w-60 rounded-2xl bg-blue-50 px-4 py-6 text-center dark:bg-blue-500/10"
  >
    <!-- Une petite icône pour le côté visuel -->
    <div class="mb-3 flex justify-center">
      <div class="rounded-full bg-blue-100 p-2 dark:bg-blue-900/30">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-5 w-5 text-blue-600 dark:text-blue-400"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="Ref: M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
          />
        </svg>
      </div>
    </div>

    <h3 class="mb-2 text-sm font-semibold text-blue-900 dark:text-blue-400">Agenda du jour</h3>

    <p class="mb-0 text-xs leading-relaxed text-gray-600 dark:text-gray-400">
      Vous avez
      <span class="font-bold text-blue-700 dark:text-blue-300">12 consultations</span> prévues
      aujourd'hui.
    </p>

    <div class="mt-4 border-t border-blue-100 pt-4 dark:border-blue-800">
      <p class="text-xs font-medium text-gray-500 dark:text-gray-500 uppercase tracking-wider">
        Prochain patient
      </p>
      <p class="text-lg font-bold text-blue-600 dark:text-blue-400">09:30</p>
    </div>
  </div>
</template>
