begin_x = 0
for x in range(5):
	begin_y = (height / 6) * x
	height = height / 6
    win = "win"+str(x)
	win = curses.newwin(height, width, begin_y, begin_x)