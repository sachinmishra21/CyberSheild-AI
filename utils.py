
from colorama import Fore, Style, init
import os

init(autoreset=True)

def banner():
    print(Fore.CYAN + "=" * 60)
    print(Fore.GREEN + " AI Powered Cybersecurity Awareness System ")
    print(Fore.CYAN + "=" * 60)


def success(msg):
    print(Fore.GREEN + "[+] " + msg)


def warning(msg):
    print(Fore.YELLOW + "[!] " + msg)


def danger(msg):
    print(Fore.RED + "[-] " + msg)


def create_folders():
    os.makedirs("reports", exist_ok=True)
    os.makedirs("samples", exist_ok=True)