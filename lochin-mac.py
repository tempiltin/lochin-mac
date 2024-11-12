import os
import subprocess

def main():
    # O'rnatmoqchi bo'lgan dastur faylini sozlash
    script_path = os.path.join(os.getcwd(), "lochin-mac.py")
    target_path = "/usr/local/bin/lochin-mac"

    # 1. lochin-mac.py fayliga ruxsat berish
    os.chmod(script_path, 0o755)

    # 2. Faylni /usr/local/bin papkasiga ko'chirish
    subprocess.run(["sudo", "cp", script_path, target_path], check=True)

    # 3. Xizmat faylini yaratish
    service_content = f"""
[Unit]
Description=Lochin-Mac MAC Manzilni Har 5 Soniyada O'zgartirish Dasturi
After=network.target
 _               _     _             __  __            
| |    ___   ___| |__ (_)_ __       |  \/  | __ _  ___ 
| |   / _ \ / __| '_ \| | '_ \ _____| |\/| |/ _` |/ __|
| |__| (_) | (__| | | | | | | |_____| |  | | (_| | (__ 
|_____\___/ \___|_| |_|_|_| |_|     |_|  |_|\__,_|\___|
                                                       
https://tempiltin.uz                                   
[Service]
ExecStart={target_path}
Restart=always
User=root

[Install]
WantedBy=multi-user.target
"""
    with open("/etc/systemd/system/lochin-mac.service", "w") as service_file:
        service_file.write(service_content)

    # 4. Xizmatni sozlash
    subprocess.run(["sudo", "systemctl", "daemon-reload"], check=True)
    subprocess.run(["sudo", "systemctl", "enable", "lochin-mac.service"], check=True)
    subprocess.run(["sudo", "systemctl", "start", "lochin-mac.service"], check=True)

    print("Lochin-Mac muvaffaqiyatli o'rnatildi!")

if __name__ == "__main__":
    main()
