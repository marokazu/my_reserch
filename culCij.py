import numpy as np


# sijを受け取って、cijを計算する
def culcCij(sij):
    # print("culCij called")
    cij = []
    for si in sij:
        si_temp = []
        for s in si:
            s = culGonperz(s)
            si_temp.append(s)
        sumSi = sum(si_temp)
        ci = []
        for i in si_temp:
            ci.append(i/sumSi)
        cij.append(ci)
    cij = np.array(cij)
    return cij


# それぞれのinteractionを計算する関数
def culGonperz(s):
    B = 0.5
    In = 0
    n = len(s)
    i = 0
    # print(s)
    for i in range(n):
        In += (B**(n-i))*(s[n-i-1])
        # print(In)
    return In
