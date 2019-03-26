
x = input()
y = input()
a = 1
b = int(x)//2

c = 1
d = int(x)-2

a1 = 1
b1 = int(x)//2

#

c1 = 1
d1 = int(x)-2

for i in range(0, int(x) ):
   if (i <= int (int(x)//2 )):


      print("  "* b, end="")

      if (a< int(y) * 2 ):
         print(" *" * a, end="")
      else:
         print(" *" * int(y), end="")
         print("  " * int (a - int(y) * 2), end="")
         print(" *" * int(y), end="")
      a = a +2
      b = b - 1

      print()

   if (i > int (int(x)//2 )):


      print("  "* c, end="")
      if (d < int(y) * 2):
          print(" *" * d, end="")
      else:
          print(" *" * int(y), end="")
          print("  " * int(d - int(y) * 2), end="")
          print(" *" * int(y), end="")


      d = d - 2
      c= c + 1

      print()

for j in range(0, int(x) ):
   if (j <= int (int(x)//2 )):


      print("  "* b1, end="")
      if (a1 < int(y) * 2):
          print(" ?" * a1, end="")
      else:
          print(" ?" * int(y), end="")
          print("  " * int(a1 - int(y) * 2), end="")
          print(" ?" * int(y), end="")

      a1 = a1+2
      b1 = b1 - 1

      print()

   if (j > int (int(x)//2 )):


      print("  "* c1, end="")
      if (d1 < int(y) * 2):
          print(" ?" * d1, end="")
      else:
          print(" ?" * int(y), end="")
          print("  " * int(d1 - int(y) * 2), end="")
          print(" ?" * int(y), end="")

      d1 = d1 - 2
      c1= c1 + 1

      print()
