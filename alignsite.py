#!/usr/bin/python

import sys,os
from Bio import SeqIO
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.SubsMat.MatrixInfo import blosum62

def sitealign(site,seq1,seq2):
  alignments=pairwise2.align.localds(seq1,seq2,blosum62,-10,-1)
  seq_1=format_alignment(*alignments[0]).split('\n')[0]
  seq_2=format_alignment(*alignments[0]).split('\n')[2]
  #print format_alignment(*alignments[0])
  index1_list=[]			 
  i=0
  for resi in seq_1:
    if resi !='-':
      index1_list.append(i)
    i=i+1
  seq1_index=index1_list[int(site)-1]
  seq2_index=seq1_index
  if seq_2[seq2_index]=='-':
    n_site=-1
  else:
    n=0
    for i in range(0,int(seq2_index)):
      if seq_2[i]=='-':
        n=n+1
    n_site=seq2_index-n+1
    #print n_site
    #print n_site,seq1[site-1],seq2[n_site-1]
  return n_site  


#P0A8G0
fullseq='MKQLQTIADKTAITLSFICTLHCLAVPFAVALLPTLAAINLGDEAFHLWMVIVVIPTSLLALSMGCKKHRDYRLMLLGITGLSLLILAAFFGHDLMGESIETAMTVLGATIIAAGHLLNHRLCCERHTEQ'
seq='MKQLQTIADKTAITLSFICTLHCLAVPFAVALLPTLAAINLGDEAFHLWMVIVVIPTSLLALSMGCKKHRDYRLMLLGITGLSLLILAAFFGHDLMGESIETAMTVLGATIIAAGHLLNHRLCCERHTEQ'
site=101
#print sitealign(site,fullseq,seq) 
