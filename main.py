'''
    Author : Sefa Koc
'''

from __future__ import division, absolute_import, print_function
import sys
import matplotlib
from numpy.random import *  # for random sampling
seed(42)

from graph_tool.all import *
import graph_tool as gt

from test1cluster import simple_graph
from infile import InFile



def hierpath():
    g = gt.collection.data["celegansneural"]
    state = minimize_nested_blockmodel_dl(g, deg_corr=True)
    state.draw(output="celegans-hsbm-fit.png")

if __name__ == '__main__':
    # hierpath()
    # simple_graph()

    source_path = "../trisampleconverter/test_brexit/412x36x1000/"

    # infile = InFile(source_path+"OutMatrix_7x5x3_p07_n007.out", "OutMatrix_7x5x3_p07_n007.pdf")
    # infile = InFile(source_path+"OutMatrix_10x10x3_p05_n005.out", "OutMatrix_10x10x3_p05_n005.pdf")
    # infile = InFile(source_path+"OutMatrix_20x10x3_p05_n005.out", "OutMatrix_20x10x3_p05_n005.pdf")
    infile = InFile(source_path+"OutMatrix_20x10x3_p03_n003.out", "OutMatrix_20x10x3_p03_n003.pdf")
    infile.decode()
    infile.draw_graph()