import os
import sys
import time
import random
import shutil
import subprocess
from datetime import datetime

G = "\033[92m"
C = "\033[96m"
R = "\033[91m"
Y = "\033[93m"
P = "\033[95m"
W = "\033[97m"
D = "\033[2m"
X = "\033[0m"

def clear():
    os.system("clear")

def speak(msg, style="deep"):
    pitch, rate = (0.8, 0.85) if style == "deep" else (1.1, 1.0)
    try:
        subprocess.Popen(
            ["termux-tts-speak", "-p", str(pitch), "-r", str(rate), msg],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except:
        pass

def line():
    print(G + "═" * 52 + X)

def banner():
    clear()
    print(G + r"""
██╗  ██╗███████╗███╗   ███╗███████╗
██║ ██╔╝██╔════╝████╗ ████║██╔════╝
█████╔╝ █████╗  ██╔████╔██║█████╗
██╔═██╗ ██╔══╝  ██║╚██╔╝██║██╔══╝
██║  ██╗███████╗██║ ╚═╝ ██║███████╗
╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝
""" + X)
    print(C + "             K E M E   X   //   V 3.0" + X)
    line()
    print(Y + "       VISUAL CYBER SIMULATION SYSTEM" + X)
    line()

def loading(text):
    print(C + "\n" + text + X)
    for i in range(31):
        bar = "█" * i + "░" * (30-i)
        print("\r" + G + "[" + bar + "] " + str(i*100//30) + "%", end="", flush=True)
        time.sleep(0.035)
    print(X + "\n")

def matrix():
    clear()
    print(G + "MATRIX RAIN // اضغط CTRL+C للخروج\n" + X)
    chars = "01KEMEX#$%&<>"
    width = shutil.get_terminal_size((80, 24)).columns
    try:
        while True:
            print("".join(random.choice(chars) for _ in range(width)))
            time.sleep(0.045)
    except KeyboardInterrupt:
        return

def fake_scan():
    clear()
    print(G + ">>> VIRTUAL CYBER SCAN <<<" + X)
    speak("Virtual scan started")
    tasks = [
        "Initializing visual interface",
        "Loading virtual modules",
        "Checking demo systems",
        "Generating simulation data",
        "Finishing visual scan"
    ]
    for task in tasks:
        print(C + "\n[+] " + task + X)
        time.sleep(0.8)
        print(G + "[ OK ]" + X)
    print(Y + "\n[!] DEMO ONLY - NO REAL ACCESS" + X)
    speak("Simulation completed")
    input("\nاضغط Enter للرجوع...")

def dashboard():
    clear()
    print(G + "========== SYSTEM DASHBOARD ==========" + X)
    print(C + "Time       : " + X + datetime.now().strftime("%H:%M:%S"))
    print(C + "Date       : " + X + datetime.now().strftime("%Y-%m-%d"))
    print(C + "Platform   : " + X + sys.platform)
    print(C + "Python     : " + X + sys.version.split()[0])
    print(C + "Terminal   : " + X + str(shutil.get_terminal_size()))
    print(G + "\nSTATUS: ALL VISUAL MODULES READY" + X)
    input("\nEnter للرجوع...")

def voice_center():
    clear()
    print(P + "========== VOICE CENTER ==========" + X)
    print("1 - Deep AI style")
    print("2 - Cinematic style")
    choice = input("\nاختار: ")
    if choice == "1":
        speak("Welcome commander. Keme X system is ready.", "deep")
    elif choice == "2":
        speak("System online. Welcome to the cyber command center.", "movie")
    else:
        print(R + "اختيار غير صحيح" + X)
    input("\nEnter للرجوع...")

def animation():
    clear()
    print(G + "BOOT SEQUENCE" + X)
    for msg in [
        "Loading cyber interface...",
        "Preparing visual modules...",
        "Starting neon engine...",
        "Activating voice system...",
        "KEME X IS ONLINE!"
    ]:
        print(G + "[+] " + msg + X)
        time.sleep(0.7)
    speak("Keme X is online")
    input("\nEnter للرجوع...")

def menu():
    while True:
        banner()
        print(G + "[1]" + W + " Matrix Rain")
        print(G + "[2]" + W + " Virtual Cyber Scan")
        print(G + "[3]" + W + " System Dashboard")
        print(G + "[4]" + W + " AI Voice Center")
        print(G + "[5]" + W + " Boot Animation")
        print(G + "[6]" + W + " Exit")
        line()
        choice = input(C + "KEME-X@ROOT >> " + X)

        if choice == "1":
            matrix()
        elif choice == "2":
            fake_scan()
        elif choice == "3":
            dashboard()
        elif choice == "4":
            voice_center()
        elif choice == "5":
            animation()
        elif choice == "6":
            speak("Goodbye commander")
            clear()
            print(G + "KEME X SYSTEM OFFLINE" + X)
            break
        else:
            print(R + "Invalid command!" + X)
            time.sleep(1)

if __name__ == "__main__":
    banner()
    speak("Keme X system initializing")
    loading("INITIALIZING KEME X")
    menu()
