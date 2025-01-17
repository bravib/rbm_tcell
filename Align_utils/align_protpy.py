import argparse
parser = argparse.ArgumentParser() 
parser.add_argument('-rootf', nargs = '*', type = str, required=True)
parser.add_argument('-SA', nargs = '*', type = int, required=True)
parser.add_argument('-ss', nargs = '*', type = str, required=True)
parser.add_argument('-SAmin', nargs = '*', type = int, required=True)
parser.add_argument('-SAmax', nargs = '*', type = int, required=True)
args = parser.parse_args()

rootf = args.rootf[0]

import numpy as np
curr_int = np.int16

def align_seq(seqs, lea, lepmin, lepmax):
    import matlab.engine
    eng = matlab.engine.start_matlab()
    eng.addpath(rootf + '/Align_utils')
    alignc = eng.balign_prots(seqs, lea, lepmin, lepmax)
    eng.quit()
    msa_al = np.asarray(alignc).astype(curr_int) - 1 # needed for different indexing convention in matlab
    return msa_al


import sys
sys.path.append(rootf + '/PGM3/source/')
sys.path.append(rootf + '/PGM3/utilities/')
sys.path.append(rootf + '/Align_utils/')

#import butils

seqs_name = args.ss[0]

seqs = []
with open(seqs_name) as f:
    for line in f:
        linesplit = line.strip().split('\t')
        seqs.append(linesplit[0])

SA = args.SA[0]
SAmin = args.SAmin[0]
SAmax = args.SAmax[0]

msa_al = align_seq(seqs, SA, SAmin, SAmax)
np.savetxt(rootf + '/Align_utils/aligned_prot.txt', msa_al, fmt='%i')
