mdp = input("Password to encrypt : ")


lmdp = len(mdp)


print("Raw password length :", lmdp, "Characters")

#rainbow table
code = {
    "A": "K8xP4",
    "B": "mT2qZ",
    "C": "R7vL1",
    "D": "yN5cW",
    "E": "P3kH9",
    "F": "tQ8mX",
    "G": "V1rJ6",
    "H": "zL4pT",
    "I": "C7nK2",
    "J": "wF5xR",
    "K": "H9qM3",
    "L": "uP2vY",
    "M": "X6kN8",
    "N": "jR1tQ",
    "O": "L5mC7",
    "P": "qZ8pH",
    "Q": "T4xV1",
    "R": "nK7wF",
    "S": "P9yL2",
    "T": "cM3qX",
    "U": "V8rN5",
    "V": "kH1tW",
    "W": "Z6mP4",
    "X": "xQ7cJ",
    "Y": "F2vL9",
    "Z": "R5nT8",

    "a": "X7kP2",
    "b": "m9Qw4",
    "c": "T2zL8",
    "d": "pR5xN",
    "e": "7HvK1",
    "f": "Bj3M9",
    "g": "qW8tY",
    "h": "L4nC2",
    "i": "Zx7P5",
    "j": "kT1vR",
    "k": "N9mQ3",
    "l": "dF6yW",
    "m": "P2sX8",
    "n": "uJ5kL",
    "o": "R7cV1",
    "p": "wQ4nT",
    "q": "Y8mH2",
    "r": "xK3pZ",
    "s": "C5vL9",
    "t": "jN1rW",
    "u": "F7qX4",
    "v": "tP2mK",
    "w": "H9zC6",
    "x": "nR5yJ",
    "y": "V1kT8",
    "z": "Q4pL7",

    "0": "X4pL7",
    "1": "mQ8kT",
    "2": "R2vN5",
    "3": "yH7cP",
    "4": "K9tW1",
    "5": "qL3xZ",
    "6": "V8mF2",
    "7": "nP5rJ",
    "8": "T1kC6",
    "9": "wR7vH",

    "!": "K7xP2",
    "@": "mQ4vL",
    "#": "T9nW1",
    "$": "pR5kX",
    "%": "H2yC8",
    "^": "qL7mF",
    "&": "V1tN4",
    "*": "zP8rJ",
    "(": "X3kT6",
    ")": "wH5vQ",
    "-": "R9mC2",
    "_": "nF1xL",
    "=": "P7qW4",
    "+": "yK8tM",
    "[": "T2vH5",
    "]": "mX9rN",
    "{": "C4kP7",
    "}": "qL1wF",
    ";": "V8nT3",
    ":": "zR5mH",
    "'": "X7tQ2",
    ",": "N9yC1",
    ".": "wF6kT",
    "<": "R3mP8",
    ">": "qH5xV",
    "?": "L1nW7",
    "|": "mC2vQ",
    "~": "P9kX5",
    "`": "yF7tN",
    
    " ": "MnT4S"

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

