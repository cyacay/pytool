#!/usr/bin/python
import sys,os
import string
import sys
import os
from sys import argv,stderr,stdout
from os import popen,system
from os.path import exists,basename
from string import uppercase
import random

def download_pdb(pdb_id,dest_dir):
    #print "downloading %s" % ( pdb_id )
    url      = 'http://www.rcsb.org/pdb/files/%s.pdb' % ( pdb_id.upper() )
    dest     = '%s/%s.pdb' % ( os.path.abspath(dest_dir), pdb_id)
    wget_cmd = 'wget --quiet %s -O %s' % ( url, dest )
    #if remote_host:
        #wget_cmd = 'ssh %s %s' % ( remote_host, wget_cmd )

    system( wget_cmd )
    print wget_cmd
    if ( exists(dest) ):
        return dest
    else:
        print "Error: didn't download file!"

dir=sys.argv[1]
blastresult=sys.argv[2]
f=open(blastresult,'r')
for line in f.readlines():
	if "no hits" not in line:	
		line=line.strip()
		pdb_id=line.split()[2]
		download_pdb(pdb_id,dir)	  
f.close()
