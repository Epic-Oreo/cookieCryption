from hashlib import sha256
import random
from itertools import count
# Split message into 16 byte chunks
# Hash key into sha256 and split into 2 sections and rehash those sections

SWAP_VALUES = {
  0x02: 0x07,
  0x04: 0x04,
  0x09: 0x06,
  0x07: 0x00,
  0x00: 0x02,
  0x0c: 0x0b,
  0x0a: 0x09,
  0x08: 0x0d,
  0x0d: 0x03,
  0x01: 0x08,
  0x03: 0x0e,
  0x0f: 0x0f,
  0x06: 0x0a,
  0x05: 0x05,
  0x0e: 0x01,
  0x0b: 0x0c,
}

def encrypt(message: bytearray, key: bytes):
  hashedKey = sha256(key.hex().encode("utf-16")).hexdigest()
  
  keySection1 = sha256(hashedKey[32:].encode("utf-16")) # replace key
  keySection2 = sha256(hashedKey[:32].encode("utf-16")) # mix key

  print(keySection1.hexdigest())

  output = []

  for char in message:
    print(char.to_bytes().hex())

  print()
  print(hex(0x1 + 0xf))

  return "Done"

def decrypt(message, key):
  pass