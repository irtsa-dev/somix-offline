#Imports
from variables import productsFolder, ingredientsFolder
from variables import ThemeColors
from variables import GridSizes
from variables import currentRecipe


from tkinter import Button, Label
from PIL import Image, ImageTk


from random import randint






#Functions
def resetMixResult(Window) -> None:
    breaks = []   
    for i in range(len(Window.winfo_children())):
        if Window.winfo_children()[i]._name in ['mvtext', 'mvvalue', 'eftext', 'efvalue', 'mvefspace1', 'mvefspace2']: breaks.append(i)
    breaks = breaks[::-1]
    for i in breaks: Window.winfo_children()[i].destroy()

    if currentRecipe.base != '':
        Label(master = Window, name = 'mvefspace1', text = '', pady = 4).pack()
        Label(master = Window, name = 'mvtext', text = f'Market Value', background = ThemeColors['bg'], foreground = '#646464', font = ('Century Gothic', 12)).pack()
        Label(master = Window, name = 'mvvalue', text = currentRecipe.price, background = ThemeColors['bg'], foreground = '#64B464', font = ('Century Gothic', 12)).pack()
        Label(master = Window, name = 'mvefspace2', text = '', pady = 1).pack()
        Label(master = Window, name = 'eftext', text = f'Effects', background = ThemeColors['bg'], foreground = '#646464', font = ('Century Gothic', 12)).pack()
        Label(master = Window, name = 'efvalue', text = ' | '.join(currentRecipe.effects), background = ThemeColors['bg'], foreground = '#949494', font = ('Century Gothic', 12), wraplength = Window.winfo_width()).pack()



def clearRecipeDisplay(frame) -> list:
    buttons = frame.winfo_children()[:]
    for child in frame.winfo_children(): child.destroy()
    frame.pack()
    return buttons



def rebuildRecipeDisplay(Window, frames: list, labels: list, buttons: list) -> None:
    for i in range(len(buttons)):
        button = Button(frames[2], image = buttons[i].image, border = 0, activebackground = ThemeColors['selbut'], command = lambda i=i: detectButton(Window, frames, labels, 2, i), name = buttons[i]._name)
        button.image = buttons[i].image
        button.grid(row = i // GridSizes[1], column = i % GridSizes[1])



def createPhoto(folder, name: str) -> ImageTk.PhotoImage:
    photo = Image.open(f'{folder}/{name.replace(' ','').lower()}.png')
    photo = photo.resize((64, 64))
    return ImageTk.PhotoImage(photo)



def detectButton(Window, frames: list, labels: list, fid: int, index: int) -> None:
    frame_products, frame_ingredients, frame_recipe = frames
    label_error = labels[0]

    if fid == 0: frame = frame_products
    elif fid == 1: frame = frame_ingredients
    else: frame = frame_recipe
    

    button = frame.winfo_children()[index]
    action, classification, item, uid = button._name.split(' | ')

    if classification == 'base':
        if action == 'add':
            label_error.pack_forget()
            currentRecipe.base = item
            buttons = clearRecipeDisplay(frame_recipe)

            photo = createPhoto(productsFolder, item)
            buttons.insert(0, Button(frame_recipe, image = photo, border = 0, activebackground = ThemeColors['selbut'], name = f'remove | base | {item} | {randint(1111111111,9999999999)}'))
            buttons[0].image = photo
            if len(buttons) > 1:
                if buttons[1]._name.split(' | ')[1] == 'base': buttons.pop(1)
            rebuildRecipeDisplay(Window, frames, labels, buttons)
        
        else:
            currentRecipe.base = ''
            label_error.pack(side = 'bottom')
            rebuildRecipeDisplay(Window, frames, labels, clearRecipeDisplay(frame_recipe)[1:])
    
    else:
        if action == 'add':
            if len(currentRecipe.ingredients) < 15:
                currentRecipe.ingredients.append(item)
                buttons = clearRecipeDisplay(frame_recipe)

                photo = createPhoto(ingredientsFolder, item)
                buttons.append(Button(frame_recipe, image = photo, border = 0, activebackground = ThemeColors['selbut'], name = f'remove | ingredient | {item} | {randint(1111111111,9999999999)}'))
                buttons[-1].image = photo
                rebuildRecipeDisplay(Window, frames, labels, buttons)
        
        else:
            if currentRecipe.base == '': currentRecipe.ingredients.pop(index)
            else: currentRecipe.ingredients.pop(index - 1)

            buttons = clearRecipeDisplay(frame_recipe)
            buttons.pop(index)
            rebuildRecipeDisplay(Window, frames, labels, buttons)
    resetMixResult(Window)