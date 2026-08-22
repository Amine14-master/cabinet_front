<template>
  <AdminLayout>
    <!-- Conteneur Alignement Titre + Bouton -->
    <div class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between mb-5">
      <PageBreadcrumb :pageTitle="currentPageTitle" class="!mb-0" />
      
      <!-- Le bouton "Nouveau rendez-vous" placé au bon endroit -->
      <router-link 
        to="/appointments/create"
        class="inline-flex items-center justify-center gap-2 px-5 py-2.5 bg-brand-600 hover:bg-brand-700 text-white rounded-xl transition-all text-sm font-bold shadow-md shadow-brand-500/20 active:scale-[0.98] self-start sm:self-auto"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4" />
        </svg>
        Nouveau rendez-vous
      </router-link>
    </div>

    <div class="space-y-5 sm:space-y-6">
      <ComponentCard>
        <BasicTableOne />
      </ComponentCard>
    </div>
  </AdminLayout>
</template>

<script setup>
import { ref } from "vue";
import PageBreadcrumb from "@/layouts/common/PageBreadcrumb.vue";
import AdminLayout from "@/layouts/AdminLayout.vue";
import ComponentCard from "@/layouts/common/ComponentCard.vue"; // Corrigé le double slash //
import BasicTableOne from "../components/rendezVous.vue";
const currentPageTitle = ref("Rendez-vous");
</script>
