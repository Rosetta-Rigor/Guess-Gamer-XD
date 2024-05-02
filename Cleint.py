import socket

host = "localhost"
port = 7777

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((host, port))

    banner = client_socket.recv(1024).decode()
    print(banner)
    retry_choice=1
    while retry_choice==1:
        namae=input("Enter name:")
        client_socket.sendall(namae.encode())
        difficulty_choice = input("Enter your choice:\n[1]eay\n[2]medium\n[3]hard\n ")
        client_socket.sendall(difficulty_choice.encode())

        response = client_socket.recv(1024).decode()
        print(response)

        while True:
            guess = input()
            client_socket.sendall(guess.encode())

            response = client_socket.recv(1024).decode()
            print(response)

            if "Correct Answer!" in response:
                retry_choice = input("Do you want to try again? (1 for yes, 2 for no): ")
                client_socket.sendall(retry_choice.encode())
                if retry_choice == "2":
                    break
                else:
                    break


finally:
    client_socket.close()
