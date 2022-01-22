from maze import Maze
from number_maze_tiles import number_maze_tiles
from traverse_maze import traverse_maze


def main():
    maze = Maze("maze.csv")
    number_maze_tiles(maze)
    result = traverse_maze(maze)

    if result:
        print("Solved the maze!")
    else:
        print("The maze is unsolvable.")

    input("Press enter to exit...")


if __name__ == '__main__':
    main()
