import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

listing = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_x = list(range(20))
print(list_x)
# x = np.linspace(0, 2*np.pi, 201)
x = np.linspace(1, len(listing), 1)
ims = []
for i in range(len(listing)):
    # y = np.sin(x + float(i)/50.0)
    y = listing[0:i]
    x = list_x[i]
    im = plt.plot(y)
    ims.append(im)

ani = animation.ArtistAnimation(fig, ims, interval=50)

plt.show()  # これを実行するとアニメーションが表示される。
