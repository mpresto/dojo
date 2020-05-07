# 1. BASIC - Print all integers from 0 to 150
for i in range(151):
    print(i)

# 2. MULTIPLES OF FIVE - Print all multiples of 5 from 5 to 1,000
for i in range(0, 1001, 5):
    print(i)

# 3. COUNTING, THE DOJO WAY
for i in range(101):
    if i % 10 == 0:
        print("Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# 4. WHOA, THAT SUCKER'S HUGE
sum = 0
for i in range(1, 500001, 2):
    sum = sum + i
print(sum)

# 5. COUNTDOWN BY FOURS
for i in range(2018, 0, -4):
    print(i)

# 6. FLEXIBLE COUNTER
lownum = 2
highnum = 9
mult = 3

for i in range(lownum, highnum+1):
    if i % mult == 0:
        print(i)