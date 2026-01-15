import os
import platform
import subprocess
import requests
import socket

# ============================
#   GRADIENTE VERDE (11 STEP)
# ============================

GRADIENT = [
    "\033[38;2;179;240;255m",
    "\033[38;2;153;235;255m",
    "\033[38;2;128;229;255m",
    "\033[38;2;102;224;255m",
    "\033[38;2;77;219;255m",
    "\033[38;2;51;214;255m",
    "\033[38;2;26;209;255m",
    "\033[38;2;0;204;255m",
    "\033[38;2;0;180;230m",
    "\033[38;2;0;163;204m",
    "\033[38;2;0;153;179m"
]

RESET = "\033[0m"
LIGHT_GREEN = "\033[38;2;0;180;230m"
WHITE  = "\033[38;2;179;240;255m"
GREEN  = "\033[38;2;0;255;180m"

# ============================
#   LOGO (11 RIGHE)
# ============================

LOGO = [
" _______     _____  ________  _______    ______    ______   __    __ ",
"|       \\   |     \\|        \\|       \\  /      \\  /      \\ |  \\  /  \\",
"| $$$$$$$\\   \\$$$$$ \\$$$$$$$$| $$$$$$$\\|  $$$$$$\\|  $$$$$$\\| $$ /  $$",
"| $$__/ $$     | $$   | $$   | $$__| $$| $$__| $$| $$   \\$$| $$/  $$ ",
"| $$    $$__   | $$   | $$   | $$    $$| $$    $$| $$      | $$  $$  ",
"| $$$$$$$|  \\  | $$   | $$   | $$$$$$$\\| $$$$$$$$| $$   __ | $$$$$\\  ",
"| $$     | $$__| $$   | $$   | $$  | $$| $$  | $$| $$__/  \\| $$ \\$$\\ ",
"| $$      \\$$    $$   | $$   | $$  | $$| $$  | $$ \\$$    $$| $$  \\$$\\",
" \\$$       \\$$$$$$     \\$$    \\$$   \\$$ \\$$   \\$$  \\$$$$$$  \\$$   \\$$",
"",
""
]

def print_logo():
    for i, line in enumerate(LOGO):
        print(GRADIENT[i] + line + RESET)

# ============================
#   PROMPT STILE KALI
# ============================

def kali_input(text):
    return input(
        f"\033[38;2;0;180;230mroot@kali\033[0m:"
        f"\033[38;2;0;180;230m~ "
        f"\033[38;2;179;240;255m{text}"
    )

# ============================
#   API KEYS
# ============================

VERIPHONE_KEY = "A9D23A4426784422BA779D3A77F74137"
IPINFO_TOKEN  = "b8becbc7acb268"
WHOIS_KEY     = "851bc7936a03441ea95b0f23e5b5f2f3"

# ============================
#   HLR LOOKUP (TECNICO)
# ============================

def hlr_lookup():
    os.system("cls" if os.name == "nt" else "clear")
    print_logo()
    print("\nHLR LOOKUP (TECNICO)\n")

    num = kali_input("Inserisci numero (+39...): ")

    url = f"https://api.veriphone.io/v2/verify?phone={num}&key={VERIPHONE_KEY}"

    try:
        data = requests.get(url, timeout=10).json()

        print(f"\n{WHITE}Numero valido:{RESET} {GREEN}{data.get('phone_valid')}{RESET}")
        print(f"{WHITE}Formato internazionale:{RESET} {GREEN}{data.get('phone')}{RESET}")
        print(f"{WHITE}E164:{RESET} {GREEN}{data.get('e164')}{RESET}")
        print(f"{WHITE}Numero locale:{RESET} {GREEN}{data.get('local_number')}{RESET}")
        print(f"{WHITE}Prefisso paese:{RESET} {GREEN}{data.get('country_prefix')}{RESET}")

        print(f"{WHITE}Paese:{RESET} {GREEN}{data.get('country')}{RESET}")
        print(f"{WHITE}Nome paese:{RESET} {GREEN}{data.get('country_name')}{RESET}")
        print(f"{WHITE}Codice ISO2:{RESET} {GREEN}{data.get('country_code')}{RESET}")
        print(f"{WHITE}Codice ISO3:{RESET} {GREEN}{data.get('country_code_iso3')}{RESET}")

        print(f"{WHITE}Regione:{RESET} {GREEN}{data.get('region')}{RESET}")
        print(f"{WHITE}Timezone:{RESET} {GREEN}{data.get('timezone')}{RESET}")
        print(f"{WHITE}Valuta:{RESET} {GREEN}{data.get('currency')}{RESET}")

        print(f"{WHITE}Carrier:{RESET} {GREEN}{data.get('carrier')}{RESET}")
        print(f"{WHITE}Tipo linea:{RESET} {GREEN}{data.get('line_type')}{RESET}")
        print(f"{WHITE}Tipo rete operatore:{RESET} {GREEN}{data.get('carrier_type')}{RESET}")
        print(f"{WHITE}Tipo numero:{RESET} {GREEN}{data.get('phone_type')}{RESET}")

        print(f"{WHITE}HLR Status:{RESET} {GREEN}{data.get('status')}{RESET}")

    except Exception as e:
        print(f"\nErrore: {e}")

    input("\nPremi invio per tornare al menu...")

# ============================
#   GEOIP LOOKUP
# ============================

def geoip_lookup():
    os.system("cls" if os.name == "nt" else "clear")
    print_logo()
    print("\nGEOIP LOOKUP\n")

    ip = kali_input("Inserisci IP (vuoto = tuo IP): ")

    if ip.strip() == "":
        url = f"https://ipinfo.io/json?token={IPINFO_TOKEN}"
    else:
        url = f"https://ipinfo.io/{ip}/json?token={IPINFO_TOKEN}"

    try:
        data = requests.get(url, timeout=10).json()

        print(f"\n{WHITE}IP:{RESET} {GREEN}{data.get('ip')}{RESET}")
        print(f"{WHITE}Hostname:{RESET} {GREEN}{data.get('hostname')}{RESET}")
        print(f"{WHITE}Città:{RESET} {GREEN}{data.get('city')}{RESET}")
        print(f"{WHITE}Regione:{RESET} {GREEN}{data.get('region')}{RESET}")
        print(f"{WHITE}Paese:{RESET} {GREEN}{data.get('country')}{RESET}")
        print(f"{WHITE}Loc (lat,lon):{RESET} {GREEN}{data.get('loc')}{RESET}")
        print(f"{WHITE}Org/ASN:{RESET} {GREEN}{data.get('org')}{RESET}")
        print(f"{WHITE}CAP:{RESET} {GREEN}{data.get('postal')}{RESET}")
        print(f"{WHITE}Timezone:{RESET} {GREEN}{data.get('timezone')}{RESET}")

    except Exception as e:
        print(f"\nErrore: {e}")

    input("\nPremi invio per tornare al menu...")

# ============================
#   WHOIS LOOKUP
# ============================

def whois_lookup():
    os.system("cls" if os.name == "nt" else "clear")
    print_logo()
    print("\nWHOIS LOOKUP\n")

    target = kali_input("Inserisci dominio o IP: ")

    url = (
        f"https://api.whoisfreaks.com/v1.0/whois?"
        f"apiKey={WHOIS_KEY}&whois=live&domainName={target}"
    )

    try:
        data = requests.get(url, timeout=15).json()
        whois_text = data.get("whois", "Nessun dato WHOIS disponibile.")

        print(f"\n{WHITE}WHOIS RAW:{RESET}\n")
        print(whois_text)

    except Exception as e:
        print(f"\nErrore: {e}")

    input("\nPremi invio per tornare al menu...")

# ============================
#   DNS LOOKUP
# ============================

def dns_lookup():
    os.system("cls" if os.name == "nt" else "clear")
    print_logo()
    print("\nDNS LOOKUP\n")

    host = kali_input("Inserisci dominio/host: ")

    try:
        ip = socket.gethostbyname(host)
        print(f"\n{WHITE}Record A:{RESET} {GREEN}{ip}{RESET}")
    except Exception as e:
        print(f"\nErrore risoluzione A: {e}")

    input("\nPremi invio per tornare al menu...")

# ============================
#   PING
# ============================

def send_packets():
    os.system("cls" if os.name == "nt" else "clear")
    print_logo()
    print("\nPING\n")

    host = kali_input("Inserisci IP/host: ")
    count = kali_input("Numero pacchetti (default 4): ")

    if not count.isdigit():
        count = "4"

    param = "-n" if platform.system().lower().startswith("win") else "-c"

    try:
        subprocess.run(["ping", param, count, host])
    except Exception as e:
        print(f"\nErrore ping: {e}")

    input("\nPremi invio per tornare al menu...")

# ============================
#   MENU
# ============================

def menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print_logo()

        print(f"{LIGHT_GREEN}1): HLR Lookup (telefono){RESET}")
        print(f"{LIGHT_GREEN}2): GeoIP Lookup{RESET}")
        print(f"{LIGHT_GREEN}3): WHOIS Lookup{RESET}")
        print(f"{LIGHT_GREEN}4): DNS Lookup{RESET}")
        print(f"{LIGHT_GREEN}5): Ping{RESET}")
        print(f"{LIGHT_GREEN}6): Esci{RESET}\n")

        choice = kali_input("")

        if choice == "1":
            hlr_lookup()
        elif choice == "2":
            geoip_lookup()
        elif choice == "3":
            whois_lookup()
        elif choice == "4":
            dns_lookup()
        elif choice == "5":
            send_packets()
        elif choice == "6":
            print("Uscita...")
            break
        else:
            input("\nScelta non valida. Premi invio...")

if __name__ == "__main__":
    menu()
