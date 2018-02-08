#!/usr/bin/python
import sys
import Bio.PDB
from Bio.PDB.PDBParser import PDBParser
from pair_residue_matrix import *
p = PDBParser(PERMISSIVE=1)
blastresult=sys.argv[1]
metal_atomlist=["ZN","CA","MG","CU","FE","NI","MN"]
metal_resilist=["CYS","GLU","ASP","HIS"]			
f=open(blastresult,'r')
for line in f.readlines():
	if "no hits" in line:
		continue
	line=line.strip()	
	id=line.split()[2]
	file="/home/cyao/1_work/statistic_4spe/fact_pdb/"+str(id)+".pdb"
	chain=line.split()[3]
	structure=p.get_structure(id,file)
	hetid=[]
	hetchain=[]
	for model in structure.get_list():
		for chain in model.get_list():
			for residue in chain.get_list():
				residue_id=residue.get_id()
				hetfield=residue_id[0]
				if hetfield[0]=='H':
					hetid.append(residue_id)
					hetchain.append(chain.get_id())
					#print hetid
					#print hetchain
	for i in range(0,len(hetid)):
		chain_id=hetchain[i]
		atom=hetid[i][0].replace(" ",'').split('_')[1]
		#print atom
		if atom in metal_atomlist:
			target_atom=structure[0][chain_id][hetid[i]][atom]
			#print target_atom
			resis=Bio.PDB.Selection.unfold_entities(structure,'R')
			for resi in resis:
				if resi.get_resname() in metal_resilist:
					if resi.child_dict.has_key('CB'):
						CB=resi["CB"]
						CB_distance=CB-target_atom
						if CB_distance < 7 :
							resiname=AA_3name[resi.resname]
							#print resi.get_id()[1],resiname,atom,resi.get_parent().get_id(),id
							print id.lower()+resi.get_parent().get_id(),resi.get_id()[1]
		if atom == 'SF4':
			resi_sf=structure[0][chain_id][hetid[i]]
			for atom in resi_sf.get_list():
				if 'FE' in str(atom):
					atom_id=atom.get_id()
					target_atom=structure[0][chain_id][hetid[i]][atom_id]
					#print target_atom
					resis=Bio.PDB.Selection.unfold_entities(structure,'R')
					for resi in resis:
						if resi.get_resname() in metal_resilist:
							if resi.child_dict.has_key('CB'):
								CB=resi["CB"]
								CB_distance=CB-target_atom
								if CB_distance < 7 :
									resiname=AA_3name[resi.resname]
									#print resi.get_id()[1],resiname,atom_id,resi.get_parent().get_id(),id
									print id.lower()+resi.get_parent().get_id(),resi.get_id()[1]
		if atom == 'C1O' or atom == 'C2O' or atom == 'CUA':
			resi_CU=structure[0][chain_id][hetid[i]]
			for atom in resi_CU.get_list():
				if 'CU' in str(atom):
					atom_id=atom.get_id()
					target_atom=structure[0][chain_id][hetid[i]][atom_id]
					#print target_atom
					resis=Bio.PDB.Selection.unfold_entities(structure,'R')
					for resi in resis:
						if resi.get_resname() in metal_resilist:
							if resi.child_dict.has_key('CB'):
								CB=resi["CB"]
								CB_distance=CB-target_atom
								if CB_distance < 7 :
									resiname=AA_3name[resi.resname]
									#print resi.get_id()[1],resiname,atom_id,resi.get_parent().get_id(),id
									print id.lower()+resi.get_parent().get_id(),resi.get_id()[1]
	
f.close()
#atoms=Bio.PDB.Selection.unfold_e#ntities(structure,'A')
 #               ns=Bio.PDB.Neigh#borSearch(atoms)
  #              close_atoms=ns.s#earch(target_atom,5)
   #             for atom in close_atoms:
    #                    resi=atom.getparent()
     #                   if resi.get_resname() in metal_resilist:
      #                          print resi.get_id()

