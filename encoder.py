def encodetuple (tupp):
    st = ''
    for i in tupp :
        st += str(hex(i*100))[2:].upper() +"%"
    return (st)
decode = lambda st : tuple([int(int("0x" + i.lower(),16)/100) for i in st.strip().split("%") if i != ""])

winners= [1,2,3,4,5,6,7,8,9,10]
print(encodetuple(winners))
winners = ("64%C8%12C%190%1F4%258%2BC%320%384%3E8%")
print(decode(winners))
