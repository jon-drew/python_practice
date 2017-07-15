longest = ''
current = ''
for x in s:
    if (current == ''):
        current = x
    elif (current[-1] <= x):
        current += x
    elif (current[-1] > x):
        if (len(longest) < len(current)):
            longest = current
            current = x
        else:
            current = x
if (len(current) > len(longest)):
    longest = current

print ('Longest substring in alphabetical order is: ' + longest)