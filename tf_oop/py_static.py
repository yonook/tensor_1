class MyStatic:
    def reset(self): # 파이썬 메소드 선언, 언제나 static
        self.x = 0
        self.y = 0

# 인스턴스 메소드
#a =  MyStatic()
#a.reset()

# 클래스 메소드
a =  MyStatic() 
MyStatic.reset(a)

print("x : ",a.x," y : ",a.y)