class Node:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.hori = []
        self.vert = []
        self.diag = []
        self.anti = []
        self.mark = False

def doomed_gambit(coords: list[tuple[int, int]]) -> list[tuple[int, int]]:
    nodes = [Node(x, y) for x, y in coords]
    q = len(nodes)
    
    # Horizontal
    nodes = sorted(nodes, key=lambda n: (n.x, n.y))
    for i in range(q):
        if i != 0 and nodes[i].x == nodes[i-1].x:
            nodes[i].hori.append(nodes[i-1])
        if i != q - 1 and nodes[i].x == nodes[i+1].x:
            nodes[i].hori.append(nodes[i+1])
    
    # Vertical
    nodes = sorted(nodes, key=lambda n: (n.y, n.x))
    for i in range(q):
        if i != 0 and nodes[i].y == nodes[i-1].y:
            nodes[i].vert.append(nodes[i-1])
        if i != q - 1 and nodes[i].y == nodes[i+1].y:
            nodes[i].vert.append(nodes[i+1])

    # Diagonal
    nodes = sorted(nodes, key=lambda n: (n.x + n.y, n.x))
    for i in range(q):
        if i != 0 and nodes[i].x + nodes[i].y == nodes[i-1].x + nodes[i-1].y:
            nodes[i].diag.append(nodes[i-1])
        if i != q - 1 and nodes[i].x + nodes[i].y == nodes[i+1].x + nodes[i+1].y:
            nodes[i].diag.append(nodes[i+1])
            
    
    # Antidiagonal
    nodes = sorted(nodes, key=lambda n: (n.y - n.x, n.x))
    for i in range(q):
        if i != 0 and nodes[i].y - nodes[i].x == nodes[i-1].y - nodes[i-1].x:
            nodes[i].anti.append(nodes[i-1])
        if i != q - 1 and nodes[i].y - nodes[i].x == nodes[i+1].y - nodes[i+1].x:
            nodes[i].anti.append(nodes[i+1])
    
    for node in nodes:
        if len(node.hori + node.vert + node.diag + node.anti) == 1:
            node.mark = True
    
    doomed = []
    for node in nodes:
        if len(node.hori) == 0 or len(node.hori) == 1 and node.hori[0].mark:
            continue
        if len(node.vert) == 0 or len(node.vert) == 1 and node.vert[0].mark:
            continue
        if len(node.diag) == 0 or len(node.diag) == 1 and node.diag[0].mark:
            continue
        if len(node.anti) == 0 or len(node.anti) == 1 and node.anti[0].mark:
            continue
        doomed.append(node)

    return [(node.x, node.y) for node in doomed]

n = int(input())
for _ in range(n):
    input()
    xs = [int(x) for x in input().split()]
    ys = [int(y) for y in input().split()]
    pairs = doomed_gambit(list(zip(xs, ys)))
    if len(pairs) == 0:
        doomed_xs, doomed_ys = [], []
    else:
        doomed_xs, doomed_ys = list(zip(*pairs))
    
    print(*doomed_xs)
    print(*doomed_ys)
