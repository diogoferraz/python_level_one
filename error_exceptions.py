# Handle Erros and exceptions
try:
  input = input('What do you want to do read/write(r/w):')
  f = open('testfile.txt', 'w')
  if (input == 'w'):
    f.write('Test write this')
  else:
    print(f.read())

except:
  print('Error: Could not find file or read data')

else:
  print('Content written successfully')
  f.close()

finally:
  print('I always work no matter what')


