// api/appointmentService.ts
import api from './axios'

export const getDoctorAppointments = async (params = {}) => {
  const res = await api.get('appointments/doctor-appointments/', { params })
  return res.data
}

export const updateAppointmentStatus = async (
  code: string,
  status: 'scheduled' | 'completed' | 'cancelled',
) => {
  const res = await api.patch(`appointments/${code}/`, { status })
  return res.data
}

// Add patient search function
export const searchPatients = async (query: string) => {
  try {
    const res = await api.get(`appointments/patients/search/?search=${encodeURIComponent(query)}`)
    return res.data
  } catch (err: any) {
    console.log('❌ Search error:', err.response?.data)
    throw err
  }
}

/**
 * DOCTOR creates appointment (Scenario 1 & 2)
 * - If patient_code is provided: use existing patient
 * - If no patient_code: create new patient with provided info
 */
export const createDoctorAppointment = async (data: {
  appointment_date: string
  period: 'morning' | 'afternoon'
  patient_code?: string | null
  patient_first_name?: string
  patient_last_name?: string
  patient_phone?: string
}) => {
  console.log('📤 Sending:', data)

  try {
    const res = await api.post('appointments/doctor-appointments/create/', data)
    console.log('📥 Success:', res.data)
    return res.data
  } catch (err: any) {
    console.log('❌ ERROR STATUS:', err.response?.status)
    console.log('❌ ERROR DATA:', err.response?.data)
    throw err
  }
}

// api/appointmentService.ts

export interface AvailableSlot {
  date: string
  day: string
  period: string
  available_slots: number
  total_slots: number
}

export const getAvailableSlots = async (period: string = 'morning'): Promise<AvailableSlot[]> => {
  try {
    const res = await api.get(`appointments/available-slots/`, { params: { period } })
    return res.data.available_slots
  } catch (err: any) {
    console.error('Error fetching available slots:', err)
    throw err
  }
}

export const getNearestAvailableDate = async (period: string = 'morning'): Promise<string> => {
  try {
    const res = await api.get(`appointments/nearest-available-date/`, { params: { period } })
    return res.data.available_date
  } catch (err: any) {
    console.error('Error fetching nearest date:', err)
    throw err
  }
}
