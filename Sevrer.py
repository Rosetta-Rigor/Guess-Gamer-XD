import socket
import random
import os

host = "0.0.0.0"
port = 7777
banner = """
== Guessing Game v1.0 ==
"""

def generate_random_int(low, high):
    return random.randint(low, high)

scores_file = "scores.txt"

def save_scores(scores):
    with open(scores_file, "a") as file:
        for score in scores:
            for name, tries in score.items():
                file.write(f"{name}: {tries}\n")

def load_scores():
    scores = []
    if os.path.exists(scores_file):
        with open(scores_file, "r") as file:
            for line in file:
                name, tries = line.strip().split(": ")
                scores.append({name: int(tries)})
    return scores

scores = load_scores()

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
        namae = conn.recv(1024).decode().strip()
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

        tries = 0
        while True:
            guess = int(conn.recv(1024).decode().strip())
            if guess == guessme:
                tries += 1
                print(f'{namae}:{tries}')
                conn.sendall(b"Correct Answer!")
                scores.append({namae: tries})
                save_scores(scores)  # Save scores to file
                choice = int(conn.recv(1024).decode().strip())
                if choice == 2:
                    conn.sendall(b"Thanks for playing! Goodbye!")
                    conn.close()
                    conn = None
                    break
                elif choice == 1:
                    break
            elif guess > guessme:
                tries += 1
                conn.sendall(b"Guess Lower!\nEnter guess: ")
            elif guess < guessme:
                tries += 1
                conn.sendall(b"Guess Higher!\nEnter guess: ")
