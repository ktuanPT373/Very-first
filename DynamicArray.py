#not my code
import ctypes
class DynamicArray(object):
    def __init__(self):
        self.n = 0 # Count actual elements (Default is 0)
        self.capacity = 1 # Default Capacity
        self.A = self.make_array(self.capacity)
         
    def __len__(self):
      
        return self.n
     
    def __getitem__(self, k):
    
        if not 0 <= k <self.n:
            # Check it k index is in bounds of array
            return IndexError('K is out of bounds !')
         
        return self.A[k] # Retrieve from the array at index k
         
    def append(self, ele):
       
        if self.n == self.capacity:
            # Double capacity if not enough room
            self._resize(2 * self.capacity)
         
        self.A[self.n] = ele # Set self.n index to element
        self.n += 1
 
    def insertAt(self,item,index):
         
        if index<0 or index>self.n:
            print("please enter appropriate index..")
            return
         
        if self.n==self.capacity:
            self._resize(2*self.capacity)
             
         
        for i in range(self.n-1,index-1,-1):
            self.A[i+1]=self.A[i]
             
         
        self.A[index]=item
        self.n+=1
 
 
         
    def delete(self):
      
        if self.n==0:
            print("Array is empty deletion not Possible")
            return
         
        self.A[self.n-1]=0
        self.n-=1
         
         
         
     
    def removeAt(self,index):

        if self.n==0:
            print("Array is empty deletion not Possible")
            return
                 
        if index<0 or index>=self.n:
            return IndexError("Index out of bound....deletion not possible")       
         
        if index==self.n-1:
            self.A[index]=0
            self.n-=1
            return       
         
        for i in range(index,self.n-1):
            self.A[i]=self.A[i+1]           
             
         
        self.A[self.n-1]=0
        self.n-=1
 
         
    def _resize(self, new_cap):
        
         
        B = self.make_array(new_cap) # New bigger array
         
        for k in range(self.n): # Reference all existing values
            B[k] = self.A[k]
             
        self.A = B # Call A the new bigger array
        self.capacity = new_cap # Reset the capacity  
def make_array(self, new_cap):
       
        return (new_cap * ctypes.py_object)()