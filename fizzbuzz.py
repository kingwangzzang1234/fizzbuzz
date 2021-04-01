def fizzbuzz():
    user_num = int(input('Type number: '))
    for i in range(1,user_num+1):
        if i%3==0:
            print('fizz')
        else:
            print(i)

if __name__=='__main__':
    fizzbuzz()
