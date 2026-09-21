<template>
  <aside
    class="flex h-screen w-64 flex-col bg-white border-r border-slate-200/80 shrink-0 sticky top-0 transition-all z-30"
  >
    <!-- Header -->
    <div class="flex h-20 items-center px-6 shrink-0 mb-4 pt-4">
      <router-link to="/dashboard" class="flex items-center gap-3 w-full">
        <div
          class="w-10 h-10 bg-gradient-to-br from-brand-400 to-brand-600 rounded-2xl flex items-center justify-center shadow-lg shadow-brand-500/20"
        >
          <svg class="w-6 h-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2.5"
              d="M12 4v16m8-8H4"
            />
          </svg>
        </div>
        <div>
          <h1 class="text-xl font-bold tracking-tight text-gray-900 leading-none font-figtree">
            Poura
          </h1>
          <p class="text-[10px] text-brand-500 font-bold tracking-wider uppercase mt-1">
            Espace Médecin
          </p>
        </div>
      </router-link>
    </div>

    <!-- Navigation -->
    <div class="flex-1 overflow-y-auto custom-scrollbar p-4 space-y-6">
      <div v-for="group in filteredMenuGroups" :key="group.title">
        <h3 class="px-4 text-[10px] font-bold uppercase tracking-widest text-gray-400 mb-2">
          {{ group.title }}
        </h3>
        <nav class="space-y-1">
          <router-link
            v-for="item in group.items"
            :key="item.name"
            :to="item.path"
            v-slot="{ isActive }"
          >
            <div
              :class="[
                'flex items-center gap-3 px-4 py-3 rounded-2xl transition-all duration-300 group relative',
                isActive
                  ? 'bg-brand-50 text-brand-700 font-bold shadow-[inset_0_2px_4px_rgba(8,145,178,0.05)]'
                  : 'text-gray-500 hover:bg-gray-50/80 hover:text-gray-900 font-medium',
              ]"
            >
              <!-- Active Indicator -->
              <div
                v-if="isActive"
                class="absolute left-0 top-1/2 -translate-y-1/2 w-1.5 h-6 bg-brand-600 rounded-r-full"
              ></div>
              <component
                :is="item.icon"
                :class="[
                  'h-5 w-5 transition-transform duration-300',
                  isActive
                    ? 'scale-110 text-brand-600'
                    : 'group-hover:scale-110 group-hover:text-brand-500',
                ]"
              />
              <span class="text-sm tracking-wide">{{ item.name }}</span>
            </div>
          </router-link>
        </nav>
      </div>
    </div>

    <!-- Footer Logout -->
    <div class="p-6 pt-4">
      <button
        @click="handleLogout"
        class="flex items-center gap-3 w-full px-4 py-3 rounded-2xl text-gray-500 hover:text-red-600 hover:bg-red-50 font-medium transition-all duration-300 border border-transparent hover:border-red-100"
      >
        <svg
          class="w-5 h-5 transition-transform group-hover:-translate-x-1"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2.5"
            d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"
          />
        </svg>
        <span class="text-sm">Déconnexion</span>
      </button>
    </div>
  </aside>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import {
  HomeIcon,
  CalendarIcon,
  UserGroupIcon,
  DocumentTextIcon as DocsIcon,
  DocumentIcon,
  ViewColumnsIcon as GridIcon,
  CubeIcon as BoxIcon,
  ClockIcon,
  UserCircleIcon,
} from '@heroicons/vue/24/outline'

const router = useRouter()

const menuGroups = [
  {
    title: 'Principal',
    items: [
      { icon: HomeIcon, name: 'Tableau de bord', path: '/dashboard' },
      { icon: CalendarIcon, name: 'Rendez-vous', path: '/appointments' },
      { icon: GridIcon, name: "File d'Attente", path: '/queue/today' },
      { icon: UserGroupIcon, name: 'Patients', path: '/patients' },
    ],
  },
  {
    title: 'Clinique',
    items: [
      { icon: DocsIcon, name: 'Consultations', path: '/consultations' },
      { icon: DocumentIcon, name: 'Ordonnances', path: '/ordonnances' },
      { icon: BoxIcon, name: 'Médicaments', path: '/medicaments' },
    ],
    roles: ['doctor'],
  },
  {
    title: 'Paramètres',
    items: [
      { icon: ClockIcon, name: 'Jours de travail', path: '/working-days' },
      { icon: UserCircleIcon, name: 'Profil', path: '/profile' },
    ],
    roles: ['doctor'],
  },
]

const role = localStorage.getItem('role') || 'doctor'

const filteredMenuGroups = computed(() => {
  return menuGroups
    .filter((group) => {
      if (group.roles && !group.roles.includes(role)) return false
      return true
    })
    .map((group) => {
      let items = group.items
      if (['secretary', 'assistant'].includes(role)) {
        items = items.filter(
          (item) =>
            !['Consultations', 'Ordonnances', 'Médicaments', 'Jours de travail'].includes(
              item.name,
            ),
        )
      }
      return { ...group, items }
    })
})

const handleLogout = () => {
  localStorage.removeItem('access')
  localStorage.removeItem('refresh')
  router.push('/signin')
}
</script>

<style scoped>
.custom-scrollbar::-webkit-scrollbar {
  width: 4px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: transparent;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background: #e8f1f6;
  border-radius: 4px;
}
.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background: #a5f3fc;
}
</style>
