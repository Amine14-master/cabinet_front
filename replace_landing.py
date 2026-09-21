import os

file_path = "src/views/LandingPage.vue"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace Nav and Hero Section
old_nav_hero = """    <!-- Navigation -->
    <nav
      class="sticky top-0 z-50 bg-white/80 dark:bg-gray-900/80 backdrop-blur-xl border-b border-gray-100 dark:border-gray-800 transition-colors duration-300"
    >
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
        <div class="flex items-center gap-3">
          <img src="/images/logo/logo.svg" alt="POURA" class="h-10 w-auto dark:hidden" />
          <img src="/images/logo/logo-dark.svg" alt="POURA" class="h-10 w-auto hidden dark:block" />
          <span class="font-black text-2xl tracking-tight text-gray-900 dark:text-white"
            >POURA</span
          >
        </div>
        <div class="hidden md:flex items-center gap-8">
          <a
            href="#about"
            class="text-sm font-bold text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white transition-colors"
            >{{ t.nav.about }}</a
          >
          <a
            href="#digital-cabinet"
            class="text-sm font-bold text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white transition-colors"
            >{{ t.nav.digital }}</a
          >
          <a
            href="#contact"
            class="text-sm font-bold text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white transition-colors"
            >{{ t.nav.contact }}</a
          >
        </div>
        <div class="flex items-center gap-4">
          <select
            v-model="currentLang"
            class="bg-gray-50 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 text-gray-700 dark:text-gray-300 rounded-lg px-3 py-1.5 text-xs font-bold outline-none cursor-pointer"
          >
            <option value="fr">FR</option>
            <option value="en">EN</option>
            <option value="ar">AR</option>
          </select>
          <router-link
            to="/signin"
            class="hidden sm:inline-flex items-center gap-2 px-6 py-2.5 rounded-xl bg-brand-600 hover:bg-brand-700 text-white text-sm font-bold shadow-lg shadow-brand-500/30 transition-all hover:-translate-y-0.5 active:scale-95"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-4 w-4"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
              />
            </svg>
            {{ t.nav.book }}
          </router-link>
        </div>
      </div>
    </nav>

    <!-- Hero Section -->
    <section class="relative pt-20 pb-24 lg:pb-32 bg-white dark:bg-gray-950">
      <div
        class="absolute inset-0 bg-[linear-gradient(to_right,#f1f5f9_1px,transparent_1px),linear-gradient(to_bottom,#f1f5f9_1px,transparent_1px)] bg-[size:4rem_4rem] [mask-image:radial-gradient(ellipse_60%_50%_at_50%_0%,#000_70%,transparent_100%)] dark:bg-[linear-gradient(to_right,#1e293b_1px,transparent_1px),linear-gradient(to_bottom,#1e293b_1px,transparent_1px)]"
      ></div>
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
          <div class="hero-content max-w-2xl opacity-0">
            <div
              class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-brand-50 dark:bg-brand-500/10 border border-brand-100 dark:border-brand-500/20 mb-8 shadow-sm"
            >
              <span class="flex h-2 w-2 rounded-full bg-brand-500 animate-pulse"></span>
              <span
                class="text-xs font-bold text-brand-600 dark:text-brand-400 uppercase tracking-wide"
                >{{ t.hero.badge }}</span
              >
            </div>
            <h1
              class="text-5xl sm:text-6xl lg:text-7xl font-black tracking-tight text-gray-900 dark:text-white leading-[1.1] mb-6"
              v-html="
                t.hero.title.replace(
                  'text-brand-600',
                  'text-transparent bg-clip-text bg-gradient-to-r from-brand-600 to-blue-500',
                )
              "
            ></h1>
            <p class="text-lg text-gray-500 dark:text-gray-400 font-medium mb-10 leading-relaxed">
              {{ t.hero.subtitle }}
            </p>
            <div class="flex flex-col sm:flex-row items-center gap-4">
              <router-link
                to="/signin"
                class="w-full sm:w-auto px-8 py-4 rounded-xl bg-brand-600 hover:bg-brand-700 text-white font-bold shadow-[0_8px_30px_rgb(0,0,0,0.12)] hover:shadow-[0_8px_30px_rgba(var(--color-brand-600),0.3)] transition-all flex items-center justify-center gap-2 hover:-translate-y-1 active:scale-95"
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
                    d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
                  />
                </svg>
                {{ t.hero.cta1 }}
              </router-link>
              <router-link
                to="/signup"
                class="w-full sm:w-auto px-8 py-4 rounded-xl bg-white dark:bg-gray-900 border border-gray-200 dark:border-gray-800 text-gray-900 dark:text-white font-bold hover:bg-gray-50 dark:hover:bg-gray-800 transition-all text-center flex items-center justify-center gap-2 shadow-sm hover:shadow-md hover:-translate-y-1"
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
                    d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                  />
                </svg>
                {{ t.hero.cta2 }}
              </router-link>
            </div>
          </div>
          <div
            class="hero-image relative w-full aspect-square sm:aspect-video lg:aspect-[4/3] opacity-0 group"
          >
            <div
              class="absolute inset-0 bg-brand-50/50 dark:bg-brand-500/5 rounded-[32px] transform rotate-3 scale-105 transition-transform duration-700 group-hover:rotate-6"
            ></div>
            <div
              class="absolute inset-0 bg-white dark:bg-gray-900 rounded-[32px] p-2 sm:p-4 shadow-2xl border border-gray-100 dark:border-gray-800 overflow-hidden z-10"
            >
              <img
                :src="heroImageSrc"
                alt="Medical Platform"
                class="w-full h-full object-cover rounded-[24px] shadow-inner transition-transform duration-1000 group-hover:scale-105"
              />
            </div>
          </div>
        </div>
      </div>
    </section>"""

new_nav_hero = """    <!-- Navigation -->
    <div class="pt-6 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto relative z-50">
      <nav class="bg-[#eef2fc] dark:bg-gray-900 rounded-[2rem] px-6 py-4 flex items-center justify-between shadow-sm border border-gray-100 dark:border-gray-800">
        <div class="flex items-center gap-3">
          <img src="/images/logo/logo.svg" alt="POURA" class="h-8 w-auto dark:hidden" />
          <img src="/images/logo/logo-dark.svg" alt="POURA" class="h-8 w-auto hidden dark:block" />
        </div>
        <div class="hidden md:flex items-center gap-8">
          <a href="#" class="text-sm font-bold text-gray-900 dark:text-white hover:text-[#00d0ff] transition-colors">{{ t.nav.home }}</a>
          <a href="#about" class="text-sm font-bold text-gray-600 dark:text-gray-300 hover:text-[#00d0ff] transition-colors">{{ t.nav.about }}</a>
          <a href="#digital-cabinet" class="text-sm font-bold text-gray-600 dark:text-gray-300 hover:text-[#00d0ff] transition-colors">{{ t.nav.digital }}</a>
          <a href="#contact" class="text-sm font-bold text-gray-600 dark:text-gray-300 hover:text-[#00d0ff] transition-colors">{{ t.nav.contact }}</a>
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
            <p class="text-lg text-gray-500 dark:text-gray-400 font-medium mb-10 leading-relaxed max-w-lg">
              {{ t.hero.subtitle }}
            </p>
            <div class="flex flex-col sm:flex-row items-center gap-4">
              <router-link
                to="/signin"
                class="w-full sm:w-auto px-8 py-4 rounded-full bg-[#00d0ff] hover:bg-[#00bce6] text-white font-bold shadow-lg shadow-[#00d0ff]/30 transition-all flex items-center justify-center gap-2 hover:-translate-y-0.5 active:scale-95"
              >
                {{ t.hero.cta1 }}
              </router-link>
              <router-link
                to="#about"
                class="w-full sm:w-auto px-8 py-4 rounded-full bg-transparent border-2 border-gray-900 dark:border-white text-gray-900 dark:text-white font-bold hover:bg-gray-50 dark:hover:bg-gray-900 transition-all text-center flex items-center justify-center gap-2 hover:-translate-y-0.5"
              >
                {{ t.hero.cta2 }}
              </router-link>
            </div>
          </div>

          <!-- Right side: Masonry Grid -->
          <div class="hero-image relative w-full opacity-0">
            <div class="grid grid-cols-2 gap-4 sm:gap-6 relative">
              <!-- Column 1 (Left) -->
              <div class="flex flex-col gap-4 sm:gap-6 pt-12 relative z-10">
                <!-- Reviews widget -->
                <div class="bg-white dark:bg-gray-900 rounded-3xl p-4 shadow-xl border border-gray-100 dark:border-gray-800 self-end mr-4 -mb-8 relative z-20">
                  <div class="flex -space-x-3 mb-2">
                    <img class="w-10 h-10 rounded-full border-2 border-white dark:border-gray-900 object-cover" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&h=100&fit=crop" alt="" />
                    <img class="w-10 h-10 rounded-full border-2 border-white dark:border-gray-900 object-cover" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=100&h=100&fit=crop" alt="" />
                    <img class="w-10 h-10 rounded-full border-2 border-white dark:border-gray-900 object-cover" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&h=100&fit=crop" alt="" />
                    <img class="w-10 h-10 rounded-full border-2 border-white dark:border-gray-900 object-cover" src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&h=100&fit=crop" alt="" />
                  </div>
                  <p class="text-sm font-medium text-gray-600 dark:text-gray-400 whitespace-nowrap">{{ t.hero.reviews }}</p>
                </div>
                
                <!-- Main Doctor Portrait -->
                <div class="relative rounded-[2rem] overflow-hidden aspect-[3/4] shadow-2xl">
                  <img src="https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=800" alt="Doctor" class="w-full h-full object-cover" />
                  <!-- Floating button overlay -->
                  <div class="absolute top-4 right-4 w-10 h-10 bg-white dark:bg-gray-800 rounded-full flex items-center justify-center shadow-md cursor-pointer hover:scale-110 transition-transform">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-900 dark:text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M17 8l4 4m0 0l-4 4m4-4H3" /></svg>
                  </div>
                </div>
              </div>

              <!-- Column 2 (Right) -->
              <div class="flex flex-col gap-4 sm:gap-6 relative">
                <!-- Top Right Landscape -->
                <div class="relative rounded-[2rem] overflow-hidden aspect-video shadow-2xl">
                  <img src="https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=800" alt="Consultation" class="w-full h-full object-cover" />
                  <!-- Cyan floating button overlay -->
                  <div class="absolute top-4 right-4 w-10 h-10 bg-[#00d0ff] rounded-full flex items-center justify-center shadow-md cursor-pointer hover:scale-110 transition-transform">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M17 8l4 4m0 0l-4 4m4-4H3" /></svg>
                  </div>
                </div>

                <!-- Bottom Right Landscape -->
                <div class="relative rounded-[2rem] overflow-hidden aspect-video shadow-2xl">
                  <img src="https://images.unsplash.com/photo-1622253692010-333f2da6031d?w=800" alt="Doctor smiling" class="w-full h-full object-cover" />
                  <div class="absolute top-4 right-4 w-10 h-10 bg-white dark:bg-gray-800 rounded-full flex items-center justify-center shadow-md cursor-pointer hover:scale-110 transition-transform">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-900 dark:text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M17 8l4 4m0 0l-4 4m4-4H3" /></svg>
                  </div>
                </div>

                <!-- Rating widget -->
                <div class="bg-white dark:bg-gray-900 rounded-3xl p-5 shadow-xl border border-gray-100 dark:border-gray-800 -ml-16 mt-2 relative z-20 self-start">
                  <div class="flex gap-1 mb-2">
                    <svg v-for="i in 5" :key="i" class="w-5 h-5 text-gray-900 dark:text-white" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>
                  </div>
                  <p class="text-xs text-gray-500 dark:text-gray-400 leading-tight mb-2 max-w-[120px]">{{ t.hero.rating }}</p>
                  <a href="#" class="text-xs font-bold text-gray-900 dark:text-white border-b-2 border-gray-900 dark:border-white inline-block pb-0.5">{{ t.hero.explore }}</a>
                </div>

                <!-- Social Icons column -->
                <div class="absolute -right-6 top-1/2 -translate-y-1/2 flex flex-col gap-3 z-30">
                  <a href="#" class="w-10 h-10 rounded-full border border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-800 flex items-center justify-center text-gray-600 dark:text-gray-300 hover:text-[#00d0ff] transition-colors shadow-sm">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
                  </a>
                  <a href="#" class="w-10 h-10 rounded-full border border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-800 flex items-center justify-center text-gray-600 dark:text-gray-300 hover:text-[#00d0ff] transition-colors shadow-sm">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
                  </a>
                  <a href="#" class="w-10 h-10 rounded-full border border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-800 flex items-center justify-center text-gray-600 dark:text-gray-300 hover:text-[#00d0ff] transition-colors shadow-sm">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>"""
content = content.replace(old_nav_hero, new_nav_hero)

# Translations FR
old_fr = """    hero: {
      badge: 'Prise de Rendez-vous Médical',
      title: 'Votre santé,<br/><span class="text-brand-600">accessible en un clic.</span>',
      subtitle:
        'Trouvez rapidement un médecin, prenez rendez-vous en ligne et gérez vos consultations depuis une plateforme sécurisée et intuitive.',
      cta1: 'Trouver un praticien',
      cta2: 'Vous êtes médecin ?',
      satisfaction: 'Accès 24/7',
    },"""

new_fr = """    hero: {
      title: 'Simplifiez & Réservez <br/>Vos Rendez-vous <br/><span class="text-[#00d0ff]">Pour De Meilleurs Soins</span>',
      subtitle:
        'Optimisez le processus de planification, réduisez les temps d\\'attente et améliorez la satisfaction des patients avec un accès pratique.',
      cta1: 'Réserver',
      cta2: 'En savoir plus',
      reviews: 'Avis 5 sur 5',
      rating: 'Note de 5 étoiles sur différentes plateformes',
      explore: 'Explorer plus',
    },"""

content = content.replace(old_fr, new_fr)

# Translations EN
old_en = """    hero: {
      badge: 'Medical Appointment Booking',
      title: 'Your health,<br/><span class="text-brand-600">accessible in one click.</span>',
      subtitle:
        'Quickly find a doctor, book appointments online, and manage your consultations from a secure and intuitive platform.',
      cta1: 'Find a practitioner',
      cta2: 'Are you a doctor?',
      satisfaction: '24/7 Access',
    },"""

new_en = """    hero: {
      title: 'Simplify & Book <br/>Appointment Scheduling <br/><span class="text-[#00d0ff]">For Better Care</span>',
      subtitle:
        'Streamline the scheduling process, reduce wait times, and enhance patient satisfaction with convenient and efficient access to healthcare services.',
      cta1: 'Book Now',
      cta2: 'Learn More',
      reviews: 'Reviews 5 out of 5',
      rating: '5 Star rating from different platforms',
      explore: 'Explore More from Gallery',
    },"""
content = content.replace(old_en, new_en)

# Translations AR
old_ar = """    hero: {
      badge: 'حجز المواعيد الطبية',
      title: 'صحتك،<br/><span class="text-brand-600">بضغطة زر واحدة.</span>',
      subtitle:
        'ابحث بسرعة عن طبيب، احجز مواعيدك عبر الإنترنت، وقم بإدارة استشاراتك من خلال منصة آمنة وبديهية.',
      cta1: 'ابحث عن طبيب',
      cta2: 'هل أنت طبيب؟',
      satisfaction: 'وصول 24/7',
    },"""

new_ar = """    hero: {
      title: 'بسط واحجز <br/>مواعيدك الطبية <br/><span class="text-[#00d0ff]">لرعاية أفضل</span>',
      subtitle:
        'قم بتبسيط عملية الجدولة وتقليل أوقات الانتظار وتعزيز رضا المرضى من خلال وصول مريح وفعال لخدمات الرعاية الصحية.',
      cta1: 'احجز الآن',
      cta2: 'اعرف المزيد',
      reviews: 'تقييم 5 من 5',
      rating: 'تقييم 5 نجوم من منصات مختلفة',
      explore: 'استكشف المزيد',
    },"""
content = content.replace(old_ar, new_ar)

# Remove unused heroImageSrc block
old_heroImageSrc = """const heroImageSrc = computed(() => {
  const spec = route.params.speciality?.toString().toLowerCase()
  if (spec === 'cardiology' || spec === 'cardiologue' || spec === 'cardiologie')
    return '/cardiology_3d.jpg'
  if (spec === 'dentistry' || spec === 'dentiste') return '/dentistry_3d.jpg'
  if (spec === 'ophthalmology' || spec === 'ophtalmologie') return '/ophthalmology_3d.jpg'
  return 'https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=800' // Realistic Unsplash photo
})"""
content = content.replace(old_heroImageSrc, "")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
