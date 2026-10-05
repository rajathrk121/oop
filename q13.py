class temp():
    def __init__(self):
        self.temperature=int(input("Enter temperture to convert from celsius to farenheit: "))

    def temp_conv(self):
        con_temp=(self.temperature*(9/5))+32

        print("Temperature in farenheit is : ",con_temp)

temp1=temp()
temp1.temp_conv()

