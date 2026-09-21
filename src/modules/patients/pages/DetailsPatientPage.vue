<template>
  <AdminLayout>
    <PageBreadcrumb :pageTitle="currentPageTitle" />
    <div class="space-y-5 sm:space-y-6">
      <ComponentCard>
        <DetailPatient />
      </ComponentCard>
    </div>
  </AdminLayout>
</template>

<script setup>
import { ref } from 'vue'
import PageBreadcrumb from '@/layouts/common/PageBreadcrumb.vue'
import AdminLayout from '@/layouts/AdminLayout.vue'
import ComponentCard from '@/layouts/common/ComponentCard.vue'
import DetailPatient from '../components/DetailPatient.vue'

const currentPageTitle = ref('Detail Patient ')

import { useRoute } from 'vue-router'

const route = useRoute()

const patientCode = route.params.code
</script>
