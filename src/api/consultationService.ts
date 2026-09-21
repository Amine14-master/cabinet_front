import api from './axios'

export interface Consultation {
  id: number
  appointment: number | null
  appointment_code: string | null
  appointment_date: string | null

  doctor: number
  doctor_name: string

  patient: number
  patient_name: string
  patient_code: string
  patient_phone: string

  symptoms: string
  diagnosis: string
  prescription: string
  notes: string

  created_at: string
}

export interface CreateConsultationData {
  appointment_code: string // Required - must come from appointment
  symptoms?: string
  diagnosis?: string
  prescription?: string
  notes?: string
}

export interface AppointmentForConsultation {
  code: string
  patient_name: string
  patient_code: string
  patient_phone: string
  appointment_date: string
  period: string
  status: string
}

export const getDoctorConsultations = async (searchQuery = ''): Promise<Consultation[]> => {
  const res = await api.get('appointments/consultations/', {
    params: { search: searchQuery },
  })
  return res.data
}

export const getConsultationDetails = async (id: number | string): Promise<Consultation> => {
  const res = await api.get(`appointments/consultations/${id}/`)
  return res.data
}

// Get appointment details to pre-fill consultation form
export const getAppointmentForConsultation = async (
  appointmentCode: string,
): Promise<AppointmentForConsultation> => {
  const res = await api.get(`appointments/consultations/appointment/${appointmentCode}/`)
  return res.data
}

// Create consultation from existing appointment
export const createConsultation = async (data: CreateConsultationData): Promise<any> => {
  const res = await api.post('appointments/consultations/create/', data)
  return res.data
}

export interface MedicamentSearchResult {
  id: number
  brand_name: string
  dci_name: string
  dosage: string
  form: string
}

export const searchMedicaments = async (query: string): Promise<MedicamentSearchResult[]> => {
  const { data } = await api.get('appointments/medicaments/search/', {
    params: {
      q: query,
    },
  })

  return data
}

export interface DoctorMedicament {
  id: number
  brand_name: string
  dci_name: string
  dosage: string
  form: string
  is_custom: boolean
}

export const getDoctorMedicaments = async (): Promise<DoctorMedicament[]> => {
  const { data } = await api.get('appointments/medicaments/doctor/')

  return data
}

export const updateMedicament = async (id: number, data: any) => {
  const res = await api.put(`appointments/medicaments/${id}/`, data)

  return res.data
}

export const deactivateMedicament = async (id: number) => {
  await api.delete(`appointments/medicaments/${id}/deactivate/`)
}
