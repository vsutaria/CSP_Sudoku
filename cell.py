class Cell():

    def __init__(self, i, j, domain):
        self._position = (i, j)
        self._neighbors = []
        self._domain = domain

    def __eq__(self, other):
        return self._position == other._position

    def get_neighbors(self):
        return self._neighbors

    def get_domain(self):
        return self._domain

    def add_neighbor(self, neighbor):
        if neighbor not in self._neighbors:
            self._neighbors.append(neighbor)
    