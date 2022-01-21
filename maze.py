from tile import Tile


def get_opposite_direction(direction):
    if direction == "up":
        return "down"
    elif direction == "down":
        return "up"
    elif direction == "left":
        return "right"
    elif direction == "right":
        return "left"


class Maze:
    def __init__(self, path):

        f = open(path, "r")
        csv = f.read()

        self.maze = []

        for line in csv.split("\n"):
            maze_line = []
            for tile in line.split(","):
                maze_line.append(Tile(int(tile)))
            self.maze.append(maze_line)

        self.player = [0, 0]
        self.maze[0][0].set_is_visited(True)
        self.maze[0][0].set_is_path(True)

    def display(self, mood="happy"):

        output = "██" * (len(self.maze[0]) + 2) + "\n"

        for y in range(len(self.maze)):
            line_display = ""

            for x in range(len(self.maze[y])):
                tile = self.maze[y][x]

                if self.player == [x, y]:
                    if mood == "sad":
                        line_display += ":("
                    elif mood == "overjoyed":
                        line_display += ":D"
                    else:
                        line_display += ":)"
                elif tile.is_path:
                    line_display += "░░"
                elif tile.is_visited:
                    line_display += "▓▓"
                elif tile.is_empty():
                    line_display += "  "
                elif tile.is_wall():
                    line_display += "██"
                elif tile.is_goal():
                    line_display += "!!"

            output += "██" + line_display + "██\n"

        output += "██" * (len(self.maze[0]) + 2)
        return output

    def look(self, direction):
        new_x, new_y = self.__get_new_coordinates(direction)

        if new_x is None or new_y is None:
            return None

        return self.maze[new_y][new_x]

    def move(self, direction):
        new_x, new_y = self.__get_new_coordinates(direction)

        if new_x is None or new_y is None:
            return False

        destination = self.maze[new_y][new_x]
        if not destination.is_wall():
            self.player = [new_x, new_y]
            destination.set_is_visited(True)
            destination.set_is_path(True)
            return True

        return False

    def backtrack(self, direction):
        opposite_direction = get_opposite_direction(direction)

        new_x, new_y = self.__get_new_coordinates(opposite_direction)

        origin = self.maze[self.player[1]][self.player[0]]
        destination = self.maze[new_y][new_x]
        if not destination.is_wall():
            self.player = [new_x, new_y]
            origin.set_is_path(False)
            return True

        return False

    def __get_new_coordinates(self, direction):
        new_x = self.player[0]
        new_y = self.player[1]

        if direction == "up":
            new_y -= 1
        elif direction == "down":
            new_y += 1
        elif direction == "left":
            new_x -= 1
        elif direction == "right":
            new_x += 1

        if new_x < 0 or new_x >= len(self.maze[0]) or new_y < 0 or new_y >= len(self.maze):
            return None, None

        return new_x, new_y

    def has_won(self):
        return self.maze[self.player[1]][self.player[0]].is_goal()
