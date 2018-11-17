from Person import Person
from MyUI import Label

'''
최 상위 코드는 if 블록이고, __name__은 현재 모듈의 이름을 담고있는 내장 변수입니다.
python myscript.py 같이 이 모듈이 직접 실행되는 경우에만
,__name__ 은 "__main__"으로 설정됩니다.
참고, https://dojang.io/mod/page/view.php?id=1072
'''

def person_main():
    maria = Person('마리아', 20, '서울시 서초구 반포동')
    maria.greeting()

def label_main():
    Label(input('입력하세요'))       
    #, input('x 입력'),input('y 입력'))

if __name__ == "__main__":
    # person_main()
    label_main()