class Person:
    # 인스턴스 변수가 있으면 init은 필수로 만들어야돼
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def greeting(self):
        print("안녕하세요 저는 {0} 입니다. {1}에 삽니다.".format(self.name, self.address))