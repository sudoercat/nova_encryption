import os
import sys
import subprocess

R  = "\033[0m"
B  = "\033[1m"
CY = "\033[96m"
GR = "\033[92m"
RD = "\033[91m"
YL = "\033[93m"
DM = "\033[2m"


BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
CRYPTAGE   = os.path.join(BASE_DIR, "cryptagex4.py")
CRYPTAGE2 = os.path.join(BASE_DIR, "cryptagex5.py")
DECRYPTAGE = os.path.join(BASE_DIR, "decryptage.py")


def lancer(script, label, couleur):
    print(f"\n{couleur}{B}─── {label} ───{R}\n")

    if not os.path.exists(script):
        print(f"{RD}Erreur : fichier introuvable → {script}{R}")
        return

    subprocess.run(
        [sys.executable, script],
        stdin=None,
        stdout=None,
        stderr=None
    )

def banniere():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"""{CY}{B}
  ██████   █████                               
░░██████ ░░███                                
 ░███░███ ░███   ██████  █████ █████  ██████  
 ░███░░███░███  ███░░███░░███ ░░███  ░░░░░███ 
 ░███ ░░██████ ░███ ░███ ░███  ░███   ███████ 
 ░███  ░░█████ ░███ ░███ ░░███ ███   ███░░███ 
 █████  ░░█████░░██████   ░░█████   ░░████████
░░░░░    ░░░░░  ░░░░░░     ░░░░░     ░░░░░░░░ 
{R}{DM}            Homemade encryption tool by Antoine{R}
""")

def menu():
    print(f"  {B}What do you want to do ?{R}\n")
    print(f"  {YL}[1]{R}  🔓  Decrypt a password")
    print(f"  {GR}[2]{R}  🔒  Encrypt a password (protocol x4)")
    print(f"  {GR}[3]{R}  🔒  Encrypt a password (protocol x5)")
    print(f"  {RD}[0]{R}  ✖   Leave\n")


def main():
    while True:
        banniere()
        menu()

        choix = input(f"  {B}Your choice :{R} ").strip()

        if choix == "2":
            lancer(CRYPTAGE, "ENCRYPTION", GR)
        elif choix == "3":
            lancer(CRYPTAGE2, "DECRYPTION", GR)
        elif choix == "1":
            lancer(DECRYPTAGE, "DECRYPTION", YL)
        elif choix == "0":
            print(f"\n{DM}  Good bye.{R}\n")
            sys.exit(0)
        else:
            print(f"\n  {RD}Invalid option. Choose 1, 2 or 3.{R}")

        print(f"\n{DM}  ─────────────────────────────────────────{R}")
        input(f"{DM}  Press Enter to return to the menu…{R}")

if __name__ == "__main__":
    main()