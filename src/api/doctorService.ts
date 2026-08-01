// api/doctorService.ts

import api from "./axios";

export interface CabinetUpdate {
  name?: string;
  address?: string;
  phone?: string;
  email?: string;
  website?: string;
  wilaya?: string;
  commune?: string;
  maps_link?: string;

}

export interface DoctorProfileUpdate {
  first_name?: string;
  last_name?: string;
  first_name_ar?: string;
  last_name_ar?: string;
  experience_years?: string;
  consultation_price?: string;
  gender?: "M" | "F";

  speciality?: string;

  cabinet?: CabinetUpdate;

  photo?: File;

  bio?: string;
  facebook?: string;
  instagram?: string;
  email_public?: string;
  phone?: string;
}

export const getDoctorProfile = async () => {
  const response = await api.get("doctors/profile/update/");
  return response.data;
};


export const updateDoctorProfile = async (
  doctorData: DoctorProfileUpdate
) => {
  try {
    const formData = new FormData();

    Object.entries(doctorData).forEach(([key, value]) => {
      if (value === null || value === undefined) return;

      if (key === "cabinet") {
        Object.entries(value as CabinetUpdate).forEach(([cabKey, cabValue]) => {
          if (cabValue !== null && cabValue !== undefined) {
            formData.append(`cabinet.${cabKey}`, String(cabValue));
          }
        });
      } else if (key === "photo") {
        formData.append("photo", value as File);
      } else {
        formData.append(key, String(value));
      }
    });

    const response = await api.put(
      "doctors/profile/update/",
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }
    );

    return response.data;
  } catch (error: any) {
    throw (
      error.response?.data ||
      "Erreur lors de la mise à jour du profil médecin"
    );
  }
};

export const getSpecialities = async () => {
  const response = await api.get("doctors/specialities/")
  return response.data
}