from tkinter import *
from KMeansClustering import *
from tkinter.colorchooser import *
from tkinter.messagebox import *


class ColorAI:
    
    def __init__(self):
        self.__AI = KMeansCluster(3) # this is a 3D cluster (R, G, B)


        self.__window = Tk() # I hate building UI and graphics so this is pretty bare bones
        frame = Frame(self.__window)

        self.__r = Label(frame, text = 'None')
        self.__r.grid(row = 1, column = 1)
        self.__g = Label(frame, text = 'None')
        self.__g.grid(row = 1, column = 2)
        self.__b = Label(frame, text = 'None')
        self.__b.grid(row = 1, column = 3)
        
        self.__mainbutton = Button(frame, text = "Add Observation", command = self.__addObservation)
        self.__mainbutton.grid(row = 2, column = 1)
        self.__colorbutton = Button(frame, text = "Get RGB Values", command = self.__getColor)
        self.__colorbutton.grid(row = 2, column = 2)
        self.__learnbutton = Button(frame, text = "Learn", command = self.__startAI)
        self.__learnbutton.grid(row = 2, column = 3)
        
        frame.pack()
        self.__window.mainloop()
        
    
    def __addObservation(self): # grab (R, G, B) values and create a new observation with them
        location = []
        location.append(int(self.__r["text"]) / 255)
        location.append(int(self.__g["text"]) / 255)
        location.append(int(self.__b["text"]) / 255)
        self.__AI.addObservation(tuple(location))
        for i in range(10):
            location = []
            location.append((int(self.__r["text"]) - random.randint(-20, 20)) / 255)
            location.append((int(self.__g["text"]) - random.randint(-20, 20)) / 255)
            location.append((int(self.__b["text"]) - random.randint(-20, 20)) / 255)
            self.__AI.addObservation(tuple(location))

    def __getColor(self): # uses color picker to make getting initial data points easier
        newcolor = askcolor()
        color = newcolor[0]
        self.__r["text"] = color[0] // 1
        self.__g["text"] = color[1] // 1
        self.__b["text"] = color[2] // 1

    def __startAI(self):
        groups = eval(input("How many groups? "))
        locations = self.__AI.learn(groups) # this is where the magic happens!
        self.__createLabels(locations)
        self.__mainbutton["text"] = "Guess Color"
        self.__mainbutton["command"] = self.__guessColor

    def __createLabels(self, locations): # it was getting late and I didn't want to deal with TKinter anymore so I just had it print the centroid locations to console and prompt
	# I should really update this to using TKinter so it looks nicer
        temp = []
        for location in locations:
            label = input("What color is this? " + str(location[0]*255) + ' '+ str(location[1]*255) + " " + str(location[2]*255) + " ")
            temp.append(label)
        self.__AI.createLabels(temp)
    
    def __guessColor(self): # get new color, prompt AI, and display result!
        location = [0] * 3
        location[0] = int(self.__r["text"]) / 255
        location[1] = int(self.__g["text"]) / 255
        location[2] = int(self.__b["text"]) / 255
        guess = self.__AI.guess(tuple(location))
        showinfo("Guess", "The AI guesses that this color is " + guess)



ColorAI()
