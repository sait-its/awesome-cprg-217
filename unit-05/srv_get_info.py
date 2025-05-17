import win32net

# Get information about the local computer (server)
server_name = None  # None means local computer
level = 101  # Level of detail (101 is common for general info)

server_info = win32net.NetServerGetInfo(server_name, level)

# Print server name and platform ID
print("Server Name:", server_info["name"])
print("Platform ID:", server_info["platform_id"])
print("Version:", server_info["version_major"], ".", server_info["version_minor"])
print("Server Type:", server_info["type"])
