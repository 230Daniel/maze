import os
from time import sleep


def clear_and_print_maze(maze, mood="happy"):
    display = "\n" + maze.display(mood) + "\n"
    os.system('cls')
    print(display)


def traverse_maze(maze):
    if maze.get_player_tile().get_direction_number() is None:
        clear_and_print_maze(maze, "sad")
        return False

    while not maze.get_has_won():
        clear_and_print_maze(maze)
        sleep(0.05)

        adjacent_tiles = list(
            filter(lambda tile: tile.get_direction_number() is not None, maze.get_player_adjacent_tiles()))
        best_tile = min(adjacent_tiles, key=lambda tile: tile.get_direction_number())

        old_x, old_y = maze.get_player_coordinates()
        new_x, new_y = best_tile.get_coordinates()

        if new_y < old_y:
            maze.move("up")
        elif new_y > old_y:
            maze.move("down")
        elif new_x < old_x:
            maze.move("left")
        elif new_x > old_x:
            maze.move("right")

    clear_and_print_maze(maze, "overjoyed")
    return True
