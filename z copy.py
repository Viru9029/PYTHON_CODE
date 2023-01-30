try:
  a = 10 / 0
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
    print('final')