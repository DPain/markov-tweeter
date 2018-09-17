'''
Created on 2018. 9. 14.

@author: DPain
'''

from string_helper import isDigitsPunct
from random import randint

class Markovian(object):
    '''
    classdocs
    '''

    def __init__(self, limit):
        '''
        Constructor
        '''
        self.max_tweet_size = limit
        self.key_pair_freq_dict = dict()
        self.key_pair_dict = dict()
        
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
                if (prev, word) in self.key_pair_freq_dict.keys():
                    self.key_pair_freq_dict[(prev, word)] += 1
                else:
                    self.key_pair_freq_dict[(prev, word)] = 1
                    if prev in self.key_pair_dict.keys():
                        self.key_pair_dict[prev].append(word)
                    else:
                        self.key_pair_dict[prev] = list()
                        self.key_pair_dict[prev].append(word)
                        
                prev = word

        
    def printMap(self):
        for key, arr in self.key_pair_freq_dict.items():
            print("Key:%s, List:%s" % (key, arr))
            
        for key, arr in self.key_pair_dict.items():
            print("Key:%s, size:%s" % (key, arr))
            
    def getPairFromRatio(self, key, num):
        self.key_pair_dict[key]
        return ""
            
    def generateRandomTweet(self):
        tweet = ""
        
        total = len(self.key_pair_dict)
        num = randint(0, total)
        
        i = 0
        
        word = list(self.key_pair_dict.keys())[num]
        tweet.join(word)
        i += len(word)
        
        print("Random number:%d/%d" % (num, total))
        print("Random word:%s" % word)
        
        total_freq = 0
        for pair in self.key_pair_dict[word]:
            print("Pair: " + pair)
            total_freq += self.key_pair_freq_dict[(word, pair)]
        num = randint(0, total_freq - 1)
        print(word, str(num) + "/" + str(total_freq))
        print("%s: %s" % (word, self.key_pair_dict[word]))
        
        word = self.key_pair_dict[word][num]
        
        while i + len(word) < self.max_tweet_size:
            tweet.join(word)
            i += len(word)
            
            total_freq = 0
            for pair in self.key_pair_dict[word]:
                print("Pair: %s Freq: %i" % (pair, self.key_pair_freq_dict[(word, pair)]))
                total_freq += self.key_pair_freq_dict[(word, pair)]
            num = randint(0, total_freq - 1)
            print(word, str(num) + "/" + str(total_freq))
            print("%s: %s" % (word, self.key_pair_dict[word]))
            
            word = self.getPairFromRatio(word, num)
        
        ##
        """
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
        """
    