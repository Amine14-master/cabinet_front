//  api/patientsService.ts

import api from "./axios";

export const getDoctorPatients = async (params = {}) => {
  const res = await api.get("patients/doctor-patients/", {
    params
  })

  return res.data      
}


export const getPatientByCode = async (code: string) => {
  const res = await api.get(`patients/doctor-patient/${code}/`);
  return res.data;
};

export const updatePatientStatus = async (code: string, status: string) => {
  const response = await api.patch(`patients/${code}/update/`, { status });
  return response.data;
};

export const createPatientManual = async (patientData: any) => {
  try {
    const response = await api.post(`patients/manual-create/`, patientData);
    return response.data;
  } catch (error: any) {

    throw error.response?.data || "Erreur lors de la création du patient";
  }}

export const getDoctorPatientProfile = async (code: string) => {
  const res = await api.get(`patients/doctor-patient/${code}/profile/`);
  return res.data;
};