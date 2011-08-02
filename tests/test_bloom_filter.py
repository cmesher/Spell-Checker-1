import unittest
import sys
sys.path.append("../lib")

from BloomFilter import BloomFilter

class TestBloomFilter(unittest.TestCase):
    """Test the Bloom Filter Class"""
    
    def setUp(self):
        #create a  bloom filter object with a bit array size of 25 
        bloom_filter = BloomFilter(25)

    def test_constructor(self):
        """Test the constructor"""
        bloom_filter = BloomFilter(25)
        self.assertEqual(bloom_filter.bit_array_size,25)
       
    def test_working(self):
        bloom_filter = BloomFilter(25)
        #check if it works as expected
        bloom_filter.add_word("these")
        self.assertTrue(bloom_filter.check_word("these"))
        bloom_filter.add_word("fdfdf")
        self.assertTrue(bloom_filter.check_word("fdfdf"))
        self.assertFalse(bloom_filter.check_word("plaban"))




if __name__=="__main__":
    unittest.main()
    
        
