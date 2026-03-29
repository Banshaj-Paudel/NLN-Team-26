export type Stressor = 'academics' | 'job-search' | 'workplace'

export type OnboardingData = {
  name: string
  careerStage: string
  stressor: Stressor
}

export type CheckInData = {
  sleep: number
  mood: number
  tasksDone: number
  tasksPlanned: number
  journal: string
}

export type ForecastStatus = 'Green' | 'Amber' | 'Red'

export type ForecastData = {
  status: ForecastStatus
  scores: number[]
  summary: string
}

export type AnchorData = {
  name: string
  role: string
  story: string
  tags: string[]
  initials: string
}

export type BookingData = {
  slot: string
}
