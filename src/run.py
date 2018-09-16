from markovian import Markovian

'''
Created on 2018. 9. 14.

@author: DPain
'''

def main():
    markovian = Markovian(limit=280)
    markovian.readFile()
    markovian.printMap()
    text = markovian.generateRandomTweet()

main()