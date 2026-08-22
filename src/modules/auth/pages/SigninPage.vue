<template>
  <FullScreenLayout>
    <div class="min-h-screen flex w-full bg-white dark:bg-gray-950 font-figtree">
      
      <!-- LEFT SIDE: Form -->
      <div class="w-full lg:w-1/2 flex items-center justify-center p-8 sm:p-12 relative overflow-hidden">
        
        <!-- Decorative subtle blurs for light/dark mode -->
        <div class="absolute -top-[10%] -left-[10%] w-[50%] h-[50%] rounded-full bg-brand-500/5 blur-[120px] pointer-events-none"></div>
        <div class="absolute bottom-[0%] -right-[10%] w-[40%] h-[40%] rounded-full bg-blue-light-500/5 blur-[100px] pointer-events-none"></div>

        <div class="w-full max-w-md relative z-10">
          <!-- Logo & Header -->
          <div class="mb-10">
            <div class="flex items-center gap-2 mb-8">
              <div class="w-10 h-10 bg-brand-600 rounded-xl flex items-center justify-center text-white font-bold text-2xl shadow-lg shadow-brand-500/30">P</div>
              <span class="font-black text-2xl tracking-tight text-gray-900 dark:text-white">POURA</span>
            </div>
            <h1 class="text-3xl sm:text-4xl font-black text-gray-900 dark:text-white mb-3 tracking-tight">Bon retour !</h1>
            <p class="text-gray-500 dark:text-gray-400 font-medium">Connectez-vous pour gérer votre cabinet et vos patients.</p>
          </div>

          <!-- Form -->
          <form @submit.prevent="handleSubmit" class="space-y-5">
            <div class="space-y-2">
              <label for="email" class="text-sm font-bold text-gray-700 dark:text-gray-300">Adresse Email</label>
              <input
                v-model="email"
                type="email"
                id="email"
                placeholder="docteur@exemple.com"
                class="w-full h-12 px-4 rounded-xl border border-gray-200 bg-gray-50 text-gray-900 focus:bg-white focus:border-brand-500 focus:ring-4 focus:ring-brand-500/10 transition-all outline-none dark:bg-gray-900 dark:border-gray-800 dark:text-white dark:focus:border-brand-500"
                required
              />
            </div>

            <div class="space-y-2">
              <div class="flex items-center justify-between">
                <label for="password" class="text-sm font-bold text-gray-700 dark:text-gray-300">Mot de passe</label>
                <router-link to="/reset-password" class="text-xs font-bold text-brand-600 hover:text-brand-700 transition-colors">Mot de passe oublié ?</router-link>
              </div>
              <div class="relative">
                <input
                  v-model="password"
                  :type="showPassword ? 'text' : 'password'"
                  id="password"
                  placeholder="••••••••"
                  class="w-full h-12 pl-4 pr-12 rounded-xl border border-gray-200 bg-gray-50 text-gray-900 focus:bg-white focus:border-brand-500 focus:ring-4 focus:ring-brand-500/10 transition-all outline-none dark:bg-gray-900 dark:border-gray-800 dark:text-white dark:focus:border-brand-500"
                  required
                />
                <button
                  type="button"
                  @click="togglePasswordVisibility"
                  class="absolute right-4 top-1/2 -translate-y-1/2 text-gray-400 hover:text-brand-600 transition-colors"
                >
                  <svg v-if="!showPassword" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                  </svg>
                  <svg v-else class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.29 3.29m0 0a9.97 9.97 0 013.028-1.563M12 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411" />
                  </svg>
                </button>
              </div>
            </div>

            <!-- Error Message -->
            <div v-if="errorMessage" class="p-3 bg-red-50 dark:bg-red-500/10 border border-red-100 dark:border-red-500/20 rounded-xl flex items-start gap-3">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-red-500 mt-0.5 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
              <p class="text-sm font-medium text-red-600 dark:text-red-400 leading-tight">
                {{ errorMessage }}
              </p>
            </div>

            <button type="submit" class="w-full h-12 bg-brand-600 hover:bg-brand-700 active:scale-[0.98] text-white font-bold rounded-xl shadow-lg shadow-brand-500/30 transition-all flex items-center justify-center gap-2 mt-4">
              Se Connecter
              <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                <path stroke-linecap="round" stroke-linejoin="round" d="M14 5l7 7m0 0l-7 7m7-7H3" />
              </svg>
            </button>
          </form>

          <div class="mt-8 text-center">
            <p class="text-sm font-medium text-gray-500 dark:text-gray-400">
              Vous n'avez pas de compte ?
              <router-link to="/signup" class="text-brand-600 hover:text-brand-700 font-bold transition-colors">Inscrivez-vous</router-link>
            </p>
          </div>
        </div>
      </div>

      <!-- RIGHT SIDE: Visual/Image -->
      <div class="hidden lg:block lg:w-1/2 relative bg-gray-900">
        <img src="/clinic_model_1787418202621.jpg" alt="POURA Clinic" class="absolute inset-0 w-full h-full object-cover" />
        <!-- Overlays -->
        <div class="absolute inset-0 bg-brand-900/60 mix-blend-multiply"></div>
        <div class="absolute inset-0 bg-gradient-to-t from-gray-900/90 via-gray-900/20 to-transparent"></div>
        
        <!-- Branding Content -->
        <div class="absolute bottom-0 left-0 w-full p-16">
          <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-white/20 mb-6">
            <span class="flex h-2 w-2 rounded-full bg-brand-400"></span>
            <span class="text-xs font-bold text-white uppercase tracking-wide">Espace Praticien</span>
          </div>
          <h2 class="text-4xl font-black text-white leading-tight mb-4">Rejoignez le réseau de santé de demain.</h2>
          <p class="text-lg text-white/80 font-medium max-w-lg">Gérez vos rendez-vous, collaborez avec d'autres spécialistes et offrez une expérience de soin exceptionnelle à vos patients.</p>
        </div>
      </div>

    </div>
  </FullScreenLayout>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router' 
import { login } from '@/api/authService.ts' 
import FullScreenLayout from '@/layouts/FullScreenLayout.vue'

const router = useRouter() 

const email = ref('')
const password = ref('')
const showPassword = ref(false)
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

    // allow authorized roles
    if (['gr_doctor', 'doctor', 'secretary', 'assistant'].includes(data.role)) {
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