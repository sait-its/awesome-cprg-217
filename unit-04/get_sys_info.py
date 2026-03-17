import subprocess

CMD_HOSTNAME = "hostname"
CMD_FREE_MEMORY = "free -h | grep Mem | awk '{print $4}'"
CMD_FREE_ROOT_DISK = "df -h / | tail -1 | awk '{print $4}'"
CMD_KERNEL_VERSION = "uname -r"
CMD_SSHD_STATUS = "systemctl status sshd.service | grep Active | awk '{print $2}'"


def get_cli_output(command):
    """Run a CLI command and return the output as a string."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Command '{' '.join(command)}' failed with error: {result.stderr}")
    return result.stdout.strip()


def get_system_info():
    hostname = {"Hostname": get_cli_output(CMD_HOSTNAME)}
    free_memory = {"Free memory": get_cli_output(CMD_FREE_MEMORY)}
    free_root_disk = {"Free root disk": get_cli_output(CMD_FREE_ROOT_DISK)}
    kernel_version = {"Kernel version": get_cli_output(CMD_KERNEL_VERSION)}
    sshd_status = {"sshd status": get_cli_output(CMD_SSHD_STATUS)}
    return hostname | free_memory | free_root_disk | kernel_version | sshd_status


if __name__ == "__main__":
    print(get_system_info())
