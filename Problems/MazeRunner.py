#Introduction
"""
Welcome Adventurer. Your aim is to navigate the maze and reach the finish point without touching any walls. Doing so will kill you instantly!

Task

You will be given a 2D array of the maze and an array of directions. Your task is to follow the directions given. 
If you reach the end point before all your moves have gone, you should return Finish. If you hit any walls or go outside the maze border, 
you should return Dead. If you find yourself still in the maze after using all the moves, you should return Lost.

The Maze array will look like

maze = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,3],
        [1,0,1,0,1,0,1],
        [0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1],
        [1,0,0,0,0,0,1],
        [1,2,1,0,1,0,1]]

..with the following key

      0 = Safe place to walk
      1 = Wall
      2 = Start Point
      3 = Finish Point

  direction = ["N","N","N","N","N","E","E","E","E","E"] == "Finish"

Rules
1. The Maze array will always be square i.e. N x N but its size and content will alter from test to test.

2. The start and finish positions will change for the final tests.

3. The directions array will always be in upper case and will be in the format of N = North, E = East, W = West and S = South.

4. If you reach the end point before all your moves have gone, you should return Finish.

5. If you hit any walls or go outside the maze border, you should return Dead.

6. If you find yourself still in the maze after using all the moves, you should return Lost.
"""

# Output Examples
"""
maze_runner(maze,["N","N","N","N","N","E","E","E","E","E"]), "Finish")
maze_runner(maze,["N","N","N","N","N","E","E","S","S","E","E","N","N","E"]), "Finish")
maze_runner(maze,["N","N","N","N","N","E","E","E","E","E","W","W"]), "Finish")
"""

# Solution

def maze_runner(maze, directions):
    map = {}
    myPosition = [0,0]
    endPosition = [0,0]
    for i in range(len(maze)):
        for j in range(len(maze)):
            if maze[i][j] == 0:
                map[(i,j)] = 'Safe'
            if maze[i][j] == 1:
                map[(i,j)] = 'Wall'
            if maze[i][j] == 2:
                map[(i,j)] = 'Start'
                myPosition[0], myPosition[1] = i, j
            if maze[i][j] == 3:
                map[(i,j)] = 'End'
                endPosition[0], endPosition[1] = i, j
    for i in directions:
        if myPosition == endPosition:
            return "Finish"
        match i:
            case "N":
                newPosition = [myPosition[0] - 1, myPosition[1]]
                if (newPosition[0], newPosition[1]) not in map:
                    return "Dead"
                match map[(newPosition[0], newPosition[1])]:
                    case 'Safe':
                        myPosition = newPosition
                    case 'Wall':
                        return "Dead"
                    case 'End':
                        return "Finish"
            case "S":
                newPosition = [myPosition[0] + 1, myPosition[1]]
                if (newPosition[0], newPosition[1]) not in map:
                    return "Dead"
                match map[(newPosition[0], newPosition[1])]:
                    case 'Safe':
                        myPosition = newPosition
                    case 'Wall':
                        return "Dead"
                    case 'End':
                        return "Finish"
            case "W":
                newPosition = [myPosition[0], myPosition[1] - 1]
                if (newPosition[0], newPosition[1]) not in map:
                    return "Dead"
                match map[(newPosition[0], newPosition[1])]:
                    case 'Safe':
                        myPosition = newPosition
                    case 'Wall':
                        return "Dead"
                    case 'End':
                        return "Finish"
            case "E":
                newPosition = [myPosition[0], myPosition[1] + 1]
                if (newPosition[0], newPosition[1]) not in map:
                    return "Dead"
                match map[(newPosition[0], newPosition[1])]:
                    case 'Safe':
                        myPosition = newPosition
                    case 'Wall':
                        return "Dead"
                    case 'End':
                        return "Finish"
    return "Lost"

print(maze_runner([[1,1,1,1,1,1,1],
                   [1,0,0,0,0,0,3],
                   [1,0,1,0,1,0,1],
                   [0,0,1,0,0,0,1],
                   [1,0,1,0,1,0,1],
                   [1,0,0,0,0,0,1],
                   [1,2,1,0,1,0,1]], ["N","N","N","N","N","E","E","S","S","S","S","S","S"]))