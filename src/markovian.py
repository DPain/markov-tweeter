'''
Created on 2018. 9. 14.

@author: DPain
'''

from string_helper import isDigitsPunct
from Random import randint

class Markovian(object):
    '''
    classdocs
    '''

    def __init__(self, limit):
        '''
        Constructor
        '''
        self.max_tweet_size = limit
        self.dict = dict()
        self.total_freq = dict()
        
        print("Instantiated a Markovian with Max Tweet Size:%d" % self.max_tweet_size)
        
    def readFile(self):
        file = open("../rsc/10.txt", "r")
        
        text = file.read()
        
        start_word = "1:1 "
        start_index = text.find(start_word) + len(start_word)
        
        words = text[start_index:5000].split()
        print(words)
        
        prev = words[0]
        for word in words[1:]:
            if not isDigitsPunct(word):
                if (prev, word) in self.dict.keys():
                    self.dict[(prev, word)] += 1
                else:
                    self.dict[(prev, word)] = 1
                    if prev in self.total_freq.keys():
                        self.total_freq[prev] += 1
                    else:
                        self.total_freq[prev] = 1
                        
                prev = word

        
    def printMap(self):
        for key, arr in self.dict.items():
            print("Key:%s, List:%s" % (key, arr))
            
        for key, arr in self.total_freq.items():
            print("Key:%s, size:%s" % (key, arr))
            
    def generateRandomTweet(self):
        tweet = ""
        
        total = len(self.total_freq)
        num = randint(0, total)
        
        i = 0
        
        word = self.total_freq.keys()[num]
        tweet += word
        i += len(word)
        
        print("Random number:%d/%d\n", num, total)
        print("Random word:%s\n", word)
        
        total = self.total_freq[word]
        num = randint(0, total)
        ##
        Node* node = (Node*) getNodeFromRatio(&base, num);
        // Account for trailing \0 character
        while(i + strlen(node->pair) < (TWITTER_MAX_SIZE - 1)) {
            strcat(tweet, " ");
            strcat(tweet, node->pair);
            // Including space
            i += (strlen(node->pair) + 1);
    
            //printf("Random key pair:%s - %s %d Tweet Size:%d\n", base->key, node->pair, num, i);
            
            //printf("Getting Base\n");
            base = getBase(&map, node->pair);
            // If there are no key pairs available, it will always randomly choose another base
            while(base == NULL) {
                mapSize = getMapSize(&map);
                num = rand() % mapSize;
                base = getNthBase(&map, num);
            }
            
            nodeSize = getTotalFreq(&map, base->key);
            num = rand() % nodeSize;
            
            node = (Node*) getNodeFromRatio(&base, num);
        }
        
        strcpy(output, tweet);
    }
    