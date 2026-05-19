#rainbow table inverse
decode = {
    "K7mQ": "a",
    "a9T3": "b",
    "8pLx": "c",
    "Q2vN": "d",
    "m4Zc": "e",
    "T8aR": "f",
    "6xPq": "g",
    "n1Kf": "h",
    "Z5mD": "i",
    "r7Vb": "j",
    "3LqT": "k",
    "h9Xc": "l",
    "P6nS": "m",
    "v2mJ": "n",
    "7cQd": "o",
    "L1zW": "p",
    "x8Rk": "q",
    "D4tN": "r",
    "q5Mv": "s",
    "B9sP": "t",
    "2nXr": "u",
    "k6Tg": "v",
    "s8Hq": "x",
    "N7dC": "y",
    "f1Rz": "z",
"v3Kq": "A",
  "T9xM": "B",
  "p7Ld": "C",
  "Q4nZ": "D",
  "h8Rc": "E",
  "m2Vt": "F",
  "X6sP": "G",
  "b5Jk": "H",
  "N1wQ": "I",
  "c7Dz": "J",
  "R3fL": "K",
  "y9Tm": "L",
  "k6Xc": "M",
  "Z2pV": "N",
  "s8Qn": "O",
  "D5aR": "P",
  "t1Hj": "Q",
  "W4mS": "R",
  "n9Kp": "S",
  "e6Xb": "T",
  "J3qT": "U",
  "g8Lr": "V",
  "P2vC": "W",
  "u7Nd": "X",
  "F9sZ": "Y",
  "a4Rk": "Z",
    "j4Wp": "0",
    "R8nt": "1",
    "5gMc": "2",
    "Xv2b": "3",
    "9hFs": "4",
    "w3Qe": "5",
    "G7ky": "6",
    "2rTd": "7",
    "n6Jz": "8",
    "H1mx": "9",
"j4Wm": "!",
"R8vT": "@",
"5nKq": "#",
"Xc2P": "$",
"7mZd": "%",
"bL9s": "^",
"Q3tF": "&",
"6hNr": "*",
"yW4k": "(",
"1pDx": ")",
"Mv8J": "-",
"c5Rn": "_",
"Z9qB": "+",
"f2Ts": "=",
"8kXv": "[",
"nP6m": "]",
"3dLw": "{",
"Hq7c": "}",
"t1Nz": "|",
"5rKj": ";",
"Wd4M": ":",
"9xBp": "'",
"L6fs": '"',
"2mQh": ",",
"Vk8n": ".",
"r3Zt": "<",
"7cPy": ">",
"Jd5R": "/",
"4wNq": "?",
"sX1v": "`",
"mT9k": "~",
"MnT4": " "
}

mdp_crypte = input("Password to decrypt : ")

#chaque code fait 4 caractères, on découpe par blocs de 4
lmdp_crypte = len(mdp_crypte)

if lmdp_crypte % 4 != 0:
    print("Error: Encrypted password is invalid (incorrect length)")
else:
    resultat = ""
    for i in range(0, lmdp_crypte, 4):
        bloc = mdp_crypte[i:i+4]
        lettre = decode.get(bloc, "?")  # "?" si le bloc est inconnu
        resultat += lettre

    print("Crypted password : ", mdp_crypte)
    print("Encrypted password length : ", len(mdp_crypte))
    print("The decrypted password is : ", resultat)
    print("The decrypted password length is : ", len(resultat), "Characters")
