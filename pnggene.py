#!/usr/bin/python

import sys,os
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
#print dict.keys()
script_input=str()
for name in dict.keys(): 
  resilist=dict[name].resi
  #print name,resilist
  resi= '+'.join(resilist)
  pdb=dict[name].pdb
  script_output=dict[name].name
  #script_input=os.popen("ls ../pdb/final_pdb/"+script_output+'_'+pdb+'*').readline().strip()
  script_input="~/1_work/statistic_4spe/get_homolog_pdb/"+pdb+".pdb"
  #print script_input
  scripts='''
load %(XXX)s
as cartoon
orient 
select resi %(YYY)s
cmd.center("sele",animate=-1)
cmd.zoom("sele",buffer=10,complete=1)
cmd.show("sticks"    ,"sele")
cmd.hide("((byres (sele))&(bb.&!(n. CA|n. N&r. PRO)))")
/cmd.set('bg_rgb',0,'',0)
show sticks, sele
set cartoon_transparency, 0.2
set cartoon_fancy_helices, 1
set cartoon_dumbbell_width, 0.6
set cartoon_dumbbell_length, 1.80000
set cartoon_loop_radius, 0.3
set ray_trace_mode, 1
set ray_opaque_background, 0
png %(AAA)s.png, width=2000, height=1600, dpi=300, ray=1
zoom complete=1
cmd.spectrum("count",byres=1)
show spheres, sele
alter sele, vdw=0.6
rebuild
save %(ZZZ)s.pse
png %(ZZZ)s.png, width=2000, height=1600, dpi=300, ray=1
cmd.quit()
'''%{"XXX":script_input,"YYY":resi,"ZZZ":script_output,"AAA":script_output+"_AMPLIFY"}
  
  h=open(script_output+".pml",'w')
  h.writelines(scripts)
  h.close()

