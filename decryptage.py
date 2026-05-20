# rainbow table inverse — compatible x4 (4 chars) et x5 (5 chars)
decode = {

    "K7mQ": "a", "X7kP2": "a",
    "a9T3": "b", "m9Qw4": "b",
    "8pLx": "c", "T2zL8": "c",
    "Q2vN": "d", "pR5xN": "d",
    "m4Zc": "e", "7HvK1": "e",
    "T8aR": "f", "Bj3M9": "f",
    "6xPq": "g", "qW8tY": "g",
    "n1Kf": "h", "L4nC2": "h",
    "Z5mD": "i", "Zx7P5": "i",
    "r7Vb": "j", "kT1vR": "j",
    "3LqT": "k", "N9mQ3": "k",
    "h9Xc": "l", "dF6yW": "l",
    "P6nS": "m", "P2sX8": "m",
    "v2mJ": "n", "uJ5kL": "n",
    "7cQd": "o", "R7cV1": "o",
    "L1zW": "p", "wQ4nT": "p",
    "x8Rk": "q", "Y8mH2": "q",
    "D4tN": "r", "xK3pZ": "r",
    "q5Mv": "s", "C5vL9": "s",
    "B9sP": "t", "jN1rW": "t",
    "2nXr": "u", "F7qX4": "u",
    "k6Tg": "v", "tP2mK": "v",
    "s8Hq": "x", "nR5yJ": "x",
    "N7dC": "y", "V1kT8": "y",
    "f1Rz": "z", "Q4pL7": "z",

    "v3Kq": "A", "K8xP4": "A",
    "T9xM": "B", "mT2qZ": "B",
    "p7Ld": "C", "R7vL1": "C",
    "Q4nZ": "D", "yN5cW": "D",
    "h8Rc": "E", "P3kH9": "E",
    "m2Vt": "F", "tQ8mX": "F",
    "X6sP": "G", "V1rJ6": "G",
    "b5Jk": "H", "zL4pT": "H",
    "N1wQ": "I", "C7nK2": "I",
    "c7Dz": "J", "wF5xR": "J",
    "R3fL": "K", "H9qM3": "K",
    "y9Tm": "L", "uP2vY": "L",
    "k6Xc": "M", "X6kN8": "M",
    "Z2pV": "N", "jR1tQ": "N",
    "s8Qn": "O", "L5mC7": "O",
    "D5aR": "P", "qZ8pH": "P",
    "t1Hj": "Q", "T4xV1": "Q",
    "W4mS": "R", "nK7wF": "R",
    "n9Kp": "S", "P9yL2": "S",
    "e6Xb": "T", "cM3qX": "T",
    "J3qT": "U", "V8rN5": "U",
    "g8Lr": "V", "kH1tW": "V",
    "P2vC": "W", "Z6mP4": "W",
    "u7Nd": "X", "xQ7cJ": "X",
    "F9sZ": "Y", "F2vL9": "Y",
    "a4Rk": "Z", "R5nT8": "Z",

    "j4Wp": "0", "X4pL7": "0",
    "R8nt": "1", "mQ8kT": "1",
    "5gMc": "2", "R2vN5": "2",
    "Xv2b": "3", "yH7cP": "3",
    "9hFs": "4", "K9tW1": "4",
    "w3Qe": "5", "qL3xZ": "5",
    "G7ky": "6", "V8mF2": "6",
    "2rTd": "7", "nP5rJ": "7",
    "n6Jz": "8", "T1kC6": "8",
    "H1mx": "9", "wR7vH": "9",

    "j4Wm": "!", "K7xP2": "!",
    "R8vT": "@", "mQ4vL": "@",
    "5nKq": "#", "T9nW1": "#",
    "Xc2P": "$", "pR5kX": "$",
    "7mZd": "%", "H2yC8": "%",
    "bL9s": "^", "qL7mF": "^",
    "Q3tF": "&", "V1tN4": "&",
    "6hNr": "*", "zP8rJ": "*",
    "yW4k": "(", "X3kT6": "(",
    "1pDx": ")", "wH5vQ": ")",
    "Mv8J": "-", "R9mC2": "-",
    "c5Rn": "_", "nF1xL": "_",
    "Z9qB": "+", "yK8tM": "+",
    "f2Ts": "=", "P7qW4": "=",
    "8kXv": "[", "T2vH5": "[",
    "nP6m": "]", "mX9rN": "]",
    "3dLw": "{", "C4kP7": "{",
    "Hq7c": "}", "qL1wF": "}",
    "t1Nz": "|", "mC2vQ": "|",
    "5rKj": ";", "V8nT3": ";",
    "Wd4M": ":", "zR5mH": ":",
    "9xBp": "'", "X7tQ2": "'",
    "L6fs": '"',  "pK4vL": '"',
    "2mQh": ",", "N9yC1": ",",
    "Vk8n": ".", "wF6kT": ".",
    "r3Zt": "<", "R3mP8": "<",
    "7cPy": ">", "qH5xV": ">",
    "4wNq": "?", "L1nW7": "?",
    "sX1v": "`", "yF7tN": "`",
    "mT9k": "~", "P9kX5": "~",

    "MnT4":  " ",   # espace x4
    "MnT4S": " ",   # espace x5
}

mdp_crypte = input("Password to decrypt : ")

# Déchiffrement : on avance dans la chaîne en testant d'abord un bloc de 5,
# puis de 4. Ainsi le déchiffreur gère x4 et x5 sans avoir besoin de
# connaître le protocole utilisé à l'avance.
resultat = ""
i = 0
while i < len(mdp_crypte):
    # Essai bloc de 5 en priorité (x5 et espace x5 = "MnT4S")
    if i + 5 <= len(mdp_crypte):
        bloc5 = mdp_crypte[i:i+5]
        if bloc5 in decode:
            resultat += decode[bloc5]
            i += 5
            continue
    # Sinon essai bloc de 4 (x4)
    if i + 4 <= len(mdp_crypte):
        bloc4 = mdp_crypte[i:i+4]
        if bloc4 in decode:
            resultat += decode[bloc4]
            i += 4
            continue
    # Bloc non reconnu : on marque "?" et on avance d'un caractère
    resultat += "?"
    i += 1

print("Crypted password   : ", mdp_crypte)
print("Encrypted length   : ", len(mdp_crypte))
print("Decrypted password : ", resultat)
print("Decrypted length   : ", len(resultat), "Characters")