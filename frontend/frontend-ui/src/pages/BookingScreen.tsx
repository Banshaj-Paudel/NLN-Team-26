import Button from '../ui/Button'
import TimeSlotPicker from '../components/TimeSlotPicker'

const timeLabels = ['Today', 'Tomorrow', 'This week']

type BookingScreenProps = {
  slots: string[]
  selected: string
  onSelect: (slot: string) => void
  onConfirm: () => void
  onBack: () => void
  loading?: boolean
}

function BookingScreen({ slots, selected, onSelect, onConfirm, onBack, loading = false }: BookingScreenProps) {
  return (
    <div className="screen">
      <div>
        <p className="eyebrow">Session booking</p>
        <h1>Pick a time that works.</h1>
        <p className="muted">Your Anchor will confirm within 24 hours.</p>
      </div>

      <div className="card">
        <div className="pill-row">
          {timeLabels.map((label) => (
            <span key={label} className="pill">
              {label}
            </span>
          ))}
        </div>
        <TimeSlotPicker slots={slots} selected={selected} onSelect={onSelect} />
      </div>

      <div className="actions between">
        <Button variant="ghost" onClick={onBack}>
          Back
        </Button>
        <Button variant="primary" onClick={onConfirm} disabled={!selected || loading}>
          {loading ? 'Booking...' : 'Confirm session'}
        </Button>
      </div>
    </div>
  )
}

export default BookingScreen
