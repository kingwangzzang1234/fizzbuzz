def fizzbuzz(num):
    for i in range(1,num+1):
        if i%3==0:
            print('fizz')
        else:
            print(i)

if __name__=='__main__':
    user_num = int(input('Type number: '))
    fizzbuzz(user_num)
