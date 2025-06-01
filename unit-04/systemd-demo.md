# Simple systemd Service Demo

This demo shows how to create a systemd service that runs a bash script in the background, writing the current timestamp to `/tmp/systemd-demo.txt` every 5 seconds.

---

## 1. Bash Script

Save the following script as `/usr/local/bin/systemd-demo.sh` and make it executable:

```bash
#!/bin/bash

while true; do
  date +"%Y-%m-%d %H:%M:%S" >> /tmp/systemd-demo.txt
  sleep 5
done
```

Make it executable:

```sh
sudo chmod +x /usr/local/bin/systemd-demo.sh
```

---

## 2. systemd Service File

Create a file at `/etc/systemd/system/systemd-demo.service` with the following content:

```ini
[Unit]
Description=Simple systemd demo service that logs timestamp every 5 seconds

[Service]
ExecStart=/usr/local/bin/systemd-demo.sh
Restart=always
User=nobody
StandardOutput=null
StandardError=journal

[Install]
WantedBy=multi-user.target
```

---

## 3. Reload systemd and Start the Service

```sh
sudo systemctl daemon-reload
sudo systemctl start systemd-demo.service
```

---

## 4. Enable Service at Boot

```sh
sudo systemctl enable systemd-demo.service
```

---

## 5. Check Service Status

```sh
systemctl status systemd-demo.service
```

---

## 6. Stop and Disable the Service

To stop the service:

```sh
sudo systemctl stop systemd-demo.service
```

To disable it from starting at boot:

```sh
sudo systemctl disable systemd-demo.service
```

---

## 7. Remove the Service

```sh
sudo rm /etc/systemd/system/systemd-demo.service
sudo systemctl daemon-reload
sudo systemctl reset-failed
```

Optionally, remove the script:

```sh
sudo rm /usr/local/bin/systemd-demo.sh
```

---

**Note:**  
- Check the file `/tmp/systemd-demo.txt` to see the timestamps being logged.
- You can view logs with `journalctl -u systemd-demo.service`.
