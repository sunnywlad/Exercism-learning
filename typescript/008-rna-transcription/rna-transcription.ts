const DnaToRna: { [key: string]: string } = {
  'G': 'C',
  'C': 'G',
  'T': 'A',
  'A': 'U'
}

export function toRna(dna: string): string {
  const rna: string[] = dna.split('')
  if (rna.some(el => typeof DnaToRna[el] !== 'string')) {
    throw new Error('Invalid input DNA.');
  }
  return rna.map(el => DnaToRna[el]).join('');
}
