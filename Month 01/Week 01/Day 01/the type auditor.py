
try:
    user_input=input("Enter a numeric value: ")

    print("The type of the input is:", type(user_input))

    float_value=float(user_input)
    print("The type after conversion to float is:", type(float_value))

except ValueError:
    print("Invalid input! Please enter a numeric value.")

