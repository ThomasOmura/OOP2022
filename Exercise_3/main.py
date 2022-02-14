import CellPhone

def main():
    #Inntroduction on what to do
    print("Provide the information about your cell phone. ")

    #get the inputs from the user
    manufact = input("Please enter the manufacturer: ")
    model = input("Please enter the model: ")
    r_price = float(input("Please enter the retail price: "))

    #call the class, no values are assigned to the 
    #functions inside the class
    phone = CellPhone(manufact, model, r_price)

    #all of the information will be displayed
    print("Here's the information you have entered.")
    print("Manufacturer:", phone.get_manufact())
    print("Model:", phone.get_model())
    print("Retail price:", phone.get_r_price())

#needs to be called so the program gets executed
main()