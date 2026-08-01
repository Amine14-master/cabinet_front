import api from "./axios";
// ==========================================
// TO SCRIPT DEJA EXISTANT ... 
// ==========================================

export interface PrescriptionItemDetail {
  medicament_name: string;
  dosage: string;
  duration: string;
  frequency: string;
  instructions: string;
}

export interface OrdonnanceFullDetails {
  id: number;
  code: string;
  created_at: string;
  patient_name: string;
  patient_phone: string;
  appointment_code: string;
  symptoms: string;
  diagnosis: string;
  notes: string;
  items: PrescriptionItemDetail[];
}

// Récupérer les détails complets d'une ordonnance précise
export const getOrdonnanceDetail = async (code: string): Promise<OrdonnanceFullDetails> => {
  const res = await api.get(`appointments/ordonnance/${code}/`);
  return res.data;
}; 

// 🟢 ZID HADO DRK FI LA FIN DU FICHIER :
export interface DoctorOrdonnanceListItem {
  id: number;
  code: string;
  created_at: string;
  is_validated: boolean;
  patient_name: string;
  patient_code: string;
  appointment_code: string;
  items_count: number;
}

// Récupérer la liste des ordonnances du médecin connecté
export const getDoctorOrdonnances = async (): Promise<DoctorOrdonnanceListItem[]> => {
  const res = await api.get("appointments/doctor/ordonnances/my-list/");
  return res.data;
};

export const downloadOrdonnancePDF = async (code: string) => {
  const response = await api.get(
    `appointments/ordonnance/${code}/pdf/`,
    {
      responseType: "blob",
    }
  )

  return response.data
}

export interface CreateCustomMedicamentPayload {
  brand_name: string;
  dci_name: string;
  dosage: string;
  form: string;
}



export interface CustomMedicamentResponse {
  id: number;
  brand_name: string;
  dci_name: string;
  dosage: string;
}

export const createCustomMedicament = async (
  payload: CreateCustomMedicamentPayload
): Promise<CustomMedicamentResponse> => {
  const res = await api.post(
    "appointments/medicaments/add/",
    payload
  );

  return res.data;
};


