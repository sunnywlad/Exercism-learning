function radiusSquared(x: number, y: number): number {
  return x ** 2 + y ** 2;
}

export function score(x: number, y: number): number {
  const radSq = radiusSquared(x, y);
  if (radSq > 10 ** 2) {
    return 0
  } else if (radSq > 5 ** 2) {
    return 1
  } else if (radSq > 1 ** 2) {
    return 5
  } else {
    return 10
  }
}
