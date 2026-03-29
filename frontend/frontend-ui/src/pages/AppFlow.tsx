import { useEffect, useState } from 'react'
import AnchorScreen from './AnchorScreen'
import BookingScreen from './BookingScreen'
import BookingSuccess from './BookingSuccess'
import DailyCheckIn from './DailyCheckIn'
import ForecastScreen from './ForecastScreen'
import Onboarding from './Onboarding'
import ProgressSteps from '../components/ProgressSteps'
import Button from '../ui/Button'
import { bookSession, fetchAnchor, fetchSlots, saveOnboarding, submitCheckIn } from '../services/api'
import type { AnchorData, CheckInData, ForecastData, OnboardingData } from '../types/app'

const steps = ['Onboarding', 'Check-in', 'Forecast', 'Anchor', 'Booking']

const initialOnboarding: OnboardingData = {
  name: '',
  careerStage: '',
  stressor: 'academics',
}

const initialCheckIn: CheckInData = {
  sleep: 6,
  mood: 6,
  tasksDone: 6,
  tasksPlanned: 7,
  journal: '',
}

const initialForecast: ForecastData = {
  status: 'Amber',
  scores: [24, 28, 35, 42, 51, 58, 62],
  summary: "You've been in Amber for 3 days. Time to act.",
}

const initialAnchor: AnchorData = {
  name: 'Aanya P.',
  role: 'Final year CS',
  story: 'Survived a tough job search season and built a repeatable reset plan.',
  tags: ['Job rejection', 'Final year CS', 'Startup stress'],
  initials: 'AP',
}

type AppFlowProps = {
  onExit?: () => void
}

function AppFlow({ onExit }: AppFlowProps) {
  const [step, setStep] = useState(0)
  const [onboarding, setOnboarding] = useState(initialOnboarding)
  const [checkIn, setCheckIn] = useState(initialCheckIn)
  const [forecast, setForecast] = useState(initialForecast)
  const [anchor, setAnchor] = useState(initialAnchor)
  const [slots, setSlots] = useState<string[]>([])
  const [selectedSlot, setSelectedSlot] = useState('')
  const [loading, setLoading] = useState({
    onboarding: false,
    checkIn: false,
    anchor: false,
    slots: false,
    booking: false,
  })
  const [booked, setBooked] = useState(false)

  useEffect(() => {
    if (step === 3 && !loading.anchor) {
      setLoading((prev) => ({ ...prev, anchor: true }))
      fetchAnchor().then((result) => {
        if (result.anchor) setAnchor(result.anchor)
        setLoading((prev) => ({ ...prev, anchor: false }))
      })
    }
  }, [step, loading.anchor])

  useEffect(() => {
    if (step === 4 && !loading.slots) {
      setLoading((prev) => ({ ...prev, slots: true }))
      fetchSlots().then((result) => {
        if (result.slots) setSlots(result.slots)
        setLoading((prev) => ({ ...prev, slots: false }))
      })
    }
  }, [step, loading.slots])

  const handleOnboardingNext = async () => {
    setLoading((prev) => ({ ...prev, onboarding: true }))
    await saveOnboarding(onboarding)
    setLoading((prev) => ({ ...prev, onboarding: false }))
    setStep(1)
  }

  const handleCheckInNext = async () => {
    setLoading((prev) => ({ ...prev, checkIn: true }))
    const result = await submitCheckIn(checkIn)
    if (result.forecast) setForecast(result.forecast)
    setLoading((prev) => ({ ...prev, checkIn: false }))
    setStep(2)
  }

  const handleBook = async () => {
    if (!selectedSlot) return
    setLoading((prev) => ({ ...prev, booking: true }))
    await bookSession({ slot: selectedSlot })
    setLoading((prev) => ({ ...prev, booking: false }))
    setBooked(true)
  }

  const resetFlow = () => {
    setStep(1)
    setBooked(false)
    setSelectedSlot('')
  }

  return (
    <div className="app-shell">
      <header className="app-header">
        <div className="header-row">
          {onExit ? (
            <button type="button" className="brand brand-button" onClick={onExit}>
              <span className="logo-mark"></span>
              <div>
                <p className="brand-name">BurnMap</p>
                <p className="brand-subtitle">Burnout forecasting + human anchors</p>
              </div>
            </button>
          ) : (
            <div className="brand">
              <span className="logo-mark"></span>
              <div>
                <p className="brand-name">BurnMap</p>
                <p className="brand-subtitle">Burnout forecasting + human anchors</p>
              </div>
            </div>
          )}
          {onExit ? (
            <Button variant="ghost" onClick={onExit}>
              Back to landing
            </Button>
          ) : null}
        </div>
        <ProgressSteps steps={steps} current={Math.min(step, steps.length - 1)} />
      </header>

      <div className="app-content">
        {step === 0 && (
          <Onboarding
            data={onboarding}
            onChange={setOnboarding}
            onNext={handleOnboardingNext}
            loading={loading.onboarding}
          />
        )}
        {step === 1 && (
          <DailyCheckIn
            data={checkIn}
            onChange={setCheckIn}
            onNext={handleCheckInNext}
            onBack={() => setStep(0)}
            loading={loading.checkIn}
          />
        )}
        {step === 2 && (
          <ForecastScreen
            forecast={forecast}
            onNext={() => setStep(3)}
            onBack={() => setStep(1)}
          />
        )}
        {step === 3 && (
          <AnchorScreen anchor={anchor} onNext={() => setStep(4)} onBack={() => setStep(2)} />
        )}
        {step === 4 && !booked && (
          <BookingScreen
            slots={slots}
            selected={selectedSlot}
            onSelect={setSelectedSlot}
            onConfirm={handleBook}
            onBack={() => setStep(3)}
            loading={loading.booking}
          />
        )}
        {step === 4 && booked && <BookingSuccess onRestart={resetFlow} />}
      </div>
    </div>
  )
}

export default AppFlow
