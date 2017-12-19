import math

INFINITY = math.inf  # float("inf")


class myQueue(list):
    def __init__(self, a = []):
        list.__init__(self, a)

    def dequeue(self):
        return self.pop(0)

    def enqueue(self, x):
        self.append(x)


class Vertex:
    def __init__(self, data):
        self.data = data

    def __repr__(self):         # voor afdrukken
        return str(self.data)

    def __lt__(self, other):    # voor sorteren
        return self.data < other.data


def vertices(G):
    return sorted(G)


def edges(G):
    return [(u, v) for u in vertices(G) for v in G[u]]


def clear(G):
    for v in vertices(G):
        k = [e for e in vars(v) if e != 'data']
        for e in k:
            delattr(v, e)


def BFS(G, s):
    V = vertices(G)
    s.predecessor = None
    s.distance = 0
    for v in V:
        if v != s:
            v.distance = INFINITY  # v krijgt het attribuut 'distance'
    q = myQueue()
    q.enqueue(s)
    # print("q:", q)
    while q:
        u = q.dequeue()
        for v in G[u]:
            if v.distance == INFINITY:  # v is nog niet bezocht
                v.distance = u.distance + 1
                v.predecessor = u  # v krijgt het attribuut 'predecessor'
                q.enqueue(v)
#        print("q:", q)


def show_tree_info(G):
    print('tree:', end = ' ')
    for v in vertices(G):
        print('(' + str(v), end = '')
        if hasattr(v, 'distance'):
            print(',d:' + str(v.distance), end = '')
        if hasattr(v, 'predecessor'):
            print(',p:' + str(v.predecessor),  end = '')
        print(')', end = ' ')
    print()

# show_tree_info(G)


def show_sorted_tree_info(G):
    print('sorted tree:')
    V = vertices(G)
#    V = [v for v in V if hasattr(v,'distance') and hasattr(v,'predecessor')]
    V.sort(key = lambda x: (x.distance, x.predecessor))
    d = 0
    for v in V:
        if v.distance > d:
            print()
            d += 1
        print('(' + str(v) + ',d:' + str(v.distance) + ',p:' + str(v.predecessor),  end = '')
        print(')', end = ' ')
    print()

# show_sorted_tree_info(G)


def path_BFS(G, u, v):
    BFS(G, u)
    a = []
    if hasattr(v, 'predecessor'):
        current = v
        while current:
            a.append(current)
            current = current.predecessor
        a.reverse()
    return a


def is_connected(G):
    BFS(G, vertices(G)[0])  # Set distance attributes

    for vertex in G:
        if vertex.distance == INFINITY:  # If a vertex still has INFINITY, it means that it's not connected with V[0]
            return False
    return True


def no_cycles(G):
    # BFS
    s = vertices(G)[0]
    V = vertices(G)
    s.predecessor = None
    s.distance = 0
    for vertex in V:
        if vertex != s:
            vertex.distance = INFINITY  # v krijgt het attribuut 'distance'
    q = myQueue()
    q.enqueue(s)

    while q:
        u = q.dequeue()
        for vertex in G[u]:
            if vertex.distance == INFINITY:  # Vertex not yet visited
                vertex.distance = u.distance + 1
                vertex.predecessor = u  # Vertex gets attribute 'predecessor'
                q.enqueue(vertex)
            elif u.predecessor != vertex:  # U already visited by a other vertex
                return False  # No Cykel
    return True  # No Cykel


def get_bridges(G):
    bridges = []

    for e in edges(G):
        # Remove the edges
        G[e[0]].remove(e[1])
        G[e[1]].remove(e[0])
        if not is_connected(G):
            bridges.append(e)

        # repair bridge
        G[e[0]].append(e[1])
        G[e[1]].append(e[0])

    return bridges


def strongly_connected(G):
    if not is_connected(G):
        return False

    # reverse the graph
    other = {}
    for edge in edges(G):
        if edge[1] in other.keys():
            other[edge[1]].append(edge[0])
        else:
            other[edge[1]] = [edge[0]]

    return is_connected(other)


def is_euler_graph(G):
    for vertex in G:
        if len(G[vertex]) & 1:
            return False

    return True


def get_euler_circuit(G, s):
    # first check if it is a Euler graph
    if not is_euler_graph(G):
        return []

    # loop through the steps inside the node
    path = [s]
    while G[s]:
        tpm = None

        # Find the first non bridge neighbor else take bridge neighbor
        for t in G[s]:
            tmp = t  # Temp save the value
            if (s, t) not in get_bridges(G):
                break

        #  Add the steps and remove the traversed nodes from each other
        if tmp is not None:
            # path
            path.append(tmp)
            # Remove (s, t) and (t, s) edge
            G[s].remove(tmp)
            G[tmp].remove(s)
            # Check next neighbor
            s = tmp

    return path


v = [Vertex(i) for i in range(8)]

G1 = {
    v[0]: [v[4], v[5]],
    v[1]: [v[4], v[5], v[6]],
    v[2]: [v[4], v[5], v[6]],
    v[3]: [v[7]],
    v[4]: [v[0], v[1], v[5]],
    v[5]: [v[1], v[2], v[4]],
    v[6]: [v[1], v[2]],
    v[7]: [v[3]]
}

G2 = {
    v[0]: [v[4], v[5]],
    v[1]: [v[4], v[5], v[6]],
    v[2]: [v[4], v[5], v[6]],
    v[4]: [v[0], v[1], v[5]],
    v[5]: [v[1], v[2], v[4]],
    v[6]: [v[1], v[2]],
}

G3 = {
    v[0]: [v[4], v[5]],
    v[1]: [v[4], v[6]],
    v[2]: [v[5]],
    v[3]: [v[7]],
    v[4]: [v[0], v[1]],
    v[5]: [v[0], v[2]],
    v[6]: [v[1]],
    v[7]: [v[3]],
}

G4 = {
    v[0]: [v[1], v[3]],
    v[1]: [v[0], v[2]],
    v[2]: [v[1], v[3], v[4]],
    v[3]: [v[0], v[2]],
    v[4]: [v[2], v[5], v[6]],
    v[5]: [v[4], v[6]],
    v[6]: [v[4], v[5], v[7]],
    v[7]: [v[6]],
}

G5 = {
    v[0]: [v[1]],
    v[1]: [v[2]],
    v[2]: [v[0]],
}

G6 = {
    v[0]: [v[1]],
    v[2]: [v[0], v[1]],
}

G7 = {
    v[0]: [v[1], v[2]],
    v[1]: [v[2], v[0]],
    v[2]: [v[0], v[1]],
}

G8 = {
    v[0]: [v[1], v[2]],
    v[1]: [v[0], v[3]],
    v[2]: [v[0], v[3]],
    v[3]: [v[1], v[2], v[4], v[6]],
    v[4]: [v[3], v[5], v[6], v[7]],
    v[5]: [v[4], v[6]],
    v[6]: [v[3], v[4], v[5], v[7]],
    v[7]: [v[4], v[6]],
}

print("is_connected(G1):", is_connected(G1))
print("is_connected(G2):", is_connected(G2))
print("no_cycles(G1):", no_cycles(G1))
print("no_cycles(G2):", no_cycles(G2))
print("no_cycles(G3):", no_cycles(G3))
print("get_bridges(G4):", get_bridges(G4))
print("strongly_connected(G5):", strongly_connected(G5))
print("strongly_connected(G6):", strongly_connected(G6))
print("is_euler_graph(G8):", is_euler_graph(G8))

for vertex in vertices(G8):
    print("get_euler_circuit(G8, {}):".format(vertex), get_euler_circuit(G8, vertex))

