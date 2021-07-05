import hashlib
a= input ("enter a string ")
b= hashlib.sha1(a.encode())
x= b.hexdigest()
print ("1.string into sha1- ",x)
c= hashlib.sha224(a.encode())
y= c.hexdigest()
print ("2.string into sha224- ",y)
d= hashlib.sha256(a.encode())
z= d.hexdigest()
print ("3.string into sha256- ",z)

