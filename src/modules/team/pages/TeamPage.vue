<template>
  <admin-layout>
    <div class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between mb-6">
      <PageBreadcrumb :pageTitle="currentPageTitle" class="!mb-0" />

      <button 
          @click="openAddMemberModal"
        class="inline-flex items-center justify-center gap-2 px-4 py-2.5 bg-brand-500 hover:bg-brand-600 text-white rounded-xl transition-all text-sm font-medium shadow-sm active:scale-[0.98]"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4" />
        </svg>
        Ajouter un membre
      </button>
    </div>

    <div class="rounded-2xl border border-gray-200 bg-white p-5 dark:border-gray-800 dark:bg-white/[0.03] lg:p-6">
      <List ref="listRef" />
    </div>
  </admin-layout>
</template>

<script setup lang="ts">
import { ref } from "vue";

import { createStaff } from "@/api/staffService";

import AdminLayout from "../../../layouts/AdminLayout.vue";
import PageBreadcrumb from "@/layouts/common/PageBreadcrumb.vue";
import List from "../components/ListCard.vue";

const currentPageTitle = ref("Équipe du Cabinet");

const listRef = ref<any>(null);

const openAddMemberModal = () => {
  console.log("Button clicked");
  console.log(listRef.value);

  listRef.value?.openAddMemberModal();
};

const handleMemberCreated = async (data: any) => {
  try {
    await createStaff(data);

    listRef.value?.fetchStaff();
  } catch (error) {
    console.error(error);
  }
};
</script>