def RSHash(key):
    """Represent the hash developed by  Robert Sedgwicks

       @type: string
       @param key: string to hash
    """
    if not isinstance(key,str):
        raise TypeError,"Key is not of string type"
    
    a    = 378551
    b    =  63689
    hash_ =      0
    for i in range(len(key)):
      hash_ = hash_ * a + ord(key[i])
      a = a * b
    return hash_


def JSHash(key):
    """Represent the  hash developed by Justin Sobel

       @type: string
       @param key: string to hash
    """
    if not isinstance(key,str):
        raise TypeError,"Key is not of string type"
    
    hash_ = 1315423911
    for i in range(len(key)):
      hash_ ^= ((hash_ << 5) + ord(key[i]) + (hash_ >> 2))
    return hash_


def PJWHash(key):
    
    """Represent the  hash developed by Peter J. Weinberger of AT&T Bell Labs

       @type: string
       @param key: string to hash
    """
    
    if not isinstance(key,str):
        raise TypeError,"Key is not of string type"
    BitsInUnsignedInt = 4 * 8
    ThreeQuarters     = long((BitsInUnsignedInt  * 3) / 4)
    OneEighth         = long(BitsInUnsignedInt / 8)
    HighBits          = (0xFFFFFFFF) << (BitsInUnsignedInt - OneEighth)
    hash_             = 0
    test              = 0

    for i in range(len(key)):
        hash_ = (hash_ << OneEighth) + ord(key[i])
        test = hash_ & HighBits
    if test != 0:
        hash_ = (( hash_ ^ (test >> ThreeQuarters)) & (~HighBits));
    return (hash_ & 0x7FFFFFFF)
    
   


def ELFHash(key):
    """Similiar to PJWHash but for 32 bit processors

       @type: string
       @param key: string to hash
    """
    if not isinstance(key,str):
        raise TypeError,"Key is not of string type"
    
    
    hash_ = 0
    x    = 0
    for i in range(len(key)):
      hash_ = (hash_ << 4) + ord(key[i])
      x = hash_ & 0xF0000000
      if x != 0:
        hash_ ^= (x >> 24)
      hash_ &= ~x
    return hash_


def BKDRHash(key):
    """Represent the  hash developed by Brian Kernighan and Dennis Ritchie

       @type: string
       @param key: string to hash
    """
    if not isinstance(key,str):
        raise TypeError,"Key is not of string type"
    
    seed = 131 # 31 131 1313 13131 131313 etc..
    hash_ = 0
    for i in range(len(key)):
      hash_ = (hash_ * seed) + ord(key[i])
    return hash_


def SDBMHash(key):
    """Represent the SDBMHash

       @type: string
       @param key: string to hash
    """
    if not isinstance(key,str):
        raise TypeError,"Key is not of string type"
    
    
    hash_ = 0
    for i in range(len(key)):
      hash_ = ord(key[i]) + (hash_ << 6) + (hash_ << 16) - hash_;
    return hash_


def DJBHash(key):
    """Represent the  hash developed by Professor Daniel J. Bernstein

       @type: string
       @param key: string to hash
    """
    if not isinstance(key,str):
        raise TypeError,"Key is not of string type"
    
    hash_ = 5381
    for i in range(len(key)):
       hash_ = ((hash_ << 5) + hash_) + ord(key[i])
    return hash_


def DEKHash(key):
    """Represent the  hash developed by Donald E. Knuth

       @type: string
       @param key: string to hash
    """
    if not isinstance(key,str):
        raise TypeError,"Key is not of string type"
    
    
    hash_ = len(key);
    for i in range(len(key)):
      hash_ = ((hash_ << 5) ^ (hash_ >> 27)) ^ ord(key[i])
    return hash_


def BPHash(key):
    """Represent the  BPHash

       @type: string
       @param key: string to hash
    """
    if not isinstance(key,str):
        raise TypeError,"Key is not of string type"
    
    hash_ = 0
    for i in range(len(key)):
       hash_ = hash_ << 7 ^ ord(key[i])
    return hash_


def FNVHash(key):
    """Represent the  FNVHash

       @type: string
       @param key: string to hash
    """
    if not isinstance(key,str):
        raise TypeError,"Key is not of string type"
    
    fnv_prime = 0x811C9DC5
    hash_ = 0
    for i in range(len(key)):
      hash_ *= fnv_prime
      hash_ ^= ord(key[i])
    return hash_


def APHash(key):
    """Represent the  hash developed by Arash Partow

       @type: string
       @param key: string to hash
    """
    if not isinstance(key,str):
        raise TypeError,"Key is not of string type"
    
    hash_ = 0xAAAAAAAA
    for i in range(len(key)):
      if ((i & 1) == 0):
        hash_ ^= ((hash_ <<  7) ^ ord(key[i]) * (hash_ >> 3))
      else:
        hash_ ^= (~((hash_ << 11) + ord(key[i]) ^ (hash_ >> 5)))
    return hash_


