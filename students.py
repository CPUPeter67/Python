class CSStudent:
 
    # Class Variable
    stream = 'cse'            
 
    # The init method or constructor
    def __init__(self, roll):
   
        # Instance Variable   
        self.roll = roll    

    def setAddress(self, address):
        self.address = address
     
    # Retrieves instance variable   
    def getAddress(self):   
        return self.address  
 
# Driver Code
add = CSStudent(101)
add.setAddress("Pune, Maharashtra")
print(add.getAddress())  
  
# Objects of CSStudent class
a = CSStudent(101)
b = CSStudent(102)
  
print(a.stream)  # prints "cse"
print(b.stream)  # prints "cse"
print(a.roll)    # prints 101
  
# Class variables can be accessed using class
# name also
print(CSStudent.stream) # prints "cse"  