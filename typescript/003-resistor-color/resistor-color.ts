export const COLORS: string[] = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white'] as const

export const colorCode = (color: string): number => COLORS.indexOf(color)
