<template>
  <div class="space-y-6 p-1">
    <div
      class="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between bg-white p-4 rounded-xl border border-gray-100 shadow-sm"
    >
      <div class="relative flex-1 max-w-md">
        <span class="absolute inset-y-0 left-0 flex items-center pl-3.5 text-gray-400">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="w-4 h-4"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
            />
          </svg>
        </span>
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Rechercher un médicament (nom, DCI...)"
          class="w-full rounded-lg border border-gray-200 py-2 pl-10 pr-4 text-sm focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none"
        />
      </div>

      <div
        class="px-4 py-2 bg-indigo-50 rounded-lg text-xs font-bold text-indigo-700 uppercase tracking-wider"
      >
        {{ filteredData.length }} Médicaments
      </div>
    </div>

    <div class="overflow-hidden rounded-xl border border-gray-100 bg-white shadow-sm">
      <table class="min-w-full table-fixed">
        <thead class="bg-gray-50 border-b border-gray-100">
          <tr>
            <th class="px-6 py-4 text-left text-xs font-bold text-gray-400 uppercase">
              Médicament
            </th>
            <th class="px-6 py-4 text-left text-xs font-bold text-gray-400 uppercase">DCI</th>
            <th class="px-6 py-4 text-left text-xs font-bold text-gray-400 uppercase">Forme</th>
            <th class="px-6 py-4 text-left text-xs font-bold text-gray-400 uppercase">Dosage</th>
            <th class="px-6 py-4 text-center text-xs font-bold text-gray-400 uppercase">Actions</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-100">
          <tr v-if="loading" class="text-center">
            <td colspan="5" class="py-10 text-sm text-gray-500 italic">Chargement en cours...</td>
          </tr>
          <tr
            v-else
            v-for="item in paginatedData"
            :key="item.id"
            class="hover:bg-gray-50/80 transition-colors"
          >
            <td class="px-6 py-4 text-sm font-semibold text-gray-900">{{ item.brand_name }}</td>
            <td class="px-6 py-4 text-sm text-gray-600">{{ item.dci_name }}</td>
            <td class="px-6 py-4 text-sm text-gray-600">{{ item.form }}</td>
            <td class="px-6 py-4 text-sm text-gray-600">{{ item.dosage || '-' }}</td>
            <td class="px-6 py-4 flex justify-center gap-2">
              <button
                @click="openEditDrawer(item)"
                class="px-3 py-1 text-xs font-medium rounded-lg bg-gray-100 hover:bg-gray-200 text-gray-700"
              >
                Modifier
              </button>
              <button
                @click="deleteMedicament(item)"
                class="px-3 py-1 text-xs font-medium rounded-lg bg-red-50 text-red-600 hover:bg-red-100"
              >
                Supprimer
              </button>
            </td>
          </tr>
        </tbody>
      </table>

      <div
        v-if="filteredData.length > 0"
        class="flex items-center justify-between px-6 py-4 border-t border-gray-100 bg-gray-50/20"
      >
        <div class="text-xs text-gray-400">
          Affichage de {{ startIndex + 1 }} à {{ Math.min(endIndex, filteredData.length) }} sur
          {{ filteredData.length }} résultats
        </div>
        <div class="flex items-center gap-2">
          <button
            @click="prevPage"
            :disabled="currentPage === 1"
            class="px-3 py-1.5 text-xs font-medium rounded-lg border bg-white hover:bg-gray-50 disabled:opacity-50"
          >
            Précédent
          </button>
          <span class="text-xs font-medium text-gray-500"
            >{{ currentPage }} / {{ totalPages }}</span
          >
          <button
            @click="nextPage"
            :disabled="currentPage === totalPages"
            class="px-3 py-1.5 text-xs font-medium rounded-lg border bg-white hover:bg-gray-50 disabled:opacity-50"
          >
            Suivant
          </button>
        </div>
      </div>
    </div>

    <Transition name="slide">
      <div v-if="selectedMedicament" class="fixed inset-0 z-50 flex justify-end">
        <div class="absolute inset-0 bg-black/20 backdrop-blur-sm" @click="closeEditDrawer"></div>
        <div class="relative w-full max-w-sm bg-white shadow-2xl flex flex-col h-full">
          <div class="p-5 border-b flex justify-between items-center bg-gray-50/50">
            <h2 class="text-base font-bold text-gray-800">Modifier le médicament</h2>
            <button @click="closeEditDrawer" class="text-gray-400 hover:text-gray-600">✕</button>
          </div>
          <div class="p-5 flex-1 space-y-4 overflow-y-auto">
            <div>
              <label class="block text-xs font-bold text-gray-500 uppercase mb-1"
                >Nom du médicament</label
              >
              <input
                v-model="selectedMedicament.brand_name"
                class="w-full p-2.5 border rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none"
              />
            </div>
            <div>
              <label class="block text-xs font-bold text-gray-500 uppercase mb-1">DCI</label>
              <input
                v-model="selectedMedicament.dci_name"
                class="w-full p-2.5 border rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none"
              />
            </div>
            <div>
              <label class="block text-xs font-bold text-gray-500 uppercase mb-1">Forme</label>
              <input
                v-model="selectedMedicament.form"
                class="w-full p-2.5 border rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none"
              />
            </div>
            <div>
              <label class="block text-xs font-bold text-gray-500 uppercase mb-1">Dosage</label>
              <input
                v-model="selectedMedicament.dosage"
                class="w-full p-2.5 border rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none"
              />
            </div>
          </div>
          <div class="p-5 border-t bg-gray-50 flex gap-3">
            <button
              @click="closeEditDrawer"
              class="flex-1 py-2.5 rounded-lg text-sm font-medium border text-gray-600 hover:bg-gray-100"
            >
              Annuler
            </button>
            <button
              @click="saveChanges"
              :disabled="isSaving"
              class="flex-1 bg-blue-600 text-white py-2.5 rounded-lg text-sm font-bold hover:bg-blue-700 disabled:opacity-50"
            >
              {{ isSaving ? 'Enregistrement...' : 'Enregistrer' }}
            </button>
          </div>
        </div>
      </div>
    </Transition>

    <Transition name="fade">
      <div
        v-if="itemToDelete"
        class="fixed inset-0 z-[60] flex items-center justify-center p-4 bg-black/40 backdrop-blur-sm"
      >
        <div class="bg-white rounded-xl shadow-xl w-full max-w-sm p-6 space-y-4">
          <h3 class="font-bold text-lg text-gray-800">Confirmer la suppression</h3>
          <p class="text-sm text-gray-600">
            Êtes-vous sûr de vouloir supprimer <strong>{{ itemToDelete.brand_name }}</strong> ?
          </p>
          <div class="flex gap-3 mt-6">
            <button
              @click="itemToDelete = null"
              class="flex-1 py-2 rounded-lg text-sm font-medium border hover:bg-gray-50"
            >
              Annuler
            </button>
            <button
              @click="confirmDelete"
              class="flex-1 py-2 rounded-lg text-sm font-bold bg-red-600 text-white hover:bg-red-700"
            >
              Supprimer
            </button>
          </div>
        </div>
      </div>
    </Transition>

    <div
      v-if="showCustomModal"
      class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/50 backdrop-blur-sm"
    >
      <div class="bg-white rounded-xl shadow-2xl w-full max-w-md p-6 space-y-4">
        <h2 class="text-lg font-bold text-gray-800">Ajouter un nouveau médicament</h2>
        <div class="space-y-3">
          <div>
            <label class="text-xs font-bold text-gray-500 uppercase">Nom</label
            ><input
              v-model="customMedicament.brand_name"
              class="w-full p-2 border rounded-lg text-sm"
            />
          </div>
          <div>
            <label class="text-xs font-bold text-gray-500 uppercase">DCI</label
            ><input
              v-model="customMedicament.dci_name"
              class="w-full p-2 border rounded-lg text-sm"
            />
          </div>
          <div>
            <label class="text-xs font-bold text-gray-500 uppercase">Forme</label
            ><input v-model="customMedicament.form" class="w-full p-2 border rounded-lg text-sm" />
          </div>
          <div>
            <label class="text-xs font-bold text-gray-500 uppercase">Dosage</label
            ><input
              v-model="customMedicament.dosage"
              class="w-full p-2 border rounded-lg text-sm"
            />
          </div>
        </div>
        <div class="flex gap-3 mt-6">
          <button @click="showCustomModal = false" class="flex-1 py-2 border rounded-lg text-sm">
            Annuler
          </button>
          <button
            @click="saveCustomMedicament"
            class="flex-1 py-2 bg-blue-600 text-white rounded-lg text-sm font-bold"
          >
            Enregistrer
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, reactive, defineExpose, watch } from 'vue'
import {
  getDoctorMedicaments,
  updateMedicament,
  deactivateMedicament,
} from '@/api/consultationService'
import { createCustomMedicament } from '@/api/ordonnaceService'

const medicaments = ref([])
const searchQuery = ref('')
const loading = ref(true)
const isSaving = ref(false)
const selectedMedicament = ref(null)
const itemToDelete = ref(null)
const showCustomModal = ref(false)
const customMedicament = reactive({ brand_name: '', dci_name: '', dosage: '', form: '' })

// Pagination
const currentPage = ref(1)
const itemsPerPage = ref(8)

const fetchData = async () => {
  loading.value = true
  try {
    medicaments.value = await getDoctorMedicaments()
  } catch (e) {
    console.error(e)
  } finally {
    loading.value = false
  }
}

const openCustomMedicamentModal = () => {
  showCustomModal.value = true
}
defineExpose({ openCustomMedicamentModal })

const saveCustomMedicament = async () => {
  try {
    await createCustomMedicament(customMedicament)
    await fetchData()
    showCustomModal.value = false
  } catch (e) {
    alert('Erreur')
  }
}

const openEditDrawer = (item) => (selectedMedicament.value = { ...item })
const closeEditDrawer = () => (selectedMedicament.value = null)

const saveChanges = async () => {
  isSaving.value = true
  try {
    await updateMedicament(selectedMedicament.value.id, selectedMedicament.value)
    await fetchData()
    closeEditDrawer()
  } catch (e) {
    alert('Erreur')
  } finally {
    isSaving.value = false
  }
}

const deleteMedicament = (item) => {
  itemToDelete.value = item
}
const confirmDelete = async () => {
  try {
    await deactivateMedicament(itemToDelete.value.id)
    await fetchData()
  } finally {
    itemToDelete.value = null
  }
}

const filteredData = computed(() => {
  const q = searchQuery.value.toLowerCase()
  return medicaments.value.filter(
    (m) => m.brand_name?.toLowerCase().includes(q) || m.dci_name?.toLowerCase().includes(q),
  )
})

const totalPages = computed(() => Math.ceil(filteredData.value.length / itemsPerPage.value) || 1)
const startIndex = computed(() => (currentPage.value - 1) * itemsPerPage.value)
const endIndex = computed(() => startIndex.value + itemsPerPage.value)
const paginatedData = computed(() => filteredData.value.slice(startIndex.value, endIndex.value))

const nextPage = () => {
  if (currentPage.value < totalPages.value) currentPage.value++
}
const prevPage = () => {
  if (currentPage.value > 1) currentPage.value--
}

watch(searchQuery, () => {
  currentPage.value = 1
})
onMounted(fetchData)
</script>

<style scoped>
.slide-enter-active,
.slide-leave-active {
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.slide-enter-from,
.slide-leave-to {
  transform: translateX(100%);
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
