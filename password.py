import random as ran
str1=""
n=int(input("Enter the length of password : "))
for i in range(0,n,2):
  c=ran.choice(list("abcdefghijklmnopqrstuvwx@#$%^&*€£¥1234567890yzABCDEFGHIJKLMNOPQRSTUVWXYZ"))
  str1+=c
  if i!=n-1:
    b=ran.choice(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#$&€£*¥1234567890"))
    str1+=b
print("Your password is: ",str1)    
