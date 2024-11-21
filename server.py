import threading
import sqlite3
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 9999))
server_socket.listen(5)
print("[S]: Server socket created")

def validate_user(username, password):
    """Check if username and password match database records"""
    try:
        conn = sqlite3.connect('mydb.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usernames WHERE user = ? AND pass = ?", 
                      (username.strip(), password.strip()))
        result = cursor.fetchone() is not None
        conn.close()
        print(f"[S]: Validation result: {result}") 
        return result
    except Exception as e:
        print(f"[S]: Database error: {e}")
        return False

def handle_client(client):
    """Handle a client connection"""
    try:
       
        client.send("Username: ".encode())
        username = client.recv(1024).decode().strip()
        print(f"[S]: Received username: {username}")

     
        client.send("Password: ".encode())
        password = client.recv(1024).decode().strip()
        print(f"[S]: Received password for user: {username}")

      
        if validate_user(username, password):
            client.send("Login Success!".encode())
            print(f"[S]: Login successful for user: {username}")
        else:
            client.send("Login Failure!".encode())
            print(f"[S]: Login failed for user: {username}")

    except Exception as e:
        print(f"[S]: Error: {e}")
    finally:
        client.close()
        print("[S]: Client connection closed")


print("[S]: Server is waiting for connections...")
while True:
    client, addr = server_socket.accept()
    print(f"[S]: Connected to {addr}")
        
    client_thread = threading.Thread(target=handle_client, args=(client,))
    client_thread.start()

    server_socket.close()
    exit()