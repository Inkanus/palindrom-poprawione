p = "Kajak kajak"
p = p.lower()

def is_palindrome(i):
   if len(i) <= 1:
       return True
   else:
       if i[0] != i[len(i)-1]:
           return False
       else:
           return is_palindrome(i[1:len(i)-1])
print(is_palindrome(p))

