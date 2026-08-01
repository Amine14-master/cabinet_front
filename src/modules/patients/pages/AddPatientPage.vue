<template>
  <AdminLayout>
    <PageBreadcrumb :pageTitle="currentPageTitle" />
    <div class="space-y-5 sm:space-y-6">

     <ComponentCard >
        <AddPatient />
      </ComponentCard>
    </div>

  </AdminLayout>
</template>

<script setup>
import { ref } from "vue";
import PageBreadcrumb from "@/layouts/common/PageBreadcrumb.vue";
import AdminLayout from "@/layouts/AdminLayout.vue";
import ComponentCard from "@/layouts/common/ComponentCard.vue";
import AddPatient from "../components/AddPatient.vue";
const currentPageTitle = ref("Ajouter Patient");

</script>
