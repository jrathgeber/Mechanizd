name = 'lala'
age = 5

# 1) my name is lala and my age is 5
print(f'my name is {name} and my age is {age}')

# 2) name='lala' age=5
print(f'{name=} {age=}')

pi = 3.14159
e = 2.71828

# 3) 3.14 2.7183
print(f'{pi:.2f} {e:.4f}')

# 4) Align
x = 'hi'
print(f'>{x:<20}<')      # >hi                  <
print(f'>{x:^20}<')      # >         hi         <
print(f'>{x:>20}<')      # >                  hi<

# 5)
x = 'hi'

print(f'>{x:-<20}<')      # >hi------------------<
print(f'>{x:=^20}<')      # >=========hi=========<
print(f'>{x:x>20}<')      # >xxxxxxxxxxxxxxxxxxhi<