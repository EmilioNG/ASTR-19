Date: "10/11/2024"

#start the class
class Penguin:
    
    #define a member function of the class to -rint out desired values
     def print(self):
        print("Favorite animal is Penguin")
        print(f"Length of arms = {self.arm_length}")
        print(f"Length of legs = {self.leg_length}")
        print(f"Number of eyes = {self.eye_num}")
        print(f"Has tail? = {self.has_tail}")
        print(f"Is it furry = {self.has_fur}")
     
    #initialize the class with a function
     def __init__(self,alength=1.0,llength=1.0,enum=1,tail=False,fur=False):
        self.arm_length = alength
        self.leg_length = llength
        self.eye_num = enum
        self.has_tail = tail
        self.has_fur = fur
        
def main():
    #set the values for the length of the arm, legs, number of eyes, tail, and fur
    alength = str(14.96) + " inches"
    llength = str(5.32) + " inches"
    enum = str(2) + " eyes"
    tail = True
    fur = False
    
    #initialize the class
    emperor_penguin = Penguin(alength=alength,llength=llength,enum=enum,tail=tail,fur=fur)
    
    #print the values using the class
    emperor_penguin.print()
    
#initialize the program
if __name__=="__main__":
    main()