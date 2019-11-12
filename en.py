import marshal,base64
a=input("[?] File: ")
b=input("[?] Out : ")
c=open(a,"r").read()
d=base64.b64encode(bytes(c,"utf-8"))
e=compile(d,"<billal>","exec")
f=marshal.dumps(e)
g="""
# Encoding Type: utf-8
# OBFUSCATED : Billal Fauzan
# OBFUSCATE type : Dragon OBF
# Origin : enc.py
# copyright 2019 BILLAL FAUZAN
#================================
# Time  : Tue Nov 12 18:29:07 2019\n"""
open(b,"w").write(g+"import marshal,base64\nexec(marshal.loads(base64.b64decode(%s)))"%(repr(f)))
