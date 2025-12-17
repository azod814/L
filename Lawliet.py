#!/usr/bin/env python3
import os
import subprocess
import time
import sys

# ========== COLORS ==========
RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
CYAN    = "\033[96m"
BLUE    = "\033[94m"
MAGENTA = "\033[95m"
RESET   = "\033[0m"
BOLD    = "\033[1m"

ADB_PORT = "5555"

# ========== UTILS ==========
def clear():
    os.system("clear")

def run(cmd):
    return subprocess.getoutput(cmd)

# ========== BANNER ==========
def banner():
    print(CYAN + BOLD + r"""
      ___       ___           ___           ___                   ___           ___     
     /\__\     /\  \         /\__\         /\__\      ___        /\  \         /\  \    
    /:/  /    /::\  \       /:/ _/_       /:/  /     /\  \      /::\  \        \:\  \   
   /:/  /    /:/\:\  \     /:/ /\__\     /:/  /      \:\  \    /:/\:\  \        \:\  \  
  /:/  /    /::\~\:\  \   /:/ /:/ _/_   /:/  /       /::\__\  /::\~\:\  \       /::\  \ 
 /:/__/    /:/\:\ \:\__\ /:/_/:/ /\__\ /:/__/     __/:/\/__/ /:/\:\ \:\__\     /:/\:\__\
 \:\  \    \/__\:\/:/  / \:\/:/ /:/  / \:\  \    /\/:/  /    \:\~\:\ \/__/    /:/  \/__/
  \:\  \        \::/  /   \::/_/:/  /   \:\  \   \::/__/      \:\ \:\__\     /:/  /     
   \:\  \       /:/  /     \:\/:/  /     \:\  \   \:\__\       \:\ \/__/     \/__/      
    \:\__\     /:/  /       \::/  /       \:\__\   \/__/        \:\__\                  
     \/__/     \/__/         \/__/         \/__/                 \/__/                  
""" + RESET)

    print(BOLD + YELLOW + "        Android Wireless Control Tool – Kali Linux\n" + RESET)
    print(GREEN + "  • USB once → Wi-Fi always")
    print(GREEN + "  • Multi-device support")
    print(GREEN + "  • Screen • Control • Screenshot\n" + RESET)

# ========== DEVICE ==========
def list_devices():
    output = run("adb devices")
    lines = output.splitlines()[1:]
    devices = []

    for line in lines:
        if "device" in line and not "offline" in line:
            devices.append(line.split()[0])
    return devices

def select_device(devices):
    print(BOLD + CYAN + "\nConnected Devices:\n" + RESET)
    for i, d in enumerate(devices):
        print(f"{GREEN}[{i+1}]{RESET} {d}")

    choice = input(YELLOW + "\nSelect device number: " + RESET)
    try:
        return devices[int(choice) - 1]
    except:
        return None

# ========== WIFI MODE ==========
def enable_wifi_adb(device):
    print(CYAN + "\n[*] Switching to Wi-Fi mode..." + RESET)
    run(f"adb -s {device} tcpip {ADB_PORT}")
    time.sleep(2)

    ip = run(f"adb -s {device} shell ip route").split()[8]
    print(GREEN + f"[+] Connecting to {ip}:{ADB_PORT}" + RESET)
    run(f"adb connect {ip}:{ADB_PORT}")

# ========== SCREEN ==========
def start_screen(device):
    print(GREEN + "[+] Launching screen control..." + RESET)
    os.system(f"scrcpy -s {device} &")

# ========== MENU ==========
def device_menu(device):
    while True:
        print(BOLD + MAGENTA + f"\nDevice: {device}\n" + RESET)
        print(f"{CYAN}[1]{RESET} Enable Wi-Fi Mode (remove cable)")
        print(f"{CYAN}[2]{RESET} Screen Control")
        print(f"{CYAN}[3]{RESET} Take Screenshot")
        print(f"{CYAN}[4]{RESET} Disconnect Device")
        print(f"{CYAN}[5]{RESET} Back to Device List")
        print(f"{RED}[0]{RESET} Exit")

        ch = input(YELLOW + "\nChoose option: " + RESET)

        if ch == "1":
            enable_wifi_adb(device)

        elif ch == "2":
            start_screen(device)

        elif ch == "3":
            os.system(f"adb -s {device} exec-out screencap -p > screenshot.png")
            print(GREEN + "[✓] Screenshot saved as screenshot.png" + RESET)

        elif ch == "4":
            run("adb disconnect")
            print(YELLOW + "[!] Disconnected" + RESET)

        elif ch == "5":
            return

        elif ch == "0":
            sys.exit()

        else:
            print(RED + "Invalid option!" + RESET)

# ========== MAIN ==========
def main():
    while True:
        clear()
        banner()

        devices = list_devices()
        if not devices:
            print(RED + "No devices detected. Connect phone + enable USB debugging." + RESET)
            time.sleep(2)
            continue

        device = select_device(devices)
        if device:
            device_menu(device)

if __name__ == "__main__":
    main()
