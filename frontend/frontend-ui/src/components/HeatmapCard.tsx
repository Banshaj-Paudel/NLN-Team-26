const heatCells = Array.from({ length: 40 }, (_, index) => {
  const tone = index % 7 === 0 ? 'hot' : index % 5 === 0 ? 'warm' : 'cool'
  return { id: index, tone }
})

type HeatmapCardProps = {
  title: string
  subtitle: string
  status: 'Green' | 'Amber' | 'Red'
  tags: string[]
}

const statusClassMap = {
  Green: 'green',
  Amber: 'amber',
  Red: 'red',
}

function HeatmapCard({ title, subtitle, status, tags }: HeatmapCardProps) {
  const statusClass = statusClassMap[status]

  return (
    <div className="map-card">
      <div className="map-header">
        <div>
          <p className="card-title">{title}</p>
          <p className="card-subtitle">{subtitle}</p>
        </div>
        <span className={`status ${statusClass}`}>{status}</span>
      </div>
      <div className="heatmap">
        {heatCells.map((cell) => (
          <span key={cell.id} className={`heat ${cell.tone}`}></span>
        ))}
      </div>
      <div className="map-footer">
        <span>Top stressors</span>
        <div className="tags">
          {tags.map((tag) => (
            <span key={tag}>{tag}</span>
          ))}
        </div>
      </div>
    </div>
  )
}

export default HeatmapCard
