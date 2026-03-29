type TimeSlotPickerProps = {
  slots: string[]
  selected: string
  onSelect: (slot: string) => void
}

function TimeSlotPicker({ slots, selected, onSelect }: TimeSlotPickerProps) {
  return (
    <div className="slot-grid">
      {slots.map((slot) => (
        <button
          key={slot}
          type="button"
          className={`slot ${selected === slot ? 'active' : ''}`}
          onClick={() => onSelect(slot)}
        >
          {slot}
        </button>
      ))}
    </div>
  )
}

export default TimeSlotPicker
