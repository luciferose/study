from tkinter import *
import tkinter.messagebox
import model

cell_size=7
is_running=False

def option_handler(event):
    global is_running, start_button, choice
    is_running = False
    start_button.configure(text='start')
    selection = choice.get()
    if selection == 'random':
        model.randomsize(model.grid_model, model.width, model.height)
    elif selection == 'Chose a Pattern':
        clear_handler(event)

    update()

def start_handler(event):
    global is_running, start_button
    if is_running:
        is_running = False
        start_button.configure(text='start')
    else:
        is_running = True
        start_button.configure(text='pause')
        update()

def clear_handler(event):
    global clear_button, grid_view, is_running
    if is_running == False:
        grid_view.delete(ALL)
        for i in range(0, model.height):
            for j in range(0, model.width):
                if model.grid_model[i][j] == 1:
                    model.grid_model[i][j] = 0
    else:
        tkinter.messagebox.askokcancel('the game of life','please click pause')

def grid_handler(event):
    global grid_view, cell_size
    x = int(event.x / cell_size-1)
    y = int(event.y / cell_size-1)
    if model.grid_model[x][y] == 1:
        model.grid_model[x][y] = 0
        draw_cell(x, y, 'white')
    else:
        model.grid_model[x][y] = 1
        draw_cell(x, y, 'black')

def setup():
    global root, grid_view, cell_size, start_button, clear_button, choice
    root = Tk()
    root.title('the game of life')
    grid_view = Canvas(root, width=model.width * cell_size, height=model.height*cell_size, bg='white', bd=1, relief='sunken')
    start_button = Button(root, text = 'start', width = 12)
    start_button.bind('<Button-1>',start_handler)
    clear_button = Button(root, text = 'clear', width = 12)
    clear_button.bind('<Button-1>', clear_handler)
    choice = StringVar(root)
    choice.set('Choose a Pattern')
    option = OptionMenu(root, choice, 'Chose a Pattern', 'random',command=option_handler)
    option.config(width = 20)
    grid_view.grid(row = 0, columnspan = 3, padx = 20, pady = 20)
    grid_view.bind('<Button-1>', grid_handler)
    start_button.grid(row = 1, column=0, sticky=W, padx=20, pady=20)
    clear_button.grid(row = 1, column=2, sticky=E, padx=20, pady=20)
    option.grid(row = 1, column=1, padx=20)

def update():
    global grid_view, root, is_running
    grid_view.delete(ALL)
    model.next_gen()
    for i in range(0,model.height):
        for j in range(0,model.width):
            if model.grid_model[i][j] == 1:
                draw_cell(i, j, 'black')
    if is_running:
        root.after(1000,update)

def draw_cell(x, y, color):
    global grid_view, cell_size

    if color == 'black':
        outline = 'grey'
    else:
        outline = 'white'
    grid_view.create_rectangle(x*cell_size+4, y*cell_size+4, x*cell_size+cell_size+4, y*cell_size+cell_size+4, fill=color, outline=outline)

if __name__ == '__main__':
    setup()
    update()
    mainloop()