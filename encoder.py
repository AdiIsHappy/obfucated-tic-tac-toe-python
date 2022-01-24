def encodetuple (tupp):
    st = ''
    for i in tupp :
        st += str(hex(i*100))[2:].upper() +"%"
    return (st)
decode = lambda st : tuple([int(int("0x" + i.lower(),16)/100) for i in st.strip().split("%") if i != ""])

winners=((1,7,3,9),(5,),(2,4,6,8))
for i in winners : print(encodetuple(i))
winners = ("64%2BC%12C%384%", "1F4%", "C8%190%258%320%")
for i in winners: print(decode(i))
