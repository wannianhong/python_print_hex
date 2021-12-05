def print_hex(bytes):
    cycle=len(bytes)//16
    
    for i in range(cycle):
        lhex=""
        lascii=""
        for y in range(16):
            lhex += '{:x}'.format(int(bytes[i*16+y])) 
            lhex+=" "
            if chr(bytes[i*16+y]).isascii():
                lascii += chr(bytes[i*16+y])
            else:
                lascii+="."

        print(lhex+lascii)

       
    
    n=len(bytes)%16 
    lhex=""
    lascii=""
    for i in range(n):
        lhex += '{:x}'.format(int(bytes[cycle*16+i])) 
        lhex+=" "
        if chr(bytes[cycle*16+i]).isascii():
                lascii += chr(bytes[cycle*16+i])
        else:
                lascii+="."
    print("%-47s %s" % (lhex, lascii))


    


ta="1234567890abcdefghijklmn"
ta+="中国"
print_hex(ta.encode())
