import type { ButtonHTMLAttributes } from 'react'

type ButtonVariant = 'primary' | 'secondary' | 'ghost' | 'tiny'

type ButtonProps = ButtonHTMLAttributes<HTMLButtonElement> & {
  variant?: ButtonVariant
  compact?: boolean
}

function Button({ variant = 'primary', compact = false, className = '', ...props }: ButtonProps) {
  const classes = [variant, compact ? 'compact' : '', className].filter(Boolean).join(' ')
  return <button className={classes} {...props} />
}

export default Button
