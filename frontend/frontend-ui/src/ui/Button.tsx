import type { ButtonHTMLAttributes } from 'react'

type ButtonVariant = 'primary' | 'secondary' | 'ghost' | 'tiny'

type ButtonProps = ButtonHTMLAttributes<HTMLButtonElement> & {
  variant?: ButtonVariant
  compact?: boolean
}

function Button({ variant = 'primary', compact = false, className = '', type, ...props }: ButtonProps) {
  const classes = ['btn', variant, compact ? 'compact' : '', className]
    .filter(Boolean)
    .join(' ')
  return <button className={classes} type={type ?? 'button'} {...props} />
}

export default Button
