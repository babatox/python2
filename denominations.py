def no_notes(a):
   Q =[ 2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
   x =0
   for i in range(7):
      q =Q[i]
      x= a // q
      print("notes of", q, ":", x)
      a = a % q
amount = int(input("Enter the amount: "))
no_notes (amount)

   
   
   