# challenge 1.1 To Implement a recursive function to calculate the factorial of a given number

def fact_rec(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fact_rec(n - 1)


number = 6
res = fact_rec(number)
n=int(input("Enter the number"))
print("The Factorial of {} is {}".format(number,res))
