#-*- encoding:utf-8 -*-



m = int(input("총 건수 : "))

n = int(input("한 페이지에 보여줄 건 수 : "))



result = 1 if m < n else (m/n +1 if m%float(n) > 0 else m/n)

print("출력 값 : %d" %result)