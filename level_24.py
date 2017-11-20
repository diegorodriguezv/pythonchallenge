# LEVEL 24
# http://www.pythonchallenge.com/pc/hex/ambiguity.html

from collections import deque

from PIL import Image

img = Image.open('data/maze.png')  # type = Image.Image
maze = img.load()
wall = (255, 255, 255, 255)
print(img.size)
print(maze[640, 0])
print(img.mode)

# look for the start and end positions right to left (to avoid the problem number on the top left)
w, h = img.size
start, end = None, None
for x in range(w - 1, -1, -1):
    if maze[x, 0] != wall and start is None:
        start = (x, 0)
    if maze[x, h - 1] != wall and end is None:
        end = (x, h - 1)

print(start, end)


# print(maze[start], maze[end])


def neighbors(pos, maze, size, visited):
    """Returns a list with the neighbors of pos not in visited."""
    x, y = pos
    w, h = size
    result = []
    for x_offset in (-1, 1):
        new_x = x + x_offset
        new_y = y
        if 0 <= new_x < w and 0 <= new_y < h and maze[new_x, new_y] != wall and (new_x, new_y) not in visited:
            result.append((new_x, new_y))
    for y_offset in (-1, 1):
        new_x = x
        new_y = y + y_offset
        if 0 <= new_x < w and 0 <= new_y < h and maze[new_x, new_y] != wall and (new_x, new_y) not in visited:
            result.append((new_x, new_y))
    return result


# print(neighbors(start, maze, img.size, []))
# print(neighbors(end, maze, img.size, []))
# print(neighbors((639, 1), maze, img.size, []))
# print(neighbors((1, 639), maze, img.size, []))
# print(neighbors(start, maze, img.size, [start]))
# print(neighbors(end, maze, img.size, [end]))
# print(neighbors((639, 1), maze, img.size, [start]))
# print(neighbors((1, 639), maze, img.size, [end]))


def bfs(start, end, maze, size):
    """Returns a tree with positions that lead from start to end or None if no solution exists. The tree is a dict that
    represent each node as a key and it's parent (or predecessor) as a value. The visited set is also returned for
    visualization purposes."""
    parents = {}
    visited = set()
    fringe = deque()
    fringe.append(start)
    finished = False
    while not finished:
        if len(fringe) == 0:
            return None
        node = fringe.popleft()
        visited.add(node)
        if node == end:
            return parents, visited
        for neighbor in neighbors(node, maze, size, visited):
            parents[neighbor] = node
            fringe.append(neighbor)


tree, visited = bfs(start, end, maze, img.size)
print(len(tree))
print(len(visited))

# create a list with the solution (shortest path) from the tree
sol = deque()
child = end
sol.append(child)
while True:
    parent = tree[child]
    sol.appendleft(parent)
    if parent == start:
        break
    child = parent
print(len(sol))

# print([sol[i] for i in range(10)])
# print([sol[i] for i in range(len(sol) - 1, len(sol) - 11, -1)])

# fill a list of pixels and an array of the even numbered bytes (the odd ones are all zero)
pixels = []
even_bytes = bytearray()  # b'')
even = False
for i in range(len(sol)):
    if even:
        even_bytes.append(img.getpixel(sol[i])[0])
    even = not even
    pixels.append(img.getpixel(sol[i]))

print(pixels[:10])
print(even_bytes[:10])

# paint visited nodes blue
visited_l = list(visited)
for i in range(len(visited)):
    img.putpixel(visited_l[i], (0, 0, 255, 255))
# paint the shortest path green
for i in range(len(sol)):
    img.putpixel(sol[i], (0, 255, 0, 255))
img.save('data/maze_sol.png')

# the even bytes start with b'PK\x03\x04' which look like a zip fle
with open('data/level_24.zip', 'wb') as f:
    f.write(even_bytes)


