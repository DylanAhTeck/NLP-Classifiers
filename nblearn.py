from pathlib import Path
import sys 

def load_data(dir, folder):
    list = []
    for path in Path(dir).rglob(folder + '/*.txt'):
        with open(path, "r", encoding="latin1") as f:
            body = f.read().splitlines()
            list.append(" ".join(body))
    
    return list
    #print(list)


BASE_DATA_DIR = "Enron-Archive/enron4"

path = sys.argv[1]

spam = [(text, "spam") for text in load_data(path, 'spam')]
ham = [(text, "ham") for text in load_data(path, 'ham')]