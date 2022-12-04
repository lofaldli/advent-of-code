from math import prod
from aocd import data
    

def get_edges(pixels):
    return [
        int(row, 2) for row in (
            pixels[0], ''.join(row[-1] for row in pixels),
            pixels[-1], ''.join(row[0] for row in pixels)
        )
    ]
    
def flipx(pixels):
    return [''.join(reversed(row)) for row in pixels]
        
def flipy(pixels):
    return list(reversed(pixels))

def find_corners(tiles):
    edges_dict = {}
    for id, pixels in tiles.items():
        edges_dict[id] = set(get_edges(pixels) + get_edges(flipx(pixels)) + get_edges(flipy(pixels)))    
    corners = []
    for id in edges_dict:
        others = set.union(*[v for k, v in edges_dict.items() if k != id])
        if len(edges_dict[id].intersection(others)) == 4:
            corners.append(id)
    return corners
    
class Tile:
    def __init__(self, id, pixels, xflipped=False, yflipped=False, rotation=0):
        self.id, self.pixels, self.xflipped, self.yflipped, self.rotation = id, pixels, xflipped, yflipped, rotation
        
    def edges(self):
        pixels = self.pixels[:]
        if self.yflipped:
            pixels = flipy(pixels)
        if self.xflipped:
            pixels = flipx(pixels)
        edges = get_edges(pixels)
        return edges[:self.rotation] + edges[self.rotation:]
        
    def border(self, other):
        intersection = set(self.edges()).intersection(set(other.edges()))
        if len(intersection) == 1:
            return intersection.pop()
        else:
            return None
               
    def __repr__(self):
        return f'Tile(id={self.id}, xflipped={self.xflipped}, yflipped={self.yflipped}, rotation={self.rotation})'
        
lines = iter(data.splitlines())
tiles = dict()
T = str.maketrans('.#', '01')
while True:
    try:
        id = int(next(lines)[5:-1])
    except StopIteration:
        break
    rows = []
    for line in lines:
        if line == '':
            break
        rows.append(line.translate(T))
    tiles[id] = rows

corners = find_corners(tiles)
tiles = {id:Tile(id, pixels) for id, pixels in tiles.items()}
print('part 1', prod(corners))


size = int(len(tiles)**0.5)
grid = []
row = []
current = tiles.pop(corners[0])

row.append(current)
current_edges = set(current.edges())
xflip = False
while len(row) < size:
    for tile in tiles.values():
        tile.xflipped = xflip
        border = current.border(tile)
        if border is not None:
            print(border)
            current.rotation = (current.edges().index(border) - 1) % 4
            tile.rotation = (tile.edges().index(border) - 3) % 4
            row.append(tile)
            current = tile
            break
    else:
        xflip = True

for tile in row:
    print(tile, tile.edges())      

