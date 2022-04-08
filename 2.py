from tkinter import*
root=Tk()

root.title("Fibonacci")
root.geometry("400x200")

root.mainloop()
label_series=Label(root, text="Fibonacci Series:  ")
label_flower = Label(root)
label_spiral = Label(root)

def Fibonacci():
num =  10
first_no = 0
second_no  = 1
sum = 0
counter = 1

while (counter <= num):
label_series["text"] += str(sum) + " "
counter =  counter + 1
first no = second_no
second_no = sum
sum-first no + second no
label_flower["text"] = "Flower if fully bloomed"
label_spiral["text"] = "Spirals in right direction are " +
str(first_no) + "and spirals in left direction are" + str(second_no) +
"/n. Total spiral are " + str(sum)

btn = Button(root, text="Show Fibonacci Series", command=Fibbonacci)
btn.pack()
label.series.pack()
label_flower.pack()
label_spiral.pack()

root.mainloop()
 



