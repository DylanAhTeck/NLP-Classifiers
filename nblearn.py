from pathlib import Path
import sys 

def load_data(dir, folder):
    list = []
    for path in Path(dir).rglob(folder + '/*.txt'):
        with open(path, "r", encoding="latin1") as f:
            body = f.read().split()
            
            list.append(body)
            #list.append(" ".join(body))
    
    return list
    #print(list)


path = sys.argv[1]

spam = [(text, "spam") for text in load_data(path, 'spam')]
ham = [(text, "ham") for text in load_data(path, 'ham')]


numOfSpamMail = len(spam)
numOfHamMail = len(ham)
all = spam + ham

# Estimate P(word|Spam)

# Dictionary of words to word-count
SpamDict = {}
HamDict = {}
uniqueTokens = set()

# Number of total words (including duplicates) in dict
SpamDictCount = 0
HamDictCount = 0

# Number of spam/not-spam emails
SpamMessageCount = 0
NotSpamMessageCount = 0


SpamMailWithToken = {}
HamMailWithToken = {} 

def featurizeTokens(token, is_spam):
    global SpamDictCount, HamDictCount, SpamMessageCount, NotSpamMessageCount, uniqueTokens
    
    visited = set()
    for word in token:

        uniqueTokens.add(word)
        # if word not in visited:
        #     visited.add(word)
        #     if is_spam: 
        #         SpamMailWithToken[word] = SpamMailWithToken.get(word, 0) + 1
        #     else:
        #         HamMailWithToken[word] = HamMailWithToken.get(word, 0) + 1

        # Count total number of spam/not-spam emails
        if is_spam:
            SpamMessageCount += 1
        else:
            NotSpamMessageCount += 1

        # Add to SpamDict if is_spam
        if is_spam:
            if not word in SpamDict:
                SpamDict[word] = 1
            else:
                SpamDict[word] += 1
            SpamDictCount += 1

        # Else add to HamDict
        else:
            if not word in HamDict:
                HamDict[word] = 1
            else:
                HamDict[word] += 1
            HamDictCount += 1


for (token, label) in all:
    featurizeTokens(token, label == 'spam')

# Calculate P(Spam) and P(~Spam)
#Pspam = SpamMessageCount / (SpamMessageCount + NotSpamMessageCount)
#Pnotspam = 1 - Pspam
# print(Pspam)


# P(token|spam)
# P(token|ham)
# P(A|B) = P(A ∩ B) / P(B)

f= open("nbmodel.txt","w+")
pSpam = numOfSpamMail/(numOfHamMail + numOfSpamMail)
pHam = numOfHamMail/(numOfHamMail + numOfSpamMail)
f.write(str(pSpam) + " " + str(pHam) + "\n")

for word in uniqueTokens:
    pTokenSpam = (SpamDict.get(word, 0) + 1)/(SpamMessageCount + len(uniqueTokens))
    pTokenHam = (HamDict.get(word, 0) + 1)/(NotSpamMessageCount + len(uniqueTokens))
    st = word + " " + str(pTokenSpam) + " " + str(pTokenHam)
    f.write(st + "\n")
    
f.close()
