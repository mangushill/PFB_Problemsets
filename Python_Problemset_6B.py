#!/usr/bin/env python3

#Problemset 6B
#total_book=""
#with open("./Python_06.txt", "r") as petty_read, open("Python_06_write.txt","w") as petty_write:
	#for line in petty_read:
		#line = line.rstrip()
		#book=line.upper()
		#print(book)
		#total_book += book
		#petty_write.write(f"{total_book}\n")

#genes={} #this is the new dictionary
#with open("./Python_06.seq.txt", "r") as py6_nuc_read:
#	for line in py6_nuc_read:
#		line = line.rstrip()
#		gene_id,seq = line.split('\t')
#		genes [gene_id] = seq
#		#print("This is the reverse complement", (genes))
#		print(f">{gene_id} 'This is the reverse complement'\n{seq}")

genes={} #this is a new dictionary
total_nts = 0
with open("./Python_06.fastq", "r") as py6_nuc_read:
	for line in py6_nuc_read:
		line = line.rstrip()
		nt_count = len(line)
		print(nt_count)
		sum_count = enumerate(line)
		print(sum_count)
		
		
