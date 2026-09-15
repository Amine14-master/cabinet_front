import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),

  scrollBehavior() {
    return { left: 0, top: 0 }
  },

  routes: [
    // ================= AUTH =================
    {
      path: '/signin',
      name: 'Signin',
      component: () => import('../modules/auth/pages/SigninPage.vue'),
      meta: { title: 'Signin', requiresAuth: false },
    },
    {
      path: '/signup',
      name: 'Signup',
      component: () => import('../modules/auth/pages/SignupPage.vue'),
      meta: { title: 'Signup', requiresAuth: false },
    },

    // ================= PUBLIC =================
    {
      path: '/',
      name: 'Landing',
      component: () => import('../views/LandingPage.vue'),
      meta: { title: 'Accueil', requiresAuth: false },
    },
    {
      path: '/:speciality/:cabinetCode',
      name: 'Platform',
      component: () => import('../views/LandingPage.vue'),
      meta: { title: 'Cabinet', requiresAuth: false },
    },

    // ================= DASHBOARD =================
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: () => import('../modules/dashboard/pages/Dashboard.vue'),
      meta: { title: 'Dashboard', requiresAuth: true },
    },

    // ================= CORE PAGES =================
    {
      path: '/working-days',
      name: 'Jours de travail',
      component: () => import('../modules/appointments/pages/DoctorWorkingDay.vue'),
      meta: { title: 'Calendar', requiresAuth: true },
    },
    {
      path: '/profile',
      name: 'Profile',
      component: () => import('../modules/profile/pages/UserProfile.vue'),
      meta: { title: 'Profile', requiresAuth: true },
    },

    {
      path: '/security',
      name: 'Security',
      component: () => import('../modules/profile/pages/UserSecurity.vue'),
      meta: { title: 'Security', requiresAuth: true },
    },
    {
      path: '/form-elements',
      name: 'FormElements',
      component: () => import('../views/Forms/FormElements.vue'),
      meta: { title: 'Form Elements', requiresAuth: true },
    },

    // ================= MODULES =================
    // Change your Patient routes to this:
    {
      path: "/patients",
      name: "PatientTable",
      component: () => import("../modules/patients/pages/PatientsPage.vue"),
      meta: {
        title: "List Patients",
        requiresAuth: true,
      },
    },
    {
      path: '/patients/add',
      name: 'AddPatient',
      component: () => import('@/modules/patients/pages/AddPatientPage.vue'),
      meta: { title: 'Ajouter un Patient', requiresAuth: true }
    },
    {
      path: "/patients/:code",
      name: "patient-details",
      component: () => import("@/modules/patients/pages/DetailsPatientPage.vue"),
    },
    {
      path: '/appointments',
      name: 'RendezVous',
      component: () => import('../modules/appointments/pages/RendezVous.vue'),
      meta: { title: 'Rendez-vous', requiresAuth: true },
    },
    {
      path: '/appointments/create',
      name: 'RendezVousAdd',
      component: () => import('../modules/appointments/pages/AddRendezVousPage.vue'),
      meta: { title: 'Ajouter un Rendez-vous', requiresAuth: true },
    },
    {
      path: '/queue/today',
      name: 'DailyQueue',
      component: () => import('../modules/appointments/pages/DailyQueue.vue'),
      meta: { title: 'File d\'Attente du Jour', requiresAuth: true },
    },
    {
      path: '/consultations',
      name: 'ConsultationsList',
      component: () => import('@/modules/consultations/pages/ConsultationPage.vue')
    },

    {
      path: '/consultations/create',
      name: 'ConsultationCreate',
      component: () => import('@/modules/consultations/pages/AddConsultationPage.vue')
    },
    {
      path: '/consultations/:id',
      name: 'ConsultationDetail',
      component: () => import('@/modules/consultations/components/ConsultationDetail.vue')
    },
    {
      path: '/ordonnances',
      name: 'OrdonanceList',
      component: () => import('@/modules/ordonnances/pages/OrdonnancesPage.vue')
    },


    {
      path: '/medicaments',
      name: 'MedicamentList',
      component: () => import('@/modules/medicaments/pages/MedicamentsPage.vue')
    },
    {
      path: '/medicaments/create',
      name: 'MedicamentCreate',
      component: () => import('@/modules/medicaments/pages/AddMedicamentsPage.vue')
    },
    // ================= TEAM =================


    {
      path: '/team',
      name: 'Team',
      component: () => import('@/modules/team/pages/TeamPage.vue')
    },


    // ================= UI =================




    // ================= ERROR =================
    {
      path: '/404',
      name: 'NotFound',
      component: () => import('../modules/errors/pages/NotFound.vue'),
      meta: { title: '404' },
    },

    // fallback
    {
      path: '/:pathMatch(.*)*',
      redirect: '/404',
    },
  ],
})

// ================= AUTH GUARD =================
router.beforeEach((to) => {
  const token = localStorage.getItem('access')
  const role = localStorage.getItem('role') || 'patient'
  const isAuthenticated = !!token

  document.title = to.meta.title
    ? `${to.meta.title} | Poura`
    : 'Poura'

  // not logged in → block protected pages
  if (to.meta.requiresAuth && !isAuthenticated) {
    return { name: 'Signin' }
  }

  // logged in → block auth pages and landing page
  if (isAuthenticated && (to.name === 'Signin' || to.name === 'Signup' || to.name === 'Landing')) {
    return { name: 'Dashboard' }
  }

  // Role-based route protection
  if (isAuthenticated) {
    const restrictedForStaff = ['/consultations', '/medicaments', '/ordonnances', '/team']
    const isRestrictedPath = restrictedForStaff.some(path => to.path.startsWith(path))
    
    if (['secretary', 'assistant'].includes(role) && isRestrictedPath) {
      return { path: '/appointments' }
    }
  }

  return true
})

export default router