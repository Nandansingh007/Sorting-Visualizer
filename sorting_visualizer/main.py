import pygame
import random
import math

pygame.init()

class DrawInformation:
    BLACK=0,0,0
    WHITE=255,255,255
    GREEN=0,255,0
    RED=255,0,0
    BACKGROUND_COLOR=WHITE

    #grey gradients

    GRADIENTS = [
        (128,128,128),
        (160,160,160),
        (192,192,192)
    ]

    #font in the window
    FONT = pygame.font.SysFont('comicsans', 20)
    LARGE_FONT = pygame.font.SysFont('comicsans', 25)

    SIDE_PAD=100
    TOP_PAD=150

    def __init__(self,width,height,lst):
        self.width=width
        self.height=height

        #creating a window in a pygame
        self.window=pygame.display.set_mode((width,height))

        #setting up caption
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        
        self.set_list(lst)

    def set_list(self,lst):
        self.lst=lst
        self.min_value=min(lst)
        self.max_value=max(lst)

        self.block_width = round((self.width-self.SIDE_PAD) / len(lst))
        self.block_height = math.floor((self.height-self.TOP_PAD)/(self.max_value-self.min_value))
        
        self.start_x = self.SIDE_PAD // 2

#function to draw window, font 
def draw(draw_info, algo_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    title = draw_info.LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Desending'} ", 1 , draw_info.GREEN)
    draw_info.window.blit(title, (draw_info.width/2 - title.get_width()/2, 5))

    controls = draw_info.FONT.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Desending ", 1 , draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2, 45))

    sorting = draw_info.FONT.render("I - Insertion Sort | B - Bubble Sort ", 1 , draw_info.BLACK)
    draw_info.window.blit(sorting, (draw_info.width/2 - sorting.get_width()/2, 75))

    draw_list(draw_info)
    pygame.display.update()

#function to draw the list on the window
def draw_list(draw_info, color_position={}, clear_bg = False):
    lst=draw_info.lst

    if clear_bg:
        clear_rect=(draw_info.SIDE_PAD//2, draw_info.TOP_PAD,
                     draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    for i,val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y= draw_info.height - (val - draw_info.min_value)  * draw_info.block_height

        color = draw_info.GRADIENTS[i % 3]

        if i in color_position:
            color = color_position[i]

        pygame.draw.rect(draw_info.window , color, (x , y, draw_info.block_width, draw_info.height ) )

    if clear_bg:
        pygame.display.update()



#function to generate random list
def generate_starting_list(n, min_value, max_value):
    lst = []

    for _ in range(n):
        val = random.randint(min_value , max_value)
        lst.append(val)

    return lst

#bubble sort function
def bubble_sort(draw_info,ascending=True):
    lst = draw_info.lst

    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            num1 = lst[j]
            num2 = lst[j+1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j] , lst[j+1] = lst[j+1] , lst[j]
                draw_list(draw_info,{j: draw_info.GREEN, j+1: draw_info.RED}, True)
                yield True                  #generator calling the function each time for sorting

    return lst

#insertion sort function
def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(1, len(lst)):
        current = lst[i]

        while True:
            ascending_sort = i > 0 and lst[i-1] > current and ascending
            descending_sort = i > 0 and lst[i-1] < current and  not ascending

            if not ascending_sort and not descending_sort:
                break

            lst[i] = lst[i-1]
            i = i-1
            lst[i]=current
            draw_list(draw_info, {i-1: draw_info.GREEN, i: draw_info.RED}, True)
            yield True                          #get control back to main function to operate under the keypress

    return lst

        
#main function
def main():
    run =True
    clock=pygame.time.Clock()

    #variable declared and defined
    n = 50
    min_value=0
    max_value=100
    sorting = False
    ascending = True

    sorting_algorithm = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algorithm_generator = None

    lst = generate_starting_list(n, min_value, max_value)

    draw_info = DrawInformation(800, 600, lst)

    while run:
        clock.tick(40)

        #condition for the sorting using generator
        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, sorting_algo_name, ascending)

        for event in pygame.event.get():

            #for responding to the close button
            if event.type == pygame.QUIT:
                run = False
            
            if event.type != pygame.KEYDOWN:
                continue

            #generate random list by clicking r button
            if event.key == pygame.K_r:

                lst = generate_starting_list(n, min_value, max_value)
                draw_info.set_list(lst)
                sorting = False

            #starting the sorting when space is pressed 
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info,ascending)

            #when a=pressed then ascending sorting
            elif event.key == pygame.K_a and not sorting:
                ascending = True

            #When d=pressed, descending sort 
            elif event.key == pygame.K_d and not sorting:
                ascending = False

            #when i=pressed, then insertion sorting
            elif event.key == pygame.K_i and not sorting:
                sorting_algorithm = insertion_sort
                sorting_algo_name = "Insertion Sorting"

            #when b=pressed, then bubble sorting
            elif event.key == pygame.K_b and not sorting:
                sorting_algorithm = bubble_sort
                sorting_algo_name = "Bubble Sorting"

    pygame.quit()

if __name__ == "__main__":
    main()
