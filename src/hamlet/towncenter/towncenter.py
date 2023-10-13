# define the towncenter class and it's related services, functions, variables, etcfrom ..hamlet import GeoEntity

class Towncenter(GeoEntity):
    def __init__(self, name, location, bulletin_board):
        super().__init__(name, location)
        self.bulletin_board = bulletin_board

    def get_bulletin_board(self):
        return self.bulletin_board
