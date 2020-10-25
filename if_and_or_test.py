# age =input("나이를 입력하세요"))

#if age<14:
#     print("어린이")
# elif age >=14 and age<20:
#     print("청소년")
# elif age >=20 and age <50:
#     print("청년")
# else:
#     print("노땅!!")

a=int(input("숫자를 입력하세요"))
b=int(input("숫자를 입력하세요"))

if(a%2==0)and(b%2==0):
    print('두 수 모두 짝수입니다')
elif(a%2==0)or(b%2==0):
    print('두 수 중 하나 이상이 짝수입니다')
