<template>
  <AdminLayout>
    <PageBreadcrumb :pageTitle="currentPageTitle" />
    <div class="space-y-5 sm:space-y-6">

     <ComponentCard >
        <AddRendezVous />
      </ComponentCard>
    </div>

  </AdminLayout>
</template>

<script setup>
import { ref } from "vue";
import PageBreadcrumb from "@/layouts/common/PageBreadcrumb.vue";
import AdminLayout from "@/layouts/AdminLayout.vue";
import ComponentCard from "@/layouts/common/ComponentCard.vue";
import AddRendezVous from "../components/AddRendezVous.vue";
const currentPageTitle = ref("Ajouter un nouveau rendez-vous");

</script>
