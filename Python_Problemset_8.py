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

#genes={} 
#gene_id="" 
#dna="" 
#nuc_counts={}
#with open("./Python_08.fasta", "r") as dna_fasta_read: 
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

#import re
#genes={}
#gene_id=""
#dna=""
#codons_F2={}
#codons_F3={}
#codons_F1={}
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
#		codons_F1[gene_id] = re.findall(r"(.{3})",genes[gene_id][0:])
#		codons_F2[gene_id] = re.findall(r"(.{3})",genes[gene_id][1:])
#		codons_F3[gene_id] = re.findall(r"(.{3})",genes[gene_id][2:])
#print(codons_F1)
#print(codons_F2)
#print(codons_F3)
#print(genes)

import re
genes={}
gene_id=""
codons_F2={}
codons_F3={}
codons_F1={}
with open("./Python_06.fasta", "r") as dna_fasta_read:
	for line in dna_fasta_read:
		line = line.rstrip()
		if '>' in line:
			gene_id = line
			genes[gene_id] = ''
		else:
			genes[gene_id] += line
print(line)
	for gene_id in genes:	
		genes[gene_id] = genes[gene_id].replace('G','c')
#		genes[gene_id] = genes[gene_id].replace('T','u')
#		genes[gene_id] = genes[gene_id].replace('C','g')
#		genes[gene_id] = genes[gene_id].replace('A','t')
#		genes[gene_id] = genes[gene_id].upper
#		codons_F1[gene_id] = re.findall(r".{3}",genes[gene_id][::-1])
#		codons_F2[gene_id] = re.findall(r"(.{3})",genes[gene_id][-2::-1])
#		codons_F3[gene_id] = re.findall(r"(.{3})",genes[gene_id][-3::-1])
		
#print(f'F1: {codons_F1}')
#print(f'F2: {codons_F2}')
#print(f'F3: {codons_F3}')
print(genes)

