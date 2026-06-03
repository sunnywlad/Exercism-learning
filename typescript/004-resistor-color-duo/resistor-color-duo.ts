export const COLORS: string[] = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white'] as const

export function decodedValue([tensColor, unitsColor]: string[]): number {
  return (COLORS.indexOf(tensColor) * 10) + COLORS.indexOf(unitsColor)
}
