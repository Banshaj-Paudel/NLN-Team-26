import type { ForecastStatus } from '../types/app'

type StatusBadgeProps = {
  status: ForecastStatus
}

const statusClassMap = {
  Green: 'status-green',
  Amber: 'status-amber',
  Red: 'status-red',
}

function StatusBadge({ status }: StatusBadgeProps) {
  const className = statusClassMap[status]
  return <span className={`status-pill ${className}`}>{status}</span>
}

export default StatusBadge
