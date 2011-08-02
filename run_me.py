"""This program implements a spell checker"""

#!/usr/bin/env python
__author__ = "plaban nayak"

from lib.BloomFilter import BloomFilter
import sys

if __name__ == "__main__":
    print "This program implements a spell checker"
    # open the file to read correct words
    try:
        file_ = open("./list_of_words.txt","r")
        
    except IOError:
        print "File containing list of correct words not found"
        sys.exit(1)
         
    # read the words from file
    words = file_.readlines()
        
    # count the size of bloom filter bit array for minimal false positives
    k = 11
    n = len(words)
    size = int (k * n * 10 / 7)        

    # create a bloom filter object
    bloom_filter = BloomFilter(size)
    print "Wait: adding words to dictionary"
    for word in words:
        word = word.strip("\r\n")
        #add words to the Bloom Filter
        bloom_filter.add_word(word)
    
    while True:
        print "Enter a word to check for spelling or ctrl -c to exit"
        try:
            word = str(raw_input())
            word = word.lower()
            if bloom_filter.check_word(word) :
                print "Correct"
            else:
                print "Incorrect"
        except KeyboardInterrupt :
            sys.exit(1)
            
        
    
    
        
        
    
        
        
    

    
    
   
        
    
        
    
    
    
