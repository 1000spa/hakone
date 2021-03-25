a = input("16진수로 변환할 수를 입력하세요. : ")

def hex(a):
     num = []
     while a != 0:
          char = "0123456789abcdef"
          num.append(char[a%16])
          a = a//16
     num.reverse()
     for i in num:
          print(i,end='')

hex(a)
