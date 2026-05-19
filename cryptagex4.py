mdp = input("Password to encrypt : ")


lmdp = len(mdp)


print("Raw password length :", lmdp, "Characters")

#rainbow table
code = {
    "a": "K7mQ",
    "b": "a9T3",
    "c": "8pLx",
    "d": "Q2vN",
    "e": "m4Zc",
    "f": "T8aR",
    "g": "6xPq",
    "h": "n1Kf",
    "i": "Z5mD",
    "j": "r7Vb",
    "k": "3LqT",
    "l": "h9Xc",
    "m": "P6nS",
    "n": "v2mJ",
    "o": "7cQd",
    "p": "L1zW",
    "q": "x8Rk",
    "r": "D4tN",
    "s": "q5Mv",
    "t": "B9sP",
    "u": "2nXr",
    "v": "k6Tg",
    "x": "s8Hq",
    "y": "N7dC",
    "z": "f1Rz",
    "A": "v3Kq",
    "B": "T9xM",
    "C": "p7Ld",
    "D": "Q4nZ",
    "E": "h8Rc",
    "F": "m2Vt",
    "G": "X6sP",
    "H": "b5Jk",
    "I": "N1wQ",
    "J": "c7Dz",
    "K": "R3fL",
    "L": "y9Tm",
    "M": "k6Xc",
    "N": "Z2pV",
    "O": "s8Qn",
    "P": "D5aR",
    "Q": "t1Hj",
    "R": "W4mS",
    "S": "n9Kp",
    "T": "e6Xb",
    "U": "J3qT",
    "V": "g8Lr",
    "W": "P2vC",
    "X": "u7Nd",
    "Y": "F9sZ",
    "Z": "a4Rk",
    "0": "j4Wp",
    "1": "R8nt",
    "2": "5gMc",
    "3": "Xv2b",
    "4": "9hFs",
    "5": "w3Qe",
    "6": "G7ky",
    "7": "2rTd",
    "8": "n6Jz",
    "9": "H1mx",
"!": "j4Wm",
"@": "R8vT",
"#": "5nKq",
"$": "Xc2P",
"%": "7mZd",
"^": "bL9s",
"&": "Q3tF",
"*": "6hNr",
"(": "yW4k",
")": "1pDx",
"-": "Mv8J",
"_": "c5Rn",
"+": "Z9qB",
"=": "f2Ts",
"[": "8kXv",
"]": "nP6m",
"{": "3dLw",
"}": "Hq7c",
"|": "t1Nz",
";": "5rKj",
":": "Wd4M",
"'": "9xBp",
'"': "L6fs",
",": "2mQh",
".": "Vk8n",
"<": "r3Zt",
">": "7cPy",
"/": "Jd5R",
"?": "4wNq",
"`": "sX1v",
"~": "mT9k",
    " ": "MnT4"
}


aya = {}

for i in range(lmdp):
    def ayaa(x=i):
        lettre = mdp[x]
        return code.get(lettre, lettre)

    aya[i] = ayaa


resultat = ""

for i in aya:
    resultat += aya[i]()

print("The encrypted password is : ", resultat)
print("Encrypted password length : ", len(resultat), "characters")