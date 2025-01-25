# noqa

import math

from manim import *
 
class Proof_of_cosine_law(Scene): 
    koordinat = Axes(
            x_range=[-6,6,1],
            y_range=[-6,6,1],
            x_length=12,
            y_length=12,
            axis_config={
            "include_tip":False}
        )
        
    def construct(self):
        self.introduction()
        vc = self.shape()
        self.scaleCamera(vc)
        self.text(vc)

        
        
    def introduction(self):
        text = Tex("Pembuktian Aturan Cosinus").set_color_by_gradient(BLUE,YELLOW)
        self.play(Write(text))
        self.wait()
        self.play(FadeOut(text))
        text1 = [Tex(r"sebelumnya anda harus memahami bahwa $\sin$ dan $\cos$ dapat didefinisikan sebagai $x = \cos(\theta) \ y = \sin(\theta)$").scale(0.8)]
        self.play(Write(text1[0]))
        self.play(FadeOut(text1[0]))
        
        
    def shape(self):
        flexdot = Dot(self.koordinat.c2p(3,math.sqrt(7)))
        dot1 = Dot(self.koordinat.c2p(2,0))
        dataLine = [always_redraw(lambda: Line(self.koordinat.c2p(0,0),flexdot)),
                    always_redraw(lambda: Line(self.koordinat.c2p(0,0), self.koordinat.c2p(2,0))),
                    always_redraw(lambda: Line(self.koordinat.c2p(2,0),flexdot))
                    ]
        circle1 = Circle(radius=2,color=YELLOW).move_to(self.koordinat.coords_to_point(0,0))
        circle2 = circle1.copy()
        polygon = always_redraw(lambda: VGroup(
            dataLine[0],dataLine[1],dataLine[2]
            ))
        sudut = always_redraw(lambda: Angle(
            dataLine[1],
            dataLine[0],
            radius=1, color=BLUE
        ))
        data = [self.koordinat,flexdot,polygon,sudut,circle1,circle2,dot1]
        data_label = [Tex("$c$").next_to(dataLine[0],LEFT,buff=-1),
                      Tex("$a$").next_to(dataLine[1],DOWN),
                      Tex("$b$").next_to(dataLine[2],RIGHT,buff=-0.1),
                      MathTex("A (", r" c \cdot \cos(\theta) ", ",", r" c \cdot \sin(\theta)", ")").next_to(flexdot,UP,buff=-0.2).scale(0.5),
                      MathTex(r"C(",r"a",",",r"0",")").next_to(dot1,DOWN,buff=0.2).scale(0.5),
                      Tex(r"$\theta$").shift([0.6,0.2,0])]
        for i in data:
            self.play(Write(i))
            if i == circle2:
                self.play(circle2.animate.scale(2))
                
        def update_arc(dot,alpha):
            x,y = 3,math.sqrt(7)
            fAngle = math.atan2(y,x)
            angle = fAngle+ TAU * alpha
            x = 4*math.cos(angle)
            y = 4*math.sin(angle)
            dot.move_to(self.koordinat.c2p(x,y))
            
        self.play(UpdateFromAlphaFunc(flexdot,update_arc),run_time=2) 
        self.play(*[Write(i) for i in data_label])
        return VGroup(flexdot,circle1,circle2,
                      polygon,sudut,*[i for i in data_label],self.koordinat,dot1)
    
    def scaleCamera(self, bangun:VGroup):
        self.play(bangun.animate.scale(1.2).shift(LEFT*6+ DOWN*3))
        self.wait()
    
    def text(self, grub:VGroup):
        data_constan = [Tex(r"b =jarak titik A dan titik C, oleh karena itu $b = D(A,C)$").shift([0,3,0]).scale(0.8),
                        MathTex("D = \sqrt{(", "x_2", "-", "x_1", ")^2 + (" , "y_2", " -", " y_1", ")^2}").shift([2,2,0]),
                        MathTex("D = \sqrt{(",r" c \cdot \cos(\theta) ","- ","a",r")^2","+ (",  r" c \cdot \sin(\theta)","-","0",r")^2}").shift([2,2,0])]
        self.play(Write(data_constan[0]),Write(data_constan[1]))
        """[x_2,y_2, 0->4,1->5,
            x_1,y_1, 2_>6 ... +4
            X_2,y_2,
            x_1,y_1]
        """
        self.play(Transform(data_constan[1],data_constan[2]))
        data_change = [grub[8][1],grub[8][3],
                       grub[9][1],grub[9][3],
                       data_constan[2][1],data_constan[2][6],
                       data_constan[2][3],data_constan[2][8]]
        for i in range(4):
            self.play(Transform(data_change[i],data_change[i+4]),data_change[i+4].animate.set_color(BLUE))
        self.wait()  
        self.play(FadeOut(grub))  
        self.play(data_constan[2].animate.shift(LEFT*2), FadeOut(data_constan[1]))
        self.wait(2)
        data_equation = [
            MathTex(r"D = \sqrt{(",r" c \cdot \cos(\theta) ","- ","a",r")^2","+ (",  r" c \cdot \sin(\theta)","-","0",r")^2}"),
            MathTex(r"D = \sqrt{",r" c^2 \cos^2(\theta)", r"+ a^2 -",r"2ac\cos(\theta)) + ", r"c^2 \sin(\theta)^2}"),
            MathTex(r"D = \sqrt{",r" c^2 \cos^2(\theta) + c^2 \sin(\theta)^2",r" + a^2 - 2ac\cos(\theta))}"),
            MathTex(r"D = \sqrt{",r"c^2",r" + a^2 - 2ac\cos(\theta))}"),
            MathTex(r"D^2 =",r"c^2",r" + a^2 - 2ac\cos(\theta)"),
            MathTex(r"b^2 =",r"c^2",r" + a^2 - 2ac\cos(\theta)")
        ]
        cek = MathTex(r"\sin^2(\theta) + \cos^2 (\theta) = 1")
        for i in range(len(data_equation)):
            if i != 5:
                self.play(Transform(data_constan[2],data_equation[i+1].shift([2,2,0] + 2*LEFT)))
                if i == 2:
                    self.play(Create(SurroundingRectangle(data_equation[2][1],color=BLUE)))
                    self.play(FadeOut(cek))
                if i == 1:
                    self.play(Write(cek))z
                self.wait(1.5)
        self.wait()