<template>
  <div
    :dir="currentLang === 'ar' ? 'rtl' : 'ltr'"
    class="min-h-screen bg-gray-50 dark:bg-gray-950 font-figtree selection:bg-brand-500/30 overflow-x-hidden"
  >
    <!-- Navigation -->
    <div class="pt-6 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto relative z-50">
      <nav
        class="bg-[#eef2fc] dark:bg-gray-900 rounded-[2rem] px-6 py-4 flex items-center justify-between shadow-sm border border-gray-100 dark:border-gray-800"
      >
        <div class="flex items-center gap-3">
          <img src="/images/logo/logo.svg" alt="POURA" class="h-8 w-auto dark:hidden" />
          <img src="/images/logo/logo-dark.svg" alt="POURA" class="h-8 w-auto hidden dark:block" />
        </div>
        <div class="hidden md:flex items-center gap-8">
          <a
            href="#"
            class="text-sm font-bold text-gray-900 dark:text-white hover:text-[#00d0ff] transition-colors"
            >{{ t.nav.home }}</a
          >
          <a
            href="#about"
            class="text-sm font-bold text-gray-600 dark:text-gray-300 hover:text-[#00d0ff] transition-colors"
            >{{ t.nav.about }}</a
          >
          <a
            href="#digital-cabinet"
            class="text-sm font-bold text-gray-600 dark:text-gray-300 hover:text-[#00d0ff] transition-colors"
            >{{ t.nav.digital }}</a
          >
          <a
            href="#contact"
            class="text-sm font-bold text-gray-600 dark:text-gray-300 hover:text-[#00d0ff] transition-colors"
            >{{ t.nav.contact }}</a
          >
        </div>
        <div class="flex items-center gap-4">
          <select
            v-model="currentLang"
            class="bg-transparent text-gray-700 dark:text-gray-300 rounded-lg px-2 py-1 text-sm font-bold outline-none cursor-pointer"
          >
            <option value="fr">FR</option>
            <option value="en">EN</option>
            <option value="ar">AR</option>
          </select>
          <router-link
            to="/signin"
            class="hidden sm:inline-flex items-center gap-2 px-6 py-2.5 rounded-full bg-white dark:bg-gray-800 text-gray-900 dark:text-white text-sm font-bold shadow-sm transition-all hover:bg-gray-50 dark:hover:bg-gray-700"
          >
            {{ t.nav.book }}
          </router-link>
        </div>
      </nav>
    </div>

    <!-- Hero Section -->
    <section class="relative pt-12 pb-24 lg:pb-32 bg-white dark:bg-gray-950">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="grid grid-cols-1 xl:grid-cols-2 gap-12 lg:gap-16 items-center">
          <!-- Left side -->
          <div class="hero-content max-w-2xl opacity-0 xl:pr-10">
            <h1
              class="text-5xl sm:text-6xl lg:text-7xl font-black tracking-tight text-gray-900 dark:text-white leading-[1.1] mb-6"
              v-html="t.hero.title"
            ></h1>
            <p
              class="text-lg text-gray-500 dark:text-gray-400 font-medium mb-10 leading-relaxed max-w-lg"
            >
              {{ t.hero.subtitle }}
            </p>

            <!-- Search Bar (Doctolib style) -->
            <div
              class="w-full max-w-4xl bg-white dark:bg-gray-900 rounded-full shadow-2xl p-2 flex flex-col sm:flex-row items-center gap-2 border border-gray-100 dark:border-gray-800"
            >
              <!-- Field 1 -->
              <div
                class="flex-1 flex items-center px-4 py-2 w-full border-b sm:border-b-0 sm:border-r border-gray-100 dark:border-gray-700"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5 text-gray-400 shrink-0"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  stroke-width="2"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                  />
                </svg>
                <input
                  type="text"
                  :placeholder="t.search.placeholder1"
                  class="w-full bg-transparent border-none outline-none focus:ring-0 text-gray-900 dark:text-white placeholder-gray-500 font-medium ml-3"
                />
              </div>

              <!-- Field 2 -->
              <div class="flex-1 flex items-center px-4 py-2 w-full">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5 text-gray-400 shrink-0"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  stroke-width="2"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"
                  />
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"
                  />
                </svg>
                <input
                  type="text"
                  :placeholder="t.search.placeholder2"
                  class="w-full bg-transparent border-none outline-none focus:ring-0 text-gray-900 dark:text-white placeholder-gray-500 font-medium ml-3"
                />
              </div>

              <!-- Button -->
              <button
                class="w-full sm:w-auto px-8 py-3.5 rounded-full bg-[#032b43] hover:bg-[#043d5d] text-white font-bold transition-colors flex items-center justify-center gap-2 shrink-0"
              >
                {{ t.search.button }}
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-4 w-4"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  stroke-width="3"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
                </svg>
              </button>
            </div>
          </div>

          <!-- Right side: Masonry Grid -->

          <!-- Right side: New Modern Hero Image -->
          <div class="hero-image relative w-full opacity-0">
            <div class="relative w-full aspect-[4/3] max-w-2xl ml-auto rounded-[3rem] overflow-hidden shadow-[0_20px_60px_rgba(0,0,0,0.1)] group z-20">
              <!-- Main Image -->
              <img src="/images/hero_main.jpg" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-1000" />
              
              <!-- Subtle gradient overlay -->
              <div class="absolute inset-0 bg-gradient-to-t from-black/40 via-transparent to-transparent pointer-events-none"></div>
              
              <!-- Floating Widget: Trust & Reviews -->
              <div class="absolute bottom-6 left-6 bg-white/70 dark:bg-gray-900/70 backdrop-blur-xl p-4 rounded-2xl shadow-xl border border-white/50 dark:border-gray-800/50 flex items-center gap-4 hover:-translate-y-1 transition-transform duration-300">
                <div class="flex -space-x-2">
                  <img class="w-10 h-10 rounded-full border-2 border-white dark:border-gray-800 object-cover" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100" />
                  <img class="w-10 h-10 rounded-full border-2 border-white dark:border-gray-800 object-cover" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=100" />
                  <img class="w-10 h-10 rounded-full border-2 border-white dark:border-gray-800 object-cover" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100" />
                </div>
                <div>
                  <div class="flex gap-1 text-amber-400">
                    <svg v-for="i in 5" :key="i" class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
                  </div>
                  <p class="text-xs font-bold text-gray-900 dark:text-white mt-1">Excellent 5/5</p>
                </div>
              </div>
              
              <!-- Floating Widget: Quick Action -->
              <div class="absolute top-8 right-6 bg-white/70 dark:bg-gray-900/70 backdrop-blur-xl p-4 rounded-2xl shadow-xl border border-white/50 dark:border-gray-800/50 flex items-center gap-3 hover:-translate-y-1 transition-transform duration-300">
                <div class="w-12 h-12 bg-[#00d0ff] rounded-xl flex items-center justify-center text-white shadow-[0_4px_15px_rgba(0,208,255,0.4)]">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" /></svg>
                </div>
                <div>
                  <p class="text-[11px] text-gray-500 font-medium uppercase tracking-wider">Disponibilité</p>
                  <p class="text-sm font-extrabold text-gray-900 dark:text-white">24/7 Digital</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Nearby Pharmacies Section -->
    <section
      class="py-16 bg-gray-50 dark:bg-gray-950 relative border-t border-gray-100 dark:border-gray-900"
    >
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="flex items-center justify-between mb-8">
          <h2 class="text-2xl sm:text-3xl font-black text-gray-900 dark:text-white">
            {{ t.pharmacies.title }}
          </h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
          <div
            v-for="(pharmacy, i) in pharmacies"
            :key="i"
            class="relative overflow-hidden bg-white/70 dark:bg-gray-900/70 backdrop-blur-xl rounded-[2rem] p-6 shadow-[0_8px_30px_rgb(0,0,0,0.04)] border border-white/80 dark:border-gray-800/50 flex flex-col gap-5 hover:shadow-[0_8px_30px_rgb(0,208,255,0.1)] hover:-translate-y-1.5 transition-all duration-300 group"
          >
            <!-- Decorative gradient blur in background -->
            <div class="absolute -top-24 -right-24 w-48 h-48 bg-[#00d0ff]/10 dark:bg-[#00d0ff]/20 rounded-full blur-3xl opacity-0 group-hover:opacity-100 transition-opacity duration-700 pointer-events-none"></div>

            <!-- Header: Icon & Title -->
            <div class="flex gap-4 items-start relative z-10">
              <div
                class="w-14 h-14 rounded-2xl bg-gradient-to-br from-green-50 to-green-100/50 dark:from-green-900/40 dark:to-green-900/10 text-green-600 dark:text-green-400 flex items-center justify-center shrink-0 border border-green-200/50 dark:border-green-800/50 shadow-inner group-hover:scale-105 transition-transform duration-300"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-7 w-7"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  stroke-width="2"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"
                  />
                </svg>
              </div>
              <div class="flex-1 pt-1">
                <h3 class="text-lg font-extrabold text-gray-900 dark:text-white leading-tight mb-1.5 group-hover:text-[#00d0ff] transition-colors line-clamp-2">
                  {{ pharmacy.name }}
                </h3>
                <div class="flex items-center text-sm font-medium text-gray-500 dark:text-gray-400 gap-1.5">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-4 w-4"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    stroke-width="2"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"
                    />
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"
                    />
                  </svg>
                  <span>{{ pharmacy.distance }} km {{ t.pharmacies.distance }}</span>
                </div>
              </div>
            </div>

            <!-- Status -->
            <div class="flex items-center justify-between bg-gray-50/50 dark:bg-gray-800/30 rounded-xl p-3 border border-gray-100/50 dark:border-gray-800/50 relative z-10">
              <span
                v-if="pharmacy.isOpen"
                class="inline-flex items-center gap-2 text-xs font-bold text-green-700 dark:text-green-400"
              >
                <span class="w-2 h-2 rounded-full bg-green-500 animate-[pulse_2s_ease-in-out_infinite]"></span>
                {{ t.pharmacies.openNow }}
              </span>
              <span
                v-else
                class="inline-flex items-center gap-2 text-xs font-bold text-red-600 dark:text-red-400"
              >
                <span class="w-2 h-2 rounded-full bg-red-500"></span>
                Fermé
              </span>
              <span class="text-xs font-semibold text-gray-500">
                {{ t.pharmacies.closesAt }} 2{{ (i % 4) + 1 }}:00
              </span>
            </div>

            <!-- Actions -->
            <div class="grid grid-cols-2 gap-3 mt-auto relative z-10">
              <a
                :href="'https://www.google.com/maps/search/?api=1&query=' + pharmacy.lat + ',' + pharmacy.lon"
                target="_blank"
                class="flex items-center justify-center gap-2 py-2.5 rounded-xl bg-gray-100/80 hover:bg-gray-200 dark:bg-gray-800/80 dark:hover:bg-gray-700 text-gray-700 dark:text-white text-sm font-bold transition-all active:scale-95 group/btn"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-4 w-4 text-gray-500 dark:text-gray-400 group-hover/btn:text-gray-900 dark:group-hover/btn:text-white transition-colors"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  stroke-width="2"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7" />
                </svg>
                Map
              </a>
              <a
                href="tel:123456789"
                class="flex items-center justify-center gap-2 py-2.5 rounded-xl bg-[#00d0ff] hover:bg-[#00b8e6] text-white shadow-lg shadow-[#00d0ff]/25 hover:shadow-[#00d0ff]/40 text-sm font-bold transition-all active:scale-95 group/call"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-4 w-4 group-hover/call:animate-bounce"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  stroke-width="2"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                </svg>
                {{ t.pharmacies.call }}
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- About Our Company Section -->
    <section id="about-company" class="py-24 bg-white dark:bg-gray-950 relative overflow-hidden">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
          <!-- Left Content -->
          <div>
            <h2
              class="text-3xl sm:text-4xl lg:text-5xl font-black text-gray-900 dark:text-white leading-tight mb-8"
            >
              {{ t.aboutCompany.title }}
            </h2>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-8">
              <!-- Item 1 -->
              <div>
                <div class="flex items-center gap-3 mb-3">
                  <div
                    class="w-8 h-8 rounded-full bg-[#eef2fc] dark:bg-gray-800 flex items-center justify-center text-[#00d0ff]"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="h-4 w-4"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                      stroke-width="3"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        d="M14 5l7 7m0 0l-7 7m7-7H3"
                      />
                    </svg>
                  </div>
                  <h4 class="text-xl font-bold text-gray-900 dark:text-white">
                    {{ t.aboutCompany.point1Title }}
                  </h4>
                </div>
                <p class="text-gray-500 dark:text-gray-400 text-sm leading-relaxed">
                  {{ t.aboutCompany.point1Desc }}
                </p>
              </div>

              <!-- Item 2 -->
              <div>
                <div class="flex items-center gap-3 mb-3">
                  <div
                    class="w-8 h-8 rounded-full bg-[#eef2fc] dark:bg-gray-800 flex items-center justify-center text-[#00d0ff]"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="h-4 w-4"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                      stroke-width="3"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        d="M14 5l7 7m0 0l-7 7m7-7H3"
                      />
                    </svg>
                  </div>
                  <h4 class="text-xl font-bold text-gray-900 dark:text-white">
                    {{ t.aboutCompany.point2Title }}
                  </h4>
                </div>
                <p class="text-gray-500 dark:text-gray-400 text-sm leading-relaxed">
                  {{ t.aboutCompany.point2Desc }}
                </p>
              </div>

              <!-- Item 3 -->
              <div>
                <div class="flex items-center gap-3 mb-3">
                  <div
                    class="w-8 h-8 rounded-full bg-[#eef2fc] dark:bg-gray-800 flex items-center justify-center text-[#00d0ff]"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="h-4 w-4"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                      stroke-width="3"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        d="M14 5l7 7m0 0l-7 7m7-7H3"
                      />
                    </svg>
                  </div>
                  <h4 class="text-xl font-bold text-gray-900 dark:text-white">
                    {{ t.aboutCompany.point3Title }}
                  </h4>
                </div>
                <p class="text-gray-500 dark:text-gray-400 text-sm leading-relaxed">
                  {{ t.aboutCompany.point3Desc }}
                </p>
              </div>

              <!-- Item 4 -->
              <div>
                <div class="flex items-center gap-3 mb-3">
                  <div
                    class="w-8 h-8 rounded-full bg-[#eef2fc] dark:bg-gray-800 flex items-center justify-center text-[#00d0ff]"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="h-4 w-4"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                      stroke-width="3"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        d="M14 5l7 7m0 0l-7 7m7-7H3"
                      />
                    </svg>
                  </div>
                  <h4 class="text-xl font-bold text-gray-900 dark:text-white">
                    {{ t.aboutCompany.point4Title }}
                  </h4>
                </div>
                <p class="text-gray-500 dark:text-gray-400 text-sm leading-relaxed">
                  {{ t.aboutCompany.point4Desc }}
                </p>
              </div>
            </div>
          </div>

          <!-- Right Image & Stats -->
          <div class="relative mt-10 lg:mt-0">
            <div class="rounded-3xl overflow-hidden shadow-2xl">
              <img
                src="/images/doctor_with_patients.png"
                alt="Team of Doctors"
                class="w-full h-auto object-cover"
              />
            </div>

            <!-- Floating Stats Cards -->
            <div
              class="absolute -bottom-8 left-1/2 -translate-x-1/2 w-[90%] sm:w-[110%] grid grid-cols-3 gap-2 sm:gap-4 z-20"
            >
              <div
                class="bg-[#eefcfc] dark:bg-gray-800 rounded-2xl p-4 text-center shadow-lg border border-white dark:border-gray-700"
              >
                <h3 class="text-2xl sm:text-3xl font-black text-gray-900 dark:text-white mb-1">
                  20K
                </h3>
                <p class="text-xs sm:text-sm font-medium text-gray-600 dark:text-gray-400">
                  {{ t.aboutCompany.stat1 }}
                </p>
              </div>
              <div
                class="bg-[#eefcfc] dark:bg-gray-800 rounded-2xl p-4 text-center shadow-lg border border-white dark:border-gray-700"
              >
                <h3 class="text-2xl sm:text-3xl font-black text-gray-900 dark:text-white mb-1">
                  120K
                </h3>
                <p class="text-xs sm:text-sm font-medium text-gray-600 dark:text-gray-400">
                  {{ t.aboutCompany.stat2 }}
                </p>
              </div>
              <div
                class="bg-[#eefcfc] dark:bg-gray-800 rounded-2xl p-4 text-center shadow-lg border border-white dark:border-gray-700"
              >
                <h3 class="text-2xl sm:text-3xl font-black text-gray-900 dark:text-white mb-1">
                  70+
                </h3>
                <p class="text-xs sm:text-sm font-medium text-gray-600 dark:text-gray-400">
                  {{ t.aboutCompany.stat3 }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Treatments / Features Section -->
    <section id="treatments" class="py-32 bg-gray-50 dark:bg-gray-900 relative">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-16">
          <div>
            <h2 class="text-sm font-bold text-[#00d0ff] mb-3">{{ t.treatments.badge }}</h2>
            <h3 class="text-3xl sm:text-4xl font-black text-gray-900 dark:text-white">
              {{ t.treatments.title }}
            </h3>
          </div>
          <div class="max-w-md">
            <p class="text-sm text-gray-500 dark:text-gray-400 leading-relaxed">
              {{ t.treatments.desc }}
            </p>
          </div>
          <div>
            <router-link
              to="/signin"
              class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#00d0ff] hover:bg-[#00bce6] text-white font-bold transition-colors"
            >
              {{ t.treatments.viewAll }}
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-4 w-4"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                stroke-width="2"
              >
                <path stroke-linecap="round" stroke-linejoin="round" d="M14 5l7 7m0 0l-7 7m7-7H3" />
              </svg>
            </router-link>
          </div>
        </div>

        <div class="w-full">
          <swiper
            :slidesPerView="1.2"
            :spaceBetween="20"
            :loop="true"
            :autoplay="{ delay: 3000, disableOnInteraction: false }"
            :breakpoints="{
              '640': { slidesPerView: 2, spaceBetween: 20 },
              '1024': { slidesPerView: 4, spaceBetween: 30 },
            }"
            :modules="swiperModules"
            class="pb-12"
          >
            <!-- Card 1 -->
            <swiper-slide v-for="(feat, index) in t.treatments.items" :key="index" class="h-auto py-6">
              <div
                class="group h-full bg-white/60 dark:bg-gray-800/60 backdrop-blur-2xl rounded-3xl p-4 shadow-[0_8px_30px_rgb(0,0,0,0.04)] dark:shadow-[0_8px_30px_rgb(0,0,0,0.2)] border border-white/80 dark:border-gray-700/50 flex flex-col hover:-translate-y-4 hover:scale-[1.02] hover:shadow-[0_20px_40px_rgba(0,208,255,0.15)] transition-all duration-500"
              >
                <!-- Image with Icon overlay -->
                <div class="w-full h-48 rounded-2xl overflow-hidden mb-6 relative shadow-inner">
                  <img :src="feat.img" :alt="feat.title" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" />
                  <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent"></div>
                  
                  <!-- Floating Glass Icon -->
                  <div class="absolute bottom-4 left-4 w-12 h-12 bg-white/30 dark:bg-black/30 backdrop-blur-md rounded-xl flex items-center justify-center text-white border border-white/40 shadow-lg group-hover:-translate-y-1 group-hover:bg-[#00d0ff]/90 transition-all duration-300">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="h-6 w-6"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                      stroke-width="1.5"
                      v-html="feat.svg"
                    ></svg>
                  </div>
                </div>

                <div class="px-2 flex flex-col flex-grow">
                  <h4 class="text-xl font-bold text-gray-900 dark:text-white mb-3">
                    {{ feat.title }}
                  </h4>
                  <p class="text-sm text-gray-500 dark:text-gray-400 leading-relaxed mb-6 flex-grow">
                    {{ feat.desc }}
                  </p>
                  <router-link
                  to="/signin"
                  class="inline-flex items-center justify-center px-4 py-1.5 rounded-md bg-[#00d0ff] text-white text-xs font-bold w-fit hover:bg-[#00bce6] transition-colors"
                >
                  {{ t.treatments.readMore }}
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-3 w-3 ml-1"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    stroke-width="2"
                  >
                    <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
                  </svg>
                </router-link>
                </div>
              </div>
            </swiper-slide>
          </swiper>
        </div>
      </div>
    </section>

    <!-- Work Process Section -->
    <section class="py-24 bg-white dark:bg-gray-950">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <p class="text-sm font-bold text-gray-500 dark:text-gray-400 mb-2">
            {{ t.process.badge }}
          </p>
          <h2 class="text-3xl sm:text-4xl font-black text-gray-900 dark:text-white">
            {{ t.process.title }}
          </h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 lg:gap-8">
          <!-- Step 1 -->
          <div
            class="relative overflow-hidden bg-white/60 dark:bg-gray-900/60 backdrop-blur-xl rounded-[2.5rem] p-8 text-center shadow-[0_8px_30px_rgb(0,0,0,0.04)] dark:shadow-[0_8px_30px_rgb(0,0,0,0.2)] border border-white/80 dark:border-gray-800/50 hover:shadow-[0_20px_40px_rgb(0,208,255,0.15)] hover:-translate-y-2 transition-all duration-500 group"
          >
            <!-- Shimmer Effect -->
            <div class="absolute inset-0 -translate-x-[150%] group-hover:translate-x-[150%] transition-transform duration-[1.5s] ease-in-out pointer-events-none z-20">
              <div class="w-1/2 h-full bg-gradient-to-r from-transparent via-white/50 dark:via-white/10 to-transparent skew-x-12"></div>
            </div>
            
            <!-- Decorative Glow -->
            <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-40 h-40 bg-[#00d0ff]/10 dark:bg-[#00d0ff]/20 rounded-full blur-3xl opacity-0 group-hover:opacity-100 transition-opacity duration-700 pointer-events-none"></div>

            <!-- Number Badge -->
            <div class="absolute top-6 left-6 w-10 h-10 rounded-2xl bg-white/90 dark:bg-gray-800/90 backdrop-blur-md border border-gray-100 dark:border-gray-700 flex items-center justify-center text-lg font-black text-gray-900 dark:text-white shadow-sm z-10 group-hover:text-white group-hover:bg-[#00d0ff] group-hover:border-[#00d0ff] group-hover:scale-110 transition-all duration-300">
              1
            </div>

            <!-- Image Wrapper -->
            <div class="relative w-full h-48 mx-auto rounded-[2rem] overflow-hidden mb-8 border border-white/50 shadow-inner group-hover:shadow-[0_10px_30px_rgba(0,208,255,0.2)] transition-all duration-500 z-10">
              <img src="/images/process/process_appointment.jpg" alt="Step 1" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/50 via-transparent to-transparent"></div>
              
              <!-- Floating Icon -->
              <div class="absolute bottom-4 right-4 w-12 h-12 bg-white/30 dark:bg-black/30 backdrop-blur-md rounded-xl flex items-center justify-center text-white border border-white/40 shadow-lg group-hover:-translate-y-1 group-hover:bg-[#00d0ff]/90 transition-all duration-300">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                </svg>
              </div>
            </div>
            
            <h4 class="text-2xl font-extrabold text-gray-900 dark:text-white mb-4 relative z-10 group-hover:text-[#00d0ff] transition-colors duration-300">
              {{ t.process.step1Title }}
            </h4>
            <p class="text-sm font-medium text-gray-500 dark:text-gray-400 leading-relaxed relative z-10">
              {{ t.process.step1Desc }}
            </p>
          </div>

          <!-- Step 2 -->
          <div
            class="relative overflow-hidden bg-white/60 dark:bg-gray-900/60 backdrop-blur-xl rounded-[2.5rem] p-8 text-center shadow-[0_8px_30px_rgb(0,0,0,0.04)] dark:shadow-[0_8px_30px_rgb(0,0,0,0.2)] border border-white/80 dark:border-gray-800/50 hover:shadow-[0_20px_40px_rgb(0,208,255,0.15)] hover:-translate-y-2 transition-all duration-500 group"
          >
            <!-- Shimmer Effect -->
            <div class="absolute inset-0 -translate-x-[150%] group-hover:translate-x-[150%] transition-transform duration-[1.5s] ease-in-out pointer-events-none z-20" style="transition-delay: 0.1s">
              <div class="w-1/2 h-full bg-gradient-to-r from-transparent via-white/50 dark:via-white/10 to-transparent skew-x-12"></div>
            </div>
            
            <!-- Decorative Glow -->
            <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-40 h-40 bg-[#00d0ff]/10 dark:bg-[#00d0ff]/20 rounded-full blur-3xl opacity-0 group-hover:opacity-100 transition-opacity duration-700 pointer-events-none"></div>

            <!-- Number Badge -->
            <div class="absolute top-6 left-6 w-10 h-10 rounded-2xl bg-white/90 dark:bg-gray-800/90 backdrop-blur-md border border-gray-100 dark:border-gray-700 flex items-center justify-center text-lg font-black text-gray-900 dark:text-white shadow-sm z-10 group-hover:text-white group-hover:bg-[#00d0ff] group-hover:border-[#00d0ff] group-hover:scale-110 transition-all duration-300">
              2
            </div>

            <!-- Image Wrapper -->
            <div class="relative w-full h-48 mx-auto rounded-[2rem] overflow-hidden mb-8 border border-white/50 shadow-inner group-hover:shadow-[0_10px_30px_rgba(0,208,255,0.2)] transition-all duration-500 z-10">
              <img src="/images/process/process_doctor.jpg" alt="Step 2" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/50 via-transparent to-transparent"></div>
              
              <!-- Floating Icon -->
              <div class="absolute bottom-4 right-4 w-12 h-12 bg-white/30 dark:bg-black/30 backdrop-blur-md rounded-xl flex items-center justify-center text-white border border-white/40 shadow-lg group-hover:-translate-y-1 group-hover:bg-[#00d0ff]/90 transition-all duration-300">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                </svg>
              </div>
            </div>
            
            <h4 class="text-2xl font-extrabold text-gray-900 dark:text-white mb-4 relative z-10 group-hover:text-[#00d0ff] transition-colors duration-300">
              {{ t.process.step2Title }}
            </h4>
            <p class="text-sm font-medium text-gray-500 dark:text-gray-400 leading-relaxed relative z-10">
              {{ t.process.step2Desc }}
            </p>
          </div>

          <!-- Step 3 -->
          <div
            class="relative overflow-hidden bg-white/60 dark:bg-gray-900/60 backdrop-blur-xl rounded-[2.5rem] p-8 text-center shadow-[0_8px_30px_rgb(0,0,0,0.04)] dark:shadow-[0_8px_30px_rgb(0,0,0,0.2)] border border-white/80 dark:border-gray-800/50 hover:shadow-[0_20px_40px_rgb(0,208,255,0.15)] hover:-translate-y-2 transition-all duration-500 group"
          >
            <!-- Shimmer Effect -->
            <div class="absolute inset-0 -translate-x-[150%] group-hover:translate-x-[150%] transition-transform duration-[1.5s] ease-in-out pointer-events-none z-20" style="transition-delay: 0.2s">
              <div class="w-1/2 h-full bg-gradient-to-r from-transparent via-white/50 dark:via-white/10 to-transparent skew-x-12"></div>
            </div>
            
            <!-- Decorative Glow -->
            <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-40 h-40 bg-[#00d0ff]/10 dark:bg-[#00d0ff]/20 rounded-full blur-3xl opacity-0 group-hover:opacity-100 transition-opacity duration-700 pointer-events-none"></div>

            <!-- Number Badge -->
            <div class="absolute top-6 left-6 w-10 h-10 rounded-2xl bg-white/90 dark:bg-gray-800/90 backdrop-blur-md border border-gray-100 dark:border-gray-700 flex items-center justify-center text-lg font-black text-gray-900 dark:text-white shadow-sm z-10 group-hover:text-white group-hover:bg-[#00d0ff] group-hover:border-[#00d0ff] group-hover:scale-110 transition-all duration-300">
              3
            </div>

            <!-- Image Wrapper -->
            <div class="relative w-full h-48 mx-auto rounded-[2rem] overflow-hidden mb-8 border border-white/50 shadow-inner group-hover:shadow-[0_10px_30px_rgba(0,208,255,0.2)] transition-all duration-500 z-10">
              <img src="/images/process/process_solution.jpg" alt="Step 3" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/50 via-transparent to-transparent"></div>
              
              <!-- Floating Icon -->
              <div class="absolute bottom-4 right-4 w-12 h-12 bg-white/30 dark:bg-black/30 backdrop-blur-md rounded-xl flex items-center justify-center text-white border border-white/40 shadow-lg group-hover:-translate-y-1 group-hover:bg-[#00d0ff]/90 transition-all duration-300">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
            </div>
            
            <h4 class="text-2xl font-extrabold text-gray-900 dark:text-white mb-4 relative z-10 group-hover:text-[#00d0ff] transition-colors duration-300">
              {{ t.process.step3Title }}
            </h4>
            <p class="text-sm font-medium text-gray-500 dark:text-gray-400 leading-relaxed relative z-10">
              {{ t.process.step3Desc }}
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Reviews Section -->
    <section class="py-16 bg-white dark:bg-gray-950">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between mb-10">
          <h2 class="text-3xl font-black text-gray-900 dark:text-white">{{ t.reviews.title }}</h2>
          <div class="flex gap-2">
            <button
              class="w-10 h-10 rounded-full border border-gray-200 dark:border-gray-700 flex items-center justify-center hover:bg-gray-50 dark:hover:bg-gray-800 text-gray-600 dark:text-gray-300 transition-colors"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M15 19l-7-7 7-7"
                />
              </svg>
            </button>
            <button
              class="w-10 h-10 rounded-full bg-[#00d0ff] hover:bg-[#00bce6] flex items-center justify-center text-white shadow-md transition-colors"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M9 5l7 7-7 7"
                />
              </svg>
            </button>
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <!-- Review 1 -->
          <div
            class="bg-gray-50 dark:bg-gray-900 rounded-3xl flex flex-col sm:flex-row overflow-hidden shadow-sm border border-gray-100 dark:border-gray-800"
          >
            <div class="w-full sm:w-2/5 h-48 sm:h-auto shrink-0">
              <img
                src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400"
                alt="Patient"
                class="w-full h-full object-cover"
              />
            </div>
            <div class="p-6 sm:p-8 flex flex-col relative">
              <svg
                class="absolute bottom-4 right-4 w-16 h-16 text-gray-200 dark:text-gray-800"
                fill="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  d="M14.017 21v-7.391c0-5.704 3.731-9.57 8.983-10.609l.995 2.151c-2.432.917-3.995 3.638-3.995 5.849h4v10h-9.983zm-14.017 0v-7.391c0-5.704 3.748-9.57 9-10.609l.996 2.151c-2.433.917-3.996 3.638-3.996 5.849h3.983v10h-9.983z"
                />
              </svg>
              <div class="flex gap-1 mb-3">
                <svg
                  v-for="i in 5"
                  :key="i"
                  class="w-4 h-4 text-yellow-400"
                  fill="currentColor"
                  viewBox="0 0 20 20"
                >
                  <path
                    d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
                  ></path>
                </svg>
              </div>
              <p
                class="text-sm text-gray-600 dark:text-gray-400 leading-relaxed mb-6 italic relative z-10"
              >
                "{{ t.reviews.rev1Desc }}"
              </p>
              <div class="mt-auto relative z-10">
                <h5 class="font-bold text-gray-900 dark:text-white">{{ t.reviews.rev1Name }}</h5>
                <p class="text-xs text-gray-500 dark:text-gray-400">{{ t.reviews.rev1Role }}</p>
              </div>
            </div>
          </div>

          <!-- Review 2 -->
          <div
            class="bg-gray-50 dark:bg-gray-900 rounded-3xl flex flex-col sm:flex-row overflow-hidden shadow-sm border border-gray-100 dark:border-gray-800"
          >
            <div class="w-full sm:w-2/5 h-48 sm:h-auto shrink-0">
              <img
                src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=400"
                alt="Patient"
                class="w-full h-full object-cover"
              />
            </div>
            <div class="p-6 sm:p-8 flex flex-col relative">
              <svg
                class="absolute bottom-4 right-4 w-16 h-16 text-gray-200 dark:text-gray-800"
                fill="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  d="M14.017 21v-7.391c0-5.704 3.731-9.57 8.983-10.609l.995 2.151c-2.432.917-3.995 3.638-3.995 5.849h4v10h-9.983zm-14.017 0v-7.391c0-5.704 3.748-9.57 9-10.609l.996 2.151c-2.433.917-3.996 3.638-3.996 5.849h3.983v10h-9.983z"
                />
              </svg>
              <div class="flex gap-1 mb-3">
                <svg
                  v-for="i in 5"
                  :key="i"
                  class="w-4 h-4 text-yellow-400"
                  fill="currentColor"
                  viewBox="0 0 20 20"
                >
                  <path
                    d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
                  ></path>
                </svg>
              </div>
              <p
                class="text-sm text-gray-600 dark:text-gray-400 leading-relaxed mb-6 italic relative z-10"
              >
                "{{ t.reviews.rev2Desc }}"
              </p>
              <div class="mt-auto relative z-10">
                <h5 class="font-bold text-gray-900 dark:text-white">{{ t.reviews.rev2Name }}</h5>
                <p class="text-xs text-gray-500 dark:text-gray-400">{{ t.reviews.rev2Role }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQ Section -->
    <section class="py-24 bg-white dark:bg-gray-950">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
          <!-- FAQ Left -->
          <div>
            <h2 class="text-3xl sm:text-4xl font-black text-gray-900 dark:text-white mb-3">
              {{ t.faq.title }}
            </h2>
            <p class="text-gray-500 dark:text-gray-400 mb-10">{{ t.faq.subtitle }}</p>

            <div class="space-y-4">
              <!-- Item 1 -->
              <div class="border-b border-gray-200 dark:border-gray-800 pb-4">
                <button class="w-full flex items-center justify-between text-left group">
                  <span
                    class="text-sm font-bold text-gray-900 dark:text-white group-hover:text-[#00d0ff] transition-colors"
                    >{{ t.faq.q1 }}</span
                  >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5 text-gray-400 group-hover:text-[#00d0ff]"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M20 12H4"
                    />
                  </svg>
                </button>
                <p class="mt-4 text-sm text-gray-500 dark:text-gray-400 leading-relaxed pr-6">
                  {{ t.faq.a1 }}
                </p>
              </div>

              <!-- Item 2 -->
              <div class="border-b border-gray-200 dark:border-gray-800 pb-4">
                <button class="w-full flex items-center justify-between text-left group">
                  <span
                    class="text-sm font-bold text-gray-900 dark:text-white group-hover:text-[#00d0ff] transition-colors"
                    >{{ t.faq.q2 }}</span
                  >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5 text-gray-400 group-hover:text-[#00d0ff]"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M12 4v16m8-8H4"
                    />
                  </svg>
                </button>
              </div>

              <!-- Item 3 -->
              <div class="border-b border-gray-200 dark:border-gray-800 pb-4">
                <button class="w-full flex items-center justify-between text-left group">
                  <span
                    class="text-sm font-bold text-gray-900 dark:text-white group-hover:text-[#00d0ff] transition-colors"
                    >{{ t.faq.q3 }}</span
                  >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5 text-gray-400 group-hover:text-[#00d0ff]"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M12 4v16m8-8H4"
                    />
                  </svg>
                </button>
              </div>

              <!-- Item 4 -->
              <div class="border-b border-gray-200 dark:border-gray-800 pb-4">
                <button class="w-full flex items-center justify-between text-left group">
                  <span
                    class="text-sm font-bold text-gray-900 dark:text-white group-hover:text-[#00d0ff] transition-colors"
                    >{{ t.faq.q4 }}</span
                  >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5 text-gray-400 group-hover:text-[#00d0ff]"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M12 4v16m8-8H4"
                    />
                  </svg>
                </button>
              </div>
            </div>
          </div>

          <!-- FAQ Right Image Collage -->
          <div class="relative mt-8 lg:mt-0 lg:ml-10">
            <div
              class="absolute top-0 right-0 w-64 h-64 border-[16px] border-[#00d0ff]/20 rounded-full -translate-y-8 translate-x-8 z-0"
            ></div>
            <div
              class="relative z-10 w-4/5 h-[450px] bg-gray-200 rounded-3xl overflow-hidden shadow-xl"
            >
              <img
                src="https://images.unsplash.com/photo-1582750433449-648ed127bb54?w=600"
                alt="Doctor"
                class="w-full h-full object-cover"
              />
            </div>
            <div
              class="absolute bottom-8 right-0 z-20 w-3/5 h-[300px] bg-gray-200 rounded-3xl overflow-hidden shadow-2xl border-4 border-white dark:border-gray-950"
            >
              <img
                src="https://images.unsplash.com/photo-1638202993928-7267aad84c31?w=600"
                alt="Nurses"
                class="w-full h-full object-cover"
              />
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Banner Section -->
    <section class="py-10 bg-white dark:bg-gray-950">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div
          class="bg-[#0b1120] rounded-[2rem] p-8 md:p-12 flex flex-col md:flex-row items-center justify-between gap-8 shadow-2xl relative overflow-hidden"
        >
          <div
            class="absolute top-0 left-0 w-64 h-64 bg-blue-500/10 rounded-full blur-3xl -translate-y-1/2 -translate-x-1/2"
          ></div>

          <div class="relative z-10">
            <p class="text-sm font-bold text-gray-400 mb-2">{{ t.banner.subtitle }}</p>
            <h2 class="text-3xl md:text-5xl font-black text-white">{{ t.banner.title }}</h2>
          </div>

          <div class="relative z-10 flex flex-col sm:flex-row items-center gap-6">
            <div class="flex items-center gap-4 border-r border-gray-700 pr-6 hidden sm:flex">
              <div
                class="w-12 h-12 rounded-full border border-gray-600 flex items-center justify-center text-white"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  stroke-width="2"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"
                  />
                </svg>
              </div>
              <div>
                <p class="text-xs text-gray-400 mb-1">{{ t.banner.call }}</p>
                <div class="flex flex-col gap-1">
                  <a href="tel:+213552171158" class="text-lg font-bold text-white hover:text-[#00d0ff] transition-colors leading-none">+213 552 17 11 58</a>
                  <a href="tel:+213672302733" class="text-lg font-bold text-white hover:text-[#00d0ff] transition-colors leading-none">+213 672 30 27 33</a>
                </div>
              </div>
            </div>
            <router-link
              to="/signin"
              class="px-8 py-4 rounded-xl bg-[#00d0ff] hover:bg-[#00bce6] text-white font-bold transition-colors w-full sm:w-auto text-center"
            >
              {{ t.banner.btn }}
            </router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- Blogs Section -->
    <section class="py-24 bg-gray-50 dark:bg-gray-900">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-12">
          <div>
            <p class="text-sm font-bold text-gray-500 dark:text-gray-400 mb-2">
              {{ t.blogs.badge }}
            </p>
            <h2 class="text-3xl sm:text-4xl font-black text-gray-900 dark:text-white">
              {{ t.blogs.title }}
            </h2>
          </div>
          <div class="max-w-xl">
            <p class="text-sm text-gray-500 dark:text-gray-400 leading-relaxed">
              {{ t.blogs.desc }}
            </p>
          </div>
          <div class="flex gap-2">
            <button
              class="w-10 h-10 rounded-full border border-gray-200 dark:border-gray-700 flex items-center justify-center hover:bg-gray-200 dark:hover:bg-gray-800 text-gray-600 dark:text-gray-300 transition-colors"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M15 19l-7-7 7-7"
                />
              </svg>
            </button>
            <button
              class="w-10 h-10 rounded-full bg-[#00d0ff] hover:bg-[#00bce6] flex items-center justify-center text-white shadow-md transition-colors"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M9 5l7 7-7 7"
                />
              </svg>
            </button>
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <!-- Blog 1 -->
          <div
            class="bg-white dark:bg-gray-800 rounded-3xl overflow-hidden shadow-lg border border-gray-100 dark:border-gray-700 group flex flex-col h-full"
          >
            <div class="h-56 overflow-hidden">
              <img
                src="https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=600"
                alt="Blog"
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
              />
            </div>
            <div class="p-6 flex flex-col flex-grow">
              <div
                class="flex items-center gap-4 text-xs font-bold text-gray-500 dark:text-gray-400 mb-4 border-b border-gray-100 dark:border-gray-700 pb-4"
              >
                <div class="flex items-center gap-1.5">
                  <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                    />
                  </svg>
                  By Admin
                </div>
                <div class="flex items-center gap-1.5">
                  <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
                    />
                  </svg>
                  23 Jun 2024
                </div>
              </div>
              <h4 class="text-xl font-bold text-gray-900 dark:text-white mb-3 leading-snug">
                {{ t.blogs.b1Title }}
              </h4>
              <p class="text-sm text-gray-500 dark:text-gray-400 leading-relaxed mb-6 flex-grow">
                {{ t.blogs.b1Desc }}
              </p>
              <router-link
                to="#"
                class="inline-flex items-center justify-center px-4 py-1.5 rounded-md bg-[#00d0ff] text-white text-xs font-bold w-fit hover:bg-[#00bce6] transition-colors"
              >
                {{ t.treatments.readMore }}
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-3 w-3 ml-1"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  stroke-width="2"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
                </svg>
              </router-link>
            </div>
          </div>

          <!-- Blog 2 -->
          <div
            class="bg-white dark:bg-gray-800 rounded-3xl overflow-hidden shadow-lg border border-gray-100 dark:border-gray-700 group flex flex-col h-full"
          >
            <div class="h-56 overflow-hidden">
              <img
                src="https://images.unsplash.com/photo-1505751172876-fa1923c5c528?w=600"
                alt="Blog"
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
              />
            </div>
            <div class="p-6 flex flex-col flex-grow">
              <div
                class="flex items-center gap-4 text-xs font-bold text-gray-500 dark:text-gray-400 mb-4 border-b border-gray-100 dark:border-gray-700 pb-4"
              >
                <div class="flex items-center gap-1.5">
                  <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                    />
                  </svg>
                  By Dr. Smith
                </div>
                <div class="flex items-center gap-1.5">
                  <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
                    />
                  </svg>
                  21 Jun 2024
                </div>
              </div>
              <h4 class="text-xl font-bold text-gray-900 dark:text-white mb-3 leading-snug">
                {{ t.blogs.b2Title }}
              </h4>
              <p class="text-sm text-gray-500 dark:text-gray-400 leading-relaxed mb-6 flex-grow">
                {{ t.blogs.b2Desc }}
              </p>
              <router-link
                to="#"
                class="inline-flex items-center justify-center px-4 py-1.5 rounded-md bg-[#00d0ff] text-white text-xs font-bold w-fit hover:bg-[#00bce6] transition-colors"
              >
                {{ t.treatments.readMore }}
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-3 w-3 ml-1"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  stroke-width="2"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
                </svg>
              </router-link>
            </div>
          </div>

          <!-- Blog 3 -->
          <div
            class="bg-white dark:bg-gray-800 rounded-3xl overflow-hidden shadow-lg border border-gray-100 dark:border-gray-700 group flex flex-col h-full"
          >
            <div class="h-56 overflow-hidden">
              <img
                src="https://images.unsplash.com/photo-1581056771107-24ca5f033842?w=600"
                alt="Blog"
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
              />
            </div>
            <div class="p-6 flex flex-col flex-grow">
              <div
                class="flex items-center gap-4 text-xs font-bold text-gray-500 dark:text-gray-400 mb-4 border-b border-gray-100 dark:border-gray-700 pb-4"
              >
                <div class="flex items-center gap-1.5">
                  <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                    />
                  </svg>
                  By Team
                </div>
                <div class="flex items-center gap-1.5">
                  <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
                    />
                  </svg>
                  18 Jun 2024
                </div>
              </div>
              <h4 class="text-xl font-bold text-gray-900 dark:text-white mb-3 leading-snug">
                {{ t.blogs.b3Title }}
              </h4>
              <p class="text-sm text-gray-500 dark:text-gray-400 leading-relaxed mb-6 flex-grow">
                {{ t.blogs.b3Desc }}
              </p>
              <router-link
                to="#"
                class="inline-flex items-center justify-center px-4 py-1.5 rounded-md bg-[#00d0ff] text-white text-xs font-bold w-fit hover:bg-[#00bce6] transition-colors"
              >
                {{ t.treatments.readMore }}
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-3 w-3 ml-1"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  stroke-width="2"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
                </svg>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer
      class="border-t border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 pt-16 pb-8 relative"
    >
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col md:flex-row items-center justify-between gap-6 mb-12">
          <div class="flex items-center gap-3 opacity-100">
            <img src="/images/logo/logo.svg" alt="POURA" class="h-10 w-auto dark:hidden" />
            <img
              src="/images/logo/logo-dark.svg"
              alt="POURA"
              class="h-10 w-auto hidden dark:block"
            />
            <span class="font-black tracking-tight text-gray-900 dark:text-white text-3xl"
              >POURA</span
            >
          </div>
          <div class="flex gap-6">
            <a href="#" class="text-gray-400 hover:text-brand-600 transition-colors"
              >Politique de confidentialité</a
            >
            <a href="#" class="text-gray-400 hover:text-brand-600 transition-colors">CGU</a>
            <a href="#" class="text-gray-400 hover:text-brand-600 transition-colors"
              >Mentions légales</a
            >
          </div>
        </div>
        <div class="text-center pt-8 border-t border-gray-100 dark:border-gray-800">
          <p class="text-gray-400 dark:text-gray-500 text-sm font-medium">
            &copy; {{ new Date().getFullYear() }} POURA. {{ t.footer.rights }}
          </p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { animate } from 'motion'
// Swiper 3D Carousel Imports
import { Swiper, SwiperSlide } from 'swiper/vue'
import { EffectCoverflow, Pagination, Autoplay } from 'swiper/modules'
import 'swiper/css'
import 'swiper/css/effect-coverflow'
import 'swiper/css/pagination'

const route = useRoute()
const currentLang = ref('fr')
const swiperModules = [EffectCoverflow, Pagination, Autoplay]

// Pharmacy Data Logic
const pharmacies = ref<any[]>([])
const isLoadingPharmacies = ref(true)

const fetchPharmacies = (lat: number, lon: number) => {
  const query = `[out:json];node["amenity"="pharmacy"](around:5000,${lat},${lon});out 5;`
  const url = `https://overpass-api.de/api/interpreter?data=${encodeURIComponent(query)}`

  fetch(url)
    .then((res) => res.json())
    .then((data) => {
      if (data && data.elements && data.elements.length > 0) {
        pharmacies.value = data.elements.map((el: any) => ({
          name: el.tags.name || 'Pharmacie',
          lat: el.lat,
          lon: el.lon,
          distance: (Math.random() * 2 + 0.1).toFixed(1), // Estimated distance
          isOpen: Math.random() > 0.2, // Simulated status
        }))
      }
      // Fill remaining with dummies if needed
      while (pharmacies.value.length < 5) {
        pharmacies.value.push({
          name: 'Pharmacie Centrale',
          lat: lat,
          lon: lon,
          distance: '1.2',
          isOpen: true,
        })
      }
      isLoadingPharmacies.value = false
    })
    .catch(() => {
      loadDummyPharmacies()
    })
}

const loadDummyPharmacies = () => {
  pharmacies.value = [
    { name: 'Pharmacie Centrale', lat: 36.75, lon: 3.05, distance: '0.4', isOpen: true },
    { name: 'Pharmacie du Centre', lat: 36.75, lon: 3.05, distance: '0.8', isOpen: true },
    { name: 'Pharmacie des Oliviers', lat: 36.75, lon: 3.05, distance: '1.2', isOpen: false },
    { name: 'Pharmacie El Chifa', lat: 36.75, lon: 3.05, distance: '2.0', isOpen: true },
    { name: 'Pharmacie Ibn Sina', lat: 36.75, lon: 3.05, distance: '3.5', isOpen: true },
  ]
  isLoadingPharmacies.value = false
}

const translations = {
  fr: {
    search: {
      placeholder1: 'Chercher une spécialité, un médecin...',
      placeholder2: 'Où ? (ex: Paris, Code postal)',
      button: 'Rechercher',
    },
    pharmacies: {
      title: 'Pharmacies de garde à proximité',
      distance: 'à proximité',
      openNow: 'Ouvert maintenant',
      closesAt: 'Ferme à',
      call: 'Appeler',
    },
    nav: {
      home: 'Accueil',
      about: 'Fonctionnalités',
      digital: 'Pour les praticiens',
      contact: 'Contact',
      book: 'Prendre Rendez-vous',
    },
    hero: {
      title:
        'Simplifiez & Réservez <br/>Vos Rendez-vous <br/><span class="text-[#00d0ff]">Pour De Meilleurs Soins</span>',
      subtitle:
        "Optimisez le processus de planification, réduisez les temps d'attente et améliorez la satisfaction des patients avec un accès pratique.",
      cta1: 'Réserver',
      cta2: 'En savoir plus',
      reviews: 'Avis 5 sur 5',
      rating: 'Note de 5 étoiles sur différentes plateformes',
      explore: 'Explorer plus',
    },
    aboutCompany: {
      title: 'A propos de notre société',
      point1Title: 'Approche Centrée sur le Patient',
      point1Desc: 'Nous priorisons la santé et le bien-être de nos patients avant tout.',
      point2Title: 'Services de Santé',
      point2Desc: 'Nous offrons une large gamme de services médicaux primaires et spécialisés.',
      point3Title: 'Technologie Médicale',
      point3Desc: 'Nos installations de pointe sont équipées des dernières technologies.',
      point4Title: 'Équipe Collaborative',
      point4Desc: 'Notre équipe multidisciplinaire de professionnels travaille ensemble.',
      stat1: 'Clients Satisfaits',
      stat2: 'Médecins Experts',
      stat3: 'Prix Nationaux',
    },
    treatments: {
      badge: 'Nos Fonctionnalités',
      title: 'Simplifiez votre parcours',
      desc: 'Notre plateforme offre une large gamme doutils pour gérer vos rendez-vous, dossiers médicaux et consultations en ligne facilement.',
      viewAll: 'Voir Tout',
      readMore: 'Lire Plus',
      items: [
        {
          title: 'Agenda Connecté',
          desc: 'Consultez les disponibilités en temps réel et prenez rendez-vous 24h/24.',
          svg: '<path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />',
          img: '/images/carousel/agenda_connecte.jpg',
        },
        {
          title: 'Téléconsultation',
          desc: 'Consultez votre médecin à distance en toute sécurité avec ordonnance digitale.',
          svg: '<path stroke-linecap="round" stroke-linejoin="round" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z" />',
          img: '/images/carousel/teleconsultation.jpg',
        },
        {
          title: 'Dossier Sécurisé',
          desc: 'Vos données médicales sont cryptées de bout en bout dans un espace privé.',
          svg: '<path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />',
          img: '/images/carousel/dossier_securise.jpg',
        },
        {
          title: 'Ordonnances Digitales',
          desc: 'Recevez vos ordonnances en toute sécurité prêtes à être partagées.',
          svg: '<path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />',
          img: '/images/carousel/ordonnances_digitales.jpg',
        },
        {
          title: 'Suivi Personnalisé',
          desc: 'Visualisez lévolution de votre santé avec un tableau de bord intuitif.',
          svg: '<path stroke-linecap="round" stroke-linejoin="round" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />',
          img: '/images/carousel/suivi_personnalise.jpg',
        },
        {
          title: 'Paiement Sécurisé',
          desc: 'Payez vos consultations en ligne avec notre système de paiement sécurisé.',
          svg: '<path stroke-linecap="round" stroke-linejoin="round" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z" />',
          img: '/images/carousel/paiement_securise.jpg',
        },
      ],
    },
    process: {
      badge: 'Processus',
      title: 'Comment ça marche',
      step1Title: 'Prendre Rendez-vous',
      step1Desc: 'Prenez facilement rendez-vous en ligne pour des soins personnalisés rapides.',
      step2Title: 'Choisir le Médecin',
      step2Desc: 'Choisissez votre médecin préféré parmi notre équipe qualifiée.',
      step3Title: 'Obtenir une Solution',
      step3Desc: 'Recevez une solution de santé personnalisée répondant à vos besoins.',
    },
    reviews: {
      title: 'Avis des Patients',
      rev1Desc:
        'Les avis de nos patients soulignent les soins exceptionnels quils reçoivent. Découvrez leurs histoires.',
      rev1Name: 'Devon Lane',
      rev1Role: 'Manager',
      rev2Desc:
        'Une plateforme incroyable qui ma permis de trouver le bon spécialiste en quelques minutes.',
      rev2Name: 'Robert Fox',
      rev2Role: 'Designer',
    },
    faq: {
      title: 'Questions fréquemment posées',
      subtitle: 'Tout ce que vous devez savoir sur le produit et la facturation.',
      q1: 'Comment prendre un rendez-vous ?',
      a1: 'Planifier un rendez-vous est simple. Vous pouvez réserver en ligne via notre site web, où vous pouvez sélectionner la date, lheure et le médecin.',
      q2: 'Comment me préparer à une téléconsultation ?',
      q3: 'Quels types de traitements offrez-vous ?',
      q4: 'Puis-je accéder à mes dossiers médicaux en ligne ?',
    },
    banner: {
      subtitle: 'Nous Sommes Prêts',
      title: 'Nous sommes prêts pour tout',
      call: 'Appelez Maintenant',
      btn: 'Prendre Rendez-vous',
    },
    blogs: {
      badge: 'Nos Blogs',
      title: 'Dernières Nouvelles & Blogs',
      desc: 'Restez informé avec nos dernières actualités médicales, conseils de bien-être et sujets liés à la santé.',
      b1Title: 'Conseils Experts de Nos Médecins',
      b1Desc: "Nos médecins fournissent des conseils d'experts sur la gestion de votre santé.",
      b2Title: 'Conseils Santé & Bien-être',
      b2Desc:
        'Découvrez des conseils de santé et de bien-être de nos experts pour maintenir un équilibre.',
      b3Title: 'Aperçus des Soins Préventifs',
      b3Desc: 'Obtenez des informations précieuses sur les stratégies de soins préventifs.',
    },
    footer: { rights: 'Tous droits réservés.' },
  },
  en: {
    search: {
      placeholder1: 'Search specialty, doctor, or condition...',
      placeholder2: 'Where? (e.g. Paris, Zip code)',
      button: 'Search',
    },
    pharmacies: {
      title: 'Nearby on-duty Pharmacies',
      distance: 'nearby',
      openNow: 'Open Now',
      closesAt: 'Closes at',
      call: 'Call',
    },
    nav: {
      home: 'Home',
      about: 'Features',
      digital: 'For Practitioners',
      contact: 'Contact',
      book: 'Book Appointment',
    },
    hero: {
      title:
        'Simplify & Book <br/>Appointment Scheduling <br/><span class="text-[#00d0ff]">For Better Care</span>',
      subtitle:
        'Streamline the scheduling process, reduce wait times, and enhance patient satisfaction with convenient and efficient access to healthcare services.',
      cta1: 'Book Now',
      cta2: 'Learn More',
      reviews: 'Reviews 5 out of 5',
      rating: '5 Star rating from different platforms',
      explore: 'Explore More from Gallery',
    },
    aboutCompany: {
      title: 'About Our Company',
      point1Title: 'Patient-First Approach',
      point1Desc: 'We prioritize the health and well-being of our patients above all.',
      point2Title: 'Healthcare Services',
      point2Desc: 'We offer a wide range of primary and specialized medical services.',
      point3Title: 'Medical Technology',
      point3Desc: 'Our state-of-the-art facilities are equipped with the latest technology.',
      point4Title: 'Collaborative Team',
      point4Desc: 'Our multidisciplinary team of healthcare professionals works together.',
      stat1: 'Happy Clients',
      stat2: 'Expert Doctor',
      stat3: 'National Award',
    },
    treatments: {
      badge: 'Our Features',
      title: 'Our Company Treatments',
      desc: 'Our company offers a wide range of treatments, from primary care and chronic disease management to specialized services.',
      viewAll: 'View All',
      readMore: 'Read More',
      items: [
        {
          title: 'Primary Care',
          desc: 'Our Primary Care ensures your health with personalized, comprehensive care.',
          svg: '<path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />',
          img: '/images/carousel/agenda_connecte.jpg',
        },
        {
          title: 'Pediatric Services',
          desc: 'Provide compassionate, comprehensive care for infants, children.',
          svg: '<path stroke-linecap="round" stroke-linejoin="round" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z" />',
          img: '/images/carousel/teleconsultation.jpg',
        },
        {
          title: 'Cardiology',
          desc: 'Advanced cardiology services for heart health and disease prevention.',
          svg: '<path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />',
          img: '/images/carousel/dossier_securise.jpg',
        },
        {
          title: 'Dermatology',
          desc: 'Provide diagnosis and treatment for various skin conditions.',
          svg: '<path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />',
          img: '/images/carousel/ordonnances_digitales.jpg',
        },
        {
          title: 'Personalized Tracking',
          desc: 'Visualize your health progress with an intuitive dashboard.',
          svg: '<path stroke-linecap="round" stroke-linejoin="round" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />',
          img: '/images/carousel/suivi_personnalise.jpg',
        },
        {
          title: 'Secure Payment',
          desc: 'Pay for your online consultations securely with our payment gateway.',
          svg: '<path stroke-linecap="round" stroke-linejoin="round" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z" />',
          img: '/images/carousel/paiement_securise.jpg',
        },
      ],
    },
    process: {
      badge: 'Work Process',
      title: 'How We Do Work Process',
      step1Title: 'Make appointment',
      step1Desc: 'Easily make an appointment online for prompt, personalized care.',
      step2Title: 'Choose Doctor',
      step2Desc: 'Choose your preferred doctor from our skilled team.',
      step3Title: 'Get a Solution',
      step3Desc: 'Receive a personalized health solution from our expert team.',
    },
    reviews: {
      title: 'Patients Reviews',
      rev1Desc:
        'Our patients reviews highlight the exceptional care and support they receive. Discover their stories.',
      rev1Name: 'Devon Lane',
      rev1Role: 'Company Manager',
      rev2Desc:
        'An incredible platform that allowed me to find the right specialist in just a few minutes.',
      rev2Name: 'Robert Fox',
      rev2Role: 'UI/UX Designer',
    },
    faq: {
      title: 'Frequently asked questions',
      subtitle: 'Everything you need to know about the product and billing.',
      q1: 'How do I make an appointment?',
      a1: 'Scheduling an appointment is simple. You can book online through our website, where you can select the date, time, and preferred doctor.',
      q2: 'How do I prepare for a telehealth appointment?',
      q3: 'What types of treatments do you offer?',
      q4: 'Can I access my medical records online?',
    },
    banner: {
      subtitle: 'We Are Ready',
      title: 'We Are Ready for any',
      call: 'Call Now',
      btn: 'Book Appointment',
    },
    blogs: {
      badge: 'Our Blogs',
      title: 'Our Latest News & Blogs',
      desc: 'Stay informed with our latest news and blogs, where we share updates on medical advancements and wellness tips.',
      b1Title: 'Expert Advice from Our Doctors',
      b1Desc: 'Our doctors provide expert advice on managing your health, offering practical tips.',
      b2Title: 'Health & Wellness Tips',
      b2Desc:
        'Discover actionable health and wellness tips from our experts to help you maintain balance.',
      b3Title: 'Preventative Care Insights',
      b3Desc: 'Gain valuable insights into preventative care strategies to stay ahead.',
    },
    footer: { rights: 'All rights reserved.' },
  },
  ar: {
    search: {
      placeholder1: 'ابحث عن تخصص، طبيب، أو حالة...',
      placeholder2: 'أين؟ (مثل: باريس، الرمز البريدي)',
      button: 'بحث',
    },
    pharmacies: {
      title: 'صيدليات الحراسة القريبة',
      distance: 'بالقرب منك',
      openNow: 'مفتوح الآن',
      closesAt: 'يغلق عند',
      call: 'اتصل',
    },
    nav: {
      home: 'الرئيسية',
      about: 'المميزات',
      digital: 'للممارسين',
      contact: 'اتصال',
      book: 'حجز موعد',
    },
    hero: {
      title: 'بسط واحجز <br/>مواعيدك الطبية <br/><span class="text-[#00d0ff]">لرعاية أفضل</span>',
      subtitle:
        'قم بتبسيط عملية الجدولة وتقليل أوقات الانتظار وتعزيز رضا المرضى من خلال وصول مريح.',
      cta1: 'احجز الآن',
      cta2: 'اعرف المزيد',
      reviews: 'تقييم 5 من 5',
      rating: 'تقييم 5 نجوم من منصات مختلفة',
      explore: 'استكشف المزيد',
    },
    aboutCompany: {
      title: 'نبذة عن شركتنا',
      point1Title: 'نهج يضع المريض أولاً',
      point1Desc: 'نحن نعطي الأولوية لصحة ورفاهية مرضانا قبل كل شيء.',
      point2Title: 'خدمات الرعاية الصحية',
      point2Desc: 'نقدم مجموعة واسعة من الخدمات الطبية الأولية والمتخصصة.',
      point3Title: 'التكنولوجيا الطبية',
      point3Desc: 'مرافقنا الحديثة مجهزة بأحدث التقنيات.',
      point4Title: 'فريق متعاون',
      point4Desc: 'يعمل فريقنا متعدد التخصصات من المتخصصين في الرعاية الصحية معًا.',
      stat1: 'عميل سعيد',
      stat2: 'طبيب خبير',
      stat3: 'جائزة وطنية',
    },
    treatments: {
      badge: 'ميزاتنا',
      title: 'علاجات الشركة',
      desc: 'تقدم منصتنا مجموعة واسعة من العلاجات، من الرعاية الأولية وإدارة الأمراض المزمنة إلى الخدمات المتخصصة.',
      viewAll: 'عرض الكل',
      readMore: 'اقرأ المزيد',
      items: [
        {
          title: 'الرعاية الأولية',
          desc: 'تضمن الرعاية الأولية لدينا صحتك من خلال رعاية شخصية وشاملة.',
          svg: '<path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />',
          img: '/images/carousel/agenda_connecte.jpg',
        },
        {
          title: 'خدمات طب الأطفال',
          desc: 'توفير رعاية شاملة وعطوفة للرضع والأطفال.',
          svg: '<path stroke-linecap="round" stroke-linejoin="round" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z" />',
          img: '/images/carousel/teleconsultation.jpg',
        },
        {
          title: 'طب القلب',
          desc: 'خدمات طب القلب المتقدمة لصحة القلب والوقاية من الأمراض.',
          svg: '<path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />',
          img: '/images/carousel/dossier_securise.jpg',
        },
        {
          title: 'طب الأمراض الجلدية',
          desc: 'توفير التشخيص والعلاج للأمراض الجلدية المختلفة.',
          svg: '<path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />',
          img: '/images/carousel/ordonnances_digitales.jpg',
        },
        {
          title: 'متابعة شخصية',
          desc: 'تصور تطور صحتك بفضل لوحة تحكم بديهية.',
          svg: '<path stroke-linecap="round" stroke-linejoin="round" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />',
          img: '/images/carousel/suivi_personnalise.jpg',
        },
        {
          title: 'دفع آمن',
          desc: 'ادفع مقابل استشاراتك عبر الإنترنت بشكل آمن.',
          svg: '<path stroke-linecap="round" stroke-linejoin="round" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z" />',
          img: '/images/carousel/paiement_securise.jpg',
        },
      ],
    },
    process: {
      badge: 'عملية العمل',
      title: 'كيف نعمل',
      step1Title: 'تحديد موعد',
      step1Desc: 'احجز موعدك عبر الإنترنت بسهولة للحصول على رعاية سريعة.',
      step2Title: 'اختر الطبيب',
      step2Desc: 'اختر طبيبك المفضل من فريقنا الماهر.',
      step3Title: 'احصل على حل',
      step3Desc: 'احصل على حل صحي شخصي من فريق الخبراء لدينا.',
    },
    reviews: {
      title: 'آراء المرضى',
      rev1Desc: 'تبرز تقييمات مرضانا الرعاية والدعم الاستثنائيين الذين يتلقونهم. اكتشف قصصهم.',
      rev1Name: 'ديفون لين',
      rev1Role: 'مدير شركة',
      rev2Desc: 'منصة رائعة سمحت لي بالعثور على الأخصائي المناسب في بضع دقائق فقط.',
      rev2Name: 'روبرت فوكس',
      rev2Role: 'مصمم',
    },
    faq: {
      title: 'أسئلة مكررة',
      subtitle: 'كل ما تحتاج لمعرفته حول المنتج.',
      q1: 'كيف أحدد موعدًا؟',
      a1: 'جدولة الموعد بسيطة. يمكنك الحجز عبر الإنترنت من خلال موقعنا الإلكتروني، حيث يمكنك تحديد التاريخ والوقت.',
      q2: 'كيف أستعد لاستشارة عن بعد؟',
      q3: 'ما أنواع العلاجات التي تقدمونها؟',
      q4: 'هل يمكنني الوصول إلى سجلاتي الطبية عبر الإنترنت؟',
    },
    banner: {
      subtitle: 'نحن مستعدون',
      title: 'نحن مستعدون لأي شيء',
      call: 'اتصل الان',
      btn: 'حجز موعد',
    },
    blogs: {
      badge: 'مدوناتنا',
      title: 'أحدث الأخبار والمدونات',
      desc: 'ابق على اطلاع بأحدث الأخبار الطبية ونصائح العافية والمواضيع المتعلقة بالصحة.',
      b1Title: 'نصائح الخبراء من أطبائنا',
      b1Desc: 'يقدم أطبائنا نصائح الخبراء حول إدارة صحتك.',
      b2Title: 'نصائح الصحة والعافية',
      b2Desc: 'اكتشف نصائح عملية حول الصحة والعافية من خبرائنا.',
      b3Title: 'رؤى الرعاية الوقائية',
      b3Desc: 'احصل على رؤى قيمة حول استراتيجيات الرعاية الوقائية.',
    },
    footer: { rights: 'كل الحقوق محفوظة.' },
  },
}

const t = computed(() => translations[currentLang.value as keyof typeof translations])

onMounted(() => {
  if ('geolocation' in navigator) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        fetchPharmacies(position.coords.latitude, position.coords.longitude)
      },
      (error) => {
        console.error('Geolocation error', error)
        loadDummyPharmacies()
      },
    )
  } else {
    loadDummyPharmacies()
  }

  // @ts-ignore
  animate('.hero-content', { opacity: [0, 1], y: [20, 0] }, { duration: 0.8, easing: 'ease-out' })
  // @ts-ignore
  animate(
    '.hero-image',
    { opacity: [0, 1], x: [20, 0] },
    { duration: 0.8, delay: 0.2, easing: 'ease-out' },
  )
})
</script>

<style>
/* CSS overrides for Swiper pagination */
.swiper-pagination-bullet {
  background-color: #9ca3af !important;
}
.swiper-pagination-bullet-active {
  background-color: var(--color-brand-600, #2563eb) !important;
}

@keyframes carousel-scroll {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(calc(-100% / 2));
  }
}
.animate-carousel-scroll {
  animation: carousel-scroll 30s linear infinite;
  width: max-content;
}
/* Pause on hover */
.animate-carousel-scroll:hover {
  animation-play-state: paused;
}
</style>
