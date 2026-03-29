import Button from '../ui/Button'
import RiskGraph from '../components/RiskGraph'
import StatusBadge from '../components/StatusBadge'
import type { ForecastData } from '../types/app'

type ForecastScreenProps = {
  forecast: ForecastData
  onNext: () => void
  onBack: () => void
}

function ForecastScreen({ forecast, onNext, onBack }: ForecastScreenProps) {
  return (
    <div className="screen">
      <div className="screen-header">
        <div>
          <p className="eyebrow">Burnout forecast</p>
          <h1>Your 7-day risk trend</h1>
          <p className="muted">We refresh this every check-in.</p>
        </div>
        <StatusBadge status={forecast.status} />
      </div>

      <div className="card">
        <RiskGraph scores={forecast.scores} />
        <p className="summary">{forecast.summary}</p>
      </div>

      <div className="actions between">
        <Button variant="ghost" onClick={onBack}>
          Back
        </Button>
        <Button variant="primary" onClick={onNext}>
          View Anchor
        </Button>
      </div>
    </div>
  )
}

export default ForecastScreen
