type ProgressStepsProps = {
  steps: string[]
  current: number
}

function ProgressSteps({ steps, current }: ProgressStepsProps) {
  return (
    <div className="progress">
      {steps.map((step, index) => (
        <div key={step} className={`progress-step ${index <= current ? 'active' : ''}`}>
          <span className="dot"></span>
          <span className="label">{step}</span>
        </div>
      ))}
    </div>
  )
}

export default ProgressSteps
