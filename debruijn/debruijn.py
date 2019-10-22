import sys
import argparse
import networkx 
import pytest 
import pylint

def get_arguments():
    parser=argparse.ArgumentParser()
    parser.add_argument('-i', required=True, help='fichier fastq single end')
    parser.add_argument('-k', required=False, help='taille des kmer')
    parser.add_argument('-r', required=False, help='Reference genome')
    parser.add_argument('-o', required=True, help='fichier configuration')
    args=parser.parse_args()
    return args







pass




if __name__ == "__main__":

    arguments=get_arguments()
    

