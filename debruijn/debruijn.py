'''L’objectif de ce TP sera d’assembler le génome de l’entérovirus A71. Ce génome présente
l’intérêt d’être très court: 7408 nucléotides, linéaire et non segmenté.'''


import sys
import argparse
import networkx 
import pytest 
import pylint

def get_arguments():
    parser=argparse.ArgumentParser()
    parser.add_argument('-i', required=True, help='fichier fastq single end')
    parser.add_argument('-k', required=False, help='taille des kmer')
    parser.add_argument('-r', required=False, help='Reference genome')  #true
    parser.add_argument('-o', required=False, help='fichier contig')
    args=parser.parse_args()
    return args

###Création du graphe de de Bruijn
##Identification des k-mer unique et les mettre dans un dictionnaire 

def read_fastq(fichier_fastq):
    with open(fichier_fastq, 'r') as f:
        lines= iter(f.readlines())
        for line in lines:
           yield next(lines)
           next(lines)
           next(lines) 

def cut_kmer(seq, taillekmer):
    for i in range(len(seq)-taillekmer+1):
        yield seq[i:taillekmer]


def build_kmer_dict(fichier_fastq, taille_kmer):
    dict_kmer={}
    for x in read_fastq(fichier_fastq):
        for kmer in cut_kmer(x, taille_kmer):
            if kmer not in dict_kmer.keys():
                dict_kmer[kmer] = 1
            else:
                dict_kmer[kmer] += 1
    return dict_kmer

####Construction de l’arbre de de Bruijn

def build_graph(): 
    pass

if __name__ == "__main__":
    args = get_arguments()
    print(args.i)
    a = build_kmer_dict(args.i, 3)
    print(a)    

