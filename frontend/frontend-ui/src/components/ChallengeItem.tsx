type ChallengeItemProps = {
  title: string
  detail: string
}

function ChallengeItem({ title, detail }: ChallengeItemProps) {
  return (
    <div className="challenge">
      <div className="challenge-dot"></div>
      <div>
        <p className="challenge-title">{title}</p>
        <p className="challenge-detail">{detail}</p>
      </div>
    </div>
  )
}

export default ChallengeItem
