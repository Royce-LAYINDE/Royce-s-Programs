import turtle
t1=turtle.Turtle()
def application():
    v=int(input("Tape 1 pour un carré, 2 pour un triangle équilatéral"))
    if v==1:
        def carre(x,c):
            a=0
            t1.color(c)
            while a<4:
                t1.fd(35)
                t1.left(90)
                a=a+1
            carre(35,"yellow")
    elif v==2:
        def triangle(x,c):
            t1.color(c)
            for i in range(3):
                t1.fd(35)
                t1.left(120)
            triangle(35,"green")
    
   
    
    
        
    
        
        
        
    
 

    
         
        

    
        
         
        
