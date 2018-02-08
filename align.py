#!/usr/bin/python

import sys,os
from Bio import SeqIO
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from alignsite import *
from Bio.SubsMat.MatrixInfo import blosum62
pred_list=sys.argv[1]
f=open(pred_list,'r')
class PROTEIN:
    def __init__(self):
        self.site=[]
        #self.CH_pair=[]
        #self.prob=[]
        #self.site_dict={}
Protein_dict={}
for line in f.readlines():
  line=line.strip()
  gene=line.split('\t')[0]
  Protein_dict.setdefault(gene,PROTEIN())
  Protein=Protein_dict[gene]
  i_tag=line.split('\t')[1]
  j_tag=line.split('\t')[2]
  i=i_tag[:-1]
  j=j_tag[:-1]
  if i not in Protein.site:
    Protein.site.append(i)
  if j not in Protein.site:
    Protein.site.append(j)
 # site_dict=Protein.site_dict
 # site_dict.setdefault(i_tag,0)
 # site_dict[i_tag]=site_dict[i_tag]+1
 # site_dict.setdefault(j_tag,0)
 # site_dict[j_tag]=site_dict[j_tag]+1
 # Protein.site_dict=site_dict
f.close()
#print Protein_dict['Q9HP05'].site

def get_acc(identifier):
    """"Given a SeqRecord identifier string, return the accession number as a string.

    e.g. "gi|2765613|emb|Z78488.1|PTZ78488" -> "Z78488.1"
    """
    parts = str(identifier).split("|")
    return parts[1] 

seqdata=sys.argv[2]
fasta_dict=SeqIO.to_dict(SeqIO.parse(seqdata,'fasta'),key_function=get_acc)

blastresult=sys.argv[3]
filteraa='CDEH'
f=open(blastresult,'r') 
for line in f.readlines():
  line=line.strip()
#line="Q9HP05 - 3ANO A 5e-28"
  gene=line.split(' ')[0]
  chain=line.split()[3]
  #print line
 # handle=open("./fst/"+gene+".fst",'r')
 # fullseq=handle.readline().strip()
 # handle.close()
  fullseq=fasta_dict[gene].seq
  pdb=line.split()[2]
  #print fullseq
  seq=os.popen("sed -n '$p' ./get_homolog_pdb/"+gene+".log").readline()
  seq=seq.strip()
 # print seq
  if "no.pdb hits" not in seq:
    for resisite in Protein_dict[gene].site:
      newsite=sitealign(resisite,fullseq,seq)
      #print newsite,seq[newsite-1]
      if newsite != -1 and (str(seq[newsite-1]) in filteraa ):
        print gene+'-'+pdb.lower()+chain,newsite,seq[newsite-1]
  #else:
    #print gene,"no blast hits" 
f.close()

