// api/staffService.ts

import api from "./axios";

export interface Staff {
  code: string;
  first_name: string;
  last_name: string;
  email: string;
  phone: string;
  role: string;
  doctor_name: string | null;
  is_active: boolean;
}

export interface StaffCreateUpdate {
  first_name: string;
  last_name: string;
  email: string;
  phone: string;
  role: "SECRETARY" | "ASSISTANT";
  works_with?: string | null;
  is_active?: boolean;
}

export interface StaffPermission {
  manage_patients: boolean;
  manage_appointments: boolean;
  manage_schedule: boolean;
  manage_invoices: boolean;
  view_statistics: boolean;
  manage_settings: boolean;
}

export const getStaff = async () => {
  const response = await api.get("doctors/staff/");
  return response.data;
};

export const createStaff = async (data: StaffCreateUpdate) => {
  const response = await api.post("doctors/staff/create/", data);
  return response.data;
};

export const getStaffDetail = async (code: string) => {
  const response = await api.get(`doctors/staff/${code}/`);
  return response.data;
};

export const updateStaff = async (
  code: string,
  data: StaffCreateUpdate
) => {
  const response = await api.put(
    `doctors/staff/${code}/`,
    data
  );

  return response.data;
};

export const deleteStaff = async (code: string) => {
  const response = await api.delete(
    `doctors/staff/${code}/deactivate/`
  );

  return response.data;
};

export const getStaffPermissions = async (code: string) => {
  const response = await api.get(
    `doctors/staff/${code}/permissions/`
  );

  return response.data;
};

export const updateStaffPermissions = async (
  code: string,
  data: StaffPermission
) => {
  const response = await api.put(
    `doctors/staff/${code}/permissions/`,
    data
  );

  return response.data;
};