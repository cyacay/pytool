# pytool


1.prepare preblast: format(gene seq)
2.modify blast.py 
3.python blast.py preblast
4.python getblast.py preblast > blastresult:format(gene - pdb chain evalue)
5.python get_pdb.py blastresult > .pdb{rename} &.log{sequence}
6.python align.py blastresult > alignresult(filter:CDHE)
7.python pnggene.py alignresult
8.pymol .pml

python map.py alignresult 
python pdb_metal_resi.py alignresult > fact_site
python match.py fact_site pred_site > match
