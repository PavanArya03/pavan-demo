'''Is the number 10 even and prime'''
def is_even(number):
   return number %2==0
number=4
if is_even(number):
   print("the number is even")
else:
   print("the number is odd")