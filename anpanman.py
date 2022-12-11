from turtle import *

count = 0 #アホ
def anpanman(loop, radius):
    #一度だけ実行
    global count
    if(count == 0):
        penup()
        goto(-radius,0)
        right(90)
        pendown()
        circle(radius)
        count = 1

    if(loop == 0):
        #スキップ
        penup()
        left(90)
        forward(radius*2)
        right(90)
        pendown()

    else:
        for i in range(3):
            circle(radius/3)
            anpanman(loop-1, radius/3)
            #目を描く
            if(i != 2):
                penup()
                backward(radius/2)
                right(90)
                forward(radius/6)
                left(90)
                pendown()

                begin_fill()
                circle(radius/6)
                end_fill()

                penup()
                left(90)
                forward(radius/6)
                right(90)
                forward(radius/2)
                pendown()

        #口を描く
        penup()
        right(90)
        forward(radius*4/3)
        left(90)
        forward(radius*5/12)
        pendown()

        begin_fill()
        circle(radius/3, 180)
        end_fill()

        penup()
        forward(radius*5/12)
        right(90)
        forward(radius*2/3)
        right(90)
        pendown()

setup(1040,1040,1500,330)   #ウィンドウ大きさ、位置
pensize(3)                  #ペンの太さ
speed(0)                    #書く速さ　0が最速
anpanman(5,500)
penup()
goto(0,0)
exitonclick()