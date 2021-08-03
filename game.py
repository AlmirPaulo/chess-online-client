import simple_websocket




#Game loop
def main():
    socket = simple_websocket.Client('ws://localhost:5000/game')

    try:
        while True:
            move = input('> ')
            socket.send(move) 
            resp = socket.receive()
            print(f'< {resp}')

    except(KeyboardInterrupt, EOFError, simple_websocket.ConnectionClosed):
        socket.close()

main()
