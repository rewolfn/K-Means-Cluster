

# This Object's only job is to hold a cartesian coordinate (x, y, z) which represents (R, G, B)


class Observation:

    def __init__(self, location): #Location should be a tuple
        self.__location = location 

    def location(self): # Using location instead of getLocation reads better in the AI
        return self.__location

