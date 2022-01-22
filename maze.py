from tile import Tile


class Maze:
    def __init__(self, path):
        self.__player = (0, 0)
        self.__maze = []

        f = open(path, "r")
        csv = f.read()
        lines = csv.split("\n")

        for y in range(len(lines)):
            maze_line = []
            line = lines[y]
            tiles = line.split(",")

            for x in range(len(tiles)):
                tile = tiles[x]
                maze_line.append(Tile(x, y, int(tile)))

            self.__maze.append(maze_line)

        self.__maze[0][0].set_is_path(True)

    def get_player_coordinates(self):
        return self.__player

    def get_player_tile(self):
        x, y = self.__player
        return self.get_tile(x, y)

    def get_tile(self, x, y):
        return self.__maze[y][x]

    def get_all_tiles(self):
        return [tile for line in self.__maze for tile in line]

    def get_player_adjacent_tiles(self):
        x, y = self.__player
        return self.get_adjacent_tiles(x, y)

    def get_adjacent_tiles(self, x, y):
        coordinates = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]

        tiles = []
        for (x, y) in coordinates:

            if 0 <= x < len(self.__maze[0]) and 0 <= y < len(self.__maze):
                tile = self.__maze[y][x]
                tiles.append(tile)

        return tiles

    def get_has_won(self):
        x, y = self.__player
        return self.__maze[y][x].get_is_goal()

    def move(self, direction):
        new_x, new_y = self.__get_new_coordinates(direction)

        if new_x is None or new_y is None:
            return False

        destination = self.__maze[new_y][new_x]
        if not destination.get_is_wall():
            self.__player = (new_x, new_y)
            destination.set_is_path(True)
            return True

        return False

    def display(self, mood="happy"):

        output = "██" * (len(self.__maze[0]) + 2) + "\n"

        for y in range(len(self.__maze)):
            line_display = ""

            for x in range(len(self.__maze[y])):
                tile = self.__maze[y][x]

                if self.__player == (x, y):
                    if mood == "sad":
                        line_display += ":("
                    elif mood == "overjoyed":
                        line_display += ":D"
                    else:
                        line_display += ":)"
                elif tile.get_is_path():
                    line_display += "░░"
                elif tile.get_is_empty():
                    line_display += "  "
                elif tile.get_is_wall():
                    line_display += "██"
                elif tile.get_is_goal():
                    line_display += "##"

            output += "██" + line_display + "██\n"

        output += "██" * (len(self.__maze[0]) + 2)
        return output

    def __get_new_coordinates(self, direction):
        new_x, new_y = self.__player

        if direction == "up":
            new_y -= 1
        elif direction == "down":
            new_y += 1
        elif direction == "left":
            new_x -= 1
        elif direction == "right":
            new_x += 1

        if new_x < 0 or new_x >= len(self.__maze[0]) or new_y < 0 or new_y >= len(self.__maze):
            return None, None

        return new_x, new_y
