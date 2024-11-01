
fizznum = 0
boonum = 0


for num in range(1,50):
    if num % 5 == 0:
        fizznum += 1
        print('Fizz')
    if num % 3 == 0:
        boonum += 1
        print('Boo')
# print(f'Number of Fizz' + str(fizznum))
boonresult =  'Toatl Boos ' + str(boonum)
print(boonresult)