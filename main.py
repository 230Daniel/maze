from time import sleep

from maze import Maze


def main():
    maze = Maze("maze.csv")

    while True:
        print(maze.display())
        sleep(0.2)

        if maze.has_won():
            print("great success")
            break
        elif maze.get_tile_left() != 1:
            print("turn left")
            maze.turn_left()
            maze.forwards()
        elif maze.forwards():
            print("forwards")
            pass
        else:
            print("turn right")
            maze.turn_right()
            maze.forwards()


if __name__ == '__main__':
    main()
