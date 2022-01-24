def encodetuple (tupp):
    st = ''
    for i in tupp :
        st += str(hex(i*100))[2:].upper() +"%"
    return st
def decode(st ):
    tup = []
    for i in st.strip().split("%"):
        if i == '' : continue
        i = "0x" + i.lower()
        tup.append(int(int(i,16)/100))
    return tup

print(decode(encodetuple((3,4,5))))
