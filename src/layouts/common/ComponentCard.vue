<template>
  <div
    :class="[
      'rounded-3xl border border-gray-100 bg-white shadow-sm dark:border-gray-800 dark:bg-white/[0.03]',
      className,
    ]"
  >


    <!-- Card Body -->
    <div class="p-4 border-t border-gray-100 dark:border-gray-800 sm:p-6">
      <div class="space-y-5">
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">

interface Props {
  title: string
  className?: string
  desc?: string
}

defineProps<Props>()
</script>
