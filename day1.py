# class student:
    # self can hold refrence of current object of current class
    # x=20
    # y=30
    
    # def __init__(self):
    #     # print("This is from constructor")
#         print(id(self))
        
#     def display():
#         print("this is for display")
        
# obj=student
# print(obj.x)
# print(id(obj))
# obj2=student()
# print(id(obj2))           

class student:
    def __init__(self,x):
        print("hii")
    def __init__(self,x,y):
        print("hello") 
        
    def __init__(self,x,y,z):
        print("abhishek")
        
obj=student(15,25,35)               