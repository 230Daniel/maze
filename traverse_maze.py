from time import sleep
import os


def clear_and_print_maze(maze, mood="happy"):
    display = "\n" + maze.display(mood) + "\n"
    os.system('cls')
    print(display)


def traverse_maze(maze):
    clear_and_print_maze(maze)
    sleep(0.05)

    walkable_directions = []
    walkable_tiles = []

    for direction in ["up", "down", "left", "right"]:
        tile = maze.look(direction)
        if tile and tile.is_walkable() and not tile.is_visited:
            walkable_directions.append(direction)
            walkable_tiles.append(tile)

    for i in range(len(walkable_directions)):
        direction = walkable_directions[i]
        tile = walkable_tiles[i]

        if tile.is_visited:
            continue

        maze.move(direction)

        if maze.has_won():
            clear_and_print_maze(maze, "overjoyed")
            return True

        if traverse_maze(maze):
            return True
        else:
            maze.backtrack(direction)
            clear_and_print_maze(maze, "sad")
            sleep(0.03)

    return False
