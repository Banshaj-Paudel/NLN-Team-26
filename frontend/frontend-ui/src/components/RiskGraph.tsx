type RiskGraphProps = {
  scores: number[]
}

function RiskGraph({ scores }: RiskGraphProps) {
  const width = 320
  const height = 120
  const padding = 16
  const maxScore = 100

  const points = scores.map((score, index) => {
    const x = padding + (index / (scores.length - 1)) * (width - padding * 2)
    const y = height - padding - (score / maxScore) * (height - padding * 2)
    return { x, y }
  })

  const path = points
    .map((point, index) => `${index === 0 ? 'M' : 'L'} ${point.x} ${point.y}`)
    .join(' ')

  const areaPath = `${path} L ${width - padding} ${height - padding} L ${padding} ${height - padding} Z`

  return (
    <div className="risk-graph">
      <svg viewBox={`0 0 ${width} ${height}`} role="img" aria-label="Risk trend">
        <defs>
          <linearGradient id="riskFill" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#96c9b0" stopOpacity="0.5" />
            <stop offset="100%" stopColor="#96c9b0" stopOpacity="0" />
          </linearGradient>
        </defs>
        <path d={areaPath} fill="url(#riskFill)" />
        <path d={path} fill="none" stroke="#2f7f63" strokeWidth="3" />
        {points.map((point, index) => (
          <circle key={index} cx={point.x} cy={point.y} r="3.5" fill="#2f7f63" />
        ))}
      </svg>
    </div>
  )
}

export default RiskGraph
