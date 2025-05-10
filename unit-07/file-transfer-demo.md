# Python File Transfer System

A simple but robust file transfer system implemented in Python, consisting of a sender and receiver that communicate over a network connection. This project is great for learning about networking, file handling, and data integrity in Python.

[Source code of receiver](https://github.com/sait-its/awesome-cprg-217/blob/main/unit-07/file_receiver_service.py)

[Source code of sender](https://github.com/sait-its/awesome-cprg-217/blob/main/unit-07/sender.py)

## Features

- File transfer over TCP/IP network
- Progress bar showing transfer status
- MD5 hash verification for file integrity
- Logging system for tracking transfers
- Support for multiple sequential clients
- Automatic file naming with timestamps

## Requirements

- Python 3.x
- `tqdm` library for progress bars: `pip install tqdm`

## How It Works

### Basic Concept

The system consists of two main components:
1. A receiver (server) that listens for incoming files
2. A sender (client) that sends files to the server

### File Transfer Protocol

1. **Initial Connection**
   - Sender connects to receiver using IP address and port
   - Receiver accepts the connection

2. **Metadata Transfer**
   - Sender sends metadata string in format: `filename<SEPARATOR>filesize<SEPARATOR>md5_hash`
   - Receiver parses this information to prepare for file reception

3. **File Transfer**
   - Sender reads file in chunks and sends data
   - Receiver writes received chunks to a new file
   - Both sides show progress bars

4. **Verification**
   - Receiver calculates MD5 hash of received file
   - Compares it with the hash sent by sender
   - Sends success/failure confirmation back to sender

## Usage

### Starting the Receiver

```bash
python file_receiver_service.py
```

The receiver will:
- Start listening on all network interfaces (0.0.0.0)
- Use port 5001 by default
- Create a 'received_files' directory if it doesn't exist
- Log all activities to 'file_receiver.log'

### Send a file

```bash
python sender.py filename <receiver_ip> [-p PORT]
```

Example:

```bash
python sender.py myfile.txt 192.168.1.100 -p 5001
```

## Learning Points

This project demonstrates several important Python concepts:

1. **Network Programming**
   - Socket creation and management
   - Client-server architecture
   - TCP/IP communication

2. **File Handling**
   - Reading/writing binary files
   - File path manipulation
   - Chunked file processing

3. **Data Integrity**
   - MD5 hash calculation
   - File verification
   - Error handling

4. **Python Features**
   - Context managers (`with` statements)
   - Command line arguments
   - Progress bars with `tqdm`
   - Exception handling
   - Logging

5. **Best Practices**
   - Separation of concerns
   - Error handling and logging
   - User feedback (progress bars)
   - Clean code organization

## Tips for Learning

1. Start by understanding the basic flow:
   - How the connection is established
   - How metadata is transferred
   - How the actual file transfer works

2. Experiment with different file types and sizes

3. Try to understand the security implications:
   - What happens if the connection breaks?
   - How does the MD5 verification help?
   - What could go wrong during transfer?

4. Look at the logging output to understand the process

## Common Issues and Solutions

1. **"Address already in use" error**
   - Wait a few minutes or use a different port
   - The server has SO_REUSEADDR enabled to minimize this issue

2. **Connection refused**
   - Ensure the server is running
   - Check if the IP address and port are correct
   - Verify firewall settings

3. **Incomplete transfers**
   - The system will detect and report these
   - Check network stability
   - Look at the log file for details