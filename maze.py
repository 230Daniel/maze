class Maze:
    def __init__(self, path):

        f = open(path, "r")
        csv = f.read()

        self.maze = []

        for line in csv.split("\n"):
            maze_line = []
            for tile in line.split(","):
                maze_line.append(int(tile))
            self.maze.append(maze_line)

        self.player = [0, 0]
        self.player_facing = "r"

    def display(self):

        output = "██" * (len(self.maze[0]) + 2) + "\n"

        for y in range(len(self.maze)):
            line_display = ""

            for x in range(len(self.maze[y])):
                tile = self.maze[y][x]

                if self.player == [x, y]:
                    line_display += ":)"
                elif tile == 0:
                    line_display += "  "
                elif tile == 1:
                    line_display += "██"
                elif tile == 2:
                    line_display += "░░"

            output += "██" + line_display + "██\n"

        output += "██" * (len(self.maze[0]) + 2)
        return output

    def up(self):
        new_x = self.player[0]
        new_y = self.player[1] - 1
        return self.__move(new_x, new_y)

    def down(self):
        new_x = self.player[0]
        new_y = self.player[1] + 1
        return self.__move(new_x, new_y)

    def left(self):
        new_x = self.player[0] - 1
        new_y = self.player[1]
        return self.__move(new_x, new_y)

    def right(self):
        new_x = self.player[0] + 1
        new_y = self.player[1]
        return self.__move(new_x, new_y)

    def __move(self, new_x, new_y):
        if self.maze[new_y][new_x] == 1:
            return False

        self.player = [new_x, new_y]

        if self.maze[new_y][new_x] == 2:
            print("win!!")

        return True

    def forwards(self):
        if self.player_facing == "u":
            return self.up()
        elif self.player_facing == "d":
            return self.down()
        elif self.player_facing == "l":
            return self.left()
        elif self.player_facing == "r":
            return self.right()

    def turn_left(self):
        if self.player_facing == "u":
            self.player_facing = "l"
        elif self.player_facing == "l":
            self.player_facing = "d"
        elif self.player_facing == "d":
            self.player_facing = "r"
        elif self.player_facing == "r":
            self.player_facing = "u"

    def turn_right(self):
        if self.player_facing == "u":
            self.player_facing = "r"
        elif self.player_facing == "r":
            self.player_facing = "d"
        elif self.player_facing == "d":
            self.player_facing = "l"
        elif self.player_facing == "l":
            self.player_facing = "u"

    def get_tile_left(self):
        if self.player_facing == "u":
            new_x = self.player[0] - 1
            new_y = self.player[1]
        elif self.player_facing == "r":
            new_x = self.player[0]
            new_y = self.player[1] - 1
        elif self.player_facing == "d":
            new_x = self.player[0] + 1
            new_y = self.player[1]
        elif self.player_facing == "l":
            new_x = self.player[0]
            new_y = self.player[1] + 1
        else:
            new_x = self.player[0]
            new_y = self.player[1]

        if new_x < 0 or new_y < 0 or new_x >= len(self.maze[0]) or new_y >= len(self.maze):
            return 1

        return self.maze[new_y][new_x]

    def get_tile_right(self):
        if self.player_facing == "u":
            new_x = self.player[0] + 1
            new_y = self.player[1]
        elif self.player_facing == "r":
            new_x = self.player[0]
            new_y = self.player[1] + 1
        elif self.player_facing == "d":
            new_x = self.player[0] - 1
            new_y = self.player[1]
        elif self.player_facing == "l":
            new_x = self.player[0]
            new_y = self.player[1] - 1
        else:
            new_x = self.player[0]
            new_y = self.player[1]

        if new_x < 0 or new_y < 0 or new_x >= len(self.maze[0]) or new_y >= len(self.maze):
            return 1

        return self.maze[new_y][new_x]

    def has_won(self):
        return self.maze[self.player[1]][self.player[0]] == 2
