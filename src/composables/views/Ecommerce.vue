<template>
  <admin-layout>
    <doctor-dashboard />
  </admin-layout>
</template>

<script>
import AdminLayout from "../layouts/AdminLayout.vue"
import DoctorDashboard from '../components/ecommerce/DoctorDashboard.vue'

export default {
  name: 'DoctorPage',

  components: {
    AdminLayout,
    DoctorDashboard,
  },
}
</script>