#!/usr/bin/env python3

#genes={} #this is a new dictionary
#gene_id=""
#dna=""
#nuc_counts = {}

#with open("./Python_06.fasta", "r") as dna_fasta_read:
#	for line in dna_fasta_read:
#		line = line.rstrip()
#		if '>' in line: 
#			gene_id = line
#			genes[gene_id] = ''
#		else:
#			dna=dna+line
#			genes[gene_id] = dna
#	for gene_id in genes:
#		nuc_counts[gene_id] = {'A':genes[gene_id].count('A'),'C':genes[gene_id].count('C'),'G':genes[gene_id].count('G'),'T':genes[gene_id].count('T')}
#print (nuc_counts)
#print(genes)

genes={} 
gene_id="" 
dna="" 
nuc_counts={}
with open("./Python_08.fasta", "r") as dna_fasta_read: 
	for line in dna_fasta_read: 
		line = line.rstrip() 
		if '>' in line: 
			gene_id = line 
			genes[gene_id] = '' 
		else:
			dna=dna+line 
			genes[gene_id] = dna 
	for gene_id in genes: 
		nuc_counts[gene_id] = {'A':genes[gene_id].count('A'),'C':genes[gene_id].count('C'),'G':genes[gene_id].count('G'),'T':genes[gene_id].count('T')}
print (nuc_counts)
print(genes)

