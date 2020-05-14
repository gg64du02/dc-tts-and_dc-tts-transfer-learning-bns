import re

try:
   # f = open("test.txt", encoding = 'utf-8')
   f = open("./test/B00FORPEAA_EBOK.txt", encoding = 'utf-8')
   # perform file operations
   strBook = f.read()
   # print("strBook",strBook)
   # {\ql

   # POEMS
   strPoemsTmp1 = strBook.split('{\ql')
   # print("strPoemsTmp1",strPoemsTmp1)
   # for bits in strPoemsTmp1:
   #    print("strPoemsTmp1 bits",bits)
   # strPoemsTmp2 = strBook.split('{\\ql[\WA-Z0-9]*{\\qc')
   strPoemsTmp2 = strBook.split('} {')
   # print("strPoemsTmp2",strPoemsTmp2)
   # for bits in strPoemsTmp2:
   #    print("strPoemsTmp2 bits",bits)
   # print("len(strPoemsTmp1)",len(strPoemsTmp1))
   # print("len(strPoemsTmp2)",len(strPoemsTmp2))

   strPictTmp1 = strBook.split('{\*\shppict')
   # for bits in strPictTmp1:
   #    print("strPictTmp1bits",bits)
   strPictTmp2 = strBook.split('[a - z0 - 9\n]+\n\}\}')

   # strPictTmp3 = re.split("exp",strBook)
   strPictTmp3 = re.split("\}\}",strBook)
   # for bits in strPictTmp3:
   #    print("strPictTmp3 bits",bits)

   # strPictTmp8 = re.split("....shppict[\Wa-z0-9]*}}",strBook)
   strPictTmp8 = re.split("{\\\\\*\\\\shppict[\Wa-z0-9]*}}",strBook)
   # for bits in strPictTmp8:
   #    print("strPictTmp8 bits",bits)
   # print("len(strPictTmp8)",len(strPictTmp8))

   # {\\ql[\WA-Z]*} {.\n{\\qc
   # {\\ql[\WA-Z]*{\\qc
   # {.ql[\WA-Z]*{.qc
   # strPictTmp9 = re.split("{.qc",strBook)
   # strPictTmp9 = re.split("{.ql",strBook)
   # strPictTmp9 = re.split("[A-Z]*} {",strBook)
   # ql[\Wa - zA - Z0 - 9]*{
   # strPictTmp9 = re.split("[a-zA-Z0-9]*{\\\\qc",strBook)
   # strPictTmp9 = re.split("{\\\\ql[a-zA-Z0-9]*{\\\\qc",strBook)
   # ql[\Wa - zA - Z0 - 9]*qc
   # strPictTmp9 = re.split("{\\\\ql",strBook)
   # strPictTmp9 = re.split("{\\\\ql",strBook)

   strPoemsTmp3 = re.split("\\\\qc",strBook)
   # 420 qc
   # strPoemsTmp3 = re.split("ql\n[\ a-zA-Z\\\\\}]*} {*",strBook)
   # strPoemsTmp3 = re.split("\\\\ql",strBook)
   # strPoemsTmp3 = re.split("[\d]*",strBook)
   # strPoemsTmp3 = re.split("{\\\\ql",strBook)
   # strPoemsTmp3 = re.split("{\\\\ql[\n\rA-Za-z\ ]*",strBook)
   # strPoemsTmp3 = re.split("{\\\\ql[\n\rA-Za-z\ \\\\\}]*",strBook)
   # strPoemsTmp3 = re.split("{\\\\ql[\n\rA-Za-z\ \\\\\}\{]*",strBook)
   # strPoemsTmp3 = re.split("{\\\\ql[\n\rA-Za-z\ \\\\\}\{]*\t",strBook)
   # strPoemsTmp3 = re.split("{\\\\ql[\n\rA-Za-z\ \\\\\}\{.,;-]*\t",strBook)
   # strPoemsTmp3 = re.split("{\\\\ql[\n\rA-Za-z0-9\ \\\\\}\{.,;-?]*\t",strBook)
   # strPoemsTmp3 = re.split("{\\\\ql[\n\rA-Za-z0-9\ \\\\\}\{.,;-\?\t]*\t",strBook)
   # strPoemsTmp3 = re.split("{\\\\ql[\n\rA-Za-z0-9\ \\\\\}\{.,;-\?\t]+\t",strBook)
   # strPoemsTmp3 = re.split("{\\\\ql[.*\n\rA-Za-z0-9\ \\\\\}\{]+",strBook)
   # strPoemsTmp3 = re.split("{\\\\ql[.*\n\rA-Za-z0-9\ \\\\\}\{\,\;\-\?]+",strBook)
   # strPoemsTmp3 = re.split("{\\\\ql[.*\n\rA-Za-z0-9\ \\\\\}\{\,\;\-\?\(\)]+",strBook)

   # strPoemsTmp3 = re.split("\n{\\\\qc",strBook)
   strPoemsTmp3 = re.split("{\\\\ql\n.*} {",strBook)
   # for bits in strPoemsTmp3:
   #    print("strPoemsTmp3 bits",bits)
   # print("len(strPoemsTmp3)",len(strPoemsTmp3))


   stru8220Tmp1 = re.split("\\\\u8220.*",strBook)
   # for bits in stru8220Tmp1:
   #    print("stru8220Tmp1 bits",bits)
   # print("len(stru8220Tmp1)",len(stru8220Tmp1))

#
finally:
   f.close()