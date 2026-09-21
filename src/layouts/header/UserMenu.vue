<template>
  <div class="relative" ref="dropdownRef">
    <button
      class="flex items-center text-gray-700 dark:text-gray-400 focus:outline-none"
      @click.prevent="toggleDropdown"
    >
      <span class="mr-3 overflow-hidden rounded-full h-11 w-11">
        <img :src="photo" alt="User" class="w-full h-full object-cover" />
      </span>

      <span class="block mr-1 font-medium text-theme-sm">{{ username }}</span>

      <ChevronDownIcon
        :class="{ 'rotate-180': dropdownOpen }"
        class="transition-transform duration-200"
      />
    </button>

    <div
      v-if="dropdownOpen"
      class="absolute right-0 mt-[17px] flex w-[260px] flex-col rounded-2xl border border-gray-200 bg-white p-3 shadow-theme-lg dark:border-gray-800 dark:bg-gray-dark z-50"
    >
      <div class="px-3 py-2">
        <span class="block font-medium text-gray-700 text-theme-sm dark:text-gray-400">
          {{ login }}
        </span>
        <span class="mt-0.5 block text-theme-xs text-gray-500 dark:text-gray-400">
          {{ role }}
        </span>
      </div>

      <ul class="flex flex-col gap-1 pt-4 pb-3 border-b border-gray-200 dark:border-gray-800">
        <li v-for="item in menuItems" :key="item.text">
          <router-link
            :to="item.href"
            @click="closeDropdown"
            class="flex items-center gap-3 px-3 py-2 font-medium text-gray-700 rounded-lg group text-theme-sm hover:bg-gray-100 hover:text-gray-700 dark:text-gray-400 dark:hover:bg-white/5 dark:hover:text-gray-300"
          >
            <component
              :is="item.icon"
              class="w-5 h-5 text-gray-500 group-hover:text-gray-700 dark:group-hover:text-gray-300"
            />
            {{ item.text }}
          </router-link>
        </li>
      </ul>

      <button
        @click="signOut"
        class="flex items-center w-full gap-3 px-3 py-2 mt-3 font-medium text-gray-700 rounded-lg group text-theme-sm hover:bg-gray-100 hover:text-gray-700 dark:text-gray-400 dark:hover:bg-white/5 dark:hover:text-gray-300"
      >
        <LogoutIcon
          class="w-5 h-5 text-gray-500 group-hover:text-gray-700 dark:group-hover:text-gray-300"
        />
        Sign out
      </button>
    </div>
  </div>
</template>
<script setup lang="ts">
import {
  ChevronDownIcon,
  InfoCircleIcon,
  LogoutIcon,
  LockIcon,
  UserCircleIcon,
  UserGroupIcon,
} from '@/icons'
import { onMounted, onUnmounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import { getDoctorProfile } from '@/api/doctorService'

const router = useRouter()
const dropdownOpen = ref(false)
const dropdownRef = ref<HTMLElement | null>(null)

const username = ref('Utilisateur')
const role = ref('Membre')

const menuItems = [
  { href: '/profile', icon: UserCircleIcon, text: 'Modifier le profil' },
  { href: '/Security', icon: LockIcon, text: 'Sécurité du compte' },
  { href: '/team', icon: UserGroupIcon, text: 'Équipe du cabinet' },
  { href: '/profile', icon: InfoCircleIcon, text: 'Support' },
]

const toggleDropdown = () => {
  dropdownOpen.value = !dropdownOpen.value
}
const closeDropdown = () => {
  dropdownOpen.value = false
}

const signOut = async () => {
  try {
    const accessToken = localStorage.getItem('access')
    const refreshToken = localStorage.getItem('refresh')

    if (accessToken && refreshToken) {
      await fetch('http://127.0.0.1:8000/api/users/logout/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${accessToken}`,
        },
        body: JSON.stringify({ refresh: refreshToken }),
      })
    }
  } catch (e) {
    console.warn('logout request failed', e)
  }

  localStorage.clear()
  await router.replace('/signin')
}
const handleClickOutside = (event: Event) => {
  if (dropdownRef.value && !dropdownRef.value.contains(event.target as Node)) {
    closeDropdown()
  }
}

onMounted(async () => {
  document.addEventListener('click', handleClickOutside)

  const storedName = localStorage.getItem('username')
  const storedRole = localStorage.getItem('role')

  if (storedName) username.value = storedName
  if (storedRole) role.value = storedRole

  try {
    const doctor = await getDoctorProfile()

    if (doctor.photo) {
      photo.value = doctor.photo
    }

    if (doctor.first_name) {
      username.value = `Dr. ${doctor.first_name} ${doctor.last_name}`
    }
    const storedUsername = localStorage.getItem('username')

    if (storedUsername) {
      login.value = storedUsername
    }
  } catch (e) {
    console.error(e)
  }
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})

const photo = ref('/images/user/owner.jpg')
const login = ref('Utilisateur')
</script>
