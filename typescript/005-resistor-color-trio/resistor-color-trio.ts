const COLORS: string[] = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
const PREFIXES: [number, string][] = [[10**9, 'giga'], [10**6, 'mega'], [10**3, 'kilo'], [0, '']]

function decodedValue([tensColor, unitsColor, zerosColor]: string[]): number {
  return ((COLORS.indexOf(tensColor) * 10) + COLORS.indexOf(unitsColor)) * (10 ** COLORS.indexOf(zerosColor))
}
function prefixFormat(resValue: number): [string, number] {
  const prefix: [number, string] = PREFIXES.find((element) => resValue >= element[0])!
  return [prefix[1], prefix[0] !== 0 ? resValue / prefix[0] : resValue];
}

export function decodedResistorValue(resiColors: string[]): string {
  const [prefix, displayValue] = prefixFormat(decodedValue(resiColors));
  return `${displayValue} ${prefix}ohms`
}
