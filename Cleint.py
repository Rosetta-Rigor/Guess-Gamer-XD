import socket

host = "127.0.0.1"  
port = 7777

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((host, port))

banner = client_socket.recv(1024).decode()
print(banner)

difficulty = input("Enter the difficulty level (1, 2, or 3): ")
client_socket.sendall(difficulty.encode())

guess_prompt = client_socket.recv(1024).decode()
print(guess_prompt, end=" ")

while True:
    guess = input()
    client_socket.sendall(guess.encode())
    response = client_socket.recv(1024).decode()
    print(response, end=" ")
    if response == "Correct Answer!":
        break

client_socket.close()

