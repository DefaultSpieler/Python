test_h = int(input("Height of walls: "))
test_w = int(input("Width of walls : "))
coverage = 5

def paint_calc(height, width, cover):
	no_of_cans = (height * width) / cover 
	print(round(no_of_cans))


paint_calc(height = test_h, width = test_w,  cover = coverage)