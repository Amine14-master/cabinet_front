<template>
  <AdminLayout>
    <PageBreadcrumb :pageTitle="currentPageTitle" />
    <div class="space-y-5 sm:space-y-6">
      <ComponentCard title="Bar Chart 1"> <BarChartOne /> </ComponentCard>
    </div>
  </AdminLayout>
</template>

<script setup>
import BarChartOne from "@/components/charts/BarChart/BarChartOne.vue";
import ComponentCard from "@/layouts/common/ComponentCard.vue";
import PageBreadcrumb from "@/layouts/common/PageBreadcrumb.vue";
import AdminLayout from "@/layouts/AdminLayout.vue";
import { ref } from "vue";
const currentPageTitle = ref("Bar Chart");
</script>
