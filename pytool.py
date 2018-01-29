#!/usr/bin/env python
import pickle
def load_uniprot_fasta():
	database='/home/whbpt/3_wangchu/database/uniprot_sprot.pkl'
	f2=file(database,'rb')
	return pickle.load(f2)
