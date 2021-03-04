from pathlib import Path
import sys 

def load_data(dir, folder):
    list = []
    for path in Path(dir).rglob(folder + '/*.txt'):
        with open(path, "r", encoding="latin1") as f:
            body = f.read().split()
            
            list.append(body)
    
    return list

def process(list):
    count = 1
    MaxIter = 100

    biasB = 0
    avgBias = 0

    weights = {}
    ySpam = 1
    yHam = -1
    
    for iter in range(1, MaxIter):
        for (email, label) in list:
            y = ySpam if label == "spam" else yHam

            activation = 0
            for word in email:
                if word not in weights:
                    weights[word] = 0
                activation += weights[word]
            activation += biasB

            if activation * y <= 0:
                for word in email:
                    weights[word] = weights[word] + y
                    biasB = biasB + y

    return (weights, biasB)


path = sys.argv[1]

spam = [(text, "spam") for text in load_data(path, 'spam')]
ham = [(text, "ham") for text in load_data(path, 'ham')]

all = spam + ham

(weights, biasB) = process(all)

f= open("percmodel.txt","w+")
f.write(str(biasB) + "\n")

for word, weight in weights.items():
    st = word + " " + str(weight) 
    f.write(st + "\n")

f.close()