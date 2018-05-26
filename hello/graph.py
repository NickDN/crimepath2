import osmnx as ox

print('Load graph was started')
# G = ox.load_graphml('chicago_ds')
G = ox.load_graphml('chicago_2.xml')

for s, t, k in G.edges(data=True):
    G[s][t][k['key']]['h19'] = float(G[s][t][k['key']]['h19'])
print('Load graph was finished')
