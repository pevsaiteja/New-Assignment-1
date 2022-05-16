e_o=[1,2,3,4,5,6,7,8,9,10]
even,odd = 0,0
for i in e_o:
    if i % 2 :
        even += 1
    else:odd += 1
    print("Even :",even)
    print("Odd :",odd)