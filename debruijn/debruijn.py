'''L’objectif de ce TP sera d’assembler le génome de l’entérovirus A71. Ce génome présente
l’intérêt d’être très court: 7408 nucléotides, linéaire et non segmenté.'''


import sys
import argparse
import pytest 
import pylint
import networkx as nx
import matplotlib.pyplot as plt
import statistics
import os

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

#### Construction de l’arbre de de Bruijn
def build_graph(dic_kmer):
    Graph = nx.DiGraph()
    for i , (kmer, poids) in enumerate(dic_kmer.items()):
        node1 = kmer[:-1]
        node2 = kmer[1:]
        Graph.add_edge(node1 , node2 , weight = poids)
    return Graph

#### Parcourir l’arbre de de Bruijn

def get_starting_nodes(graph): 
    '''prend en entrée un graphe et retourne une liste de noeuds d’entrée'''
    list_starting= []
    for node in graph:
        pred = list(graph.predecessors(node))
        if(not pred):
            list_starting.append(node)
    return list_starting 


def get_sink_nodes(graph):
    '''prend en entrée un graphe et retourne une liste de noeuds de sortie'''
    list_sink= []
    for node in graph:
        succ = list(graph.successors(node))
        if(not succ):
            list_sink.append(node)
    return list_sink

def fill(text, width=80):
    return os.linesep.join(text[i:i+width] for i in range(0,
            len(text), width))


def get_contigs(graph, list_starting, list_sink):
    '''prend un graphe, une liste de noeuds d’entrée et une liste de sortie et
retourne une liste de tuple(contig, taille du contig)'''
    contigs = []
    for start in list_starting:
        for sink in list_sink:
            if algorithms.has_path(graph, start, sink) == True:
                chemin = algorithms.shortest_path(graph, start, sink)
                contig = chemin[0] 
                for i in range(len(chemin)-1):
                    contig += chemin[i+1][-1] 
                contigs.append((contig, len(contig)))
    return contigs

def save_contigs(contigs, name_file):
    '''ui prend un tuple (contig, taille du contig) et un nom de fichier de sortie
et écrit un fichier de sortie contenant les contigs selon le format:'''
    i = 0
    with open(name_file, "w+") as contigs_file:
        for i in range(len(contigs)):
            i += 1
            contigs_file.write('>contig_' + str(i) + ' len=' + str(contigs[i][1]) +'\n'+ str(fill(contigs[i][0])) + '\n')
    contigs_file.close
    return

###Simplification du graphe de de Bruijn
def std():
    pass
def path_average_weight():
	pass
def remove_paths(): 
	pass
def select_best_path():
    pass
def solve_bubble():
    pass
def simplify_bubbles():
    pass
##Détection des pointes (tips)
def solve_entry_tips():
    pass
def solve_out_tips():
    pass


if __name__ == "__main__":
    args = get_arguments()
    print(args.i)
    a = build_kmer_dict(args.i, 3)
    if args.o==None:
        name_file ='contigs.out'
    else:
        name_file = args.o
    print(a)
    graph = build_graph(a)
    nx.draw(build_graph(a), with_labels=True, font_weight='bold')
    #plt.show()
    print(get_starting_nodes(graph))
    print(get_sink_nodes(graph))
    #print(graph[1])
    list_starting = get_starting_nodes(graph)
    list_sink = get_sink_nodes(graph)
    contigs = get_contigs(graph, list_starting, list_sink)
    save_contigs(contigs, name_file)


