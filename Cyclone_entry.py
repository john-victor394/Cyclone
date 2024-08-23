#codex
height = float(input('Enter your height'))
print(height)
credits = float(input('Enter your credits'))
print(credits)

if height > 136.9 and credits > 9.9:
  print('Enjoy the ride')
elif height<137.0 and credits>9.9:
  print ('You are not tall enough')
elif height>136.9 and credits<10.0:
  print ("You don't have credits")
else:
  print ('You have not met the requirement')
