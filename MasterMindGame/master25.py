from graphics import*
from random import*


# Create the graphics board.
def board():
    win=GraphWin('Mastermind',500,900)
    win.setCoords(0,0,500,900)
    win.setBackground('powderblue')

    r=20
    circle1specs=[(55,35,'orange'),(105,35,'red'),(155,35,'blue'),(205,35,'pink'),
                  (255,35,'green'),(305,35,'yellow'),(355,35,'white'),(405,35,'deeppink'),]

    rec1=Rectangle(Point(0,0),Point(500,62))
    rec1.setFill('palegreen')
    rec1.draw(win)

    rec2=Rectangle(Point(0,800),Point(500,900))
    rec2.setFill('orchid')
    rec2.draw(win)
    

    
    circle1=[]
    for (cx1,cy1,color1) in circle1specs:
        circle1s=Circle(Point(cx1,cy1),r)
        circle1s.setFill(color1)
        circle1s.setWidth(3)
        circle1s.draw(win)
        circle1.append(circle1s)



    circle2centers=[(85,90),(160,90),(235,90),(310,90),
                    (85,165),(160,165),(235,165),(310,165),
                    (85,240),(160,240),(235,240),(310,240),
                    (85,315),(160,315),(235,315),(310,315),
                    (85,390),(160,390),(235,390),(310,390),
                    (85,465),(160,465),(235,465),(310,465),
                    (85,540),(160,540),(235,540),(310,540),
                    (85,615),(160,615),(235,615),(310,615),
                    (85,690),(160,690),(235,690),(310,690),
                    (85,765),(160,765),(235,765),(310,765)]

    circle2=[]
    for (cx2,cy2) in circle2centers:
        circle2s=Circle(Point(cx2,cy2),r)
        circle2s.setWidth(3)
        circle2s.draw(win)
        circle2.append(circle2s)


    circle3centers=[(400,90),(420,90),(440,90),(460,90),
                    (400,165),(420,165),(440,165),(460,165),
                    (400,240),(420,240),(440,240),(460,240),
                    (400,315),(420,315),(440,315),(460,315),
                    (400,390),(420,390),(440,390),(460,390),
                    (400,465),(420,465),(440,465),(460,465),
                    (400,540),(420,540),(440,540),(460,540),
                    (400,615),(420,615),(440,615),(460,615),
                    (400,690),(420,690),(440,690),(460,690),
                    (400,765),(420,765),(440,765),(460,765)]
    r3=8
    circle3=[]
    for (cx3,cy3) in circle3centers:
        circle3s=Circle(Point(cx3,cy3),r3)
        circle3s.setWidth(1)
        circle3s.draw(win)
        circle3.append(circle3s)
    return win,r,circle1specs,circle2centers,circle3centers,circle1,circle2,circle3



def process(win,r,circle1specs,circle2centers,circle3centers,circle1,circle2,circle3):

  # Create random colors for the player to guess.
  database=['b','g','r','p','o','y','w','d']
  s=[choice(database) for j in range(4)]
  #print(s)

  # Pre-define the letters to match the correct color and draw correct color balls. 
  anscircles=[]
  bigcirs=[]
  message1s=[]
  for j in range(4):
      
    if s[j]=='b':
        color='blue'
    elif s[j]=='g':
        color='green'
    elif s[j]=='r':
        color='red'
    elif s[j]=='p':
        color='pink'
    elif s[j]=='o':
        color='orange'
    elif s[j]=='y':
        color='yellow'
    elif s[j]=='w':
        color='white'
    elif s[j]=='d':
        color='deeppink'
    anscircle=Circle(Point(85+75*j,850),32)
    anscircle.setFill(color)
    anscircle.setWidth(3)
    anscircle.draw(win)
    anscircles.append(anscircle)
    bigcir=Circle(Point(85+75*j,850),32)
    bigcir.setFill('white')
    bigcir.draw(win)
    bigcirs.append(bigcir)
    message1=Text(Point(85+75*j,850),'?')
    message1.setStyle('bold')
    message1.setSize(35)
    message1.draw(win)
    message1s.append(message1)
                

  cilcle1finallist=[]
  for i in range(10):
  # A loop checks if the input is valid.
    t=input('\nEnter your guess(any 4 letters from o,r,b,p,g,y,w,d): ')
    validinputcheck=(len(t)-4==0)

    for k in range(len(t)):
        validinputcheck=validinputcheck*(t[k] in database)
    while validinputcheck==0:
       if len(t)-4!=0:
         print('Invaild guess! It has to be a length of 4 letters.')
         t=input('\nPlease re-enter your guess again(any 4 letters from o,r,b,p,g,y,w,d): ')
       elif validinputcheck==0:
         print('Invaild guess!Some of what you entered is not letter or not from o,r,b,p,g,y,w,d.')
         t=input('\nPlease re-enter your guess again(any 4 letters from o,r,b,p,g,y,w,d): ')

       validinputcheck=(len(t)-4==0)
       for k in range(len(t)):
         validinputcheck=validinputcheck*(t[k] in database)


    # Create a loop to draw the guess color ball and move them to desired position. 
    cilcle1finals=[]
    for k in range(4):
        for (cx1,cy1,color1) in circle1specs:
            if t[k]==color1[0]:
                circle1final=Circle(Point(cx1,cy1),r)
                circle1final.setFill(color1)
                
                circle1final.draw(win)

                cilcle1finals.append(circle1final)
                cx2,cy2=circle2centers[4*i+k]

                for j in range(4):
                    circle1final.move((cx2-cx1)/4,(cy2-cy1)/4)
                    time.sleep(0.1)
                
    cilcle1finallist.append(cilcle1finals)


    # Find the number of right color in the right place and wrong position.
    lists=list(s)
    listt=list(t)
    listboth=list(set(lists)&set(listt))
    countch=0
    for ch in listboth:
       cns=lists.count(ch)
       cnt=listt.count(ch)
       if cns<=cnt:
          cn=cns
       else:
          cn=cnt
       countch=countch+cn

    to=0
    for j in range(4):
       if s[j]==t[j]:
         to=to+1

    print(to,countch-to)

    # Draw the black and white balls to show the results
    for j in range(countch):
        
        x,y=circle3centers[j+4*i]
        cans=Circle(Point(x,y),8)         
        cans.draw(win)
        if j<=to-1:
            cans.setFill('black')
        else:
            cans.setFill('white')
            
    # Show Congratulations message once the player wins.
    if to==4:
        rec3=Rectangle(Point(50,380),Point(450,520))
        rec3.setFill('palegreen')
        rec3.draw(win)
        print('Congratulations! \^o^/You win the game.')
        message2=Text(Point(250,430),'Congratulations! You win')
        message21=Text(Point(250,480),'(^_^)  (^_^)  (^_^)')
        message2.setFill('red4')
        message21.setFill('red4')
        message2.setSize(25)
        message21.setSize(25)
        message2.draw(win)
        message21.draw(win)

        # Clear the previous balls.
        for c in bigcirs:
                c.undraw()
        for m in message1s:
                m.undraw()

        # Ask for an input to play again. 
        start2=input('\nTry again?(Enter yes to continue the game, anything else or <ENTER> to exit): ')
        if start2=='yes':
           message2.undraw()
           rec3.undraw()
           message21.undraw()

           for (cx2,cy2) in circle2centers:
             circle2s=Circle(Point(cx2,cy2),20)
             circle2s.setWidth(3)
             circle2s.setFill('powderblue')
             circle2s.draw(win)
           for (cx3,cy3) in circle3centers:
             circle3s=Circle(Point(cx3,cy3),8)
             circle3s.setWidth(1)
             circle3s.setFill('powderblue')
             circle3s.draw(win)

             

        check2=start2
        return check2          

    # Shows how many times left to complete the game.
    else:
        print('You have',9-i,'times to play the game.')
        # Shows the player lost the game at the end. 
        if i==9:
            print("\nI'm sorry that you lost the game.")
            rec4=Rectangle(Point(50,400),Point(450,500))
            rec4.setFill('palegreen')
            rec4.draw(win)
            message3=Text(Point(250,450),'Sorry,  you lost the game')
            message3.setFill('red4')
            message3.setSize(20)
            message3.draw(win)

            # Clear the previous balls.
            for c in bigcirs:
                c.undraw()
            for m in message1s:
                m.undraw()

            # Shows the correct colors if the player didn't win.
            print('\nThe correct guess is',s[0]+s[1]+s[2]+s[3],end='.\n')

            # Ask for an input to play again. 
            start3=input('\nTry again?(Enter yes to continue the game, anything else or <ENTER> to exit): ')
            
            if start3=='yes':
               message3.undraw()
               rec4.undraw()
               # Clear the previous balls.
               for (cx2,cy2) in circle2centers:
                   circle2s=Circle(Point(cx2,cy2),20)
                   circle2s.setWidth(3)
                   circle2s.setFill('powderblue')
                   circle2s.draw(win)
               for (cx3,cy3) in circle3centers:
                   circle3s=Circle(Point(cx3,cy3),8)
                   circle3s.setWidth(1)
                   circle3s.setFill('powderblue')
                   circle3s.draw(win)

            check3=start3
            return check3


# Call all the previous functions.
def main():
    
   window,radius,c1specs,c2centers,c3centers,c1,c2,c3=board() 
   tryAgain='yes'
   while tryAgain=='yes':
       print('\nYou have a total of 10 times for each run.')
       print('You will be given black and white balls to show the result everytime you try.')
       print('The black ball represents the right color in the right place.')
       print('The white ball represents the right color in the wrong place.')
       tryAgain=process(window,radius,c1specs,c2centers,c3centers,c1,c2,c3)

main()


