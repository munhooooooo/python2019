
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

