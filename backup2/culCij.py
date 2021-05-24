import numpy as np
import math


# sijを受け取って、cijを計算する
def culcCij(sij):
    # print("culCij called")
    cij2 = []
    for si in sij:
        si_temp = []
        for s in si:
            """
            # この時点でsはlist
            s = culGonperz(s)
            # 戻り値がfloatの変数
            s = culTrust(s)
            si_temp.append(s)
            # """
            si_temp.append(sum(s)/len(s))
        sumSi = sum(si_temp)
        # print(si_temp)
        ci = []

        for i in si_temp:
            ci.append(i/sumSi)
        cij2.append(ci)
        # print(cij2)
        # cij2 = si_temp
    # print(cij2)
    cij2 = np.array(cij2)
    return cij2


# それぞれのinteractionを計算する関数
def culGonperz(s):
    B = 0.5  # Bの値は動的に変わる必要がある。
    In = 0
    n = len(s)
    i = 0
    # print(s)
    for i in range(n):
        In += (B**(n-i))*(s[n-i-1])
        # print(In)
    return In


def culTrust(s):
    a = 1
    b = 0.5
    c = 0.5
    s = a*math.e**(-b*math.e**(-c*s))

    return s
