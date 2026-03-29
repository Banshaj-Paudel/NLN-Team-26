import Button from '../ui/Button'

type BookingSuccessProps = {
  onRestart: () => void
}

function BookingSuccess({ onRestart }: BookingSuccessProps) {
  return (
    <div className="screen">
      <div className="card success">
        <p className="eyebrow">Session booked</p>
        <h1>You're all set.</h1>
        <p className="muted">
          Your Anchor will confirm the session details shortly. You can continue daily check-ins anytime.
        </p>
        <Button variant="secondary" onClick={onRestart}>
          Start another check-in
        </Button>
      </div>
    </div>
  )
}

export default BookingSuccess
