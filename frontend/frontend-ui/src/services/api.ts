import axios from 'axios'
import type { AnchorData, BookingData, CheckInData, ForecastData, OnboardingData } from '../types/app'

const baseURL = import.meta.env.VITE_API_BASE_URL || ''

const client = axios.create({
  baseURL,
})

const mockForecast: ForecastData = {
  status: 'Amber',
  scores: [24, 28, 35, 42, 51, 58, 62],
  summary: "You've been in Amber for 3 days. Time to act.",
}

const mockAnchor: AnchorData = {
  name: 'Aanya P.',
  role: 'Final year CS',
  story: 'Survived a tough job search season and built a repeatable reset plan.',
  tags: ['Job rejection', 'Final year CS', 'Startup stress'],
  initials: 'AP',
}

const mockSlots = ['9:00 AM', '11:00 AM', '1:30 PM', '3:00 PM', '5:30 PM']

export async function saveOnboarding(data: OnboardingData) {
  if (!baseURL) return { ok: true }
  try {
    await client.post('/onboarding', data)
    return { ok: true }
  } catch {
    return { ok: false }
  }
}

export async function submitCheckIn(data: CheckInData) {
  if (!baseURL) return { ok: true, forecast: mockForecast }
  try {
    const response = await client.post('/check-in', data)
    return { ok: true, forecast: response.data as ForecastData }
  } catch {
    return { ok: false, forecast: mockForecast }
  }
}

export async function fetchAnchor() {
  if (!baseURL) return { ok: true, anchor: mockAnchor }
  try {
    const response = await client.get('/anchors/match')
    return { ok: true, anchor: response.data as AnchorData }
  } catch {
    return { ok: false, anchor: mockAnchor }
  }
}

export async function fetchSlots() {
  if (!baseURL) return { ok: true, slots: mockSlots }
  try {
    const response = await client.get('/sessions/slots')
    return { ok: true, slots: response.data as string[] }
  } catch {
    return { ok: false, slots: mockSlots }
  }
}

export async function bookSession(data: BookingData) {
  if (!baseURL) return { ok: true }
  try {
    await client.post('/sessions/book', data)
    return { ok: true }
  } catch {
    return { ok: false }
  }
}
