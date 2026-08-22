<template>
  <div class="min-h-screen bg-slate-50 dark:bg-zinc-950 flex transition-colors duration-200">
    <app-sidebar />
    <Backdrop />
    <div class="flex-1 flex flex-col min-w-0 min-h-screen">
      <app-header />
      <main class="flex-1 p-6 lg:p-8">
        <slot></slot>
      </main>
      <!-- Footer -->
      <footer class="p-6 pt-0 text-center">
        <p class="text-sm text-gray-400">
          Designed and Developed by 
          <span class="text-brand-500 font-medium">Poura</span>
        </p>
      </footer>
    </div>
  </div>
</template>

<script setup lang="ts">
import AppHeader from './AppHeader.vue'
import AppSidebar from './AppSidebar.vue'
import Backdrop from './Backdrop.vue'
</script>

