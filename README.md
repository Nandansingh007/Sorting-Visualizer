# Sorting-Visualizer
#Bubble and Insertion Sorting Visualizer in Python
#Sorting Algorithm Visualizer in Python

1. Implementing Bubble Sort and Merge sort

2. class in the program:
	a. DrawInformatin class:
		-color variable initialization
		-constructor __init__()
				-height,width and list is initialized
		-method self_list()
				-min_value(list)
				-max_value(list)
				-block_width,block_height,starting position of block
        
3. Funtions in the Program
	a. draw()
		-draw the font on the window, set the window background to white
	b. draw_list()
		-draw the random list as the block to the window with the different color
	c. generate_starting_list()
		-randomly generate the list
	d. bubble_sort()
		-bubble sorting algorithm 
	e. insertion_sort()
		-insertion sorting algorithm

	f. main()
		-running the window continuosly until window quitted.
		-sorting_algorithm_generator used 
		-r=pressed, calling generate_starting_list function to reset the list
		-space=pressed, starting the sorting
		-a=pressed, ascending order for sorting, d=pressed, descending order
		-i=pressed, insertion sort
		-b=pressed, bubble sort

