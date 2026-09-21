import api from './axios'

export type Period = 'morning' | 'afternoon'

export type WorkingDayPayload = {
  day: 'sunday' | 'monday' | 'tuesday' | 'wednesday' | 'thursday' | 'friday' | 'saturday'
  period: Period
  start_time: string
  end_time: string
  max_patients: number
}

export type OverridePayload = {
  date: string
  period: Period
  start_time?: string
  end_time?: string
  max_patients?: number
  is_closed: boolean
}

/* ================= WORKING DAYS (FIXED) ================= */
export const getWorkingDays = async () => {
  const { data } = await api.get('appointments/working-days/')
  return data
}

export const createWorkingDay = async (payload: WorkingDayPayload) => {
  const { data } = await api.post('appointments/working-days/', payload)
  return data
}

// (Update)
export const updateWorkingDay = async (id: number, payload: Partial<WorkingDayPayload>) => {
  const { data } = await api.put(`appointments/working-days/${id}/`, payload)
  return data
}

//   (Delete)
export const deleteWorkingDay = async (id: number) => {
  await api.delete(`appointments/working-days/${id}/`)
}

/* ================= OVERRIDES (EXCEPTIONS) ================= */
export const getOverrides = async () => {
  const { data } = await api.get('appointments/working-day-overrides/')
  return data
}

export const createOverride = async (payload: OverridePayload) => {
  const { data } = await api.post('appointments/working-day-overrides/', payload)
  return data
}

//   (Update)
export const updateOverride = async (id: number, payload: Partial<OverridePayload>) => {
  const { data } = await api.put(`appointments/overrides/${id}/`, payload)
  return data
}

//   (Delete)
export const deleteOverride = async (id: number) => {
  await api.delete(`appointments/overrides/${id}/`)
}
