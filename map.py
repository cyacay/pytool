#!/usr/bin/python
import sys,os
alignresult=sys.argv[1]
f=open(alignresult,'r')
for line in f.readlines():
	line=line.strip()
	pdb=line.split()[0]
	pdb_id=line.split()[0].split('-')[1]
	PDB=pdb_id[:-1].upper()
	site=line.split()[1]
	f3=open("/home/cyao/1_work/statistic_4spe/get_homolog_pdb/"+PDB+"_map",'r')
	re_list=[]
	atm_list=[]
	for l in f3:
		l=l.strip()
		re_list.append(l.split()[0])
		atm_list.append(l.split()[1])
	f3.close()
	index=re_list.index(site)
	atm_site=atm_list[index]
	print pdb,atm_site
