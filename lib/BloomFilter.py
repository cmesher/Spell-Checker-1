

from GeneralHashFunctions import *

class BloomFilter:
    """Represent a boom filter"""
    
    def __init__(self,bit_array_size):
        
        """Constructor"""
        if not isinstance(bit_array_size,int) or bit_array_size < 0:
            raise ValueError
        
        self.bit_array = [False] * bit_array_size
        self.bit_array_size = bit_array_size
        
    def add_word(self,string):
        """Add a string to filter"""
        
        bit_array_size = self.bit_array_size
        self.bit_array[RSHash(string)%bit_array_size] = True
        self.bit_array[JSHash(string)%bit_array_size] = True
        self.bit_array[PJWHash(string)%bit_array_size] = True
        self.bit_array[ELFHash(string)%bit_array_size] = True
        self.bit_array[BKDRHash(string)%bit_array_size] = True
        self.bit_array[SDBMHash(string)%bit_array_size] = True
        self.bit_array[DJBHash(string)%bit_array_size] = True
        self.bit_array[DEKHash(string)%bit_array_size] = True
        self.bit_array[BPHash(string)%bit_array_size]  = True
        self.bit_array[FNVHash(string)%bit_array_size] = True
        self.bit_array[APHash(string)%bit_array_size] = True
        

    def check_word(self,string):
        """Check for the existence of a word"""
        bit_array_size = self.bit_array_size 
        
        if self.bit_array[RSHash(string)%bit_array_size] and \
        self.bit_array[JSHash(string)%bit_array_size] and \
        self.bit_array[PJWHash(string)%bit_array_size] and \
        self.bit_array[ELFHash(string)%bit_array_size] and \
        self.bit_array[BKDRHash(string)%bit_array_size] and \
        self.bit_array[SDBMHash(string)%bit_array_size] and \
        self.bit_array[DJBHash(string)%bit_array_size] and \
        self.bit_array[DEKHash(string)%bit_array_size] and \
        self.bit_array[BPHash(string)%bit_array_size]  and \
        self.bit_array[FNVHash(string)%bit_array_size] and \
        self.bit_array[APHash(string)%bit_array_size] == True:
            return True
        else:
            return False
        


        
        
        
        
        
    

    
    
