#!/usr/bin/env python
# -*- condiong:uft8 -*-

height = 1.65
weight = 65
bmi = weight/height**2
print(bmi)
if bmi < 18.5:
    print('过轻')
elif bmi >= 18.5 and bmi < 25:
    print('正常')
elif bmi >= 25 and bmi < 28:
    print('过重')
elif bmi >= 28 and bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')