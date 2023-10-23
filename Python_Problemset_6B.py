#!/usr/bin/env python3

genes={} #this is a new dictionary
gene_id=""
dna=""
with open("./Python_06.fasta", "r") as dna_fasta_read:
	for line in dna_fasta_read:
		line = line.rstrip()
		if '>' in line: 
			gene_id = line
			genes [gene_id] = ''
#print(genes)
		else:
			dna=dna+line
			genes [gene_id] = dna
print(genes)
