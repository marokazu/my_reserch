from simulation import Simulation
import random
import numpy as np
from culCij import culcCij
import statistics
import matplotlib.pyplot as plt
import matplotlib.animation as anm
import pandas as pd
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

        # 最大評価の商品を買う
        """
        if now_episode != 0:
            ranv = culcMaxRep()
            buy_pr = product[ranv]
        else:
            while True:
                ranv = random.randint(0, len(product)-1)
                if ranv != self.index:
                    break
            buy_pr = product[ranv]
        """
        # productの中からランダムにデータを選ぶ
        # ただし選んだproductの作成者が自分だった場合は乱数を選び直す
        # """
        while True:
            ranv = random.randint(0, len(product)-1)
            if ranv != self.index:
                break
        buy_pr = product[ranv]
        # """
        # buy_pr = product[0]
        # 選んだproductのbuyerのindexをクラス変数に代入して保存しておく
        self.buy_pr_index = buy_pr["buyer"]
        # print("buyer index : " + str(self.index))
        # print("seller index : " + str(self.buy_pr_index))
        # print(buy_pr)

    def feedback(self):
        # print("feedback called")
        # 買った商品への評価値を決める
        rep = random.randint(0, 100)
        # rep = random.uniform(0, 1)
        # その評価値を自分の信頼値リストに追加する。
        # print(self.si)
        # 攻撃者作成
        """
        if self.index == 1 or self.index == 2 or self.index == 3 or self.index == 4 or self.index == 11 or self.index == 12 or self.index == 13 or self.index == 14 or self.index == 21 or self.index == 22 or self.index == 23 or self.index == 24:
            rep = 0
            self.si[self.buy_pr_index].append(rep)
        else:
            # こっちは攻撃者じゃない
            self.si[self.buy_pr_index].append(rep)
        """
        self.si[self.buy_pr_index].append(rep)
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
                # randseed2 = ["B", "S"]
                self.next_act = random.choice(randseed2)
        elif self.act == "S":
            randseed0 = ["B", "N"]
            # randseed0 = ["B"]
            self.next_act = random.choice(randseed0)
        elif self.act == "N":
            randseed1 = ["B", "S"]
            # randseed1 = ["B"]
            self.next_act = random.choice(randseed1)
        if len(product) == 0:
            self.next_act = "S"
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


# 現時点最高評価を持つagentの決定
def culcMaxRep():
    indexes = []
    reps = []
    for pr in product:
        indexes.append(pr["buyer"])
    # print(indexes)
    for ind in indexes:
        # print(ind)
        # print(Reputations)
        reps.append(Reputationsss[ind])
    maxRep = max(reps)
    return reps.index(maxRep)


# 初期パラメータの定義
# agentのかず
population = 300
# 各エピソード後の評価値を代入する関数
Reputations = []
# a = Simulation()
product = []
# print(len(product))
agents = []
num_episode = 101
now_episode = 0
sij = []
cij = []
# agentの作成
for i in range(population):
    # print("agent making...")
    agent = Agent(i)
    agents.append(agent)
# 評価値算出の時に使用するためのやつ
Reputationsss = []
variances = []
# animation用の配列用意
ims = []
# act格納ようlist
acts = []
# お試しで実際に何ページかシナリオを動かしてみた
for i in range(num_episode):
    print(now_episode)
    for agent in agents:
        agent.choose_act()

    # 計算で扱うために、Sijを正規化して、numpy配列に変換
    cij = culcCij(sij)

    # Reputationの計算をここで行う
    cij_T = cij.T
    # print(cij_T)
    e = 1
    for i in range(10):
        e = np.dot(cij_T, e)
    Rep = []
    for e_atr in e:
        Rep.append(sum(e_atr)/len(e_atr))
    Reputations.append(Rep*population)
    Reputationsss = Rep
    Rep = np.array(Rep)
    if now_episode % 10 == 0:
        # print(Rep*population)
        # print("Rep average : ", str(sum(Rep)/len(Rep)))
        print("Rep average : ", str(statistics.mean(Rep)*population))
        print("Rep max : ", str(max(Rep*population)),
              "   Rep min : ", str(min(Rep*population)))
        print("Rep variance : ", str(statistics.variance(Rep*population)))
        # plt.hist(Rep*population, bins=30)
        # plt.show()
        print()
    variances.append(statistics.variance(Rep*population))
    # matplotでアニメーション化するときの関数
    # im = plt.hist(Rep*population, bins=30)
    # それぞれの参加者がどの行動を行なったかを格納する変数
    act_list = []
    for agent in agents:
        act_list.append(agent.act)
    # plt.hist(act_list)
    # plt.show()
    # 全エージェントの選んだ行動のリスト
    # print(act_list)
    acts.append(act_list)
    now_episode += 1

Reputations = np.array(Reputations)
Reputations = Reputations
# df = pd.DataFrame(Reputations)
# df2 = pd.DataFrame(acts)
# df.T.to_excel("REPS_OUTPUT.xlsx", sheet_name="Reps")
# df2.T.to_excel("ACTS_OUTPUT.xlsx", sheet_name="acts")

#
"""
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


def update(i, Reputation):
    if i != 0:
        # plt.cla()
        ax.cla()
    y = Reputation[i]
    # plt.hist(y, bins=5)
    ax.hist(y, bins=100)
    ax.set_ylim(0, population**2/2/2/2)
    plt.xlabel("Reputation")
    plt.ylabel("Frequency")
    # ax.set_ylim(0, population**2)
    if i == len(Rep):
        plt.close()
    print(i)
"""

# print(Reputations)


# ヒストグラムを出したい時はこれを実行する
# ani = anm.FuncAnimation(fig, update, fargs=(Reputations,), interval=200)
#


# 分散値のグラフを表示するためのプログラム
# """
#
fig2 = plt.figure()

listing = variances
list_x = list(range(len(listing)))
# x = np.linspace(0, 2*np.pi, 201)
# x = np.linspace(1, len(listing), 1)
ims = []
for i in range(len(listing)):
    # y = np.sin(x + float(i)/50.0)
    y = listing[0:i]
    x = list(range(len(y)))
    # im = plt.fill_between(x, y, color="lightblue", alpha=0.5)
    # im = plt.plot(y, color="darkblue")
    plt.xlabel("episode")
    plt.ylabel("variances")
    im = plt.bar(x, y, width=1, color="#effef0", edgecolor='#9ffea0')
    ims.append(im)

ani = anm.ArtistAnimation(fig2, ims, interval=100)
# """
plt.show()  # これを実行するとアニメーションが表示される。
#
