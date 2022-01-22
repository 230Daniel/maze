def number_maze_tiles(maze, previous_number=-1):
    processed_a_tile = False

    for tile in maze.get_all_tiles():
        if previous_number == -1 and not tile.get_is_goal() \
                or previous_number != -1 and tile.get_direction_number() != previous_number:
            continue

        processed_a_tile = True

        x, y = tile.get_coordinates()
        adjacent_tiles = maze.get_adjacent_tiles(x, y)

        for adjacent_tile in adjacent_tiles:
            if adjacent_tile.get_is_walkable() and adjacent_tile.get_direction_number() is None:
                adjacent_tile.set_direction_number(previous_number + 1)

    if processed_a_tile:
        number_maze_tiles(maze, previous_number + 1)
