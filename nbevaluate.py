import sys
from pathlib import Path

def load_data(dir):
    correctly_classified = 0
    total_documents = 0

    correctly_classified_spam = 0
    correctly_classified_ham = 0

    classified_spam = 0
    classified_ham = 0

    actual_spam = 0
    actual_ham = 0
    with open(dir, "r", encoding="latin1") as f:
        body = f.read().splitlines()
        
        for line in body:
            split = line.split()
            path_str = str(split[1])

            if "spam" not in path_str and "ham" not in path_str:
                continue

            total_documents += 1

            if split[0] == 'ham':
                classified_ham += 1
            else:
                classified_spam += 1
            
            if "spam" in path_str:
                actual_spam += 1
                
                if split[0] == "spam":
                    correctly_classified_spam += 1
                    correctly_classified += 1
            elif "ham" in path_str:
                actual_ham += 1

                if split[0] == "ham":
                    correctly_classified_ham += 1
                    correctly_classified += 1
        
    print(correctly_classified)
    print(total_documents)
    #TODO MUST ACCOUNT FOR DIV BY 0
    spamPrecision = correctly_classified_spam/classified_spam
    hamPrecision = correctly_classified_ham/classified_ham
    print(spamPrecision)
    print(hamPrecision)

    spamRecall = correctly_classified_spam/actual_spam
    hamRecall = correctly_classified_ham/actual_ham

    print(spamRecall)
    print(hamRecall)

    spamF1 = (2 * spamPrecision * spamRecall)/(spamPrecision + spamRecall)
    hamF2 = (2 * hamPrecision * hamRecall)/(hamPrecision + hamRecall)
    #precision, recall, and F1 score
    #F1 = 2PR /(P+R)

    print(spamF1)
    print(hamF2)

dir = sys.argv[1]
load_data(dir)