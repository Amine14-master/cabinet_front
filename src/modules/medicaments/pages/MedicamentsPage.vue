<template>
  <AdminLayout>
    <div class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between mb-6">
      <PageBreadcrumb :pageTitle="currentPageTitle" class="!mb-0" />

      <button
        @click="medicamentsListRef?.openCustomMedicamentModal"
        class="inline-flex items-center justify-center gap-2 px-4 py-2.5 bg-blue-600 hover:bg-blue-700 text-white rounded-xl transition-all text-sm font-medium shadow-sm hover:shadow shadow-blue-500/10 active:scale-[0.98] self-start sm:self-auto"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="w-4 h-4"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          stroke-width="2"
        >
          <path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4" />
        </svg>
        Nouveau Médicament
      </button>
    </div>

    <div class="space-y-5 sm:space-y-6">
      <ComponentCard>
        <MedicamentsList ref="medicamentsListRef" />
      </ComponentCard>
    </div>
  </AdminLayout>
</template>

<script setup>
import { ref } from 'vue'
import PageBreadcrumb from '@/layouts/common/PageBreadcrumb.vue'
import AdminLayout from '@/layouts/AdminLayout.vue'
import ComponentCard from '@/layouts/common/ComponentCard.vue'
import MedicamentsList from '../components/MedicamentsList.vue'

const currentPageTitle = ref('Liste des médicaments')
const medicamentsListRef = ref(null)
</script>
