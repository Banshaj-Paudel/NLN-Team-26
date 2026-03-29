import Button from '../ui/Button'
import SliderField from '../components/SliderField'
import type { CheckInData } from '../types/app'

type DailyCheckInProps = {
  data: CheckInData
  onChange: (data: CheckInData) => void
  onNext: () => void
  onBack: () => void
  loading?: boolean
}

function DailyCheckIn({ data, onChange, onNext, onBack, loading = false }: DailyCheckInProps) {
  const update = (key: keyof CheckInData, value: number | string) => {
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
        <p className="eyebrow">Daily check-in</p>
        <h1>How are you feeling today?</h1>
        <p className="muted">A 60-second check-in keeps your forecast grounded in reality.</p>
      </div>

      <div className="card">
        <SliderField label="Sleep quality" value={data.sleep} onChange={(value) => update('sleep', value)} />
        <SliderField label="Mood" value={data.mood} onChange={(value) => update('mood', value)} />
        <SliderField
          label="Tasks done"
          value={data.tasksDone}
          onChange={(value) => update('tasksDone', value)}
          hint="Out of 10"
        />
        <SliderField
          label="Tasks planned"
          value={data.tasksPlanned}
          onChange={(value) => update('tasksPlanned', value)}
          hint="Out of 10"
        />
      </div>

      <label className="field">
        <span>Optional journal (2 lines max)</span>
        <textarea
          className="input"
          rows={2}
          value={data.journal}
          onChange={(event) => update('journal', event.target.value)}
          placeholder="Anything else you want to track today?"
        ></textarea>
      </label>

      <div className="actions between">
        <Button variant="ghost" type="button" onClick={onBack}>
          Back
        </Button>
        <Button variant="primary" type="submit" disabled={loading}>
          {loading ? 'Saving...' : 'See forecast'}
        </Button>
      </div>
    </form>
  )
}

export default DailyCheckIn
