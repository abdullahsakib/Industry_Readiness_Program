
try:
    num=int(input("Enter a number"))
    
    if num<0:
        raise ValueError("No Negatives")
    
    print(f"Number is {num}")

except Exception  as e:
    print(f"here error is {e}")