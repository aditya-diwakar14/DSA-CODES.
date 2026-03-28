def fact (n):
    if n == 0 :
        return 1
    elif n<0:
        return None
    else : 
        return n * fact(n-1)
num = int (input("Choose a num"))        
print(f"THE FACTORIAL OF GIVEN NUMBER IS : {fact}")

