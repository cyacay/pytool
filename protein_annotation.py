#!/usr/bin/env python
import sys
import argparse
from Bio import SeqIO
import os
def all_lower(L1):
	return [s.lower() for s in L1]
metal_list=["Calcium","Cobalt","Copper","Iron","Iron-sulfur","Magnesium","Manganese","Molybdenum","Nickel","Potassium","Sodium","Zinc"]
metal_list=all_lower(metal_list)

def analysis_multi(glist,db):
	#record = SeqIO.parse(open(db),'swiss')
	#ecord_dict=SeqIO.to_dict(record)
	for gene in glist:
		gene=gene.strip()
		gene_info=os.popen("awk \'{if($1==\"AC\" && $2 ~ /"+gene+"/){print $0,FLAG=1}{if(FLAG==1){print $0}}{if($1==\"//\")FLAG=0}}\' "+db).readlines()
		gene_info=all_lower(gene_info)
		for metal in metal_list:
				for line in gene_info:
					if metal in line:
						print gene,metal
#		print gene,record_dict[gene]
def main(argv):
	parser=argparse.ArgumentParser(description="usage:%prog[flags]{AA}")
	parser.add_argument("--gene",metavar='gene',type=str,
	help="input gene name")
	parser.add_argument("--glist",metavar='gene',type=str,
	help="input gene list")
	parser.add_argument("--db",type=str,default="4species.txt",
	help="define fasta file path")
	args=parser.parse_args()
	gene=args.gene
	db=args.db
	glist=args.glist
	if glist:
		glist=open(glist,'r').readlines()
	if gene:
		glist=[gene]
	analysis_multi(glist,db)
if __name__ == "__main__":
	sys.exit(main(sys.argv[1:]))
