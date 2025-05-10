"""
File receiver service
This service continuously listens for incoming files and handles multiple clients sequentially
"""
import socket
import tqdm
import os
import datetime
import logging
import hashlib

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='file_receiver.log',
    filemode='a'
)

# Server configuration
SERVER_HOST = "0.0.0.0"  # Listen on all network interfaces
SERVER_PORT = 5001       # Port to listen on
BUFFER_SIZE = 4096       # Bytes to receive at once
SEPARATOR = "<SEPARATOR>"  # Delimiter for metadata
SAVE_DIRECTORY = "received_files"  # Directory to save received files

def ensure_save_directory():
    """Create save directory if it doesn't exist"""
    if not os.path.exists(SAVE_DIRECTORY):
        os.makedirs(SAVE_DIRECTORY)
        logging.info(f"Created directory: {SAVE_DIRECTORY}")

def receive_file(client_socket, client_address):
    """Handle file reception from a client"""
    try:
        # Receive the file info
        received = client_socket.recv(BUFFER_SIZE).decode()
        if not received:
            logging.warning(f"Client {client_address} connected but sent no data")
            return
            
        filename, filesize, expected_md5 = received.split(SEPARATOR)
        # Remove absolute path if there is
        filename = os.path.basename(filename)
        # Generate unique filename with timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{timestamp}_{filename}"
        # Full path to save the file
        file_path = os.path.join(SAVE_DIRECTORY, filename)
        # Convert to integer
        filesize = int(filesize)
        
        logging.info(f"Receiving file: {filename} ({filesize} bytes) from {client_address}")
        
        # Start receiving the file
        md5_hash = hashlib.md5()
        progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(file_path, "wb") as f:
            bytes_received = 0
            while bytes_received < filesize:
                # Read bytes from socket
                bytes_read = client_socket.recv(BUFFER_SIZE)
                if not bytes_read:    
                    # Connection closed prematurely
                    logging.warning(f"Connection with {client_address} closed prematurely")
                    break
                # Update MD5 hash
                md5_hash.update(bytes_read)
                # Write to file and update progress
                f.write(bytes_read)
                bytes_received += len(bytes_read)
                progress.update(len(bytes_read))
        
        # Verify file integrity
        calculated_md5 = md5_hash.hexdigest()
        if bytes_received == filesize and calculated_md5 == expected_md5:
            logging.info(f"File {filename} received successfully from {client_address} (MD5 verified)")
            client_socket.send("File received successfully - MD5 verified".encode())
        else:
            error_msg = "Incomplete transfer" if bytes_received != filesize else "MD5 mismatch"
            logging.warning(f"File transfer failed from {client_address}: {error_msg}")
            client_socket.send(f"File transfer failed: {error_msg}".encode())
            
    except Exception as e:
        logging.error(f"Error receiving file from {client_address}: {str(e)}")
    finally:
        # Close the client socket
        client_socket.close()
        logging.info(f"Connection with {client_address} closed")

def start_server():
    """Start the file receiver service"""
    # Create the server socket (TCP)
    server_socket = socket.socket()
    
    # Enable address reuse to avoid "Address already in use" after restart
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        # Bind the socket to our local address
        server_socket.bind((SERVER_HOST, SERVER_PORT))
        # Enable server to accept connections
        server_socket.listen(5)
        logging.info(f"Server started - listening on {SERVER_HOST}:{SERVER_PORT}")
        print(f"[*] File receiver service started - listening on {SERVER_HOST}:{SERVER_PORT}")
        print(f"[*] Files will be saved to: {os.path.abspath(SAVE_DIRECTORY)}")
        print(f"[*] Press Ctrl+C to stop the service")
        
        # Ensure save directory exists
        ensure_save_directory()
        
        # Main service loop
        while True:
            # Accept connection
            client_socket, client_address = server_socket.accept()
            print(f"[+] Connection from {client_address}")
            
            # Handle file reception in a separate function
            receive_file(client_socket, client_address)
            
    except KeyboardInterrupt:
        print("\n[!] Server shutdown requested")
        logging.info("Server shutdown requested")
    except Exception as e:
        logging.error(f"Server error: {str(e)}")
        print(f"[!] Server error: {str(e)}")
    finally:
        # Close the server socket
        server_socket.close()
        logging.info("Server stopped")
        print("[*] Server stopped")

if __name__ == "__main__":
    start_server()