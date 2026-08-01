<template>
  <AdminLayout>
    <PageBreadcrumb :pageTitle="currentPageTitle" />
    <div className="space-y-5 sm:space-y-6">
      <ComponentCard title="Responsive Image">
        <ResponsiveImage />
      </ComponentCard>
      <ComponentCard title="Image in 2 Grid">
        <TwoColumnImageGrid />
      </ComponentCard>
      <ComponentCard title="Image in 3 Grid">
        <ThreeColumnImageGrid />
      </ComponentCard>
    </div>
  </AdminLayout>
</template>

<script setup>
import { ref } from 'vue'
import PageBreadcrumb from '@/layouts/common/PageBreadcrumb.vue'
import AdminLayout from '@/layouts/AdminLayout.vue'
import ComponentCard from '@/layouts/common/ComponentCard.vue'
import ResponsiveImage from '@/components/ui/images/ResponsiveImage.vue'
import TwoColumnImageGrid from '@/components/ui/images/TwoColumnImageGrid.vue'
import ThreeColumnImageGrid from '@/components/ui/images/ThreeColumnImageGrid.vue'
const currentPageTitle = ref('Images')
</script>

<style></style>
