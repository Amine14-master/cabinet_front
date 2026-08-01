<template >
  <admin-layout>
    <PageBreadcrumb :pageTitle="currentPageTitle" />

    <div
      class="rounded-2xl border border-gray-200 bg-white p-5 dark:border-gray-800 dark:bg-white/[0.03] lg:p-6"
    >

       <div v-if="doctor">
      <security-info-card :doctor="doctor" />
    </div>
    </div>
  </admin-layout>
</template>

<script setup>
import AdminLayout from '../../../layouts/AdminLayout.vue'
import PageBreadcrumb from '@/layouts/common/PageBreadcrumb.vue'
import { ref,onMounted } from 'vue'
import { getDoctorProfile } from '@/api/doctorService'
import SecurityInfoCard from '../components/SecurityInfoCard.vue'
const currentPageTitle = ref(' Sécurity du compte ')
const doctor = ref(null)

const fetchDoctor = async () => {
  const data = await getDoctorProfile()


  doctor.value = data
}

onMounted(fetchDoctor)
</script>
