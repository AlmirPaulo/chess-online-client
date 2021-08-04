#! /usr/bin/env python3 
import simple_websocket, random, argparse

#CLI
parser = argparse.ArgumentParser(description='Blind Chess Online')

parser.add_argument('set', type=str,help='Set a game')
# parser.add_argument('--ai', type=str,help='Set a game against AI')

args = parser.parse_args()

#Classes
class Player:
    def __init__(self, room):
        self.color = random.choice(['white','black'])
        self.room = room

    
#Functions
def set_game(room):
    p = Player(room)
    return p

def set_ai(room):
    pass

#Game loop
def main():
    socket = simple_websocket.Client('ws://localhost:5000/game')
    
    #Start Game
    player = Player(args.set)
    player_data = f'{player.color}/{player.room}'
    socket.send(player_data)
    print(player_data)
    
    #Game Mechanics
    try:
        while True:
            move = input('> ')
            socket.send(move) 
            resp = socket.receive()
            print(f'< {resp}')

    except(KeyboardInterrupt, EOFError, simple_websocket.ConnectionClosed):
        socket.close()

main()
