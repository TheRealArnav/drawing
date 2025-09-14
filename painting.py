from tkinter import*
from tkinter.colorchooser import askcolor





class Paint():

    def activate(self, button):
        self.buttonactive.config(relief=RAISED)
        button.config(relief = SUNKEN)
        self.buttonactive = button
        if self.buttonactive == self.eraser:
            self.eraseron = True
        else:
            self.eraseron = False

    def penon(self):
        self.activate(self.pen)

    def brushon(self):
        self.activate(self.brush)

    def chosecoloron(self):
        #self.activate(self.color)
        self.color1 = askcolor(color=self.color1)[1]
        print(self.color1)
    def eraser(self):
        self.activate(self.eraser)


    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x600")
        self.pen = Button(self.root, text = "Pen", bg = "white", fg = "Black", command = self.penon)
        self.pen.place(x = 50, y = 50)
        self.brush = Button(self.root, text = "Brush", bg = "white", fg = "black", command = self.brushon)
        self.brush.place(x = 100, y = 50)
        self.color = Button(self.root, text = "Color", bg = "white", fg = "black", command = self.chosecoloron)
        self.color.place(x = 150, y = 50)
        self.eraser = Button(self.root, text = "Eraser", bg = "white", fg = "black", command = self.eraser)
        self.eraser.place(x = 200, y  = 50)
        self.slider = Scale(self.root, from_= 1, to=10, orient= HORIZONTAL)
        self.slider.place(x = 250, y = 50)
        self.canvas = Canvas(self.root, bg = "white", width=500, height=800)
        self.canvas.place(x = 0, y = 100)
        self.setup()
        self.root.mainloop()


    def paint(self,event):
        self.width = self.slider.get()
        if self.eraseron == True:
            self.color = "White"
        else:
            self.color = "Black"
        
        if self.x and self.y != None:
            self.canvas.create_line(self.x,self.y,event.x,event.y,width = self.width, fill= self.color)
         
        self.x = event.x
        self.y = event.y

    def stopdrawing(self,event):
        
        self.x = None
        self.y = None



    def setup(self):
        self.x = None
        self.y = None
        self.width = self.slider.get()
        self.color1 = "Black"
        self.eraseron = False
        self.buttonactive = self.pen
        self.canvas.bind("<B1-Motion>",self.paint)
        self.canvas.bind("<ButtonRelease-1>",self.stopdrawing)



Paint_1 = Paint()
