# 부산광역시 지역구들의 생활쓰레기 배출 정보

수학과 | 201411142 | 조문호 


## 프로젝트 개요
본인의 프로젝트 개요에 대하여 작성합니다.

## 사용한 공공데이터 
[데이터보기](https://github.com/cybermin/python2019/blob/master/%EB%B6%80%EC%82%B0%EA%B5%90%ED%86%B5%EA%B3%B5%EC%82%AC_%EB%8F%84%EC%8B%9C%EC%B2%A0%EB%8F%84%EC%97%AD%EC%82%AC%EC%A0%95%EB%B3%B4_20190520.csv)

## 소스
* [링크로 소스 내용 보기](https://github.com/munhooooooo/python2019/blob/master/test.py) 

* 코드 삽입
~~~python
import pandas as pd

def mylist (m) :
    f = open(m + ".txt","r")
    n = f.readlines()
    f.close()
    r = []
    for x in n :
        x = x.replace("\n", "")
        r.append(x)
    return r

if __name__ == "__main__" :
    flag1 = True
    while flag1 :
        print("지역구 목록")
        x = mylist("지역구")
        print(x,"\n")

        a = input("원하는 지역구를 입력하세요")
        print(a)
        if a in x :
            df = pd.read_csv('부산광역시_' + a + '_생활쓰레기배출정보.csv', engine = 'python')
            print("관리구역 수 :", end = " ")
            print(df.shape[0], "\n") #행 갯수
        else :
            print("지역구 입력 오류\n")
            continue

        flag2 = True
        while flag2 :
            print("알고 싶은 정보")
            y = mylist("정보")
            print(y,"\n")

            b = input("알고 싶은 정보를 입력하세요").replace(" ","").split(",")
            for bb in b:
                if bb in y :
                    print(bb)
                    df1 = df[bb]
                    print(df1, "\n")
                else :
                    print("알고 싶은 정보 입력 오류","\n")
                    continue

            c = int(input("1 : 다른 정보, 2 : 지역구 변경, 3 : 종료"))
            if c == 1 :
                 continue
            elif c == 2 :
                flag2 = False
            else :
                flag1 = False
                flag2 = False
~~~
