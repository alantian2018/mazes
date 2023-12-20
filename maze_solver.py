from collections import deque 
import time

def read_maze():
    with open ("maze.txt") as f:
        maze = f.read().split('\n')
    maze = [list(i) for i in maze]
    return maze

def print_maze(maze, endline = True):
    for i in maze:
        print(''.join(i)) 
    if endline: 
        print("\033[F"*(len(maze)+1))

def maze_solver(maze):
    startx,starty=0,0
    endx,endy=0,0

    for i in range (len(maze)):
        for j in range (len(maze[0])):
            if (maze[i][j]=='S'):
                startx,starty = i,j
            elif maze[i][j]=='E':
                endx,endy=i,j
    visited = [[False for i in range(len(maze[0]))] for j in range(len(maze))]
    
    q = deque()
    paths = dict()
    q.append((startx,starty))

    xmoves = [0,0,1,-1]
    ymoves = [1,-1,0,0]
    maze[startx][starty] = "\033[0;31m"+maze[startx][starty] + "\x1b[0m"
    maze[endx][endy]= '\033[0;32m' + maze[endx][endy] + "\x1b[0m"

    while len(q) != 0:
        current_point = q.popleft()
        x = current_point[0]
        y = current_point[1]
        maze[x][y] = "\033[0;35m" + maze[x][y] + '\x1b[0m'
        time.sleep(.05)
        print_maze(maze)

        if (x==endx and y==endy):
            break

        visited[x][y] = True
        for a,b in zip(xmoves,ymoves):
            xx = x + a
            yy = y + b
            if (0<=xx<len(maze) and 0<=yy<len(maze[0]) and not visited[xx][yy] and maze[xx][yy]!='#'):
                visited[xx][yy]=True
                point = (xx, yy)
                q.append(point)

                paths[point] = current_point
    p = []
    
    retrace = (endx,endy)
    
    while (retrace != (startx, starty)):
        try:
            retrace = paths[retrace]
        except:
            raise ValueError("NO VALID PATH FOUND")
        if (retrace!=(endx,endy) and retrace!=(startx,starty)):
            p.append(retrace)
 
    p = p [::-1]
    
    return p
    



def visualize():
    maze = read_maze()
    p = maze_solver(maze)
    print_maze(maze)

    for c,i in enumerate(p):
        time.sleep(.05)
        maze[i[0]][i[1]]= "\033[0;36m" + '%' + '\x1b[0m'

        if c==len(p)-1:
            print_maze(maze, False)
        else:
            print_maze(maze)

if __name__== '__main__':
    visualize()