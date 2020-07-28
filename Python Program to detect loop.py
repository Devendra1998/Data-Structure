#Python  program to detect the loop in the single linked list

#Node Class


class node:
     #Constructer to initiative the node object
      def __init__(self,data):
          self.data=data
          self.next=None

class linkedlist:
     def __init__(self):
         self.head=None

     def push(self,new_data):
         new_data=node(new_data)
         new_Node.next=self.head
         self.head=new_Node

 #utility function to print the linkrd list:

def printlist(self):
     temp=self.head
     while(temp!Null):
         print(temp.data,end=" ")
         temp=temp.next

def detect_loop(self):
 s=set()
 temp=self.head
 while(temp):
    if(temp in s):
        return True
        s.add(temp):
        temp=temp.next
        return False



