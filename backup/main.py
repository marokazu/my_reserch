from simulation import Simulation
import numpy as np
from culCij import culcCij
from agentingingClassingSuping import AgentingClassSuper
np.set_printoptions(precision=3)
np.set_printoptions(threshold=np.inf)

population = 10
a = Simulation()
product = []
agents = []
# agentの作成
for i in range(population):
    agent = AgentingClassSuper(i)
    agents.append(agent)

sij = []
cij = []
# agentごとの他者への信頼値を代入する配列をつくる
for agent in agents:
    sij.append([])

for agent in agents:
    agent.sell()

print(product)
for agent in agents:
    agent.buy()

for agent in agents:
    agent.feedback()


print()
print(sij)
sij = np.array(sij)
print(sij)

cij = culcCij(sij)
cij = np.array(cij)
print(cij)
cij_T = cij.T
e = 1
for i in range(10):
    e = np.dot(cij_T, e)

print(e)
