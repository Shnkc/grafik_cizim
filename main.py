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



def hierpath():
    g = gt.collection.data["celegansneural"]
    state = minimize_nested_blockmodel_dl(g, deg_corr=True)
    state.draw(output="celegans-hsbm-fit.png")

if __name__ == '__main__':
    # hierpath()
    simple_graph()