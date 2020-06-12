from matplotlib import pyplot as plt
from scipy.cluster import hierarchy
import numpy as np
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt

#Plots Linage trye

def PlotLinageTree(trackedCells):
    G = nx.DiGraph()
    #Add all Cells As Nodes
    for trCell in trackedCells:
        cellLabel = "ID " + str(trCell.getCellID())
        G.add_node(cellLabel)

    #Add all edges
    for trCell in trackedCells:
        motherID = trCell.getMotherCell()
        cellLabelM = "ID " + str(motherID)
        cellLabelD = "ID " + str(trCell.getCellID())
        G.add_edge(cellLabelM, cellLabelD, object='10')

    nx.draw_networkx(G, pos = nx.spring_layout(G))
    nx.draw_networkx_edge_labels(G, pos = nx.spectral_layout(G))
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
