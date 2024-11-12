#!/usr/bin/env python3

import random
import subprocess
import time

def generate_mac_address():
    mac = [random.choice("0123456789ABCDEF") + random.choice("0123456789ABCDEF") for _ in range(6)]
    return ":".join(mac)

def change_mac(interface, new_mac):
    subprocess.run(["sudo", "ifconfig", interface, "down"], check=True)
    subprocess.run(["sudo", "ifconfig", interface, "hw", "ether", new_mac], check=True)
    subprocess.run(["sudo", "ifconfig", interface, "up"], check=True)

def main():
    interface = "eth0"  # Interfeys nomini o'zgartirish kerak bo'lishi mumkin
    print("Lochin-Mac dasturi ishga tushirildi......!")

    while True:
        new_mac = generate_mac_address()
        try:
            change_mac(interface, new_mac)
            print(f"O'zgartirilgan MAC manzil: {new_mac}")
        except Exception as e:
            print(f"Xato: MAC manzilni o'zgartirishda muammo: {e}")
        
        time.sleep(5)

if __name__ == "__main__":
    main()
