#%%---- 
##================================ Q4
print('------------- Q4 ')
score = int(input("점수를 입력하세요"))
if score>=90:
    print("장학생",end='')
elif score>=60:
    print("합격", end='')
else:
    print("불합격",end='')
print("입니다. ^^")
print('------------------------------------')

##================================ Q5
print('------------- Q5 ')
num = 5
if num%2 == 0:
    res = '짝수'
else:
    res = '홀수'
print(res)

res = '짝수'if num %2 == 0 else '홀수'
print('(3) : ', res)
print('------------------------------------')

##================================ Q6
print('------------- Q6 ')
nn = [100, 200, 300, 400, 500]
nn[1] = 777
print('(1) ', nn)
nn[1] = [444, 555]
print('(2) ', nn)
nn[1:4] = [444,555]
print('(3) ', nn)
nn[2:] = []
print('(4) ', nn)
print('------------------------------------')

##================================ Q9
print('------------- Q9 ')

hap = 0
for i in range(3333, 10000, 1):

    if i % 1234 != 0:
        continue

    print(i, hap)
    if hap > 100000:
        print("i ", hap )
        break
    hap += i 

print(' final :', hap)

print('------------------------------------')

##================================ Q8
print('------------- Q8 ')

hap = 0
n   = 1234
while n < 4568:

    n += 1

    if n < 1234:
        continue

    if n %444 == 0:
        print(n)
        hap += n

print(hap)

print('------------------------------------')
##================================ Q14
print('------------- Q14 ')

myData = [[n*m for n in range(1,3) ] for m in range(2,4)]
print(" result : [[2, 4], [3, 6]]")
print('--> code out:', myData)

print('------------------------------------')
##================================ Q5
print('------------- Q5 ')

nn = [100, 200, 300, 400, 500]
print('(1) ', nn[4])
print('(2) ', nn[-1])
print('(3) ', nn[-2])
print('(4) ', nn[1:4])
print('(5) ', nn[0:1])
print('(6) ', nn[2:-1])
print('(7) ', nn[0::2])
print('(8) ', nn[::-1])
print('(9) ', nn[::-2])

print('------------------------------------')
