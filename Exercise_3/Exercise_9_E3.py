#Filename: E3_9.py 
#Author: Thomás Rizzi Omura
#Description: Cellphone class for inputing different attributes.


class CellPhone:
    
    def __init__(self,manufact,model,r_price):
        self.manufact = manufact
        self.model = model
        self.r_price = r_price

    #self and manufact need to be included otherwise won't
    #come here from main
    def set_manufact(self,manufact):
        #takes the user_inp from main and assigns it here
        self.manufact = manufact

    #self and model both ned to be included otherwise won't work
    def set_model(self,model):
        self.model = model 

    def set_r_price(self, r_price):
        self.r_price = r_price
    
    #this gets the value that has been assigned to the self. function
    def get_manufact(self):
        #returns the value from earlier
        return self.manufact
    
    def get_model(self):
        return self.model

    def get_r_price(self):
        return self.r_price

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