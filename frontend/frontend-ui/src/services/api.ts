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

// Store user_id from onboarding globally for this session
let sessionUserId: number | null = null

export async function saveOnboarding(data: OnboardingData) {
  if (!baseURL) return { ok: true }
  try {
    const response = await client.post('/onboarding', {
      name: data.name,
      careerStage: data.careerStage,
      stressor: data.stressor,
    })
    if (response.data?.user_id) {
      sessionUserId = response.data.user_id
    }
    return { ok: true }
  } catch {
    return { ok: false }
  }
}

export async function submitCheckIn(data: CheckInData) {
  if (!baseURL) return { ok: true, forecast: mockForecast }
  try {
    const payload = {
      user_id: sessionUserId || 1,
      sleep: data.sleep,
      mood: data.mood,
      tasksDone: data.tasksDone,
      tasksPlanned: data.tasksPlanned,
      journal: data.journal,
    }
    const response = await client.post('/check-in', payload)
    // Parse the real forecast from the backend burnmap_result
    const result = response.data
    const forecast: ForecastData = result.forecast || {
      status: result.burnmap_result?.risk_level || 'Amber',
      scores: [result.burnmap_result?.score || 50],
      summary: result.burnmap_result?.reason || mockForecast.summary,
    }
    return { ok: true, forecast }
  } catch {
    return { ok: false, forecast: mockForecast }
  }
}

export async function fetchAnchor() {
  if (!baseURL) return { ok: true, anchor: mockAnchor }
  try {
    const params = sessionUserId ? { user_id: sessionUserId } : {}
    const response = await client.get('/anchors/match', { params })
    const data = response.data
    const anchor: AnchorData = {
      name: data.name || mockAnchor.name,
      role: data.role || mockAnchor.role,
      story: data.story || mockAnchor.story,
      tags: data.tags || mockAnchor.tags,
      initials: data.initials || mockAnchor.initials,
    }
    return { ok: true, anchor }
  } catch {
    return { ok: false, anchor: mockAnchor }
  }
}

export async function fetchSlots() {
  if (!baseURL) return { ok: true, slots: mockSlots }
  try {
    const response = await client.get('/sessions/slots')
    const slots = response.data?.slots || response.data || mockSlots
    return { ok: true, slots }
  } catch {
    return { ok: false, slots: mockSlots }
  }
}

export async function bookSession(data: BookingData) {
  if (!baseURL) return { ok: true }
  try {
    await client.post('/sessions/book', {
      slot: data.slot,
      user_id: sessionUserId,
    })
    return { ok: true }
  } catch {
    return { ok: false }
  }
}
