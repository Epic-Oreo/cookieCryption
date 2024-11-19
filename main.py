from cookieCrypt import encrypt, decrypt

def main():
  s = "hello world!"

  key = "mrKey"

  m = encrypt(bytearray(s, "utf-16"), bytes(key, "utf-16"))
  print(m)



if __name__ == "__main__":
  main()