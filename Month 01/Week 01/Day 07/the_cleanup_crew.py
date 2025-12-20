
try:
    a=int(input("Enter 1st Number"))
    b=int(input("Enter 2nd Number"))
    res=a/b
    print(f"Result: {res}")
except Exception  as e:
    print(f"here error is {e}")

finally:
    print("Execution Complete")
    