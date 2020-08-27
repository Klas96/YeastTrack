from matplotlib import pyplot as plt
from scipy.cluster import hierarchy
import numpy as np
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt
from Anlysis.visulizeLinNetworkX import plotNxTree
#import PyQt5
#from ete3 import Tree
#'from ete3 import TreeStyle
#   from igraph import *;
from networkx.drawing.nx_agraph import graphviz_layout


#def PlotLinageTree(trackedCells):
#

#Plots Linage tree
def PlotLinageTree(trackedCells):
    G = nx.DiGraph()
    #Add all Cells As Nodes
    for trCell in trackedCells:
        cellLabel = str(trCell.getCellID())#"ID " +
        G.add_node(cellLabel)

    #Add all edges
    for trCell in trackedCells:
        motherID = trCell.getMotherCell()
        if motherID == None:
            motherID = -1
        cellLabelM = str(motherID)#"ID " +
        cellLabelD = str(trCell.getCellID())#"ID " +
        relFactor = trCell.getRelatabelityFactor()
        G.add_edge(cellLabelM, cellLabelD, object=str(round(relFactor, 2)))

    btree = G#nx.balanced_tree(2,4)
    pos=graphviz_layout(G,prog='dot')
    nx.draw(G,pos,with_labels=True,arrows=True)
    #plotNxTree(G)
    #nx.draw_networkx(G, pos = nx.spring_layout(G))
    #nx.draw_networkx_edge_labels(G, pos = nx.spectral_layout(G))
    #plt.sxhow()
    #pos = nx.nx_pydot.graphviz_layout(g, prog='neato')
    #nx.draw(g, pos=layout)
    edge_labels = nx.get_edge_attributes(G, 'object')
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels)
    plt.show()


def PlotLinageTreeOLD(trackedCells):
    G = nx.DiGraph()

    G.add_node("ROOT")

    for i in range(5):
        G.add_node("Child_%i" % i)
        G.add_node("Grandchild_%i" % i)
        G.add_node("Greatgrandchild_%i" % i)

        G.add_edge("ROOT", "Child_%i" % i)
        G.add_edge("Child_%i" % i, "Grandchild_%i" % i)
        G.add_edge("Grandchild_%i" % i, "Greatgrandchild_%i" % i)

    # write dot file to use with graphviz
    # run "dot -Tpng test.dot >test.png"
    nx.nx_agraph.write_dot(G,'test.dot')

    # same layout using matplotlib with no labels
    plt.title('draw_networkx')
    pos=graphviz_layout(G, prog='dot')
    nx.draw(G, pos, with_labels=False, arrows=False)
    plt.savefig('nx_test.png')
