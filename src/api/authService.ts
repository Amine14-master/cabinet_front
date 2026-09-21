//  api/authService.ts

import api from './axios'

export const login = async (credentials: { email: string; password: any }) => {
  try {
    const response = await api.post('users/login/', credentials)

    // Si Django renvoie un token (ex: access_token ou token)
    if (response.data.access && response.data.refresh) {
      localStorage.setItem('access', response.data.access)
      localStorage.setItem('refresh', response.data.refresh)
      localStorage.setItem('username', response.data.username)
      localStorage.setItem('doctor_code', response.data.doctor_code)
    }

    return response.data
  } catch (error: any) {
    // On propage l'erreur pour la gérer dans le composant
    throw error.response?.data || 'Une erreur est survenue lors de la connexion'
  }
}

export const register = async (data: {
  firstName: string
  lastName: string
  email: string
  password: any
}) => {
  try {
    const response = await api.post('users/register/', data)

    if (response.data.access && response.data.refresh) {
      localStorage.setItem('access', response.data.access)
      localStorage.setItem('refresh', response.data.refresh)
      localStorage.setItem('username', response.data.username)
      localStorage.setItem('doctor_code', response.data.doctor_code)
    }

    return response.data
  } catch (error: any) {
    throw error.response?.data || "Une erreur est survenue lors de l'inscription"
  }
}
