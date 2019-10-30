from Crypto.Cipher import AES

PLAINTEXT = "some plaintext.."

def f(k):
    aes = AES.new(k, AES.MODE_ECB)
    cipher = aes.encrypt(PLAINTEXT)
    return extractKBits(cipher, 104, 24)

# source: https://www.geeksforgeeks.org/python-slicing-extract-k-bits-given-position/
def extractKBits(num,k,p): 
  
     # convert number into binary first 
     binary = bin(num) 
  
     # remove first two characters 
     binary = binary[2:] 
  
     end = len(binary) - p 
     start = end - k + 1
  
     # extract k  bit sub-string 
     kBitSubStr = binary[start : end+1] 
  
     # convert extracted sub-string into decimal again 
     return kBitSubStr
  
# Driver program 
if __name__ == "__main__":

    k = f("0000000000000000")


    num = 171
    k = 5
    p = 2
    extractKBits(num,k,p) 