<template>
  <admin-layout>
    <PageBreadcrumb :pageTitle="currentPageTitle" />

    <div
      class="rounded-2xl border border-gray-200 bg-white p-5 dark:border-gray-800 dark:bg-white/[0.03] lg:p-6"
    >
      <div v-if="doctor">
        <profile-card :doctor="doctor" />
        <personal-info-card :doctor="doctor" />
        <consultation-card :doctor="doctor" />
        <cabinet-card :doctor="doctor" />
      </div>
    </div>
  </admin-layout>
</template>

<script setup>
import AdminLayout from '../../../layouts/AdminLayout.vue'
import PageBreadcrumb from '@/layouts/common/PageBreadcrumb.vue'
import { ref, onMounted } from 'vue'
import { getDoctorProfile } from '@/api/doctorService'
import ProfileCard from '../components/ProfileCard.vue'
import PersonalInfoCard from '../components/PersonalInfoCard.vue'
import ConsultationCard from '../components/ConsultationCard.vue'
import CabinetCard from '../components/CabinetCard.vue'
const currentPageTitle = ref('Profile de Médecin ')
const doctor = ref(null)

const fetchDoctor = async () => {
  const data = await getDoctorProfile()

  doctor.value = data
}

onMounted(fetchDoctor)
</script>
