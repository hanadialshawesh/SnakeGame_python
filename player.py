class Player:
    
    def __init__(self, name):
        self.player_name = name
        self.position = 0

    def get_player_name(self):
        return self.player_name

    def get_position(self):
        return self.position

    def set_player_name(self, name):
        self.player_name = name

    def set_position(self, num):
        self.position += num