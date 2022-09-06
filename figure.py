import matplotlib.figure
fig = matplotlib.figure.Figure()
ax = fig.subplots()
ax.plot([1, 2, 1])
fig.savefig('myImage.png')