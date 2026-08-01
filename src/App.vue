<template>
  <ThemeProvider>
    <SidebarProvider>
      <RouterView />
    </SidebarProvider>
  </ThemeProvider>
</template>

<script setup lang="ts">
import ThemeProvider from './layouts/ThemeProvider.vue'
import SidebarProvider from './layouts/SidebarProvider.vue'
</script>
