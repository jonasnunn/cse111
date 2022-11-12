# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas)
    draw_clouds(canvas)
    draw_ground(canvas)
    draw_cacti(canvas)
    draw_gold(canvas)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas):
    draw_rectangle(canvas,0,200,800,500,fill="lightblue",outline="lightblue")

def draw_clouds(canvas):
    draw_oval(canvas, 175,375,325,425,outline="white",fill="white")
    draw_oval(canvas, 700,400,275,475,outline="white",fill="white")
    draw_oval(canvas, 50,420,200,450,outline="white",fill="white")
    draw_oval(canvas, 550,320,750,360,outline="white",fill="white")

def draw_ground(canvas):
    draw_rectangle(canvas,0,0,800,200,fill="tan",outline="tan")

def draw_cacti(canvas):
    #first cactus
    draw_rectangle(canvas,100,200,110,235,fill="green",outline="green")
    draw_rectangle(canvas,90,220,125,225,fill="green",outline="green")
    draw_rectangle(canvas,120,225,125,230,fill="green",outline="green")
    #second cactus 
    draw_rectangle(canvas,150,200,160,230,fill="green",outline="green")

    draw_rectangle(canvas,60,200,70,220,fill="green",outline="green")

    draw_rectangle(canvas,200,200,210,225,fill="green",outline="green")

    draw_rectangle(canvas,250,200,260,230,fill="green",outline="green")

    draw_rectangle(canvas,400,200,410,235,fill="green",outline="green")
    draw_rectangle(canvas,390,220,425,225,fill="green",outline="green")
    draw_rectangle(canvas,420,225,425,230,fill="green",outline="green")

    draw_rectangle(canvas,700,200,710,235,fill="green",outline="green")
    draw_rectangle(canvas,690,220,725,225,fill="green",outline="green")
    draw_rectangle(canvas,720,225,725,230,fill="green",outline="green")

    draw_rectangle(canvas,780,200,790,230,fill="green",outline="green")

def draw_gold(canvas):
    start = 0
    end = 10
    for i in range(39):
        start += 20
        end += 20
        draw_rectangle(canvas,start,80,end,85,fill="gold",outline="gold")



# Call the main function so that
# this program will start executing.
main()