"""
Client that sends the file (uploads)
"""
import socket
import tqdm
import os
import argparse
import hashlib

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

def calculate_md5(filename):
    """Calculate MD5 hash of file"""
    md5_hash = hashlib.md5()
    with open(filename, "rb") as f:
        # Read file in chunks to handle large files efficiently
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

def send_file(filename, host, port):
    # get the file size
    filesize = os.path.getsize(filename)
    # calculate md5 hash
    file_md5 = calculate_md5(filename)

    # create the client socket
    s = socket.socket()
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")

    # send the filename, filesize and md5
    s.send(f"{filename}{SEPARATOR}{filesize}{SEPARATOR}{file_md5}".encode())

    # start sending the file
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        while True:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transmission in
            # busy networks
            s.sendall(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))

    # wait for server confirmation
    response = s.recv(1024).decode()
    print(f"[+] Server response: {response}")

    # close the socket
    s.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple File Sender")
    parser.add_argument("file", help="File name to send")
    parser.add_argument("host", help="The host/IP address of the receiver")
    parser.add_argument("-p", "--port", help="Port to use, default is 5001", type=int, default=5001)
    args = parser.parse_args()
    filename = args.file
    host = args.host
    port = args.port
    send_file(filename, host, port)