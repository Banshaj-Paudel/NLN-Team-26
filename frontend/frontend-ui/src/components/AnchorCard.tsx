import Button from '../ui/Button'

type AnchorCardProps = {
  role: string
  name: string
  quote: string
}

function AnchorCard({ role, name, quote }: AnchorCardProps) {
  return (
    <div className="anchor-card">
      <div>
        <p className="card-title">Matched Anchor</p>
        <p className="card-subtitle">{role}</p>
      </div>
      <div className="anchor-profile">
        <div className="avatar"></div>
        <div>
          <p className="anchor-name">{name}</p>
          <p className="anchor-quote">{quote}</p>
        </div>
      </div>
      <Button variant="primary" compact>
        Schedule a clarity session
      </Button>
    </div>
  )
}

export default AnchorCard
