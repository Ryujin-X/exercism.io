def to_rna(dna):
	rna = ''
	dna_to_rna = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
	
	for letter in dna:
		rna += dna_to_rna[letter]
	
	return rna
