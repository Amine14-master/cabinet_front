<template>
  <div :dir="currentLang === 'ar' ? 'rtl' : 'ltr'" class="min-h-screen bg-gray-50 dark:bg-gray-950 font-figtree selection:bg-brand-500/30">
    
    <!-- Navigation (Light Theme) -->
    <nav class="sticky top-0 z-50 bg-white/80 dark:bg-gray-900/80 backdrop-blur-xl border-b border-gray-100 dark:border-gray-800 transition-colors duration-300">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
        <!-- Logo -->
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 bg-brand-600 rounded-xl flex items-center justify-center text-white font-bold text-2xl shadow-lg shadow-brand-500/30">P</div>
          <span class="font-black text-2xl tracking-tight text-gray-900 dark:text-white">POURA</span>
        </div>

        <!-- Links (Desktop) -->
        <div class="hidden md:flex items-center gap-8">
          <a href="#about" class="text-sm font-bold text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white transition-colors">{{ t.nav.about }}</a>
          <a href="#ecosystem" class="text-sm font-bold text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white transition-colors">{{ t.nav.ecosystem }}</a>
          <a href="#contact" class="text-sm font-bold text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white transition-colors">{{ t.nav.contact }}</a>
        </div>

        <!-- Actions -->
        <div class="flex items-center gap-4">
          <select v-model="currentLang" class="bg-gray-50 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 text-gray-700 dark:text-gray-300 rounded-lg px-3 py-1.5 text-xs font-bold outline-none cursor-pointer">
            <option value="fr">FR</option>
            <option value="en">EN</option>
            <option value="ar">AR</option>
          </select>
          <router-link to="/signin" class="hidden sm:inline-flex items-center gap-2 px-6 py-2.5 rounded-xl bg-brand-600 hover:bg-brand-700 text-white text-sm font-bold shadow-lg shadow-brand-500/30 transition-all active:scale-95">
            {{ t.nav.book }}
          </router-link>
        </div>
      </div>
    </nav>

    <!-- Hero Section -->
    <section class="relative pt-20 pb-32 overflow-hidden bg-white dark:bg-gray-950">
      <div class="absolute inset-0 bg-[linear-gradient(to_right,#f1f5f9_1px,transparent_1px),linear-gradient(to_bottom,#f1f5f9_1px,transparent_1px)] bg-[size:4rem_4rem] [mask-image:radial-gradient(ellipse_60%_50%_at_50%_0%,#000_70%,transparent_100%)] dark:bg-[linear-gradient(to_right,#1e293b_1px,transparent_1px),linear-gradient(to_bottom,#1e293b_1px,transparent_1px)]"></div>
      
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
          
          <!-- Text Content -->
          <div class="max-w-2xl">
            <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-brand-50 dark:bg-brand-500/10 border border-brand-100 dark:border-brand-500/20 mb-8">
              <span class="flex h-2 w-2 rounded-full bg-brand-500 animate-pulse"></span>
              <span class="text-xs font-bold text-brand-600 dark:text-brand-400 uppercase tracking-wide">{{ t.hero.badge }}</span>
            </div>
            
            <h1 class="text-5xl sm:text-6xl lg:text-7xl font-black tracking-tight text-gray-900 dark:text-white leading-[1.1] mb-6" v-html="t.hero.title.replace('text-transparent bg-clip-text bg-gradient-to-r from-brand-600 to-blue-light-600', 'text-brand-600 dark:text-brand-400')">
            </h1>
            
            <p class="text-lg text-gray-500 dark:text-gray-400 font-medium mb-10 leading-relaxed">
              {{ t.hero.subtitle }}
            </p>

            <div class="flex flex-col sm:flex-row items-center gap-4">
              <router-link to="/signin" class="w-full sm:w-auto px-8 py-4 rounded-xl bg-brand-600 hover:bg-brand-700 text-white font-bold shadow-lg shadow-brand-500/30 transition-all flex items-center justify-center gap-2 active:scale-95">
                {{ t.hero.cta1 }}
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
              </router-link>
              <a href="#about" class="w-full sm:w-auto px-8 py-4 rounded-xl bg-white dark:bg-gray-900 border border-gray-200 dark:border-gray-800 text-gray-900 dark:text-white font-bold hover:bg-gray-50 dark:hover:bg-gray-800 transition-all text-center">
                {{ t.hero.cta2 }}
              </a>
            </div>
          </div>

          <!-- Dynamic 3D Image Card -->
          <div class="relative w-full aspect-square sm:aspect-video lg:aspect-[4/3] bg-white dark:bg-gray-900 rounded-[32px] p-4 sm:p-6 shadow-[0_20px_60px_-15px_rgba(0,0,0,0.1)] dark:shadow-[0_20px_60px_-15px_rgba(0,0,0,0.5)] border border-gray-100 dark:border-gray-800 overflow-hidden group">
            <div class="absolute inset-0 bg-brand-50/50 dark:bg-brand-500/5 rounded-[32px]"></div>
            <img :src="heroImageSrc" alt="Medical Specialty" class="w-full h-full object-cover rounded-[24px] z-10 relative shadow-sm transition-transform duration-700 group-hover:scale-105" />
            
            <!-- Quick Floating Widget -->
            <div class="absolute bottom-10 left-10 right-10 bg-white/90 dark:bg-gray-900/90 backdrop-blur-md rounded-2xl p-5 border border-white/20 dark:border-gray-700/50 shadow-xl z-20 flex items-center justify-between">
              <div class="flex items-center gap-4">
                <div class="w-12 h-12 bg-brand-100 dark:bg-brand-500/20 rounded-xl flex items-center justify-center text-brand-600 dark:text-brand-400">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20m7-10V5a2 2 0 00-2-2h-.095c-.5 0-.905.405-.905.905 0 .714-.211 1.412-.608 2.006L7 11v9m7-10h-2M7 20H5a2 2 0 01-2-2v-6a2 2 0 012-2h2.5" /></svg>
                </div>
                <div>
                  <div class="text-sm font-bold text-gray-900 dark:text-white">{{ t.hero.satisfaction }}</div>
                  <div class="text-xs text-gray-500 dark:text-gray-400 mt-1">97% de patients satisfaits</div>
                </div>
              </div>
            </div>
          </div>
          
        </div>
      </div>
    </section>

    <!-- About Section -->
    <section id="about" class="py-24 bg-gray-50 dark:bg-gray-950">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="mb-16 text-center">
          <h2 class="text-sm font-bold text-brand-600 uppercase tracking-widest mb-3">{{ t.about.title }}</h2>
          <h3 class="text-4xl font-black text-gray-900 dark:text-white">{{ t.about.heading }}</h3>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- Card 1 -->
          <div class="bg-white dark:bg-gray-900 border border-gray-100 dark:border-gray-800 rounded-3xl p-8 shadow-sm hover:shadow-lg transition-shadow">
            <div class="w-14 h-14 bg-brand-50 dark:bg-brand-500/10 rounded-2xl flex items-center justify-center text-brand-600 dark:text-brand-400 mb-6">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>
            </div>
            <h4 class="text-xl font-bold text-gray-900 dark:text-white mb-3">{{ t.about.feat1Title }}</h4>
            <p class="text-gray-500 dark:text-gray-400 font-medium">{{ t.about.feat1Desc }}</p>
          </div>
          <!-- Card 2 -->
          <div class="bg-white dark:bg-gray-900 border border-gray-100 dark:border-gray-800 rounded-3xl p-8 shadow-sm hover:shadow-lg transition-shadow">
            <div class="w-14 h-14 bg-brand-50 dark:bg-brand-500/10 rounded-2xl flex items-center justify-center text-brand-600 dark:text-brand-400 mb-6">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
            </div>
            <h4 class="text-xl font-bold text-gray-900 dark:text-white mb-3">Agenda Intelligent</h4>
            <p class="text-gray-500 dark:text-gray-400 font-medium">Une gestion de file d'attente optimisée pour réduire les retards et fluidifier la journée.</p>
          </div>
          <!-- Card 3 -->
          <div class="bg-white dark:bg-gray-900 border border-gray-100 dark:border-gray-800 rounded-3xl p-8 shadow-sm hover:shadow-lg transition-shadow">
            <div class="w-14 h-14 bg-brand-50 dark:bg-brand-500/10 rounded-2xl flex items-center justify-center text-brand-600 dark:text-brand-400 mb-6">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" /></svg>
            </div>
            <h4 class="text-xl font-bold text-gray-900 dark:text-white mb-3">Sécurité Absolue</h4>
            <p class="text-gray-500 dark:text-gray-400 font-medium">Vos données médicales cryptées de bout en bout, accessibles uniquement par le personnel autorisé.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="border-t border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 py-12">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row items-center justify-between gap-6">
        <div class="flex items-center gap-3">
          <div class="w-8 h-8 bg-brand-600 rounded-lg flex items-center justify-center text-white font-bold text-lg">P</div>
          <span class="font-black tracking-tight text-gray-900 dark:text-white text-xl">POURA</span>
        </div>
        <p class="text-gray-500 dark:text-gray-400 text-sm font-medium">&copy; {{ new Date().getFullYear() }} POURA. {{ t.footer.rights }}</p>
      </div>
    </footer>

  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const currentLang = ref('fr')

const heroImageSrc = computed(() => {
  const spec = route.params.speciality?.toString().toLowerCase();
  if (spec === 'cardiology' || spec === 'cardiologue' || spec === 'cardiologie') return '/cardiology_3d.jpg';
  if (spec === 'dentistry' || spec === 'dentiste') return '/dentistry_3d.jpg';
  if (spec === 'ophthalmology' || spec === 'ophtalmologie') return '/ophthalmology_3d.jpg';
  return '/clinic_model_1787418202621.jpg'; // fallback
});

const translations = {
  fr: {
    nav: { home: 'Accueil', about: 'À propos', ecosystem: 'Écosystème', contact: 'Contact', book: 'Accès Cabinet' },
    hero: { badge: 'Plateforme Santé', title: 'Votre Cabinet,<br/><span class="text-brand-600">Entièrement Digitalisé.</span>', subtitle: 'POURA unit toutes les spécialités médicales dans une plateforme unique, fluide et esthétique. De la prévention à la guérison.', cta1: 'Espace Praticien', cta2: 'En savoir plus', satisfaction: 'Satisfaction' },
    about: { title: 'L\'Infrastructure', heading: 'Le système d\'exploitation de votre santé.', feat1Title: 'Dossier Unifié', feat1Desc: 'Un profil unique crypté accessible par tous vos praticiens en temps réel.' },
    footer: { rights: 'Tous droits réservés.' }
  },
  en: {
    nav: { home: 'Home', about: 'About', ecosystem: 'Ecosystem', contact: 'Contact', book: 'Clinic Access' },
    hero: { badge: 'Health Platform', title: 'Your Clinic,<br/><span class="text-brand-600">Fully Digitalized.</span>', subtitle: 'POURA unites all medical specialties into a single, seamless, and aesthetic platform. From prevention to healing.', cta1: 'Practitioner Area', cta2: 'Learn More', satisfaction: 'Satisfaction' },
    about: { title: 'Infrastructure', heading: 'The operating system for your health.', feat1Title: 'Unified Record', feat1Desc: 'A single encrypted profile accessible by all your practitioners in real-time.' },
    footer: { rights: 'All rights reserved.' }
  },
  ar: {
    nav: { home: 'الرئيسية', about: 'حول', ecosystem: 'النظام البيئي', contact: 'اتصال', book: 'دخول العيادة' },
    hero: { badge: 'منصة الصحة', title: 'عيادتك،<br/><span class="text-brand-600">رقمية بالكامل.</span>', subtitle: 'بورا توحد جميع التخصصات الطبية في منصة واحدة سلسة وجمالية. من الوقاية إلى الشفاء.', cta1: 'مساحة الممارس', cta2: 'اعرف المزيد', satisfaction: 'رضا' },
    about: { title: 'البنية التحتية', heading: 'نظام التشغيل لصحتك.', feat1Title: 'سجل موحد', feat1Desc: 'ملف تعريف مشفر واحد يمكن لجميع الممارسين الوصول إليه في الوقت الفعلي.' },
    footer: { rights: 'كل الحقوق محفوظة.' }
  }
}

const t = computed(() => translations[currentLang.value as keyof typeof translations])
</script>
