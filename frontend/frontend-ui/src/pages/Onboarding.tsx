import Button from '../ui/Button'
import SegmentedControl from '../components/SegmentedControl'
import type { OnboardingData, Stressor } from '../types/app'

const stressorOptions = [
  { label: 'Academics', value: 'academics' },
  { label: 'Job search', value: 'job-search' },
  { label: 'Workplace', value: 'workplace' },
]

const careerStages = [
  'High school',
  'Undergraduate',
  'Graduate program',
  'Early career (0-2 years)',
  'Career switcher',
]

type OnboardingProps = {
  data: OnboardingData
  onChange: (data: OnboardingData) => void
  onNext: () => void
  loading?: boolean
}

function Onboarding({ data, onChange, onNext, loading = false }: OnboardingProps) {
  const handleChange = (key: keyof OnboardingData, value: string) => {
    onChange({ ...data, [key]: value })
  }

  return (
    <form
      className="screen"
      onSubmit={(event) => {
        event.preventDefault()
        onNext()
      }}
    >
      <div>
        <p className="eyebrow">Welcome to BurnMap</p>
        <h1>Start with a quick snapshot.</h1>
        <p className="muted">We use this to personalize your forecast and match you with the right Anchor.</p>
      </div>

      <label className="field">
        <span>Name</span>
        <input
          className="input"
          placeholder="Your name"
          value={data.name}
          onChange={(event) => handleChange('name', event.target.value)}
          required
        />
      </label>

      <label className="field">
        <span>Career stage</span>
        <select
          className="input"
          value={data.careerStage}
          onChange={(event) => handleChange('careerStage', event.target.value)}
          required
        >
          <option value="" disabled>
            Select a stage
          </option>
          {careerStages.map((stage) => (
            <option key={stage} value={stage}>
              {stage}
            </option>
          ))}
        </select>
      </label>

      <div className="field">
        <span>Top stressor</span>
        <SegmentedControl
          options={stressorOptions}
          value={data.stressor}
          onChange={(value) => handleChange('stressor', value as Stressor)}
        />
      </div>

      <div className="actions">
        <Button variant="primary" type="submit" disabled={loading}>
          {loading ? 'Saving...' : 'Continue'}
        </Button>
      </div>
    </form>
  )
}

export default Onboarding
