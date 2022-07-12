
print('Q1')
홍길동 = {'국어':80,'영어':75,'수학':55}
print((홍길동['국어']+ 홍길동['수학']+홍길동['영어'])/3)

print('\nQ2')
a=10
if a%2==0:
    print('짝수입니다.')
else:
    print('홀수입니다.')

print('\nQ3')
a='881120-1068234' #7번째 - 인덱스 6
print('연월일은 %s이고 뒤의 숫자는 %s이다.'%(a[:6],a[7:]))

print('\nQ4')
pin = "881120-1068234"
print(pin[7])
if int(pin[7])==1:
    print('주민등록상 남성입니다.')
else:    
    print('주민등록상 여성입니다.')

print('\nQ5')
a = "a:b:c:d"
print(a.replace(':','#'))

print('\nQ6')
a=[1, 3, 5, 4, 2] 
a.sort()
a.reverse()
print(a)

print('\nQ7')
a=['Life', 'is', 'too', 'short']
b= str(a[0])+' '+str(a[1])+' '+str(a[2])+' '+str(a[3])
print(' '.join(a)) #정답
print(b)

print('\nQ8')
a=(1,2,3)

print(a+(4,))

print('\nQ9')
print('2번: key값에 튜플이 있음.\n3번:key값에 리스트가 있음.\n') #오답 2번은 튜플이 가능하다. 변수가 아니어야해서 리스트만제외

print('Q10')
a = {'A':90, 'B':80, 'C':70}
print(a.pop('B')) #딕셔너리도 pop가능

print('\nQ11')
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
print(list(set(a)))

print('\nQ12')

print('[1, 4, 3]'+'\n이유는 a와 b모두 같은 주소를 가르키기 때문에 a값이 변하면 b값도 같이 변한다. ')