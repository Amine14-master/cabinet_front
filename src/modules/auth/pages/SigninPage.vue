<template>
  <FullScreenLayout>
    <div class="relative p-6 bg-white z-1 dark:bg-gray-900 sm:p-0">
      <div class="relative flex flex-col justify-center w-full h-screen lg:flex-row dark:bg-gray-900">
        <div class="flex flex-col flex-1 w-full lg:w-1/2">
          <div class="w-full max-w-md pt-10 mx-auto">
            <router-link
              to="/"
              class="inline-flex items-center text-sm text-gray-500 transition-colors hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-300"
            >
              <svg
                class="stroke-current"
                xmlns="http://www.w3.org/2000/svg"
                width="20"
                height="20"
                viewBox="0 0 20 20"
                fill="none"
              >
                <path
                  d="M12.7083 5L7.5 10.2083L12.7083 15.4167"
                  stroke-width="1.5"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
              </svg>
              Back to dashboard
            </router-link>
          </div>

          <div class="flex flex-col justify-center flex-1 w-full max-w-md mx-auto">
            <div class="mb-5 sm:mb-8">
              <h1 class="mb-2 font-semibold text-gray-800 text-title-sm dark:text-white/90 sm:text-title-md">
                Sign In
              </h1>
              <p class="text-sm text-gray-500 dark:text-gray-400">
                Enter your email and password to sign in!
              </p>
            </div>

            <div class="grid grid-cols-1 gap-3 sm:grid-cols-2 sm:gap-5">
              <button class="inline-flex items-center justify-center gap-3 py-3 text-sm font-normal text-gray-700 transition-colors bg-gray-100 rounded-lg px-7 hover:bg-gray-200 hover:text-gray-800 dark:bg-white/5 dark:text-white/90 dark:hover:bg-white/10">
                <img src="https://www.gstatic.com/firebasejs/ui/2.0.0/images/auth/google.svg" class="w-5 h-5" alt="Google" />
                Sign in with Google
              </button>
              <button class="inline-flex items-center justify-center gap-3 py-3 text-sm font-normal text-gray-700 transition-colors bg-gray-100 rounded-lg px-7 hover:bg-gray-200 hover:text-gray-800 dark:bg-white/5 dark:text-white/90 dark:hover:bg-white/10">
                <svg width="21" class="fill-current" height="20" viewBox="0 0 21 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M15.6705 1.875H18.4272L12.4047 8.75833L19.4897 18.125H13.9422L9.59717 12.4442L4.62554 18.125H1.86721L8.30887 10.7625L1.51221 1.875H7.20054L11.128 7.0675L15.6705 1.875ZM14.703 16.475H16.2305L6.37054 3.43833H4.73137L14.703 16.475Z" />
                </svg>
                Sign in with X
              </button>
            </div>

            <div class="relative py-3 sm:py-5">
              <div class="absolute inset-0 flex items-center">
                <div class="w-full border-t border-gray-200 dark:border-gray-800"></div>
              </div>
              <div class="relative flex justify-center text-sm">
                <span class="p-2 text-gray-400 bg-white dark:bg-gray-900 sm:px-5 sm:py-2">Or</span>
              </div>
            </div>

            <form @submit.prevent="handleSubmit">
              <div class="space-y-5">
                <div>
                  <label for="email" class="mb-1.5 block text-sm font-medium text-gray-700 dark:text-gray-400">
                    Email<span class="text-red-500">*</span>
                  </label>
                  <input
                    v-model="email"
                    type="email"
                    id="email"
                    placeholder="info@gmail.com"
                    class="h-11 w-full rounded-lg border border-gray-300 bg-transparent px-4 py-2.5 text-sm text-gray-800 focus:border-blue-500 focus:ring-3 focus:ring-blue-500/10 dark:border-gray-700 dark:text-white/90 dark:bg-gray-900"
                    required
                  />
                </div>

                <div>
                  <label for="password" class="mb-1.5 block text-sm font-medium text-gray-700 dark:text-gray-400">
                    Password<span class="text-red-500">*</span>
                  </label>
                  <div class="relative">
                    <input
                      v-model="password"
                      :type="showPassword ? 'text' : 'password'"
                      id="password"
                      placeholder="Enter your password"
                      class="h-11 w-full rounded-lg border border-gray-300 bg-transparent py-2.5 pl-4 pr-11 text-sm text-gray-800 focus:border-blue-500 focus:ring-3 focus:ring-blue-500/10 dark:border-gray-700 dark:text-white/90 dark:bg-gray-900"
                      required
                    />
                    <span
                      @click="togglePasswordVisibility"
                      class="absolute z-30 text-gray-500 -translate-y-1/2 cursor-pointer right-4 top-1/2 dark:text-gray-400"
                    >
                      <svg v-if="!showPassword" class="fill-current" width="20" height="20" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M10 13.86C7.23 13.86 4.86 12.13 3.92 9.7a6.26 6.26 0 0 1 12.15 0c-.94 2.43-3.3 4.16-6.07 4.16ZM10 4.04C6.48 4.04 3.49 6.3 2.41 9.45a1 1 0 0 0 0 .5c1.08 3.15 4.07 5.41 7.59 5.41s6.51-2.26 7.59-5.41a1 1 0 0 0 0-.5C16.51 6.3 13.52 4.04 10 4.04Z" fill="#98A2B3"/>
                      </svg>
                      <svg v-else class="fill-current" width="20" height="20" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M4.63 3.57a1 1 0 0 0-1.41 1.41l1.27 1.28C3.74 6.84 2.89 8.06 2.41 9.45a1 1 0 0 0 0 .5c1.08 3.15 4.07 5.41 7.59 5.41 1.25 0 2.44-.28 3.5-.82l1.86 1.86a1 1 0 0 0 1.41-1.41L4.63 3.57Zm7.73 9.85-1.91-1.91c-.14.03-.29.05-.45.05h-.01a1.86 1.86 0 0 1-1.86-1.86c0-.15.02-.3.05-.45L5.91 6.98a6.2 6.2 0 0 0-1.98 2.72c.94 2.43 3.3 4.16 6.07 4.16.83 0 1.62-.15 2.36-.44Z" fill="#98A2B3"/>
                      </svg>
                    </span>
                  </div>
                </div>

                <div class="flex items-center justify-between">
                  <label class="flex items-center text-sm font-normal text-gray-700 cursor-pointer select-none dark:text-gray-400">
                    <input v-model="keepLoggedIn" type="checkbox" class="hidden" />
                    <div :class="keepLoggedIn ? 'border-blue-600 bg-blue-600' : 'bg-transparent border-gray-300 dark:border-gray-700'" class="mr-3 flex h-5 w-5 items-center justify-center rounded-md border-[1.25px] transition-colors">
                      <svg v-if="keepLoggedIn" width="14" height="14" viewBox="0 0 14 14" fill="none">
                        <path d="M11.66 3.5L5.25 9.91 2.33 7" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                      </svg>
                    </div>
                    Keep me logged in
                  </label>
                  <router-link to="/reset-password" class="text-sm text-blue-600 hover:text-blue-700 dark:text-blue-400">
                    Forgot password?
                  </router-link>
                </div>
                <p v-if="errorMessage" class="text-sm font-medium text-red-500 mb-4">
                  {{ errorMessage }}
                </p>
                <button type="submit" class="flex items-center justify-center w-full px-4 py-3 text-sm font-medium text-white transition rounded-lg bg-blue-600 shadow-sm hover:bg-blue-700">
                  Sign In
                </button>
              </div>
            </form>

            <div class="mt-5">
              <p class="text-sm font-normal text-center text-gray-700 dark:text-gray-400 sm:text-start">
                Don't have an account?
                <router-link to="/signup" class="text-blue-600 hover:text-blue-700 dark:text-blue-400">Sign Up</router-link>
              </p>
            </div>
          </div>
        </div>

        <div class="relative items-center hidden w-full h-full lg:w-1/2 bg-gray-950 dark:bg-white/5 lg:grid">
          <div class="flex items-center justify-center z-1">
            <CommonGridShape />
            <div class="flex flex-col items-center max-w-xs">
              <router-link to="/" class="block mb-4">
                <img width="231" height="48" src="/images/logo/auth-logo.svg" alt="Logo" />
              </router-link>
              <p class="text-center text-gray-400 dark:text-white/60">
                Free and Open-Source Tailwind CSS Admin Dashboard Template
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </FullScreenLayout>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router' 
import { login } from '@/api/authService.ts' 
import CommonGridShape from '@/layouts/common/CommonGridShape.vue'
import FullScreenLayout from '@/layouts/FullScreenLayout.vue'

const router = useRouter() 

const email = ref('')
const password = ref('')
const showPassword = ref(false)
const keepLoggedIn = ref(false)
const errorMessage = ref('') 

const togglePasswordVisibility = () => {
  showPassword.value = !showPassword.value
}

const handleSubmit = async () => {
  errorMessage.value = ''

  try {
    const data = await login({
      email: email.value,
      password: password.value
    })

    console.log('Connexion réussie:', data)

    // save tokens
    localStorage.setItem('access', data.access)
    localStorage.setItem('refresh', data.refresh)
    localStorage.setItem('role', data.role)
    localStorage.setItem('username', data.username)

    // allow only gr_doctor
    if (data.role === 'gr_doctor') {
      await router.push({ name: 'Dashboard' })
    } else {
      errorMessage.value = 'Access denied'
    }

  } catch (error: any) {
    console.error('Erreur de connexion:', error)
    errorMessage.value =
      error?.response?.data?.error ||
      error?.error ||
      'Email ou mot de passe incorrect'
  }
}
</script>