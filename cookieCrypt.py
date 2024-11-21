from hashlib import sha256
import random
from itertools import count
import numpy as np


#? Hash key into sha256 and split into 2 sections and rehash those sections
#? perform the swap op by offsettign the swap values by the key


SWAP_VALUES = [
  [0x02, 0x07],
  [0x04, 0x04],
  [0x09, 0x06],
  [0x07, 0x00],
  [0x00, 0x02],
  [0x0c, 0x0b],
  [0x0a, 0x09],
  [0x08, 0x0d],
  [0x0d, 0x03],
  [0x01, 0x08],
  [0x03, 0x0e],
  [0x0f, 0x0f],
  [0x06, 0x0a],
  [0x05, 0x05],
  [0x0e, 0x01],
  [0x0b, 0x0c],
]


def swap(half_char, offset = 0):
  tmpSwap = np.array(SWAP_VALUES.copy())
  newSwap = {}
  
  col2 = list(tmpSwap[:, 1:2].tolist())
  
  for i in range(offset):
    col2 = [col2.pop(), *col2]
    
  for i, x in enumerate(col2):
    col2[i] = x[0]
    newSwap[int(tmpSwap[i, 0])] = int(x[0])
  
  print(newSwap)
  
  return newSwap[int(half_char)]
  

def unswap(char, offset):
  pass


def encrypt(message: bytearray, key: bytes):
  hashedKey = sha256(key.hex().encode("utf-16")).hexdigest()
  
  keySection1 = sha256(hashedKey[32:].encode("utf-16")) # replace key
  keySection2 = sha256(hashedKey[:32].encode("utf-16")) # mix key

  print(keySection1.hexdigest())

  output = []
  
  splitChars = []

  for char in message:
    print(char.to_bytes().hex())

  print()

  print(swap(message[2].to_bytes().hex()[0]))


  return "Done"

def decrypt(message, key):
  pass