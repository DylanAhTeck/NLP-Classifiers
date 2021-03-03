import sys 
from pathlib import Path

def read_parameters():

    spamDict = {}
    hamDict = {}
    with open("nbmodel.txt", "r") as f:
        body = f.read().splitlines()
        firstLine = body[0].split()
        pSpam = float(firstLine[0])
        pHam = float(firstLine[1])

        for idx in range(1, len(body)):
            line = body[idx].split()
            word = line[0]
            spamDict[word] = float(line[1])
            hamDict[word] = float(line[2])

    return (spamDict, hamDict, pSpam, pHam)
            
def label_data(dir, spamDict, hamDict):
    output = open("nboutput.txt","w+")
     
    #for path in Path(dir).rglob('*.txt'):
    for path in Path(dir).rglob('*.txt'):
        with open(path, "r", encoding="latin1") as f:
            pHam = 1
            pSpam = 1
            body = f.read().split()
            for word in body:
                #Ignore words that don't exist
                if word in hamDict:
                    pHam = pHam * hamDict[word]
                    pSpam = pSpam * spamDict[word]
            if pSpam > pHam:
                output.write("spam " + str(path) + "\n")
            else:
                output.write("ham " + str(path) + "\n")
            #list.append(" ".join(body))

    output.close()
    

dir = sys.argv[1]
(spamDict, hamDict, pSpam, pHam) = read_parameters()

label_data(dir, spamDict, hamDict)
