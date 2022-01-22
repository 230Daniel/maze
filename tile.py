class Tile:
    def __init__(self, x, y, tile_type):
        self.__x = x
        self.__y = y
        self.__tile_type = tile_type
        self.__direction_number = None
        self.__is_path = False

    def get_coordinates(self):
        return self.__x, self.__y

    def get_is_empty(self):
        return self.__tile_type == 0

    def get_is_wall(self):
        return self.__tile_type == 1

    def get_is_goal(self):
        return self.__tile_type == 2

    def get_is_walkable(self):
        return self.get_is_empty() or self.get_is_goal()

    def get_direction_number(self):
        return self.__direction_number

    def set_direction_number(self, value):
        self.__direction_number = value

    def get_is_path(self):
        return self.__is_path

    def set_is_path(self, value):
        self.__is_path = value
