#Imports
from variables import ThemeColors, GridSizes
from variables import productsFolder, ingredientsFolder

from functions import detectButton, createPhoto

from mixer import Ingredients, Bases


from tkinter.ttk import Frame
from tkinter import Button, Label
from random import randint


import tkinter as GUI






#Main Window Function
def WindowMain() -> GUI.Tk:
    Window = GUI.Tk()
    Window.title('SOMIX')
    Window.geometry(f'800x550')
    Window.iconbitmap('assets/images/icon/logo.ico')

    return Window





#Display Window Function
def WindowDisplay(Window: GUI.Tk) -> None:
    def placeButton(frame: Frame, fid: int, name: str, photo, gridSize: int, index: int) -> None:
        button = Button(frame, image = photo, border = 0, activebackground = ThemeColors['selbut'], command = lambda: detectButton(Window, [frame_products, frame_ingredients, frame_recipe], [label_error], fid, index), name = name)
        button.image = photo
        button.grid(row = index // gridSize, column = index % gridSize)
        


    frame_productsLabel = Frame(master = Window, relief = 'sunken')
    frame_products = Frame(master = Window, relief = 'sunken')
    frame_ingredientsLabel = Frame(master = Window, relief = 'sunken')
    frame_ingredients = Frame(master = Window, relief = 'sunken')
    frame_recipe = Frame(master = Window, relief = 'sunken')
    frame_recipeLabel = Frame(master = Window, relief = 'sunken')

    frame_productsLabel.pack()
    frame_products.pack()
    frame_ingredientsLabel.pack()
    frame_ingredients.pack()
    frame_recipe.pack()
    frame_recipeLabel.pack(before = frame_recipe)



    Label(master = frame_productsLabel, text = 'Products', anchor = 'center', height = 1, font = ('Century Gothic', 25)).pack()
    Label(master = frame_ingredientsLabel, text = '', pady = 15).pack()
    Label(master = frame_ingredientsLabel, text = 'Ingredients', anchor = 'center', height = 1, font = ('Century Gothic', 25)).pack()
    for i in range(len(Bases)): placeButton(frame_products, 0, f'add | base | {list(Bases.keys())[i]} | {randint(1111111111,9999999999)}', createPhoto(productsFolder, list(Bases.keys())[i]), GridSizes[0], i)
    for i in range(len(Ingredients)): placeButton(frame_ingredients, 1, f'add | ingredient | {list(Ingredients.keys())[i]} | {randint(1111111111,9999999999)}', createPhoto(ingredientsFolder, list(Ingredients.keys())[i]), GridSizes[1], i)


    Label(master = frame_recipeLabel, text = '', pady = 30).pack()
    Label(master = frame_recipeLabel, text = 'Recipe', anchor = 'center', height = 1, font = ('Century Gothic', 20)).pack()



    label_error = Label(master = Window, text = 'No Product has been selected.', background = ThemeColors['bg'], foreground = '#B46464', font = ('Century Gothic', 12))
    label_error.pack(side = 'bottom')