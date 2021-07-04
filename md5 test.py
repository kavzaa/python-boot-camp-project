import hashlib
x= input ("enter the text")

def main():
    a = x.encode("utf-8")
    hash = hashlib.md5(a)
    b= hash.hexdigest()
    print (b)
    return
main()

    
