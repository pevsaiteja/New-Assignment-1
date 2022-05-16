fibonaci= int(input("Enter the fiboanci series range"))
f=0
fb_val= 0
fb1_val= 1
while(f<fibonaci):
    if(f<=1):
        Next=f
    else:
        Next=fb_val+fb1_val
        fb_val=fb1_val
        fb1_val=Next
    print(Next)
    f=f+1