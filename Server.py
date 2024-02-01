import selectors
import sys
import socket
import types
from SnakeGame2 import SnakeGame2


    
game2 = SnakeGame2()

print("-- Welcome to our game, which is a snake and ladders game --\n")
print("THE RULES OF THE GAME ARE:")
print("Every player will take turns to roll the dice")
print("The first player that reaches the highest space on the board, 100, wins")
print("If you land on any snake head, you will go down to its tail")
print("If you land at the beginning of a ladder, you will go up to the ladder's top")
print("If you roll a six, then you get an extra turn\n")

print("Snake symbol: (@)\nLadder symbol: (^)")
print(
        "----------------------------------------------\n"
        + "100 99  98   @  96  @   94  93  92  91\n"
        + "81  82  83  84  85  86  87  @   89  90 \n"
        + "41  42  43  44  45  46  47  @   49  ^  \n"
        + "^   79  78  77  76  75  74  73  72  ^  \n"
        + "61  @   63  64  65  66  67  68  69  70 \n"
        + "60  59  58  57  56  55  54  53  52  51 \n"
        + "40  39  38  37  @   35  34  33  @   31 \n"
        + "^   22  23  24  25  26  27  ^   29  30 \n"
        + "20  19  18  17  16  15  14  13  12  11 \n"
        + "^   2   3   ^   5   6   7   ^   9   10\n"
        + "----------------------------------------------\n"
)
    
def main():
    exit_game = True
    while exit_game:
        print("Please choose how you want to play:")
        print("1.with your friend\t3. exit")
    
        answer = int(input())
    
        if answer == 1:
           game2.startgame()
        elif answer == 3:
            exit_game = False
            print("Goodbye")
        else:
            print(f"{answer} is an invalid number. Please try again.")
            
            
def accept_wrapper(sock: socket.socket):
    conn, addr = sock.accept()
    print(f"Accepted connection from {addr}")
    conn.setblocking(False)

    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE

    sel.register(conn, events, data=data)


def service_connection(key: selectors.SelectorKey, mask):
    sock: socket.socket = key.fileobj
    data = key.data

    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)

        if recv_data:
            data.outb += recv_data
        else:
            print(f"Closing connection to {data.addr}")
            sel.unregister(sock)
            sock.close()

    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print(f"Echoing {data.outb!r} to {data.addr}")
            
            sent = sock.send(data.outb)
            data.outb = data.outb[sent:]


sel = selectors.DefaultSelector()
host, port = sys.argv[1], int(sys.argv[2])

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()

print(f'Listening on {(host, port)}')
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)

try:
    while True:
        events = sel.select(timeout=None)

        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask)
except KeyboardInterrupt:
    print("Caught keyboard interrupt, exiting")
finally:
    sel.close()
