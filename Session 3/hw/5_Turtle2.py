from turtle import *
speed(0)
mau = ['blue', 'yellow', 'red', 'brown', 'grey']
stt = -1
while stt <= 4:
    for i in range (5):
        stt +=1
        color(mau[stt],mau[stt])
        begin_fill()
        for i in range (2):
            forward(50)
            left(90)
            forward(100)
            left(90)
        forward(50)
        end_fill()
    mainloop()