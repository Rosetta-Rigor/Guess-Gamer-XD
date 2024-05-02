import socket
import random

host = "0.0.0.0"
port = 7777
banner = """
== Guessing Game v1.0 ==
choose difficulty:
[1]easy
[2]medium
[3]hard"""

def generate_random_int(low, high):
    return random.randint(low, high)

# initialize the socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)

print(f"server is listening on port {port}")

conn = None
while True:
    if conn is None:
        print("waiting for connection..")
        conn, addr = s.accept()
        print(f"new client: {addr[0]}")
        conn.sendall(banner.encode())
    else:
        client_input = conn.recv(1024).decode().strip()
        if client_input == "1":
            guessme = generate_random_int(1, 50)
            conn.sendall(b"Guess a number between 1 and 50:")
        elif client_input == "2":
            guessme = generate_random_int(1, 100)
            conn.sendall(b"Guess a number between 1 and 100:")
        elif client_input == "3":
            guessme = generate_random_int(1, 500)
            conn.sendall(b"Guess a number between 1 and 500:")
        else:
            conn.sendall(b"Invalid choice. Please choose 1, 2, or 3.")

        while True:
            guess = int(conn.recv(1024).decode().strip())
            if guess == guessme:
                conn.sendall(b"Correct Answer!")
                conn.close()
                conn = None
                break
            elif guess > guessme:
                conn.sendall(b"Guess Lower!\nEnter guess: ")
            elif guess < guessme:
                conn.sendall(b"Guess Higher!\nEnter guess: ")




