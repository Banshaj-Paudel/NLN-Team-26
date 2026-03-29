import Button from '../ui/Button'
import AnchorProfileCard from '../components/AnchorProfileCard'
import type { AnchorData } from '../types/app'

type AnchorScreenProps = {
  anchor: AnchorData
  onNext: () => void
  onBack: () => void
}

function AnchorScreen({ anchor, onNext, onBack }: AnchorScreenProps) {
  return (
    <div className="screen">
      <div>
        <p className="eyebrow">Your Anchor</p>
        <h1>Meet someone who has been there.</h1>
        <p className="muted">Anchors are trained peers who understand your specific pressure.</p>
      </div>

      <AnchorProfileCard anchor={anchor} />

      <div className="actions between">
        <Button variant="ghost" onClick={onBack}>
          Back
        </Button>
        <Button variant="primary" onClick={onNext}>
          Book a session
        </Button>
      </div>
    </div>
  )
}

export default AnchorScreen
