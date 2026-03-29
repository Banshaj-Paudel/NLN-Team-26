type FeatureCardProps = {
  title: string
  copy: string
  tag: string
}

function FeatureCard({ title, copy, tag }: FeatureCardProps) {
  return (
    <article className="feature-card">
      <span className="feature-tag">{tag}</span>
      <h3>{title}</h3>
      <p>{copy}</p>
    </article>
  )
}

export default FeatureCard
