import type { AnchorData } from '../types/app'

function AnchorProfileCard({ anchor }: { anchor: AnchorData }) {
  return (
    <div className="anchor-card">
      <div className="anchor-header">
        <div className="avatar">{anchor.initials}</div>
        <div>
          <h3>{anchor.name}</h3>
          <p className="muted">{anchor.role}</p>
        </div>
      </div>
      <p className="anchor-story">{anchor.story}</p>
      <div className="tag-row">
        {anchor.tags.map((tag) => (
          <span key={tag} className="tag">
            {tag}
          </span>
        ))}
      </div>
    </div>
  )
}

export default AnchorProfileCard
