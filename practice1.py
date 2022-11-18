def all_positives(x):
  sum = ""
  for i in x:
      if i < 0:
        sum = "False"
        break
      else:
        sum = "True"
  return sum