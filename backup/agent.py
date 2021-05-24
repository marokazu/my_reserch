from simulation import Simulation
import random
import numpy as np
from culCij import culcCij
np.set_printoptions(precision=3)
np.set_printoptions(threshold=np.inf)


class Agent:
    def __init__(self, index):
        self.index = index  # agentのsimulation内での番号
        self.act = "N"  # agentが選んでいる行動、デフォルトはN
        self.next_act = None  # agentの次の行動
        self.makeSi()  # agentの他者に対する評価(信頼)
        # 選んだproductのbuyerのindex
        self.buy_pr_index = None  # buyを行ったagentが次に評価するユーザのindexを一時的に保持するための関数

    def makeSi(self):
        self.si = []
        # 最初にagentの数だけlist内に信頼値listを用意しておく
        # print("makeSi called")
        # agentが他者に対して持つ信頼値のデフォルト値は0.72
        for i in range(population):
            self.si.append([0.72])
        sij.append(self.si)

    def buy(self):
        # print("buy called")
        # productの中からランダムにデータを選ぶ
        # ただし選んだproductの作成者が自分だった場合は乱数を選び直す
        while True:
            ranv = random.randint(0, len(product)-1)
            if ranv != self.index:
                break
        buy_pr = product[ranv]
        # 選んだproductのbuyerのindexをクラス変数に代入して保存しておく
        self.buy_pr_index = buy_pr["buyer"]
        # print("buyer index : " + str(self.index))
        # print("seller index : " + str(self.buy_pr_index))
        # print(buy_pr)

    def feedback(self):
        # print("feedback called")
        # 買った商品への評価値を決める
        rep = random.randint(0, 100)
        # その評価値を自分の信頼値リストに追加する。
        # print(self.si)
        self.si[self.buy_pr_index].append(rep)
        # print(self.si)
        # 評価値を一つ追加したら、cijの自分の部分を更新する
        # s_temp = []
        # print("-----------------------------------")
        # print(self.si)
        # 以下のfor文は使わない
        # for s in self.si:
        #     s_temp.append(sum(s)/len(s))

        # 変更したsiをCijに追加する
        sij[self.index] = self.si

    def sell(self):
        # print("sell called")
        # ローカルに作成した商品データを格納する変数を用意
        pr = {}
        # productのbuyerキーにはbuyerのindexを代入
        pr["buyer"] = self.index
        # categoryを4つ用意して、どれか一つ選ぶ
        pr["category"] = random.randint(1, 4)
        # グローバルのproductに追加(掲載)
        product.append(pr)

    def no_act(self):
        # print("no_act called")
        a = 1

        # 次の行動を選ぶ関数
    def choose_act(self):
        # print("choose_act called")
        if self.act == "B":
            self.next_act = "F"
        elif self.act == "F":
            if now_episode < 4:
                self.next_act = "S"
            else:
                randseed2 = ["B", "N", "S"]
                self.next_act = random.choice(randseed2)
        elif self.act == "S":
            randseed0 = ["B", "N"]
            self.next_act = random.choice(randseed0)
        elif self.act == "N":
            randseed1 = ["B", "S"]
            self.next_act = random.choice(randseed1)
        if len(product) == 0:
            self.act = "S"
        # print(self.next_act)
        self.next_act_call()

    # 次の行動を行う関数
    def next_act_call(self):
        # print("next_act_call called")
        if self.next_act == "B":
            self.buy()
            self.act = "B"
        elif self.next_act == "F":
            self.feedback()
            self.act = "F"
        elif self.next_act == "S":
            self.sell()
            self.act = "S"
        elif self.next_act == "N":
            self.no_act()
            self.act = "N"


# 初期パラメータの定義
population = 500
# a = Simulation()
product = []
# print(len(product))
agents = []
num_episode = 51
now_episode = 0
sij = []
cij = []
# agentの作成
for i in range(population):
    # print("agent making...")
    agent = Agent(i)
    agents.append(agent)
# print(agents)
# print("syoki sij")
# print(sij)

# agentごとの他者への信頼値を代入する配列をつくる
# for agent in agents:
#     sij.append([])

# お試しで実際に何ページかシナリオを動かしてみた
for i in range(num_episode):
    print(now_episode)
    for agent in agents:
        agent.choose_act()
    # sij = np.array(sij)
    # print("---------------Sij---------------")
    # print()
    # print(sij)
    # print()

    # 計算で扱うために、Sijを正規化して、numpy配列に変換
    cij = culcCij(sij)
    # cij = np.array(cij)
    # print("---------------Cij---------------")
    # print()
    # print(cij)
    # print()

    # Reputationの計算をここで行う
    cij_T = cij.T
    # print(cij_T)
    e = 1
    for i in range(6):
        e = np.dot(cij_T, e)
    Rep = []
    for e_atr in e:
        Rep.append(sum(e_atr)/len(e_atr))
    Rep = np.array(Rep)
    if now_episode % 10 == 0:
        print(Rep*population)
        print("Rep average : ", str(sum(Rep)/len(Rep)))
        print("Rep max : ", str(max(Rep*population)),
              "   Rep min : ", str(min(Rep*population)))

    now_episode += 1


###
# for agent in agents:
#     agent.sell()

# # print(product)

# for i in range(100):
#     for agent in agents:
#         agent.buy()
#         agent.feedback()


# # print()
# # print(sij)
# sij = np.array(sij)
# print("---------------Sij---------------")
# # print()
# # print(sij)
# # print()

# # 計算で扱うために、Sijを正規化して、numpy配列に変換
# cij = culcCij(sij)
# cij = np.array(cij)
# print("---------------Cij---------------")
# # print()
# # print(cij)
# # print()

# # Reputationの計算をここで行う
# cij_T = cij.T
# e = 1
# for i in range(6):
#     e = np.dot(cij_T, e)

# print("---------------Reputation---------------")
# # print()
# # print(e)
###

# print(product)
