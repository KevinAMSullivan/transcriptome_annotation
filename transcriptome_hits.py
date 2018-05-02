#!/bin/bash
#$ -V
#$ -cwd
#$ -S /bin/bash
#$ -N PythonHM
#$ -o $JOB_NAME.o$JOB_ID
#$ -e $JOB_NAME.e$JOB_ID
#$ -q omni
#$ -pe sm 1
#$ -P quanah
 


module load intel 
from Bio import SeqIO
BLASTfile = open("NW-1.physco.blastx", "r")
FASTAfile = open("NW-1.Trinity.fasta", "r")

HITS=[]
hitcount = 0

FILECONTENTS = open(BLASTfile).read() 
for RECORD in SeqIO.parse(FASTAfile, 'fasta'):
	if RECORD.id in FILECONTENTS:
		hitcount = hitcount+1
	break 
print(hitcount)
