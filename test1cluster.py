'''
    Author : Sefa Koc
    Cluster results on test 1
    cluster size = (17 x 3 x 6)
'''
from numpy.random import *  # for random sampling
seed(42)

from graph_tool.all import *

def simple_graph():
    ug  = Graph()
    ug.set_directed(False)

    keyw = []
    iss = []
    users = []

    for i in xrange(6):
        keyw.append(ug.add_vertex())

    for i in xrange(3):
        iss.append(ug.add_vertex())
    for i in xrange(17):#17
        users.append(ug.add_vertex())

    #1 - 0
    for i in xrange(6):
        if i != 3:
            ug.add_edge(iss[0], keyw[i])
            ug.add_edge(users[0], keyw[i])
            ug.add_edge(users[0], iss[0])
        if i != 5:
            ug.add_edge(iss[1], keyw[i])
            ug.add_edge(users[0], keyw[i])
            ug.add_edge(users[0], iss[1])
        if i != 4:
            ug.add_edge(iss[2], keyw[i])
            ug.add_edge(users[0], keyw[i])
            ug.add_edge(users[0], iss[2])

    #2 - 3
    for i in xrange(6):
        ug.add_edge(iss[0], keyw[i])
        ug.add_edge(users[1], keyw[i])
        ug.add_edge(users[1], iss[0])
        if i != 5:
            ug.add_edge(iss[1], keyw[i])
            ug.add_edge(users[1], keyw[i])
            ug.add_edge(users[1], iss[1])
        if i != 0 and i!=4:
            ug.add_edge(iss[2], keyw[i])
            ug.add_edge(users[1], keyw[i])
            ug.add_edge(users[1], iss[2])

    #3 - 33
    for i in xrange(6):
        ug.add_edge(iss[0], keyw[i])
        ug.add_edge(users[2], keyw[i])
        ug.add_edge(users[2], iss[0])
        if i != 2:
            ug.add_edge(iss[1], keyw[i])
            ug.add_edge(users[2], keyw[i])
            ug.add_edge(users[2], iss[1])
        if i != 1 and i!=3 and i!=5:
            ug.add_edge(iss[2], keyw[i])
            ug.add_edge(users[2], keyw[i])
            ug.add_edge(users[2], iss[2])

    #4 - 55
    for i in xrange(6):
        ug.add_edge(iss[0], keyw[i])
        ug.add_edge(users[3], keyw[i])
        ug.add_edge(users[3], iss[0])
        if i != 5:
            ug.add_edge(iss[1], keyw[i])
            ug.add_edge(users[3], keyw[i])
            ug.add_edge(users[3], iss[1])
        if i != 0 and i!=1 and i!=4:
            ug.add_edge(iss[2], keyw[i])
            ug.add_edge(users[3], keyw[i])
            ug.add_edge(users[3], iss[2])

    #5 - 82
    for i in xrange(6):
        ug.add_edge(iss[0], keyw[i])
        ug.add_edge(users[4], keyw[i])
        ug.add_edge(users[4], iss[0])
        if i != 0 and i!=4:
            ug.add_edge(iss[1], keyw[i])
            ug.add_edge(users[4], keyw[i])
            ug.add_edge(users[4], iss[1])
        if i == 1 or i == 5:
            ug.add_edge(iss[2], keyw[i])
            ug.add_edge(users[1], keyw[i])
            ug.add_edge(users[1], iss[2])

    #6 - 100
    for i in xrange(6):
        ug.add_edge(iss[0], keyw[i])
        ug.add_edge(users[5], keyw[i])
        ug.add_edge(users[5], iss[0])
        if i != 2:
            ug.add_edge(iss[1], keyw[i])
            ug.add_edge(users[5], keyw[i])
            ug.add_edge(users[5], iss[1])
        if i == 5:
            ug.add_edge(iss[2], keyw[i])
            ug.add_edge(users[5], keyw[i])
            ug.add_edge(users[5], iss[2])

    #7 - 149
    for i in xrange(6):
        ug.add_edge(iss[0], keyw[i])
        ug.add_edge(users[6], keyw[i])
        ug.add_edge(users[6], iss[0])
        if i != 1:
            ug.add_edge(iss[1], keyw[i])
            ug.add_edge(users[6], keyw[i])
            ug.add_edge(users[6], iss[1])
        if i != 0 and i != 4:
            ug.add_edge(iss[2], keyw[i])
            ug.add_edge(users[6], keyw[i])
            ug.add_edge(users[6], iss[2])

    #8 - 154
    for i in xrange(6):
        ug.add_edge(iss[0], keyw[i])
        ug.add_edge(users[7], keyw[i])
        ug.add_edge(users[7], iss[0])
        if i != 4:
            ug.add_edge(iss[1], keyw[i])
            ug.add_edge(users[7], keyw[i])
            ug.add_edge(users[7], iss[1])
        if i != 0:
            ug.add_edge(iss[2], keyw[i])
            ug.add_edge(users[7], keyw[i])
            ug.add_edge(users[7], iss[2])

    #9 - 157
    for i in xrange(6):
        if i != 2:
            ug.add_edge(iss[0], keyw[i])
            ug.add_edge(users[8], keyw[i])
            ug.add_edge(users[8], iss[0])
        if i != 1 and i != 4 and i != 5:
            ug.add_edge(iss[1], keyw[i])
            ug.add_edge(users[8], keyw[i])
            ug.add_edge(users[8], iss[1])
        if i != 0 and i != 4:
            ug.add_edge(iss[2], keyw[i])
            ug.add_edge(users[8], keyw[i])
            ug.add_edge(users[8], iss[2])

    #10 - 175
    for i in xrange(6):
        if i != 5:
            ug.add_edge(iss[0], keyw[i])
            ug.add_edge(users[9], keyw[i])
            ug.add_edge(users[9], iss[0])
        if i != 4:
            ug.add_edge(iss[1], keyw[i])
            ug.add_edge(users[9], keyw[i])
            ug.add_edge(users[9], iss[1])
        if i == 3:
            ug.add_edge(iss[2], keyw[i])
            ug.add_edge(users[9], keyw[i])
            ug.add_edge(users[9], iss[2])

    #11 - 193
    for i in xrange(6):
        if i != 1 and i != 3:
            ug.add_edge(iss[0], keyw[i])
            ug.add_edge(users[10], keyw[i])
            ug.add_edge(users[10], iss[0])
        if i != 3:
            ug.add_edge(iss[1], keyw[i])
            ug.add_edge(users[10], keyw[i])
            ug.add_edge(users[10], iss[1])
        if i != 0 and i != 1 and i != 4:
            ug.add_edge(iss[2], keyw[i])
            ug.add_edge(users[10], keyw[i])
            ug.add_edge(users[10], iss[2])

    #12 - 200
    for i in xrange(6):
        if i != 2:
            ug.add_edge(iss[0], keyw[i])
            ug.add_edge(users[11], keyw[i])
            ug.add_edge(users[11], iss[0])
        if i != 1 and i != 2 and i != 4:
            ug.add_edge(iss[1], keyw[i])
            ug.add_edge(users[11], keyw[i])
            ug.add_edge(users[11], iss[1])
        if i != 2 and i != 4:
            ug.add_edge(iss[2], keyw[i])
            ug.add_edge(users[11], keyw[i])
            ug.add_edge(users[11], iss[2])

    #13 - 206
    for i in xrange(6):
        ug.add_edge(iss[0], keyw[i])
        ug.add_edge(users[12], keyw[i])
        ug.add_edge(users[12], iss[0])
        if i != 2:
            ug.add_edge(iss[1], keyw[i])
            ug.add_edge(users[12], keyw[i])
            ug.add_edge(users[12], iss[1])
        if i != 1 and i != 2 and i != 4:
            ug.add_edge(iss[2], keyw[i])
            ug.add_edge(users[12], keyw[i])
            ug.add_edge(users[12], iss[2])

    #14 - 240
    for i in xrange(6):
        ug.add_edge(iss[0], keyw[i])
        ug.add_edge(users[13], keyw[i])
        ug.add_edge(users[13], iss[0])
        if i != 2 and i != 4:
            ug.add_edge(iss[1], keyw[i])
            ug.add_edge(users[13], keyw[i])
            ug.add_edge(users[13], iss[1])

    #15 - 243
    for i in xrange(6):
        ug.add_edge(iss[0], keyw[i])
        ug.add_edge(users[14], keyw[i])
        ug.add_edge(users[14], iss[0])
        if i != 3 and i != 4:
            ug.add_edge(iss[1], keyw[i])
            ug.add_edge(users[14], keyw[i])
            ug.add_edge(users[14], iss[1])
        if i != 0 and i != 2 and i != 4:
            ug.add_edge(iss[2], keyw[i])
            ug.add_edge(users[14], keyw[i])
            ug.add_edge(users[14], iss[2])

    #16 - 253
    for i in xrange(6):
        if i != 1:
            ug.add_edge(iss[0], keyw[i])
            ug.add_edge(users[15], keyw[i])
            ug.add_edge(users[15], iss[0])
        if i != 0 and i != 1 and i != 4:
            ug.add_edge(iss[1], keyw[i])
            ug.add_edge(users[15], keyw[i])
            ug.add_edge(users[15], iss[1])
        if i != 0 and i != 5:
            ug.add_edge(iss[2], keyw[i])
            ug.add_edge(users[15], keyw[i])
            ug.add_edge(users[15], iss[2])

    #17 - 256
    for i in xrange(6):
        ug.add_edge(iss[0], keyw[i])
        ug.add_edge(users[16], keyw[i])
        ug.add_edge(users[16], iss[0])
        if i == 4 or i == 5:
            ug.add_edge(iss[1], keyw[i])
            ug.add_edge(users[16], keyw[i])
            ug.add_edge(users[16], iss[1])
        if i != 0 and i != 5:
            ug.add_edge(iss[2], keyw[i])
            ug.add_edge(users[16], keyw[i])
            ug.add_edge(users[16], iss[2])


    # deg = ug.degree_property_map("in")
    # from math import sqrt
    # deg.a = 4*(deg.a *0.5 + 0.4)
    state = minimize_nested_blockmodel_dl(ug, deg_corr=False)
    # state = minimize_blockmodel_dl(ug, deg_corr=True)
    state.draw(output="cluster_test1.png")
    # graph_draw(ug, vertex_size=deg, vertex_fill_color=deg, vertex_font_size=18,
    #            output_size=(600, 600), output="three-nodes.png")