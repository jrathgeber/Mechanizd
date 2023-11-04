''' a normal if-elif-else block'''

score = 57
if score > 90:
  grade = 'A*'
elif score > 50:
  grade = 'pass'
else:
  grade = 'fail'

# grade = 'pass'

'''Using the ternary operator'''

score = 57
grade = 'A*' if score>90 else 'pass' if score>50 else 'fail'

# grade = 'pass'
print(grade)