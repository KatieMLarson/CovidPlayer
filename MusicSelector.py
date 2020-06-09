import random
from os import listdir
from os.path import join, isfile

mypath = '../../Music/'

def getSongs():
    return [join(mypath,file) for file in listdir(mypath)
        if file.endswith(('.mp3', '.mp4', '.wav'))]
            
songArray = getSongs()

def main():
    return random.choice(songArray)
    #subprocess.call(['cvlc', chooseSong(songArray)])
    
if __name__ == '__main__':
    main()