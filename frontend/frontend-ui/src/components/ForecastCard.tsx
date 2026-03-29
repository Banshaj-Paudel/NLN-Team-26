import Button from '../ui/Button'

type ForecastCardProps = {
  status: 'Amber' | 'Green' | 'Red'
  riskValue: string
  riskLabel: string
  note: string
}

const statusClassMap = {
  Amber: 'amber',
  Green: 'green',
  Red: 'red',
}

function ForecastCard({ status, riskValue, riskLabel, note }: ForecastCardProps) {
  const statusClass = statusClassMap[status]

  return (
    <div className="forecast-card">
      <div className="card-header">
        <div>
          <p className="card-title">Weekly Burnout Forecast</p>
          <p className="card-subtitle">Next 4 weeks - personalized</p>
        </div>
        <span className={`status ${statusClass}`}>{status}</span>
      </div>
      <div className="forecast-body">
        <div className="risk">
          <p className="risk-value">{riskValue}</p>
          <p className="risk-label">{riskLabel}</p>
        </div>
        <div className="forecast-bars">
          <div className="bar low"></div>
          <div className="bar low"></div>
          <div className="bar amber"></div>
          <div className="bar high"></div>
        </div>
      </div>
      <div className="card-footer">
        <div className="note">
          <span className="dot"></span>
          {note}
        </div>
        <Button variant="tiny">View report</Button>
      </div>
    </div>
  )
}

export default ForecastCard
