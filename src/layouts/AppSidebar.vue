<template>
  <aside
    :class="[
      'fixed mt-16 flex flex-col lg:mt-0 top-0 px-5 left-0 bg-white dark:bg-gray-900 dark:border-gray-800 text-gray-900 h-screen transition-all duration-300 ease-in-out z-99999 border-r border-gray-200',
      {
        'lg:w-[290px]': isExpanded || isMobileOpen || isHovered,
        'lg:w-[90px]': !isExpanded && !isHovered,
        'translate-x-0 w-[290px]': isMobileOpen,
        '-translate-x-full': !isMobileOpen,
        'lg:translate-x-0': true,
      },
    ]"
    @mouseenter="!isExpanded && (isHovered = true)"
    @mouseleave="isHovered = false"
  >
    <!-- Logo Section -->
    <div
      :class="[
        'py-8 flex',
        !isExpanded && !isHovered ? 'lg:justify-center' : 'justify-start',
      ]"
    >
      <router-link to="/">
        <img
          v-if="isExpanded || isHovered || isMobileOpen"
          class="dark:hidden"
          src="/images/logo/logo.svg"
          alt="Logo"
          width="150"
          height="40"
        />
        <img
          v-if="isExpanded || isHovered || isMobileOpen"
          class="hidden dark:block"
          src="/images/logo/logo-dark.svg"
          alt="Logo"
          width="150"
          height="40"
        />
        <img
          v-else
          src="/images/logo/logo-icon.svg"
          alt="Logo"
          width="32"
          height="32"
        />
      </router-link>
    </div>

    <!-- Navigation Section -->
    <div class="flex flex-col overflow-y-auto duration-300 ease-linear no-scrollbar">
      <nav class="mb-6">
        <div class="flex flex-col gap-4">
          <div v-for="(menuGroup, groupIndex) in menuGroups" :key="groupIndex">
            <h2
              :class="[
                'mb-4 text-xs uppercase flex leading-[20px] text-gray-400 font-semibold',
                !isExpanded && !isHovered ? 'lg:justify-center' : 'justify-start',
              ]"
            >
              <template v-if="isExpanded || isHovered || isMobileOpen">
                {{ menuGroup.title }}
              </template>
              <HorizontalDots v-else />
            </h2>

            <ul class="flex flex-col gap-4">
              <li v-for="(item, index) in menuGroup.items" :key="item.name">
                <!-- Toggleable Menu Item (with Subitems) -->
                <button
                  v-if="item.subItems"
                  @click="toggleSubmenu(groupIndex, index)"
                  :class="[
                    'menu-item group w-full',
                    {
                      'menu-item-active': isSubmenuOpen(groupIndex, index),
                      'menu-item-inactive': !isSubmenuOpen(groupIndex, index),
                    },
                    !isExpanded && !isHovered ? 'lg:justify-center' : 'lg:justify-start',
                  ]"
                >
                  <span
                    :class="[
                      isSubmenuOpen(groupIndex, index)
                        ? 'menu-item-icon-active'
                        : 'menu-item-icon-inactive',
                    ]"
                  >
                    <component :is="item.icon" />
                  </span>
                  <span
                    v-if="isExpanded || isHovered || isMobileOpen"
                    class="menu-item-text"
                    >{{ item.name }}</span
                  >
                  <ChevronDownIcon
                    v-if="isExpanded || isHovered || isMobileOpen"
                    :class="[
                      'ml-auto w-5 h-5 transition-transform duration-200',
                      { 'rotate-180 text-brand-500': isSubmenuOpen(groupIndex, index) },
                    ]"
                  />
                </button>

                <!-- Direct Link Menu Item -->
                <router-link
                  v-else-if="item.path"
                  :to="item.path"
                  :class="[
                    'menu-item group',
                    {
                      'menu-item-active': isActive(item.path),
                      'menu-item-inactive': !isActive(item.path),
                    },
                    !isExpanded && !isHovered ? 'lg:justify-center' : '',
                  ]"
                >
                  <span
                    :class="[
                      isActive(item.path) ? 'menu-item-icon-active' : 'menu-item-icon-inactive',
                    ]"
                  >
                    <component :is="item.icon" />
                  </span>
                  <span
                    v-if="isExpanded || isHovered || isMobileOpen"
                    class="menu-item-text"
                    >{{ item.name }}</span
                  >
                </router-link>

                <!-- Submenu Transition -->
                <transition
                  @enter="startTransition"
                  @after-enter="endTransition"
                  @before-leave="startTransition"
                  @after-leave="endTransition"
                >
                  <div
                    v-show="
                      isSubmenuOpen(groupIndex, index) &&
                      (isExpanded || isHovered || isMobileOpen)
                    "
                    class="overflow-hidden transition-all duration-300"
                  >
                    <ul class="mt-2 space-y-1 ml-9">
                      <li v-for="subItem in item.subItems" :key="subItem.name">
                        <router-link
                          :to="subItem.path"
                          :class="[
                            'menu-dropdown-item',
                            {
                              'menu-dropdown-item-active': isActive(subItem.path),
                              'menu-dropdown-item-inactive': !isActive(subItem.path),
                            },
                          ]"
                        >
                          {{ subItem.name }}
                        </router-link>
                      </li>
                    </ul>
                  </div>
                </transition>
              </li>
            </ul>
          </div>
        </div>
      </nav>
      <SidebarWidget v-if="isExpanded || isHovered || isMobileOpen" />
    </div>
  </aside>
</template>

<script setup>
import { computed } from "vue"
import { useRoute } from "vue-router"
import { useSidebar } from "@/composables/useSidebar"

import {
  LayoutDashboardIcon,
  Calendar2Line,
  ListIcon,
  DocsIcon,
  ChevronDownIcon,
  HorizontalDots,
  UserGroupIcon,
  BoxIcon,
} from "../icons"

import SidebarWidget from "./SidebarWidget.vue"

const route = useRoute()
const { isExpanded, isMobileOpen, isHovered, openSubmenu } = useSidebar()

/**
 * Sidebar optimisé pour médecin
 */
const menuGroups = [
  {
    title: "Accueil",
    items: [
      {
        icon: LayoutDashboardIcon,
        name: "Tableau de bord",
        path: "/",
      },
    ],
  },
  {
    title: "Rendez-vous",
    items: [
      {
        icon: Calendar2Line,
        name: "Jours de travail",
        path: "/working-days",
      },
      {
        icon: ListIcon,
        name: "Rendez-vous",
        path: "/appointments",
      },
    ],
  },
  {
    title: "Patients",
    items: [
      {
        icon: UserGroupIcon,
        name: "Patients",
        path: "/patients",
      },
      {
        icon: DocsIcon,
        name: "Consultations",
        path: "/consultations",
      },
      {
        icon: DocsIcon,
        name: "Ordonnances",
        path: "/ordonnances",
      },
    ],
  },
  {
    title: "Médical",
    items: [
      {
        icon: BoxIcon,
        name: "Médicaments",
        path: "/medicaments",
      },
    ],
  },
]

// التحقق من الرابط النشط
const isActive = (path) => route.path === path

// فتح وغلق الـ Submenu عند الضغط
const toggleSubmenu = (groupIndex, itemIndex) => {
  const key = `${groupIndex}-${itemIndex}`
  openSubmenu.value = openSubmenu.value === key ? null : key
}

// التحقق إذا كان الرابط الفرعي لعنصر معين نشط حالياً (إصلاح البق القديم)
const isItemRouteActive = (item) => {
  if (!item.subItems) return false
  return item.subItems.some((subItem) => isActive(subItem.path))
}

// دالة ذكية للتحقق إن كان الـ Submenu مفتوحاً لهذا العنصر بالذات
const isSubmenuOpen = (groupIndex, itemIndex) => {
  const key = `${groupIndex}-${itemIndex}`
  const item = menuGroups[groupIndex].items[itemIndex]
  
  // يفتح إذا ضغط عليه الطبيب، أو إذا كان الرابط الداخلي تاعو هو النشط حالياً
  return openSubmenu.value === key || isItemRouteActive(item)
}

// انيميشن الترانزيشن (Smooth Expand/Collapse)
const startTransition = (el) => {
  el.style.height = "auto"
  const height = el.scrollHeight
  el.style.height = "0px"
  el.offsetHeight // Force repaint
  el.style.height = height + "px"
}

const endTransition = (el) => {
  el.style.height = ""
}
</script>

<style scoped>
.no-scrollbar::-webkit-scrollbar {
  display: none;
}
.no-scrollbar {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
</style>