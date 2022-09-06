from matplotlib import pyplot
import math
x=0
y=0
pyplot.plot([1, 2, 3, 6], [1, 4, 9, 36])
pyplot.show()
pyplot.plot(x, y, 'bo')
pyplot.plot(x, y, color = 'green', linestyle = 'dashed', linewidth = 2, marker = 'o', markerfacecolor = 'blue', markersize = 5)
pyplot.plot(x, y, label = 'A')
pyplot.plot(x, y, 'r+', y, y, 'bo')


pyplot.plot([1, 3, 2, 3], [4, 8, 5, 4], linestyle = 'none', marker = 'o', c = 'lime',
  markersize = 10)
pyplot.xlim(0, 4)
pyplot.ylim(0, 10)
pyplot.title('Avec des points seulement')


val = [math.log(i + 1) for i in range(100)]
labels = ['lab' + str(i) for i in range(100)]
tickLabels = [labels[i] for i in range(100) if (i % 10) == 0]
pyplot.plot(val, linestyle = 'none', marker = '+')
pyplot.gca().get_xaxis().set_ticklabels(tickLabels, fontsize = 8, rotation = 90)
pyplot.gca().get_xaxis().set_ticks([i for i in range(len(val)) if i % 10 == 0])


x = range(10); y1 = range(10)
y2 = [x ** 2 for x in range(10)]
pyplot.fill_between(x, y1, y2, color = 'yellow')