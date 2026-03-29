type StatCardProps = {
  value: string
  label: string
  source: string
}

function StatCard({ value, label, source }: StatCardProps) {
  return (
    <article className="stat-card">
      <p className="stat-value">{value}</p>
      <p className="stat-label">{label}</p>
      <span className="stat-source">Source: {source}</span>
    </article>
  )
}

export default StatCard
