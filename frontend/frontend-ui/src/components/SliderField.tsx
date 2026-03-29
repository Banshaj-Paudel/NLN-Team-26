type SliderFieldProps = {
  label: string
  value: number
  onChange: (value: number) => void
  min?: number
  max?: number
  hint?: string
}

function SliderField({ label, value, onChange, min = 0, max = 10, hint }: SliderFieldProps) {
  return (
    <div className="slider-field">
      <div className="slider-header">
        <span>{label}</span>
        <strong>{value}</strong>
      </div>
      <input
        className="slider"
        type="range"
        min={min}
        max={max}
        value={value}
        onChange={(event) => onChange(Number(event.target.value))}
      />
      {hint ? <p className="hint">{hint}</p> : null}
    </div>
  )
}

export default SliderField
