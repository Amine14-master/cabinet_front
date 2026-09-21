<template>
  <admin-layout>
    <div v-if="role === 'admin'" class="p-8">
      <h2 class="text-2xl font-bold mb-4">Admin Dashboard</h2>
      <!-- Simple admin stats representation since we just built the endpoint -->
      <div v-if="adminStats" class="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div class="bg-white p-6 rounded-2xl shadow">
          <h3 class="text-sm text-gray-500 uppercase">Doctors</h3>
          <p class="text-3xl font-black mt-2">{{ adminStats.total_doctors }}</p>
        </div>
        <div class="bg-white p-6 rounded-2xl shadow">
          <h3 class="text-sm text-gray-500 uppercase">Cabinets</h3>
          <p class="text-3xl font-black mt-2">{{ adminStats.total_cabinets }}</p>
        </div>
        <div class="bg-white p-6 rounded-2xl shadow">
          <h3 class="text-sm text-gray-500 uppercase">Patients</h3>
          <p class="text-3xl font-black mt-2">{{ adminStats.total_patients }}</p>
        </div>
        <div class="bg-white p-6 rounded-2xl shadow">
          <h3 class="text-sm text-gray-500 uppercase">Appointments</h3>
          <p class="text-3xl font-black mt-2">{{ adminStats.total_appointments }}</p>
        </div>
      </div>
    </div>
    <doctor-dashboard v-else />
  </admin-layout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import AdminLayout from '../../../layouts/AdminLayout.vue'
import DoctorDashboard from '../components/DoctorDashboard.vue'
import api from '@/api/axios'

const role = ref(localStorage.getItem('role') || 'doctor')
const adminStats = ref(null)

onMounted(async () => {
  if (role.value === 'admin') {
    try {
      const { data } = await api.get('doctors/dashboard/stats/')
      adminStats.value = data
    } catch (e) {
      console.error(e)
    }
  }
})
</script>
