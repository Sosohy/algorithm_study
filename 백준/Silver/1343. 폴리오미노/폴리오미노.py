s = input()

s = s.replace('XXXX', 'AAAA')
s = s.replace('XX', 'BB')

if 'X' in s:
    s = -1

print(s)
