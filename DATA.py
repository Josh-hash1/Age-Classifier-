def Hash(age):    
    if age < 0:
        print("Invalid age! Please enter a non-negative value.")
    
    elif age <= 12:
        print("You are a Child.")
    elif age <= 19:
        print("You are a Teen.")
    elif age <= 64:
        print("You are an Adult.")
    elif age <= 100:
        print("You are a Senior.")
    else:
        print("You are Decomposing.")


print("Age Classifier")

while True:
    try:        
        josh = input("State your Age: ")        
        Hash(int(josh))
    except ValueError:
        print("Please Enter a Valid Age Value.")
        break
