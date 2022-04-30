import pandas as pd



def readFile(file):
    try:
        df = pd.read_csv(file, delimiter=";", header=None)
        return df.values.tolist()
    except:
        print("No such file or directory {0}".format(file))
        return -1

# from src.enigma import *

# rotors = readFile('assets/files/Rotors.csv')
# rotor1, rotor2, rotor3 = rotors[0], rotors[1], rotors[2]

# reflector = readFile('assets/files/Reflector.csv')
# Alphabet = readFile('assets/files/Alphabet.csv')