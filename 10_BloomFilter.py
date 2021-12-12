# bitArray functions from https://wiki.python.org/moin/BitArrays

from bitarray import bitarray
'''
import array
def makeBitArray(bitSize, fill = 0):
    intSize = bitSize >> 5                   # number of 32 bit integers
    if (bitSize & 31):                      # if bitSize != (32 * n) add
        intSize += 1                        #    a record for stragglers
    if fill == 1:
        fill = 4294967295                                 # all bits set
    else:
        fill = 0                                      # all bits cleared

    bitArray = array.array('Q')          # 'I' = unsigned 32-bit integer

    bitArray.extend((fill,) * intSize)

    return(bitArray)

# setBit() returns an integer with the bit at 'bit_num' set to 1.
def setBit(array_name, bit_num):
    record = bit_num >> 5
    offset = bit_num & 31
    mask = 1 << offset
    array_name[record] |= mask
    return(array_name[record])

# clearBit() returns an integer with the bit at 'bit_num' cleared.
def clearBit(array_name, bit_num):
    record = bit_num >> 5
    offset = bit_num & 31
    mask = ~(1 << offset)
    array_name[record] &= mask
    return(array_name[record])
'''

class BloomFilter:

     # constructor
     # postcondition: new Bloom filter is created
    def __init__(self, f_len):
        self.myArray = bitarray(f_len)
        #self.myArray = makeBitArray(32, f_len)


    def hash1(self, str1):
        result = 0
        for c in str1:
            code = ord(c)
            result = (result * 17 + code) % 32;
        #print(' result hash1 ', result)        
        return result

    def hash2(self, str1):
        result = 0
        for c in str1:
            code = ord(c)
            result = (result * 223 + code) % 32;
        #print(' result hash2 ', result)    
        return result

     # command
     # postcondition: the new item is added to Bloom filter
    def add(self, str1):
        self.myArray[self.hash1(str1)] = True
        self.myArray[self.hash2(str1)] = True
        #setBit(self.myArray, self.hash1(str1))
        #setBit(self.myArray, self.hash2(str1))
        

    def is_value(self, str1):
        # check is str1 in filter
        index_i = self.hash1(str1)
        index_j = self.hash1(str1)
        return self.myArray[index_i]==True and self.myArray[index_j] == True
