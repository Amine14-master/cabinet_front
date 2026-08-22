<template>
  <div :dir="currentLang === 'ar' ? 'rtl' : 'ltr'" :class="currentLang === 'ar' ? 'font-sans' : 'font-figtree'" class="min-h-screen bg-gray-50 dark:bg-gray-950 text-gray-900 dark:text-gray-100 overflow-x-hidden selection:bg-brand-500/30 transition-all duration-300">
    
    <!-- 1. NAVIGATION -->
    <nav class="fixed top-0 left-0 right-0 z-50 transition-all duration-300" :class="{ 'bg-white/90 dark:bg-gray-950/90 backdrop-blur-lg shadow-sm border-b border-gray-200/50 dark:border-gray-800/50 py-3': isScrolled, 'bg-transparent py-5': !isScrolled }">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between">
          <!-- Logo -->
          <div class="flex-shrink-0 flex items-center gap-2">
            <div class="w-10 h-10 bg-brand-600 rounded-xl flex items-center justify-center text-white font-bold text-2xl shadow-lg shadow-brand-500/30">P</div>
            <span class="font-black text-2xl tracking-tight text-gray-900 dark:text-white">POURA</span>
          </div>

          <!-- Desktop Links -->
          <div class="hidden md:flex items-center gap-8 bg-white/40 dark:bg-gray-900/40 backdrop-blur-md px-8 py-2.5 rounded-full border border-white/50 dark:border-gray-700/50 shadow-sm">
            <a href="#" class="text-sm font-bold text-brand-600 dark:text-brand-400">{{ t.nav.home }}</a>
            <a href="#about" class="text-sm font-medium text-gray-600 dark:text-gray-300 hover:text-brand-600 transition-colors">{{ t.nav.about }}</a>
            <a href="#specialties" class="text-sm font-medium text-gray-600 dark:text-gray-300 hover:text-brand-600 transition-colors">{{ t.nav.specialties }}</a>
            <a href="#ecosystem" class="text-sm font-medium text-gray-600 dark:text-gray-300 hover:text-brand-600 transition-colors">{{ t.nav.ecosystem }}</a>
            <a href="#testimonials" class="text-sm font-medium text-gray-600 dark:text-gray-300 hover:text-brand-600 transition-colors">{{ t.nav.testimonials }}</a>
            <a href="#contact" class="text-sm font-medium text-gray-600 dark:text-gray-300 hover:text-brand-600 transition-colors">{{ t.nav.contact }}</a>
          </div>

          <!-- Actions -->
          <div class="hidden md:flex items-center gap-4">
            <!-- Language Switcher -->
            <select v-model="currentLang" class="bg-transparent border-none text-gray-600 dark:text-gray-300 text-sm font-medium focus:ring-0 cursor-pointer uppercase">
              <option value="fr">FR</option>
              <option value="en">EN</option>
              <option value="ar">AR</option>
            </select>
            
            <router-link to="/signin" class="px-6 py-3 rounded-full bg-gray-900 dark:bg-white hover:bg-gray-800 dark:hover:bg-gray-100 text-white dark:text-gray-900 text-sm font-bold shadow-md transition-all active:scale-95">{{ t.nav.book }}</router-link>
          </div>

          <!-- Mobile Menu Button & Lang Switcher -->
          <div class="md:hidden flex items-center gap-4">
            <select v-model="currentLang" class="bg-transparent border-none text-gray-600 dark:text-gray-300 text-sm font-medium focus:ring-0 uppercase">
              <option value="fr">FR</option>
              <option value="en">EN</option>
              <option value="ar">AR</option>
            </select>
            <button @click="mobileMenuOpen = !mobileMenuOpen" class="text-gray-600 dark:text-gray-300 p-2">
              <svg v-if="!mobileMenuOpen" xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" /></svg>
              <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>
            </button>
          </div>
        </div>
      </div>

      <!-- Mobile Menu -->
      <div v-show="mobileMenuOpen" class="md:hidden bg-white/95 dark:bg-gray-950/95 backdrop-blur-xl border-b border-gray-100 dark:border-gray-800 absolute w-full shadow-2xl transition-all duration-300">
        <div class="px-4 py-6 space-y-4">
          <a @click="mobileMenuOpen = false" href="#" class="block text-lg font-bold text-brand-600">{{ t.nav.home }}</a>
          <a @click="mobileMenuOpen = false" href="#about" class="block text-lg font-medium text-gray-700 dark:text-gray-200">{{ t.nav.about }}</a>
          <a @click="mobileMenuOpen = false" href="#specialties" class="block text-lg font-medium text-gray-700 dark:text-gray-200">{{ t.nav.specialties }}</a>
          <a @click="mobileMenuOpen = false" href="#ecosystem" class="block text-lg font-medium text-gray-700 dark:text-gray-200">{{ t.nav.ecosystem }}</a>
          <a @click="mobileMenuOpen = false" href="#contact" class="block text-lg font-medium text-gray-700 dark:text-gray-200">{{ t.nav.contact }}</a>
          <router-link @click="mobileMenuOpen = false" to="/signin" class="block mt-6 text-center w-full px-5 py-3.5 rounded-xl bg-gray-900 dark:bg-white text-white dark:text-gray-900 font-bold shadow-md">{{ t.nav.book }}</router-link>
        </div>
      </div>
    </nav>

    <!-- 2. HERO SECTION -->
    <section class="relative pt-32 pb-20 lg:pt-40 lg:pb-32 overflow-hidden">
      <!-- Background Abstract Elements -->
      <div class="absolute top-0 right-0 -translate-y-12 translate-x-1/3 w-[800px] h-[800px] bg-brand-200/40 dark:bg-brand-900/20 rounded-full blur-3xl pointer-events-none -z-10"></div>
      <div class="absolute bottom-0 left-0 translate-y-1/3 -translate-x-1/3 w-[600px] h-[600px] bg-blue-light-200/40 dark:bg-blue-light-900/20 rounded-full blur-3xl pointer-events-none -z-10"></div>
      
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-8 items-center">
          
          <!-- Hero Text -->
          <div class="max-w-2xl">
            <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-brand-50 dark:bg-brand-900/30 border border-brand-100 dark:border-brand-800 mb-6">
              <span class="flex h-2 w-2 rounded-full bg-brand-500"></span>
              <span class="text-xs font-bold text-brand-700 dark:text-brand-300 uppercase tracking-wide">{{ t.hero.badge }}</span>
            </div>
            
            <h1 class="text-4xl sm:text-5xl lg:text-[3.5rem] font-black tracking-tight text-gray-900 dark:text-white leading-[1.1] mb-6" v-html="t.hero.title">
            </h1>
            
            <p class="text-lg sm:text-xl text-gray-600 dark:text-gray-400 font-medium leading-relaxed mb-10">
              {{ t.hero.subtitle }}
            </p>
            
            <div class="flex flex-col sm:flex-row items-center gap-4">
              <router-link to="/signin" class="w-full sm:w-auto px-8 py-4 rounded-full bg-brand-600 hover:bg-brand-700 text-white font-bold text-lg shadow-lg shadow-brand-500/30 transition-all hover:-translate-y-0.5 active:scale-95 flex items-center justify-center gap-2">
                {{ t.hero.cta1 }}
                <svg v-if="currentLang !== 'ar'" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
                <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M9.707 16.707a1 1 0 01-1.414 0l-6-6a1 1 0 010-1.414l6-6a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l4.293 4.293a1 1 0 010 1.414z" clip-rule="evenodd" /></svg>
              </router-link>
              <a href="#about" class="w-full sm:w-auto px-8 py-4 rounded-full bg-white dark:bg-gray-900 text-gray-800 dark:text-white font-bold text-lg shadow-sm border border-gray-200 dark:border-gray-800 transition-all hover:bg-gray-50 dark:hover:bg-gray-800 hover:-translate-y-0.5 text-center">
                {{ t.hero.cta2 }}
              </a>
            </div>
          </div>

          <!-- Hero Image & Floating Cards -->
          <div class="relative mt-8 lg:mt-0">
            <div class="relative rounded-[2.5rem] overflow-hidden shadow-2xl shadow-brand-900/20 border-8 border-white/50 dark:border-gray-800/50 backdrop-blur-sm z-10 aspect-[4/5] sm:aspect-square lg:aspect-[4/5]">
              <img src="/hero_handshake_3d_1787418190508.jpg" alt="Doctor and Patient Handshake" class="w-full h-full object-cover object-center" />
            </div>

            <!-- Floating Card 1: Satisfaction -->
            <div :class="currentLang === 'ar' ? '-right-6 sm:-right-12' : '-left-6 sm:-left-12'" class="absolute top-12 bg-white/90 dark:bg-gray-900/90 backdrop-blur-md rounded-2xl p-4 shadow-xl border border-white/20 dark:border-gray-700/30 z-20 animate-bounce-slow">
              <div class="flex items-center gap-4">
                <div class="w-12 h-12 rounded-full bg-brand-100 dark:bg-brand-900/50 flex items-center justify-center">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-brand-600 dark:text-brand-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20m7-10V5a2 2 0 00-2-2h-.095c-.5 0-.905.405-.905.905 0 .714-.211 1.412-.608 2.006L7 11v9m7-10h-2M7 20H5a2 2 0 01-2-2v-6a2 2 0 012-2h2.5" /></svg>
                </div>
                <div :class="currentLang === 'ar' ? 'text-right' : 'text-left'">
                  <p class="text-2xl font-black text-gray-900 dark:text-white">97%</p>
                  <p class="text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wide">{{ t.hero.satisfaction }}</p>
                </div>
              </div>
            </div>

            <!-- Floating Card 2: Find Doctor Widget -->
            <div :class="currentLang === 'ar' ? '-left-4 sm:-left-8' : '-right-4 sm:-right-8'" class="absolute bottom-12 bg-white/95 dark:bg-gray-900/95 backdrop-blur-xl rounded-3xl p-5 shadow-2xl border border-white/20 dark:border-gray-700/30 z-20 w-72">
              <p class="font-bold text-gray-900 dark:text-white mb-4 flex items-center gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-brand-500" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd" /></svg>
                {{ t.hero.findDoc }}
              </p>
              <div class="space-y-3">
                <div class="bg-gray-50 dark:bg-gray-950 rounded-xl p-3 border border-gray-100 dark:border-gray-800 flex items-center gap-3">
                  <div class="w-8 h-8 rounded-lg bg-brand-100 dark:bg-brand-900/30 flex items-center justify-center text-brand-600 font-bold">🩺</div>
                  <span class="text-sm text-gray-500">{{ t.hero.spec }}</span>
                </div>
                <div class="bg-gray-50 dark:bg-gray-950 rounded-xl p-3 border border-gray-100 dark:border-gray-800 flex items-center gap-3">
                  <div class="w-8 h-8 rounded-lg bg-blue-light-100 dark:bg-blue-light-900/30 flex items-center justify-center text-blue-light-600 font-bold">📍</div>
                  <span class="text-sm text-gray-500">{{ t.hero.loc }}</span>
                </div>
                <button class="w-full py-3 bg-gray-900 dark:bg-white text-white dark:text-gray-900 rounded-xl font-bold shadow-md hover:bg-gray-800 dark:hover:bg-gray-100 transition-colors">{{ t.hero.search }}</button>
              </div>
            </div>

            <!-- Specialties Nodes -->
            <div :class="currentLang === 'ar' ? '-left-4' : '-right-4'" class="absolute -top-4 w-16 h-16 bg-white dark:bg-gray-800 rounded-full shadow-lg border border-gray-100 dark:border-gray-700 flex items-center justify-center z-20 animate-pulse">
               <span class="text-2xl">🧠</span>
            </div>
            <div :class="currentLang === 'ar' ? '-right-8' : '-left-8'" class="absolute top-1/3 w-14 h-14 bg-white dark:bg-gray-800 rounded-full shadow-lg border border-gray-100 dark:border-gray-700 flex items-center justify-center z-20">
               <span class="text-xl">❤️</span>
            </div>
            <div :class="currentLang === 'ar' ? '-right-4' : '-left-4'" class="absolute bottom-1/4 w-12 h-12 bg-white dark:bg-gray-800 rounded-full shadow-lg border border-gray-100 dark:border-gray-700 flex items-center justify-center z-20">
               <span class="text-lg">👶</span>
            </div>

          </div>
        </div>
      </div>
    </section>

    <!-- 3. ABOUT US -->
    <section id="about" class="py-24 bg-white dark:bg-gray-900">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
          
          <!-- Abstract Visual -->
          <div class="relative flex justify-center items-center">
            <div class="w-full max-w-md aspect-square relative">
              <div class="absolute inset-0 bg-gradient-to-br from-brand-100 to-blue-light-50 dark:from-brand-900/30 dark:to-blue-light-900/10 rounded-full animate-spin-slow"></div>
              <div class="absolute inset-4 bg-white dark:bg-gray-900 rounded-full flex items-center justify-center shadow-inner">
                <!-- Abstract DNA / Network -->
                <svg class="w-3/4 h-3/4 text-brand-600/20 dark:text-brand-400/10" viewBox="0 0 100 100" fill="currentColor">
                  <circle cx="20" cy="50" r="10" />
                  <circle cx="50" cy="20" r="15" />
                  <circle cx="80" cy="50" r="10" />
                  <circle cx="50" cy="80" r="15" />
                  <path d="M20 50 Q 50 20 80 50 Q 50 80 20 50" fill="none" stroke="currentColor" stroke-width="2" />
                  <circle cx="50" cy="50" r="20" class="text-brand-500" />
                </svg>
              </div>
              <!-- Floating stat -->
              <div :class="currentLang === 'ar' ? 'left-0' : 'right-0'" class="absolute top-0 bg-white dark:bg-gray-800 rounded-2xl p-4 shadow-xl border border-gray-100 dark:border-gray-700">
                <p class="text-3xl font-black text-brand-600 text-center">50+</p>
                <p class="text-xs font-bold text-gray-500 uppercase">{{ t.about.specCount }}</p>
              </div>
            </div>
          </div>

          <!-- Content -->
          <div>
            <h2 class="text-sm font-bold text-brand-600 dark:text-brand-400 uppercase tracking-widest mb-3">{{ t.about.title }}</h2>
            <h3 class="text-3xl sm:text-4xl font-black text-gray-900 dark:text-white tracking-tight leading-tight mb-6">
              {{ t.about.heading }}
            </h3>
            <p class="text-lg text-gray-600 dark:text-gray-400 leading-relaxed mb-10">
              {{ t.about.desc }}
            </p>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
              <div class="bg-gray-50 dark:bg-gray-950 p-6 rounded-2xl border border-gray-100 dark:border-gray-800">
                <div class="w-10 h-10 rounded-xl bg-brand-100 dark:bg-brand-900/30 flex items-center justify-center mb-4 text-brand-600">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>
                </div>
                <h4 class="text-lg font-bold text-gray-900 dark:text-white mb-2">{{ t.about.feat1Title }}</h4>
                <p class="text-sm text-gray-500 dark:text-gray-400">{{ t.about.feat1Desc }}</p>
              </div>
              <div class="bg-gray-50 dark:bg-gray-950 p-6 rounded-2xl border border-gray-100 dark:border-gray-800">
                <div class="w-10 h-10 rounded-xl bg-blue-light-100 dark:bg-blue-light-900/30 flex items-center justify-center mb-4 text-blue-light-600">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>
                </div>
                <h4 class="text-lg font-bold text-gray-900 dark:text-white mb-2">{{ t.about.feat2Title }}</h4>
                <p class="text-sm text-gray-500 dark:text-gray-400">{{ t.about.feat2Desc }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 4. WHY CHOOSE US -->
    <section id="specialties" class="py-24 bg-gray-50 dark:bg-gray-950">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-3xl mx-auto mb-16">
          <h2 class="text-sm font-bold text-brand-600 dark:text-brand-400 uppercase tracking-widest mb-3">{{ t.why.title }}</h2>
          <h3 class="text-3xl sm:text-4xl font-black text-gray-900 dark:text-white tracking-tight leading-tight mb-4">
            {{ t.why.heading }}
          </h3>
          <p class="text-lg text-gray-600 dark:text-gray-400">
            {{ t.why.desc }}
          </p>
        </div>

        <div class="bg-white dark:bg-gray-900 rounded-[2.5rem] p-4 sm:p-8 shadow-xl border border-gray-100 dark:border-gray-800 grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-0">
          
          <!-- Tabs -->
          <div class="lg:col-span-5 flex flex-col justify-center space-y-2 lg:border-x-0" :class="currentLang === 'ar' ? 'lg:border-l border-gray-100 dark:border-gray-800 pl-0 lg:pl-8' : 'lg:border-r border-gray-100 dark:border-gray-800 pr-0 lg:pr-8'">
            <button v-for="(tab, index) in whyUsTabs[currentLang]" :key="index" @click="activeTab = index" 
                    class="text-start px-6 py-5 rounded-2xl transition-all duration-300 flex items-center justify-between group"
                    :class="activeTab === index ? 'bg-brand-50 dark:bg-brand-900/20 text-brand-700 dark:text-brand-300' : 'hover:bg-gray-50 dark:hover:bg-gray-800 text-gray-600 dark:text-gray-400'">
              <span class="text-lg font-bold">{{ tab.title }}</span>
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 transition-all duration-300 group-hover:opacity-100" 
                   :class="[activeTab === index ? 'opacity-100 translate-x-0' : 'opacity-0', currentLang === 'ar' ? 'rotate-180 group-hover:translate-x-0 translate-x-4' : 'group-hover:translate-x-0 -translate-x-4']" 
                   viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd" />
              </svg>
            </button>
          </div>

          <!-- Tab Content -->
          <div class="lg:col-span-7 flex flex-col justify-center" :class="currentLang === 'ar' ? 'pr-0 lg:pr-8' : 'pl-0 lg:pl-8'">
            <div class="aspect-[4/3] rounded-3xl overflow-hidden relative shadow-lg mb-6 group">
              <img src="/doctor_consultation_1787418213841.jpg" alt="Consultation" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" />
              <div class="absolute inset-0 bg-gradient-to-t from-gray-900/60 to-transparent"></div>
              <div class="absolute bottom-0 p-8" :class="currentLang === 'ar' ? 'right-0' : 'left-0'">
                <h4 class="text-2xl font-black text-white mb-2">{{ whyUsTabs[currentLang][activeTab].title }}</h4>
                <p class="text-white/90 text-sm max-w-md leading-relaxed">{{ whyUsTabs[currentLang][activeTab].description }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 5. TOTAL CARE MODEL (Banner) -->
    <section id="ecosystem" class="relative py-32 lg:py-48 flex items-center justify-center overflow-hidden">
      <div class="absolute inset-0 z-0">
        <img src="/clinic_model_1787418202621.jpg" alt="Modern Clinic Model" class="w-full h-full object-cover" />
        <div class="absolute inset-0 bg-brand-900/80 mix-blend-multiply"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-gray-900/50 to-gray-900/90"></div>
      </div>
      
      <div class="relative z-10 max-w-4xl mx-auto px-4 text-center">
        <h2 class="text-sm font-bold text-brand-400 uppercase tracking-widest mb-4">{{ t.eco.title }}</h2>
        <h3 class="text-4xl sm:text-5xl lg:text-6xl font-black text-white tracking-tight mb-8">
          {{ t.eco.heading }}
        </h3>
        <p class="text-xl text-white/80 leading-relaxed font-light mb-12 max-w-3xl mx-auto">
          {{ t.eco.desc }}
        </p>
        <button class="px-8 py-4 rounded-full bg-white text-brand-900 font-bold text-lg shadow-xl hover:bg-brand-50 transition-colors">
          {{ t.eco.cta }}
        </button>
      </div>
    </section>

    <!-- 6. TESTIMONIALS -->
    <section id="testimonials" class="py-24 bg-gray-50 dark:bg-gray-950">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-3xl mx-auto mb-16">
          <h2 class="text-3xl sm:text-4xl font-black text-gray-900 dark:text-white tracking-tight mb-4">
            {{ t.testi.title }}
          </h2>
          <p class="text-lg text-gray-600 dark:text-gray-400">
            {{ t.testi.desc }}
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div v-for="(testimonial, i) in testimonialsData[currentLang]" :key="i" class="bg-white dark:bg-gray-900 rounded-3xl p-8 shadow-sm border border-gray-100 dark:border-gray-800">
            <div class="flex gap-1 mb-6">
              <svg v-for="s in 5" :key="s" class="w-5 h-5 text-orange-400" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
            </div>
            <h4 class="text-lg font-bold text-gray-900 dark:text-white mb-3">{{ testimonial.title }}</h4>
            <p class="text-gray-600 dark:text-gray-400 mb-8 italic">"{{ testimonial.body }}"</p>
            <div class="flex items-center gap-4 mt-auto">
              <div class="w-12 h-12 rounded-full bg-gray-200 dark:bg-gray-800 flex items-center justify-center font-bold text-gray-500">{{ testimonial.initials }}</div>
              <div>
                <p class="font-bold text-gray-900 dark:text-white">{{ testimonial.author }}</p>
                <p class="text-sm text-gray-500">{{ t.testi.patient }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 7. BLOG / INSIGHTS -->
    <section class="py-24 bg-white dark:bg-gray-900">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-16">
          <div class="max-w-2xl">
            <h2 class="text-sm font-bold text-brand-600 dark:text-brand-400 uppercase tracking-widest mb-3">{{ t.blog.title }}</h2>
            <h3 class="text-3xl sm:text-4xl font-black text-gray-900 dark:text-white tracking-tight">
              {{ t.blog.heading }}
            </h3>
          </div>
          <p class="text-gray-600 dark:text-gray-400 max-w-sm">{{ t.blog.desc }}</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div v-for="(post, index) in blogPostsData[currentLang]" :key="index" class="group cursor-pointer">
            <div class="aspect-[4/3] rounded-3xl overflow-hidden mb-6 relative shadow-md">
              <img :src="post.image" :alt="post.title" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" />
            </div>
            <h4 class="text-xl font-bold text-gray-900 dark:text-white mb-3 group-hover:text-brand-600 transition-colors">{{ post.title }}</h4>
            <p class="text-gray-600 dark:text-gray-400 mb-4 line-clamp-2">{{ post.excerpt }}</p>
            <div class="flex items-center justify-between">
              <a href="#" class="text-brand-600 font-bold flex items-center gap-1 group-hover:gap-2 transition-all" :class="currentLang === 'ar' ? 'flex-row-reverse' : ''">
                {{ t.blog.readMore }}
                <svg v-if="currentLang !== 'ar'" xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
                <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M7.707 14.707a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l2.293 2.293a1 1 0 010 1.414z" clip-rule="evenodd" /></svg>
              </a>
              <span class="text-xs text-gray-500 font-medium uppercase tracking-wider">{{ post.date }}</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 8. CONTACT US -->
    <section id="contact" class="py-24 bg-gray-50 dark:bg-gray-950">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-3xl mx-auto mb-16">
          <h2 class="text-sm font-bold text-brand-600 dark:text-brand-400 uppercase tracking-widest mb-3">{{ t.contact.title }}</h2>
          <h3 class="text-3xl sm:text-4xl font-black text-gray-900 dark:text-white tracking-tight mb-4">
            {{ t.contact.heading }}
          </h3>
          <p class="text-lg text-gray-600 dark:text-gray-400">
            {{ t.contact.desc }}
          </p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-8 items-start max-w-5xl mx-auto">
          <!-- Contact Info -->
          <div class="space-y-8 bg-white dark:bg-gray-900 p-8 rounded-3xl shadow-sm border border-gray-100 dark:border-gray-800 h-full">
            <div class="flex items-start gap-4">
              <div class="w-12 h-12 rounded-2xl bg-brand-50 dark:bg-brand-900/20 flex items-center justify-center flex-shrink-0 text-brand-600">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" /><path stroke-linecap="round" stroke-linejoin="round" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" /></svg>
              </div>
              <div>
                <h4 class="text-lg font-bold text-gray-900 dark:text-white mb-1">{{ t.contact.address }}</h4>
                <p class="text-gray-600 dark:text-gray-400">123 Avenue de la Santé<br/>75001 Paris, France</p>
              </div>
            </div>
            
            <div class="flex items-start gap-4">
              <div class="w-12 h-12 rounded-2xl bg-brand-50 dark:bg-brand-900/20 flex items-center justify-center flex-shrink-0 text-brand-600">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" /></svg>
              </div>
              <div>
                <h4 class="text-lg font-bold text-gray-900 dark:text-white mb-1">{{ t.contact.phone }}</h4>
                <p class="text-gray-600 dark:text-gray-400" dir="ltr">+33 1 23 45 67 89</p>
              </div>
            </div>
            
            <div class="flex items-start gap-4">
              <div class="w-12 h-12 rounded-2xl bg-brand-50 dark:bg-brand-900/20 flex items-center justify-center flex-shrink-0 text-brand-600">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" /></svg>
              </div>
              <div>
                <h4 class="text-lg font-bold text-gray-900 dark:text-white mb-1">{{ t.contact.emailTitle }}</h4>
                <p class="text-gray-600 dark:text-gray-400">contact@poura.health</p>
              </div>
            </div>
          </div>

          <!-- Contact Form -->
          <div class="bg-white dark:bg-gray-900 p-8 rounded-3xl shadow-xl border border-gray-100 dark:border-gray-800">
            <form class="space-y-4" @submit.prevent="">
              <div>
                <label class="block text-sm font-bold text-gray-700 dark:text-gray-300 mb-1">{{ t.contact.name }}</label>
                <input type="text" class="w-full bg-gray-50 dark:bg-gray-950 border border-gray-200 dark:border-gray-800 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-brand-500/50 transition-all text-gray-900 dark:text-white" />
              </div>
              <div>
                <label class="block text-sm font-bold text-gray-700 dark:text-gray-300 mb-1">{{ t.contact.email }}</label>
                <input type="email" class="w-full bg-gray-50 dark:bg-gray-950 border border-gray-200 dark:border-gray-800 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-brand-500/50 transition-all text-gray-900 dark:text-white" />
              </div>
              <div>
                <label class="block text-sm font-bold text-gray-700 dark:text-gray-300 mb-1">{{ t.contact.message }}</label>
                <textarea rows="4" class="w-full bg-gray-50 dark:bg-gray-950 border border-gray-200 dark:border-gray-800 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-brand-500/50 transition-all resize-none text-gray-900 dark:text-white"></textarea>
              </div>
              <button class="w-full bg-brand-600 text-white rounded-xl px-4 py-3.5 font-bold shadow-md shadow-brand-500/30 hover:bg-brand-700 transition-colors active:scale-95">
                {{ t.contact.send }}
              </button>
            </form>
          </div>
        </div>
      </div>
    </section>

    <!-- 9. FOOTER -->
    <footer class="bg-gray-900 pt-24 pb-12 rounded-t-[3rem] mt-12 text-gray-100">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 mb-16">
          
          <div class="lg:col-span-5">
            <h3 class="text-4xl font-black text-white mb-6">{{ t.footer.title }}</h3>
            <p class="text-gray-400 mb-8 max-w-md">{{ t.footer.desc }}</p>
            <div class="flex max-w-md bg-white/5 p-1.5 rounded-full backdrop-blur-sm border border-white/10 focus-within:border-white/30 transition-colors">
              <input type="email" :placeholder="t.footer.placeholder" class="w-full bg-transparent px-4 py-2 outline-none text-white placeholder-gray-500" />
              <button class="bg-brand-600 text-white px-6 py-2 rounded-full font-bold hover:bg-brand-500 transition-colors">{{ t.footer.sub }}</button>
            </div>
          </div>

          <div class="lg:col-span-2 lg:col-start-8">
            <h4 class="font-bold text-white mb-6 uppercase tracking-wider text-sm">{{ t.footer.links }}</h4>
            <ul class="space-y-4">
              <li><a href="#" class="text-gray-400 hover:text-brand-400 transition-colors">{{ t.nav.home }}</a></li>
              <li><a href="#about" class="text-gray-400 hover:text-brand-400 transition-colors">{{ t.nav.about }}</a></li>
              <li><a href="#specialties" class="text-gray-400 hover:text-brand-400 transition-colors">{{ t.nav.specialties }}</a></li>
              <li><a href="#blog" class="text-gray-400 hover:text-brand-400 transition-colors">{{ t.blog.title }}</a></li>
            </ul>
          </div>

          <div class="lg:col-span-3">
            <h4 class="font-bold text-white mb-6 uppercase tracking-wider text-sm">{{ t.footer.specs }}</h4>
            <ul class="space-y-4">
              <li><a href="#" class="text-gray-400 hover:text-brand-400 transition-colors">Cardiologie</a></li>
              <li><a href="#" class="text-gray-400 hover:text-brand-400 transition-colors">Pédiatrie</a></li>
              <li><a href="#" class="text-gray-400 hover:text-brand-400 transition-colors">Neurologie</a></li>
              <li><a href="#" class="text-gray-400 hover:text-brand-400 transition-colors">Santé Mentale</a></li>
            </ul>
          </div>
        </div>

        <div class="pt-8 border-t border-gray-800 flex flex-col md:flex-row items-center justify-between gap-4">
          <div class="flex items-center gap-2">
            <div class="w-6 h-6 bg-brand-600 rounded-md flex items-center justify-center text-white font-bold text-xs">P</div>
            <span class="font-black tracking-tight text-white">POURA</span>
          </div>
          <div class="flex gap-4">
            <a href="#" class="text-gray-500 hover:text-white transition-colors">Twitter</a>
            <a href="#" class="text-gray-500 hover:text-white transition-colors">LinkedIn</a>
            <a href="#" class="text-gray-500 hover:text-white transition-colors">Instagram</a>
          </div>
          <p class="text-sm text-gray-500 text-center md:text-right">
            &copy; {{ new Date().getFullYear() }} POURA. {{ t.footer.rights }}
          </p>
        </div>
      </div>
    </footer>

  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue'

const isScrolled = ref(false)
const mobileMenuOpen = ref(false)
const activeTab = ref(0)
const currentLang = ref('fr')

const handleScroll = () => {
  isScrolled.value = window.scrollY > 20
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
  document.documentElement.style.scrollBehavior = 'smooth'
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
  document.documentElement.style.scrollBehavior = ''
})

const translations = {
  fr: {
    nav: { home: 'Accueil', about: 'À propos', specialties: 'Spécialités', ecosystem: 'Écosystème', testimonials: 'Témoignages', contact: 'Contact', book: 'Prendre Rendez-vous' },
    hero: { badge: 'Toutes les spécialités couvertes', title: 'Votre Partenaire de Confiance : Le <span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-600 to-blue-light-600">Réseau Santé Intégré</span> Pour Tous.', subtitle: 'POURA unit toutes les spécialités médicales dans une plateforme unique, offrant des soins complets, connectés et humains. De la prévention à la guérison.', cta1: 'Explorer les Services', cta2: 'En savoir plus', satisfaction: 'Satisfaction Patient', findDoc: 'Trouver un spécialiste', spec: 'Spécialité (ex: Cardiologue)', loc: 'Localisation (ex: Paris)', search: 'Rechercher' },
    about: { title: 'À Propos de POURA', heading: 'Connecter les patients et les médecins sans effort.', desc: 'POURA est né d\'une vision simple : la santé doit être accessible, coordonnée et transparente. Nous réunissons toutes les spécialités médicales pour offrir un parcours de soins fluide, de la première consultation au suivi post-opératoire.', specCount: 'Spécialistes', feat1Title: 'Dossier Unifié', feat1Desc: 'Un dossier patient unique partagé entre tous vos spécialistes pour une prise en charge globale.', feat2Title: 'Suivi Multi-spécialités', feat2Desc: 'Coordination immédiate entre cardiologues, généralistes et thérapeutes sur une seule plateforme.' },
    why: { title: 'Pourquoi Nous Choisir', heading: 'Un Chemin Simplifié Vers des Soins Complets.', desc: 'Nous combinons expertise médicale de pointe et technologie intuitive pour transformer l\'expérience de soin.' },
    eco: { title: 'Écosystème', heading: 'Le Modèle de Soin Intégral POURA', desc: 'Notre modèle "Total Care" rassemble médecins, spécialistes, pharmaciens et experts bien-être au même endroit. Du diagnostic au rétablissement, nous créons un réseau de guérison fluide entièrement centré sur vous.', cta: 'Découvrir l\'écosystème' },
    testi: { title: 'Histoires Vraies, Vraies Guérisons', desc: 'Découvrez comment notre plateforme a transformé la vie de nos patients.', patient: 'Patient Régulier' },
    blog: { title: 'Blog', heading: 'Explorez des Insights d\'Experts pour une Vie Plus Saine.', desc: 'Découvrez des conseils d\'experts sur la médecine, le bien-être et les habitudes saines pour vous aider à vivre votre meilleure vie.', readMore: 'Lire la suite' },
    contact: { title: 'Contactez-nous', heading: 'Nous sommes là pour vous aider.', desc: 'Vous avez des questions sur POURA ? N\'hésitez pas à nous contacter. Notre équipe vous répondra dans les plus brefs délais.', name: 'Nom complet', email: 'Adresse email', message: 'Votre message', send: 'Envoyer le message', address: 'Adresse', phone: 'Téléphone', emailTitle: 'Email' },
    footer: { title: 'Prenez une longueur d\'avance sur votre santé.', desc: 'Recevez des conseils de santé, des guides de bien-être et bien plus dans votre boîte de réception.', placeholder: 'Votre adresse email', sub: 'S\'abonner', links: 'Liens Rapides', specs: 'Spécialités', rights: 'Tous droits réservés.' }
  },
  en: {
    nav: { home: 'Home', about: 'About', specialties: 'Specialties', ecosystem: 'Ecosystem', testimonials: 'Testimonials', contact: 'Contact', book: 'Book Appointment' },
    hero: { badge: 'All Specialties Covered', title: 'Your Trusted Partner: The <span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-600 to-blue-light-600">Integrated Healthcare</span> Network For All.', subtitle: 'POURA unites all medical specialties into a single platform, offering comprehensive, connected, and human care. From prevention to healing.', cta1: 'Explore Services', cta2: 'Learn More', satisfaction: 'Patient Satisfaction', findDoc: 'Find a Specialist', spec: 'Specialty (e.g. Cardiologist)', loc: 'Location (e.g. London)', search: 'Search' },
    about: { title: 'About POURA', heading: 'Connecting patients and doctors effortlessly.', desc: 'POURA was born from a simple vision: healthcare should be accessible, coordinated, and transparent. We bring together all medical specialties to offer a seamless care journey, from the first consultation to post-operative follow-up.', specCount: 'Specialists', feat1Title: 'Unified Record', feat1Desc: 'A single patient record shared across all your specialists for comprehensive care.', feat2Title: 'Multi-specialty Tracking', feat2Desc: 'Immediate coordination between cardiologists, general practitioners, and therapists on one platform.' },
    why: { title: 'Why Choose Us', heading: 'A Simplified Path to Comprehensive Care.', desc: 'We combine cutting-edge medical expertise and intuitive technology to transform the care experience.' },
    eco: { title: 'Ecosystem', heading: 'The POURA Total Care Model', desc: 'Our "Total Care" model brings together doctors, specialists, pharmacists, and wellness experts in one place. From diagnosis to recovery, we create a seamless healing network entirely centered on you.', cta: 'Discover the ecosystem' },
    testi: { title: 'Real Stories, Real Healing', desc: 'Discover how our platform has transformed the lives of our patients.', patient: 'Regular Patient' },
    blog: { title: 'Blog', heading: 'Explore Expert Insights for a Healthier Life.', desc: 'Discover expert advice on medicine, wellness, and healthy habits to help you live your best life.', readMore: 'Read more' },
    contact: { title: 'Contact Us', heading: 'We are here to help.', desc: 'Do you have questions about POURA? Do not hesitate to contact us. Our team will get back to you as soon as possible.', name: 'Full Name', email: 'Email address', message: 'Your message', send: 'Send Message', address: 'Address', phone: 'Phone', emailTitle: 'Email' },
    footer: { title: 'Stay ahead of your health journey.', desc: 'Get health tips, wellness guides, and more delivered to your inbox.', placeholder: 'Your email address', sub: 'Subscribe', links: 'Quick Links', specs: 'Specialties', rights: 'All rights reserved.' }
  },
  ar: {
    nav: { home: 'الرئيسية', about: 'معلومات عنا', specialties: 'التخصصات', ecosystem: 'النظام البيئي', testimonials: 'آراء العملاء', contact: 'اتصل بنا', book: 'حجز موعد' },
    hero: { badge: 'جميع التخصصات مشمولة', title: 'شريكك الموثوق: شبكة <span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-600 to-blue-light-600">الرعاية الصحية المتكاملة</span> للجميع.', subtitle: 'توحد بورا جميع التخصصات الطبية في منصة واحدة، وتقدم رعاية شاملة ومتصلة وإنسانية. من الوقاية إلى الشفاء.', cta1: 'استكشاف الخدمات', cta2: 'اعرف المزيد', satisfaction: 'رضا المرضى', findDoc: 'ابحث عن طبيب', spec: 'التخصص (مثل طبيب قلب)', loc: 'الموقع (مثل باريس)', search: 'بحث' },
    about: { title: 'عن بورا', heading: 'ربط المرضى والأطباء بكل سهولة.', desc: 'ولدت بورا من رؤية بسيطة: يجب أن تكون الرعاية الصحية في متناول الجميع ومنسقة وشفافة. نحن نجمع بين جميع التخصصات الطبية لتقديم رحلة رعاية سلسة، من الاستشارة الأولى إلى المتابعة بعد الجراحة.', specCount: 'متخصص', feat1Title: 'سجل موحد', feat1Desc: 'سجل مريض واحد مشترك بين جميع المتخصصين لديك للحصول على رعاية شاملة.', feat2Title: 'متابعة متعددة التخصصات', feat2Desc: 'تنسيق فوري بين أطباء القلب والممارسين العامين والمعالجين على منصة واحدة.' },
    why: { title: 'لماذا تختارنا', heading: 'مسار مبسط لرعاية شاملة.', desc: 'نحن نجمع بين الخبرة الطبية المتطورة والتكنولوجيا البديهية لتحويل تجربة الرعاية.' },
    eco: { title: 'النظام البيئي', heading: 'نموذج بورا للرعاية الشاملة', desc: 'يجمع نموذج "الرعاية الشاملة" الخاص بنا بين الأطباء والمتخصصين والصيادلة وخبراء العافية في مكان واحد. من التشخيص إلى التعافي، ننشئ شبكة شفاء سلسة تتمحور بالكامل حولك.', cta: 'اكتشف النظام البيئي' },
    testi: { title: 'قصص حقيقية، شفاء حقيقي', desc: 'اكتشف كيف غيرت منصتنا حياة مرضانا.', patient: 'مريض دائم' },
    blog: { title: 'المدونة', heading: 'استكشف رؤى الخبراء لحياة أكثر صحة.', desc: 'اكتشف نصائح الخبراء حول الطب والعافية والعادات الصحية لمساعدتك على عيش أفضل حياة.', readMore: 'اقرأ المزيد' },
    contact: { title: 'اتصل بنا', heading: 'نحن هنا للمساعدة.', desc: 'هل لديك أسئلة حول بورا؟ لا تتردد في الاتصال بنا. سيعود فريقنا إليك في أقرب وقت ممكن.', name: 'الاسم الكامل', email: 'عنوان البريد الإلكتروني', message: 'رسالتك', send: 'إرسال الرسالة', address: 'العنوان', phone: 'الهاتف', emailTitle: 'البريد الإلكتروني' },
    footer: { title: 'ابق متقدماً في رحلتك الصحية.', desc: 'احصل على نصائح صحية وأدلة عافية والمزيد مباشرة في بريدك الوارد.', placeholder: 'عنوان بريدك الإلكتروني', sub: 'اشترك', links: 'روابط سريعة', specs: 'التخصصات', rights: 'كل الحقوق محفوظة.' }
  }
}

const t = computed(() => translations[currentLang.value as keyof typeof translations])

const whyUsTabs = {
  fr: [
    { title: 'Compassion', description: 'Nous sommes déterminés à fournir les meilleurs soins médicaux avec sensibilité. Chaque patient est unique et mérite une attention particulière.' },
    { title: 'Collaboration Interdisciplinaire', description: 'Nos spécialistes travaillent ensemble en parfaite synergie. Votre cardiologue communique directement avec votre généraliste via notre plateforme.' },
    { title: 'Transparence', description: 'Des diagnostics clairs, des traitements expliqués en détail et un accès complet à votre dossier médical à tout moment.' },
    { title: 'Flexibilité', description: 'Prise de rendez-vous en quelques clics, consultations en ligne ou en cabinet, selon vos besoins et vos disponibilités.' }
  ],
  en: [
    { title: 'Compassion', description: 'We are committed to providing the best medical care with sensitivity. Every patient is unique and deserves special attention.' },
    { title: 'Interdisciplinary Collaboration', description: 'Our specialists work together in perfect synergy. Your cardiologist communicates directly with your general practitioner via our platform.' },
    { title: 'Transparency', description: 'Clear diagnoses, detailed treatments, and full access to your medical records at any time.' },
    { title: 'Flexibility', description: 'Book appointments in a few clicks, online or in-office consultations, according to your needs and availability.' }
  ],
  ar: [
    { title: 'الرحمة', description: 'نحن ملتزمون بتقديم أفضل رعاية طبية بحساسية. كل مريض فريد ويستحق اهتمامًا خاصًا.' },
    { title: 'التعاون متعدد التخصصات', description: 'يعمل المتخصصون لدينا معًا في تآزر مثالي. يتواصل طبيب القلب الخاص بك مباشرة مع طبيبك العام عبر منصتنا.' },
    { title: 'الشفافية', description: 'تشخيصات واضحة وعلاجات مشروحة بالتفصيل وإمكانية الوصول الكامل إلى سجلاتك الطبية في أي وقت.' },
    { title: 'المرونة', description: 'حجز المواعيد ببضع نقرات، عبر الإنترنت أو في العيادة، وفقًا لاحتياجاتك وتوافرك.' }
  ]
}

const testimonialsData = {
  fr: [
    { title: 'Une équipe bienveillante', body: 'Le personnel a rendu chaque étape facile. Je me suis senti accompagné et confiant concernant mon traitement dès le premier jour.', author: 'Robert Fox', initials: 'RF' },
    { title: 'Expérience fluide', body: 'Fini les heures d\'attente. La coordination entre mon généraliste et mon spécialiste via POURA a été immédiate.', author: 'Cody Fisher', initials: 'CF' },
    { title: 'Soin de haute qualité', body: 'La qualité des médecins sur la plateforme est incroyable. J\'ai enfin pu trouver le spécialiste qu\'il me fallait rapidement.', author: 'Albert Flores', initials: 'AF' }
  ],
  en: [
    { title: 'A caring team', body: 'The staff made every step easy. I felt supported and confident about my treatment from day one.', author: 'Robert Fox', initials: 'RF' },
    { title: 'Seamless experience', body: 'No more waiting hours. The coordination between my GP and specialist via POURA was immediate.', author: 'Cody Fisher', initials: 'CF' },
    { title: 'High quality care', body: 'The quality of doctors on the platform is incredible. I finally found the specialist I needed quickly.', author: 'Albert Flores', initials: 'AF' }
  ],
  ar: [
    { title: 'فريق مهتم', body: 'جعل الموظفون كل خطوة سهلة. شعرت بالدعم والثقة بشأن علاجي منذ اليوم الأول.', author: 'روبرت فوكس', initials: 'RF' },
    { title: 'تجربة سلسة', body: 'لا مزيد من ساعات الانتظار. كان التنسيق بين طبيبي العام والأخصائي عبر بورا فوريًا.', author: 'كودي فيشر', initials: 'CF' },
    { title: 'رعاية عالية الجودة', body: 'جودة الأطباء على المنصة لا تصدق. وجدت أخيرًا الأخصائي الذي أحتاجه بسرعة.', author: 'ألبرت فلوريس', initials: 'AF' }
  ]
}

const blogPostsData = {
  fr: [
    { title: '5 Habitudes Quotidiennes pour un Cœur en Pleine Forme', excerpt: 'Découvrez des gestes simples pour améliorer votre santé cardiovasculaire au quotidien et renforcer votre muscle cardiaque.', date: '12 Oct 2026', image: '/blog_heart_1787418233143.jpg' },
    { title: 'Le Lien Entre Bien-être Mental & Santé Physique', excerpt: 'Comprenez comment le stress affecte votre corps et pourquoi la santé mentale est essentielle pour prévenir les maladies.', date: '28 Sep 2026', image: '/blog_mental_1787418242969.jpg' },
    { title: 'Les Bénéfices des Bilan de Santé Réguliers', excerpt: 'Des examens réguliers peuvent détecter les problèmes tôt. Découvrez quels tests sont recommandés selon votre âge et votre mode de vie.', date: '15 Sep 2026', image: '/blog_fitness_1787418253447.jpg' }
  ],
  en: [
    { title: '5 Daily Habits for a Healthy Heart', excerpt: 'Discover simple actions to improve your daily cardiovascular health and strengthen your heart muscle.', date: '12 Oct 2026', image: '/blog_heart_1787418233143.jpg' },
    { title: 'The Link Between Mental Wellness & Physical Health', excerpt: 'Understand how stress affects your body and why mental health is essential for preventing diseases.', date: '28 Sep 2026', image: '/blog_mental_1787418242969.jpg' },
    { title: 'The Benefits of Regular Health Checkups', excerpt: 'Regular exams can detect problems early. Discover which tests are recommended based on your age and lifestyle.', date: '15 Sep 2026', image: '/blog_fitness_1787418253447.jpg' }
  ],
  ar: [
    { title: '5 عادات يومية لقلب سليم', excerpt: 'اكتشف إجراءات بسيطة لتحسين صحة القلب والأوعية الدموية اليومية وتقوية عضلة القلب.', date: '12 أكتوبر 2026', image: '/blog_heart_1787418233143.jpg' },
    { title: 'الرابط بين العافية العقلية والصحة البدنية', excerpt: 'افهم كيف يؤثر الإجهاد على جسمك ولماذا الصحة العقلية ضرورية للوقاية من الأمراض.', date: '28 سبتمبر 2026', image: '/blog_mental_1787418242969.jpg' },
    { title: 'فوائد الفحوصات الصحية المنتظمة', excerpt: 'يمكن للفحوصات المنتظمة اكتشاف المشاكل مبكرًا. اكتشف الاختبارات الموصى بها بناءً على عمرك ونمط حياتك.', date: '15 سبتمبر 2026', image: '/blog_fitness_1787418253447.jpg' }
  ]
}
</script>
