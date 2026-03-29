type Option = {
  label: string
  value: string
}

type SegmentedControlProps = {
  options: Option[]
  value: string
  onChange: (value: string) => void
}

function SegmentedControl({ options, value, onChange }: SegmentedControlProps) {
  return (
    <div className="segmented">
      {options.map((option) => (
        <button
          key={option.value}
          className={`segment ${value === option.value ? 'active' : ''}`}
          type="button"
          onClick={() => onChange(option.value)}
        >
          {option.label}
        </button>
      ))}
    </div>
  )
}

export default SegmentedControl
