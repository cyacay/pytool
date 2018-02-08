#!/usr/bin/python
import sys,os
f=sys.argv[1]
file=open(f,'r')
for line in file.readlines():
  gene=line.strip('\t').split()[0]
#handle=[]
  try:
    handle=os.popen("grep 'pdb' /home/cyao/1_work/statistic_4spe/high_confident_tempfile/"+gene+"_pdb.blast").readlines()[0]
    evalue=handle.strip().split()[-1]
    title=handle.strip().split('  ')[0]
    pdbnum=title.strip().split('|')[1]
    chainnum=title.strip().split('|')[2]
    #print handle,evalue
    print gene,"-",pdbnum,chainnum,evalue
  except:
    print gene,"-","no hits"
    continue
file.close()  
