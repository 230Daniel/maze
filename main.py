from maze import Maze
from traverse_maze import traverse_maze


def main():
    maze = Maze("maze.csv")
    traverse_maze(maze)

    input()


if __name__ == '__main__':
    main()
