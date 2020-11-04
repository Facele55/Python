# python program to print initials of a name 
def fullname(str1):
   # split the string into a list 
   lst = str1.split()
   newspace = ""
   # traverse in the list 
   for i in range(len(lst)-1):
      str1 = lst[i]
   # adds the capital first character 
      newspace += (str1[0].upper()+'. ')
   # l[-1] gives last item of list l.
      newspace += lst[-1].title()
   return newspace 

str1=input("Enter Full Name ->")
print("Short Form of Name Is ->",fullname(str1))
