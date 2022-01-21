class Tile:
    def __init__(self, value):
        self.value = value
        self.is_visited = False
        self.is_path = False

    def is_empty(self):
        return self.value == 0

    def is_wall(self):
        return self.value == 1

    def is_goal(self):
        return self.value == 2

    def is_walkable(self):
        return self.is_empty() or self.is_goal()

    def set_is_visited(self, value):
        self.is_visited = value

    def set_is_path(self, value):
        self.is_path = value
