#!/usr/bin/python
import os
import sys
filename=sys.argv[1]
inputhandle=open(filename,'r').readlines()
os.system("mkdir high_confident_tempfile")
for line in inputhandle:
	line=line.strip()
	name=line.split()[0]
	peptide=line.split()[1]
	os.chdir('/home/cyao/1_work/statistic_4spe/high_confident_tempfile')
	filesequence = open(name+".fst", "w")
	filesequence.write("".join(peptide))
	filesequence.close()
	os.system("blastp -query " + name + ".fst" + "  -db /home/cyao/database/pdbaa/pdbaa  -out " + name + "_pdb.blast" + " -outfmt 0 -evalue 1e-10")
