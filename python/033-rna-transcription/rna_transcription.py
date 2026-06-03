ADN_TO_RNA = {
    'A': 'U',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

def to_rna(dna_strand):
    if not isinstance(dna_strand, str):
        raise TypeError('Input must be a string')
    if not all(letter in ADN_TO_RNA for letter in dna_strand):
        raise ValueError('Input is not a valid ADN sequence')
    return ''.join(ADN_TO_RNA[letter] for letter in dna_strand)
