import math 
VERTEX = 23

s = [1344,1106]
o1 = [1532,1306]
o2 = [1470,1442]
o3 = [1440,1424]
o4 = [1368,1462]
o5 = [1113,1490]
o6 = [1021,1346]
o7 = [956,1254]
o8 = [810,1289]
o9 = [958,1190]
o10 = [1275,1090]
o11 = [1097,989]
o12 = [1306,815]
o13 = [1327,720]
o14 = [1479,655]
o15 = [897,847]
o16 = [783,919]
o17 = [751,1015]
o18 = [789,1042]
o19 = [783,1115]
o20 = [724,1209]
o21 = [488,1514]
o22 = [469,1458]
o23 = [347,1199]

oysters = [s,o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12,o13,o14,o15,o16,o17,o18,o20,o21,o22,o23]

def generate_graph():
    distances = []
    graph = [[0]*VERTEX for i in range(VERTEX)]
    for i in range(0, VERTEX):
        for j in range(0, VERTEX):
            distance = int(math.dist(oysters[i],oysters[j]))
            graph[i][j] = distance
            distances.append(distance) 
        distances = []

    print(graph)
    return graph



