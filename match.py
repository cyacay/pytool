#!/usr/bin/python

import sys,os

fact=sys.argv[1]
pdb_dict={}
f1=open(fact,'r')
for line in f1.readlines():
	line=line.strip()
	pdb_id=line.split()[0]
	if pdb_id not in pdb_dict.keys():
		pdb_dict.setdefault(pdb_id,[])
	site=line.split()[1]
	if site not in pdb_dict[pdb_id]:
		pdb_dict[pdb_id].append(site)	
f1.close()

pred=sys.argv[2]
class pred_gene():
	def __init__(self):
		self.gene_id=str()
		self.blast_pdb=str()
		self.pred_site=[]


f2=open(pred,'r')
gene_dict=dict()
for line in f2.readlines():
	line=line.strip()
	gene=line.split('-')[0]
	if gene not in gene_dict.keys():
		gene_dict.setdefault(gene,pred_gene())
	Pred=gene_dict[gene]
	Pred.gene_id=gene
	Pred.blast_pdb=line.split('-')[1].split()[0]
	site=line.split()[1]
	if site not in Pred.pred_site:
		Pred.pred_site.append(site)
f2.close()
sum_match=0.0
sum_pred=0.0
sum_fact=0.0
sum_p=0.0
for item in pdb_dict.values():
	sum_fact=sum_fact+len(item)
for item in gene_dict.keys():
	sum_p=sum_p+len(gene_dict[item].pred_site)

for gene in gene_dict.keys():
	match_num=0
	pdb=gene_dict[gene].blast_pdb
	if pdb not in pdb_dict.keys():
			print "no metal in "+pdb
			continue
	for pred_site in gene_dict[gene].pred_site:
		sum_pred=sum_pred+1		
		if pred_site in pdb_dict[pdb]:
			match_num=match_num+1
			sum_match=sum_match+1
	print gene,pdb,"pred:",len(gene_dict[gene].pred_site),"fact:",len(pdb_dict[pdb]),"matched:",match_num
#print sum_p,sum_match,sum_pred,sum_fact
#print pdb_dict.values()
print "precision=",sum_match/sum_pred,"recall=",sum_match/sum_fact
