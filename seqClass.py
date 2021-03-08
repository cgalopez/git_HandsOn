#!/usr/bin/env python
#The script was corrected in another branch called fix which was merged with master once script performed well

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()	#collects argument

args.seq = args.seq.upper()    # Converts into uppercase in case needed 
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq) and not re.search('U', args.seq):	#if there is T and no U the seq is DNA
        print ('The sequence is DNA')
    elif re.search('U', args.seq)and not re.search('T', args.seq):
        print ('The sequence is RNA')	#if there is U and no T it is  RNA
    else:
        print ('The sequence can be DNA or RNA') #There are no U or T bases in the query seq
else:
    print ('The sequence is not DNA nor RNA')

if args.motif:
  args.motif = args.motif.upper()
  print("Motif search enabled: looking for motif {args.motif} in sequence {args.seq}...")
  #previous line modified in order to avoid syntax errors
  if re.search(args.motif, args.seq):
  #changed match for search: if the motif has to match the sequence, it does not make sense...
    print("The motif is FOUND in the sequence")
  else:
    print("The motif is NOT FOUND in the sequence")


