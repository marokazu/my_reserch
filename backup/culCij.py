import numpy as np


# sijを受け取って、cijを計算する
def culcCij(sij):
    # print("culCij called")
    cij = []
    # print("dsfjscodicvjsdivjdsvjdsovjsdo")
    # print(sij)
    # print("dsfjscodicvjsdivjdsvjdsovjsdo")
    for si in sij:
        si_temp = []
        for s in si:
            # print("----------")
            # print(si)
            # print("----------")
            # print(sij)
            si_temp.append(sum(s)/len(s))
            # print(si_temp)
        sumSi = sum(si_temp)
        ci = []
        for i in si_temp:
            ci.append(i/sumSi)
        #     print(ci)
        # print(len(ci))
        cij.append(ci)
        # print(cij)
    cij = np.array(cij)
    # print(cij)
    return cij
