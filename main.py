import random
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def graph_generation(cells, h):
    G = nx.Graph(undirected=True)
    row = int(cells / h)
    cells = row * h
    for i in range(cells):
        G.add_node(i, weight=0)

    if cells < 30:
        print("Not enough cells")

    else:
        x = 0
        for j in range(h):
            for i in range(row - 1):
                G.add_edge(x, x + 1)
                x = x + 1
            x = x + 1
        x = 0
        y = 1
        for i in range(h - 1):
            for j in range(row):
                G.add_edge(x, x + row)
                x = x + 1
            for k in range(row - 1):
                G.add_edge(y, y + row - 1)
                y += 1
            y += 1

        x = 0

        for i in range(row):
            G.add_edge(i, i + (row * (h - 1)))
        for i in range(row - 1):
            G.add_edge(i, i + 1 + (row * (h - 1)))
        for i in range(h):
            if i == 0:
                G.add_edge(i, row - 1)
                G.add_edge(i, cells - 1)
            elif i == h - 1:
                G.add_edge(i * row, i * row + row - 1)
                G.add_edge(i * row, i * row - 1)
            else:
                G.add_edge(i * row, i * row + row - 1)
                G.add_edge(i * row, i * row - 1)
    return G, cells


def adjacency_list(G):
    adj_list=[]
    tab=[]
    for i in G.adjacency():
        for j in i[1]:
            tab.append(j)
        adj_list.append(tab)
        tab=[]
    for i in range(len(adj_list)):
        if len(adj_list[i])!=6:
            print(i, adj_list[i])
    return adj_list


def weights_generation(start, stop, masa, G, adj_list):
    weights_old = nx.get_node_attributes(G, "weight")
    weights_old[start] = masa
    weights_old[stop] = masa
    n = 0
    for i in adj_list:
        if n != start and n != stop:
            weight = np.random.normal(50, 25)
            a = 0
            b = 0
            c = 0
            if weight < 33:
                waga = 1
            elif weight > 66:
                waga = 3
            else:
                waga = 2
            x = 0

            for j in i:
                if weights_old[n] == weights_old[j]:
                    x += 1

                if weights_old[j] == 1:
                    a += 1
                elif weights_old[j] == 2:
                    b += 1
                elif weights_old[j] == 3:
                    c += 1
            tab = [a, b, c]
            if x <= 2:
                weights_old[n] = waga
            else:
                weights_old[n] = tab.index(min(tab)) + 1
        n += 1
    nx.set_node_attributes(G, weights_old, 'weight')

    return G, weights_old


def graph_display(G, cells):
    if cells <= 400:
        colors = [G.nodes[n]['weight'] for n in G.nodes]
        fig = plt.figure(1, figsize=(32, 20), dpi=90)

        nx.draw(
            G,
            cmap=plt.cm.Blues,
            with_labels=True,
            node_color=colors,
            node_size=3000,
        )
        fig.set_facecolor("#414141")
        plt.show()


def connections_gen(adj_list, cells, weights):
    connections = []
    for i in range(cells):
        tab = []
        tab.append(i)
        for j in adj_list[i]:
            if weights[i] is weights[j]:
                tab.append(j)
        if len(tab) > 1:
            connections.append(tab)
        else:
            connections.append([i])

    jd = 0
    i = 1
    while (jd == 0):
        start = len(connections)
        for i in connections:
            for j in i:
                for k in connections:
                    if j in k and i != k and j:
                        for n in range(len(k)):
                            if k[n] not in i:
                                i.append(k[n])
                        connections.remove(k)

        koniec = len(connections)
        if start - koniec == 0:
            jd = 1
        elif len(connections) == 1:
            print("Error")
            break
        else:
            jd = 0
    return connections


def all_paths(start, stop, G, masa, adj_list, weights, connections):
    path = nx.shortest_path(G, start, stop)
    for i in range(len(adj_list)):
        if i not in path:
            waga = random.randint(1, 3)
            weights[i] = waga
        if i in path and weights[i] != masa:
            waga = random.randint(1, 3)
            weights[i] = waga

    nx.set_node_attributes(G, weights, 'weight')
    return G, weights


cells = 120
h = 8  # NEEDS TO BE EVEN!!!!!
start = 0
stop = 72
masa = 1

G, cells = graph_generation(cells, h)
adj_list = adjacency_list(G)
G, weights = weights_generation(start, stop, masa, G, adj_list)
connections = [[], []]
jd = 0
graph_display(G, cells)
while jd == 0:
    connections = connections_gen(adj_list, cells, weights)
    G, weights = all_paths(start, stop, G, masa, adj_list, weights, connections)
    graph_display(G, cells)
    connections = connections_gen(adj_list, cells, weights)
    for i in connections:
        if start in i and stop in i:
            print(i)
            jd = 1