import sys 
from pathlib import Path
import math

def read_parameters():
    weights = {}
    bias = 0
    with open("percmodel.txt", "r") as f:
        body = f.read().splitlines()
        bias = float(body[0])

        for idx in range(1, len(body)):
            line = body[idx].split()
            word = line[0]
            weights[word] = float(line[1])

    return (weights, bias)
            

def label_data(dir, weights, bias):
    output = open("percoutput.txt","w+")
   
    for path in Path(dir).rglob('*.txt'):
        with open(path, "r", encoding="latin1") as f:
            alpha = 0

            body = f.read().split()
            for word in body:
                #Ignore words that don't exist
                if word in weights:
                    alpha += weights[word]
            alpha += bias 
            if alpha > 0:
                output.write("spam " + str(path) + "\n")
            elif alpha < 0:
                output.write("ham " + str(path) + "\n")

    output.close()
    

dir = sys.argv[1]
(weights, bias) = read_parameters()

label_data(dir, weights, bias)
