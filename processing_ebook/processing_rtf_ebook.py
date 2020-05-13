import re

try:
   # f = open("test.txt", encoding = 'utf-8')
   f = open("./test/B00FORPEAA_EBOK.txt", encoding = 'utf-8')
   # perform file operations
   strBook = f.read()
   print("strBook",strBook)
   # {\ql

   # POEMS
   strPoemsTmp = strBook.split('{\ql')
   # print("strPoemsTmp",strPoemsTmp)
   # for bits in strPoemsTmp:
   #    print("bits",bits)

   strPictTmp1 = strBook.split('{\*\shppict')
   # for bits in strPictTmp1:
   #    print("strPictTmp1bits",bits)
   strPictTmp2 = strBook.split('[a - z0 - 9\n]+\n\}\}')

   # strPictTmp3 = re.split("exp",strBook)
   strPictTmp3 = re.split("\}\}",strBook)
   # for bits in strPictTmp3:
   #    print("strPictTmp3 bits",bits)

   strPictTmp8 = re.split("....shppict[\Wa-z0-9]*}}",strBook)
   for bits in strPictTmp8:
      print("strPictTmp8 bits",bits)
   print("len(strPictTmp8)",len(strPictTmp8))
#
finally:
   f.close()