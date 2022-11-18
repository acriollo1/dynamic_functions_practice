from practice1 import all_positives 

########################################################################################################################
# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.

x = [1,2,3,-4]
print(all_positives(x))

########################################################################################################################
# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list (stored in the variable numbers) as long as they are greater than 0 and less than 1000, and returns the result of said sum.

def sum_less():
  sum = 0
  while True 
  x = list(input("List of numbers:"))
    for i in x:
      if i < 0 or i > 1000:
        sum += i
    return sum

print(sum_less())

########################################################################################################################
# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.
