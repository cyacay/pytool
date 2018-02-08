#!/usr/bin/python
import sys,os
import Bio.PDB
from Bio.PDB.PDBParser import PDBParser
from pair_residue_matrix import *
alignresult=sys.argv[1]
class PROTEIN:
	def __init__(self):
		self.name=str()
		self.resi=[]
		self.pdb=str()

dict={}
f=open(alignresult,'r')
for line in f.readlines():
	line=line.strip()
	n_p=line.split()[0]
	pdb=n_p.split("-")[1]
	gene=n_p.split("-")[0]
	resi=line.split()[1]
	if gene not in dict.keys():
		dict.setdefault(gene,PROTEIN())
	Protein=dict[gene]
	Protein.name=gene
	Protein.pdb=pdb
	if resi not in Protein.resi:
		Protein.resi.append(resi) 
  #print dict[pdb]
f.close()

p = PDBParser(PERMISSIVE=1)
model=0
chain='A'
for item in dict.keys():
	resi_list=dict[item].resi
	id=dict[item].pdb
	file=os.popen("ls ./pdb/final_pdb/"+dict[item].name+'_'+id+'*').readline().strip()
	structure=p.get_structure(id,file)	
	for i in range(0,len(resi_list)):
		int_i=int(resi_list[i])
		resi_i=structure[model][chain][int_i]		
		atom_i=resi_i["CB"]
		for j in range(i+1,len(resi_list)):
			int_j=int(resi_list[j])
			resi_j=structure[model][chain][int_j]			
			atom_j=resi_j["CB"]
			distance=atom_i-atom_j
			print dict[item].name+'_'+id,resi_list[i]+"_"+resi_i.get_resname(),resi_list[j]+"_"+resi_j.get_resname(),distance

