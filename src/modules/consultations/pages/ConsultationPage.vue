<template>
  <AdminLayout>
    <PageBreadcrumb :pageTitle="currentPageTitle" />
    <div class="space-y-5 sm:space-y-6">
      <ComponentCard>
        <AddConsultation />
      </ComponentCard>
    </div>
  </AdminLayout>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import PageBreadcrumb from "@/layouts/common/PageBreadcrumb.vue";
import AdminLayout from "@/layouts/AdminLayout.vue";
import ComponentCard from "@/layouts/common/ComponentCard.vue";
import AddConsultation from "../components/ConsultationsList.vue";

const route = useRoute();
const currentPageTitle = ref("Liste des Consultations");

// Log the appointment code from URL for debugging
onMounted(() => {
  console.log('Appointment code from URL:', route.query.appointment_code);
});
</script>