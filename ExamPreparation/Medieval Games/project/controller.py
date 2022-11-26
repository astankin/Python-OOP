from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    @staticmethod
    def find_winner(player1, player2):
        if player1.stamina > player2.stamina:
            return player1
        return player2

    def find_player(self, name):
        for player in self.players:
            if player.name == name:
                return player

    def find_supply(self, supply_type):
        counter = -1
        for supply in reversed(self.supplies):
            counter += 1
            if type(supply).__name__ == supply_type:
                self.supplies.pop(len(self.supplies) - counter - 1)
                return supply
        if supply_type == "Food":
            raise Exception("There are no food supplies left!")
        if supply_type == "Drink":
            raise Exception("There are no drink supplies left!")

    def check_if_player_in_players(self, player):
        for player_in_list in self.players:
            if player_in_list.name == player.name:
                return True
        return False

    @staticmethod
    def find_attacker_defender(player1, player2):
        if player1.stamina < player2.stamina:
            return player1, player2
        return player2, player1

    def add_player(self, *players_: Player):
        added_players = []
        for player in players_:
            if not self.check_if_player_in_players(player):
                self.players.append(player)
                added_players.append(player.name)
        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *supplys_):
        self.supplies.extend(supplys_)

    def sustain(self, player_name: str, sustenance_type: str):
        if sustenance_type not in ["Food", "Drink"]:
            return
        if not self.find_player(player_name):
            return
        player = self.find_player(player_name)
        if player.stamina == 100:
            return f"{player_name} have enough stamina."
        supply = self.find_supply(sustenance_type)
        if supply:
            if player.stamina + supply.energy > 100:
                player.stamina = 100
            else:
                player.stamina += supply.energy
            return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name, second_player_name):
        player1 = self.find_player(first_player_name)
        player2 = self.find_player(second_player_name)

        if player1.stamina == 0 and player2.stamina == 0:
            return f"Player {player1.name} does not have enough stamina.\n" \
                   f"Player {player2.name} does not have enough stamina."
        if player1.stamina == 0:
            return f"Player {player1.name} does not have enough stamina."
        if player2.stamina == 0:
            return f"Player {player2.name} does not have enough stamina."

        attacker = self.find_attacker_defender(player1, player2)[0]
        defender = self.find_attacker_defender(player1, player2)[1]

        if defender.stamina - attacker.stamina / 2 <= 0:
            defender.stamina = 0
            return f"Winner: {attacker.name}"
        defender.stamina -= attacker.stamina / 2
        if attacker.stamina - defender.stamina / 2 <= 0:
            attacker.stamina = 0
            return f"Winner: {defender.name}"
        attacker.stamina -= defender.stamina / 2
        winner = self.find_winner(player1, player2)
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - (player.age * 2) < 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2
        for player in self.players:
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        info = []
        for player in self.players:
            info.append(str(player))
        for supply in self.supplies:
            info.append(supply.details())
        result = "\n".join(info)
        return result







