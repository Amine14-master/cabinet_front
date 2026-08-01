<template>
  <div v-if="loading" class="flex justify-center py-12">
    <span class="text-gray-500">Chargement...</span>
  </div>

  <div
    v-else-if="staff.length === 0"
    class="flex items-center justify-center py-16 text-gray-500"
  >
    Aucun membre de l'équipe.
  </div>

  <div
    v-else
    class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4"
  >
    <div
      v-for="member in staff"
      :key="member.code"
      class="p-5 bg-white border border-gray-200 rounded-2xl dark:bg-gray-900 dark:border-gray-800 shadow-theme-xs"
    >
      <!-- Header -->
      <div class="flex justify-between items-start mb-4">
        <div>
          <h3 class="font-semibold text-gray-800 dark:text-white">
            {{ member.first_name }} {{ member.last_name }}
          </h3>

          <p class="text-xs text-gray-500 dark:text-gray-400 mt-0.5">
            {{ member.role }}
          </p>
        </div>

        <span
          :class="[
            'px-2.5 py-1 rounded-lg text-[10px] font-medium uppercase tracking-wider',
            member.is_active
              ? 'bg-green-50 text-green-600 dark:bg-green-900/20 dark:text-green-400'
              : 'bg-red-50 text-red-600 dark:bg-red-900/20 dark:text-red-400'
          ]"
        >
          {{ member.is_active ? "Actif" : "Inactif" }}
        </span>
      </div>

      <!-- Footer -->
      <div
        class="pt-4 border-t border-gray-100 dark:border-gray-800 flex justify-between items-center"
      >
        <button
          @click="openDetails(member.code)"
          class="text-xs text-brand-500 font-medium hover:text-brand-600"
        >
          Voir détails
        </button>

        <div class="flex gap-3">
          <!-- Edit -->
          <button
            @click="editMember(member.code)"
            class="text-gray-400 hover:text-brand-500 transition-colors"
          >
            <svg
              width="16"
              height="16"
              viewBox="0 0 16 16"
              fill="none"
            >
              <path
                d="M11.333 2.667L13.333 4.667L4.667 13.333H2.667V11.333L11.333 2.667Z"
                stroke="currentColor"
                stroke-width="1.5"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </svg>
          </button>

          <!-- Delete -->
<button
  @click="toggleStatus(member)"
  :class="[
    'transition-colors',
    member.is_active
      ? 'text-gray-400 hover:text-red-500'
      : 'text-gray-400 hover:text-green-500'
  ]"
>
  <!-- active => تعطيل -->
  <svg
    v-if="member.is_active"
    width="16"
    height="16"
    viewBox="0 0 16 16"
    fill="none"
  >
    <path
      d="M8 2V8M4.5 4.5A5 5 0 1 0 11.5 4.5"
      stroke="currentColor"
      stroke-width="1.5"
    />
  </svg>

  <!-- inactive => تفعيل -->
  <svg
    v-else
    width="16"
    height="16"
    viewBox="0 0 16 16"
    fill="none"
  >
    <path
      d="M13 8A5 5 0 1 1 8 3"
      stroke="currentColor"
      stroke-width="1.5"
    />
    <path
      d="M8 1V5H12"
      stroke="currentColor"
      stroke-width="1.5"
    />
  </svg>

</button>
        </div>
      </div>
    </div>
  </div>
 <Modal
  v-if="showAddModal"
  @close="showAddModal = false"
>
  <template #body>

    <div
      class="relative w-full max-w-xl rounded-3xl bg-white dark:bg-gray-900 shadow-2xl"
    >

      <div class="border-b p-6">
        <h2 class="text-xl font-semibold">
          Ajouter un membre
        </h2>

        <p class="text-sm text-gray-500 mt-1">
          Ajouter un secrétaire ou assistant.
        </p>
      </div>

      <div class="p-6 space-y-5">

        <div>
          <label class="block text-sm mb-2">
            Prénom
          </label>

          <input
            v-model="form.first_name"
            class="w-full rounded-xl border px-4 py-3"
          />
        </div>

        <div>
          <label class="block text-sm mb-2">
            Nom
          </label>

          <input
            v-model="form.last_name"
            class="w-full rounded-xl border px-4 py-3"
          />
        </div>
      <div>
        <label>Email</label>

        <input
          v-model="form.email"
          type="email"
          class="w-full rounded-xl border px-4 py-3"
        />
      </div>

      <div>
        <label>Téléphone</label>

        <input
          v-model="form.phone"
          class="w-full rounded-xl border px-4 py-3"
        />
      </div>
        <div>
          <label class="block text-sm mb-2">
            Rôle
          </label>

          <select
            v-model="form.role"
            class="w-full rounded-xl border px-4 py-3"
          >
            <option value="SECRETARY">
              Secrétaire
            </option>

            <option value="ASSISTANT">
              Assistant(e)
            </option>
          </select>
        </div>

        <div class="flex items-center gap-3">

          <input
            type="checkbox"
            v-model="form.is_active"
          >

          <span>Actif</span>

        </div>

      </div>

      <div
        class="flex justify-end gap-3 border-t p-6"
      >
        <button
          @click="showAddModal = false"
          class="px-5 py-2 rounded-xl border"
        >
          Annuler
        </button>

        <button
          @click="saveMember"
          class="px-5 py-2 rounded-xl bg-brand-500 text-white"
        >
          Ajouter
        </button>

      </div>

    </div>

  </template>
</Modal>
<Modal
  v-if="showEditModal"
  @close="showEditModal = false"
>
  <template #body>

    <div class="relative w-full max-w-xl rounded-3xl bg-white dark:bg-gray-900 shadow-2xl">

      <div class="border-b p-6">
        <h2 class="text-xl font-semibold">
          Modifier le membre
        </h2>
      </div>


      <div class="p-6 space-y-5">

        <input
          v-model="form.first_name"
          class="w-full rounded-xl border px-4 py-3"
          placeholder="Prénom"
        />

        <input
          v-model="form.last_name"
          class="w-full rounded-xl border px-4 py-3"
          placeholder="Nom"
        />

        <input
          v-model="form.email"
          class="w-full rounded-xl border px-4 py-3"
          placeholder="Email"
        />

        <input
          v-model="form.phone"
          class="w-full rounded-xl border px-4 py-3"
          placeholder="Téléphone"
        />


        <select
          v-model="form.role"
          class="w-full rounded-xl border px-4 py-3"
        >
          <option value="SECRETARY">
            Secrétaire
          </option>

          <option value="ASSISTANT">
            Assistant(e)
          </option>

        </select>


        <label class="flex gap-3 items-center">

          <input
            type="checkbox"
            v-model="form.is_active"
          />

          Actif

        </label>


      </div>


      <div class="flex justify-end gap-3 border-t p-6">

        <button
          @click="showEditModal=false"
          class="px-5 py-2 rounded-xl border"
        >
          Annuler
        </button>


        <button
          @click="saveEditMember"
          class="px-5 py-2 rounded-xl bg-brand-500 text-white"
        >
          Enregistrer
        </button>

      </div>

    </div>

  </template>
</Modal>
<Transition name="slide">
  <div v-if="showDetails && selectedMember" class="fixed inset-0 z-50 overflow-hidden">
    <!-- Overlay -->
    <div class="absolute inset-0 bg-black/50 backdrop-blur-sm" @click="closeDetails"></div>

    <!-- Drawer Panel -->
    <div class="absolute right-0 top-0 h-full w-full max-w-lg bg-white dark:bg-gray-900 shadow-2xl flex flex-col transform transition-transform">
      
      <!-- Header -->
      <div class="px-6 py-5 border-b dark:border-gray-800 flex justify-between items-center bg-gray-50/50 dark:bg-gray-900/50">
        <h2 class="text-lg font-bold text-gray-800 dark:text-white">Détails du membre</h2>
        <button @click="closeDetails" class="p-2 hover:bg-gray-200 dark:hover:bg-gray-800 rounded-full transition-colors">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
        </button>
      </div>

      <!-- Scrollable Body -->
      <div class="flex-1 overflow-y-auto p-6 space-y-8">
        
        <!-- Profile Section -->
        <div class="flex items-center gap-4">
          <div class="w-16 h-16 rounded-2xl bg-brand-100 text-brand-600 flex items-center justify-center text-xl font-bold border border-brand-200">
            {{ selectedMember.first_name.charAt(0) }}{{ selectedMember.last_name.charAt(0) }}
          </div>
          <div>
            <h3 class="text-xl font-bold text-gray-900 dark:text-white">{{ selectedMember.first_name }} {{ selectedMember.last_name }}</h3>
            <span class="inline-block px-2 py-0.5 rounded-md bg-gray-100 dark:bg-gray-800 text-xs font-medium text-gray-600">{{ selectedMember.role }}</span>
          </div>
        </div>

        <!-- Info Grid -->
        <div class="grid grid-cols-2 gap-4">
          <div class="p-4 rounded-2xl bg-gray-50 dark:bg-gray-800/50 border dark:border-gray-800">
            <p class="text-[10px] uppercase tracking-wider text-gray-400 font-bold mb-1">Email</p>
            <p class="text-sm font-semibold truncate">{{ selectedMember.email || "Non renseigné" }}</p>
          </div>
          <div class="p-4 rounded-2xl bg-gray-50 dark:bg-gray-800/50 border dark:border-gray-800">
            <p class="text-[10px] uppercase tracking-wider text-gray-400 font-bold mb-1">Téléphone</p>
            <p class="text-sm font-semibold">{{ selectedMember.phone || "Non renseigné" }}</p>
          </div>
        </div>

        <!-- Permissions Section -->
        <div>
          <h4 class="font-bold text-gray-900 dark:text-white mb-4">
            Permissions
          </h4>

          <div class="space-y-3">

            <div
              v-for="permission in permissions"
              :key="permission.key"
              class="flex justify-between items-center p-3 border rounded-xl"
            >

              <span>
                {{ permission.label }}
              </span>

              <input
                type="checkbox"
                v-model="permission.enabled"
              />

            </div>

          </div>

          <button
            @click="savePermissions"
            class="mt-5 w-full py-3 rounded-xl bg-brand-500 text-white"
          >
            Enregistrer les permissions
          </button>

        </div>
      </div>

      <!-- Fixed Footer -->
      <div class="p-6 border-t dark:border-gray-800 bg-white dark:bg-gray-900">
        <button @click="closeDetails" class="w-full py-3 rounded-xl bg-gray-900 dark:bg-white text-white dark:text-gray-900 font-semibold hover:opacity-90 transition-opacity">
          Fermer
        </button>
      </div>
    </div>
  </div>
</Transition>
</template>

<script setup lang="ts">
import { ref, onMounted,reactive  } from "vue";
import Modal from "./Modal.vue"
import {
  getStaff,
  getStaffDetail,
  deleteStaff,
  createStaff ,
  updateStaff,
  getStaffPermissions,
  updateStaffPermissions
} from "@/api/staffService";
import type { Staff, StaffCreateUpdate } from "@/api/staffService";
const showAddModal = ref(false);
const showEditModal = ref(false);
const editingCode = ref("");
const selectedMember = ref<any>(null);
const showDetails = ref(false);
const permissions = ref<any[]>([]);
const permissionCode = ref("");
const form = reactive<StaffCreateUpdate>({
  first_name: "",
  last_name: "",
  email: "",
  phone: "",
  role: "SECRETARY",
  is_active: true,
});
const staff = ref<Staff[]>([]);
const loading = ref(false);

const fetchStaff = async () => {
  loading.value = true;

  try {
    staff.value = await getStaff();
  } catch (error) {
    console.error(error);
  } finally {
    loading.value = false;
  }
};
const openDetails = async (code: string) => {
  try {
    selectedMember.value = await getStaffDetail(code);

    permissions.value = selectedMember.value.permissions || [];

    permissionCode.value = code;

    showDetails.value = true;

  } catch(error){
    console.error(error);
  }
};
const savePermissions = async () => {
  const payload = Object.fromEntries(
    permissions.value.map(p => [
      p.key,
      p.enabled
    ])
  );

  await updateStaffPermissions(
    permissionCode.value,
    payload
  );
};
const closeDetails = () => {
  showDetails.value = false;

  setTimeout(() => {
    selectedMember.value = null;
  }, 250);
};

const editMember = async (code: string) => {
  try {
    const member = await getStaffDetail(code);

    editingCode.value = code;

    Object.assign(form, {
      first_name: member.first_name,
      last_name: member.last_name,
      email: member.email || "",
      phone: member.phone || "",
      role: member.role,
      is_active: member.is_active,
    });

    showEditModal.value = true;

  } catch (error) {
    console.error(error);
  }
};
const saveEditMember = async () => {
  try {
    await updateStaff(
      editingCode.value,
      form
    );

    showEditModal.value = false;

    await fetchStaff();

  } catch(error) {
    console.error(error);
  }
};

const toggleStatus = async (member: Staff) => {
  try {
    await updateStaff(member.code, {
      first_name: member.first_name,
      last_name: member.last_name,
      email: member.email,
      phone: member.phone,
      role: member.role.includes("Assistant")
        ? "ASSISTANT"
        : "SECRETARY",
      is_active: !member.is_active,
    });

    await fetchStaff();

  } catch (error) {
    console.error(error);
  }
};
const removeMember = async (code: string) => {
  console.log("delete code:", code);

  try {
    const res = await deleteStaff(code);
    console.log("delete response:", res);

    await fetchStaff();

  } catch (error:any) {
    console.log("delete error:", error.response?.data || error);
  }
};
const openAddMemberModal = () => {
  showAddModal.value = true;
};

const saveMember = async () => {
  try {
    await createStaff(form);

    showAddModal.value = false;

    form.first_name = "";
    form.last_name = "";
    form.role = "SECRETARY";
    form.is_active = true;

    await fetchStaff();
  } catch (err) {
    console.error(err);
  }
};

onMounted(fetchStaff);

defineExpose({
  fetchStaff,
  openAddMemberModal,
});
const slots = defineSlots<{
  body(): any
}>();


</script>

<style scoped>
/* Conserve tes styles d'animation et scrollbars */
.slide-enter-active, .slide-leave-active { 
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1); 
}
.slide-enter-from, .slide-leave-to { 
  transform: translateX(100%); 
}
.custom-scrollbar::-webkit-scrollbar { height: 5px; width: 5px; }
.custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
.custom-scrollbar::-webkit-scrollbar-thumb { background: #e4e4e7; border-radius: 10px; }
.dark .custom-scrollbar::-webkit-scrollbar-thumb { background: #27272a; }
</style>