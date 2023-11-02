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

# 6) Insert commas into large numbers
print(f'{1000:,}')      # 1,000
print(f'{10000:,}')     # 10,000
print(f'{100000:,}')    # 100,000
print(f'{1000000:,}')   # 1,000,000

# 7 ) Convert numbers to percventages
print(f'{0.25:.0%}')    # 25%
print(f'{0.5:.1%}')     # 50.0%
print(f'{0.75:.2%}')    # 75.00%
print(f'{1.5:.3%}')     # 150.000%

# 8) Positive and negative numbers
print(f'{4:+}')      # +4
print(f'{-5:+}')     # -5
print(f'{3.14:+}')   # +3.14

#9) Formating datetime
import datetime
today = datetime.datetime.today()
print(f'{today:%B %d, %Y}')    # April 28, 2023

#10) Showing raw output
name = 'rocky'
print(f'my name is {name!r}')
# my name is 'rocky'

#11) Convert Integer to hex
print(f'{9:#0x}')       # 0x9
print(f'{10:#0x}')      # 0xa
print(f'{11:#0x}')      # 0xb
print(f'{12:#0x}')      # 0xc
print(f'{13:#0x}')      # 0xd
print(f'{14:#0x}')      # 0xe
print(f'{15:#0x}')      # 0xf
print(f'{16:#0x}')      # 0x10
print(f'{17:#0x}')      # 0x11
print(f'{100:#0x}')     # 0x64

#12) Rounding numbers
print(f'{3.14159:.3g}')        # 3.14
print(f'{314159:.3g}')         # 3.14e+05
print(f'{0.00314159:.3g}')     # 0.00314

#13) Bonary
print(f'{1:b}')    # 1
print(f'{2:b}')    # 10
print(f'{4:b}')    # 100
print(f'{5:b}')    # 101
print(f'{8:b}')    # 1000
print(f'{9:b}')    # 1001