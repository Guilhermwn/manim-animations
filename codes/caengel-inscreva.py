from manim import *

config.background_color = ManimColor('#00ff00')
RED = ManimColor('#FF0000')

class subscribe(Scene):
    def construct(self):
        
        # FIRST DECLARATIONS
        circ = Circle(radius=1.5)
        circ.set_stroke(width=20)
        yt = SVGMobject('icons8-youtube.svg', fill_color=WHITE).scale(0.7)
        
        # FIRST ANIMATION
        self.play(Create(circ), run_time=0.6)
        self.play(circ.animate.set_fill(RED, 1), run_time=0.5)
        self.play(circ.animate.set_sheen(-0.3, DR), run_time=1.2)
        self.play(Write(yt), run_time=0.7)
        self.play(
            Rotate(yt, PI*2), 
            rate_func=rate_functions.ease_in_out_back
        )
        
        # GROUPING
        circle_g = VGroup(circ, yt)

        # GROUP ANIMATION
        self.play(
            circle_g.animate.shift(LEFT*5), 
            rate_func=rate_functions.ease_in_out_back
        )

        # SECOND DECLARATION
        text_holder = Rectangle(width=0.5, color=WHITE, fill_opacity=1)
        text_holder.move_to(LEFT*5, aligned_edge=LEFT)
        text_holder.z_index=-1
        text_subs = Text('INSCREVA-SE NO CANAL', color=BLACK, font='JetBrains Mono')
        text_subs.shift(RIGHT)

        # SECOND ANIMATION
        self.add(text_holder)
        self.play(
            text_holder.animate.stretch_to_fit_width(12).shift(RIGHT*5),
            run_time=0.8, 
            rate_func=rate_functions.ease_out_bounce
        )
        self.play(AddTextLetterByLetter(text_subs))
        
        # FIRST STOP
        self.wait(2.5)

        # THIRD DECLARATION
        bell = SVGMobject('icons8-bell.svg', fill_color=WHITE)
        bell.shift(LEFT*5)
        text_bell = Text('ATIVE O SININHO', color=BLACK, font='JetBrains Mono')
        text_bell.shift(RIGHT)

        # THIRD ANIMATION
        self.play(RemoveTextLetterByLetter(text_subs))
        self.play(Unwrite(yt))
        self.play(Write(bell))
        self.play(
            LaggedStart(
                Wiggle(bell, rotation_angle=0.05 * TAU, run_time=2.5),
                AddTextLetterByLetter(text_bell),
                lag_ratio=0.30
        ))
        self.play(Wiggle(bell, rotation_angle=0.05 * TAU, run_time=2))
        
        # SECOND STOP
        self.wait(2)
        
        # REGROUPING 
        circle_g = VGroup(circ, bell)

        # FINISHING ANIMATION
        self.play(RemoveTextLetterByLetter(text_bell))
        self.play(text_holder.animate.stretch_to_fit_width(0.5).shift(LEFT*5))
        self.remove(text_holder)
        self.play(circle_g.animate.shift(RIGHT*5), rate_func=rate_functions.ease_in_out_back)
        self.play(ShrinkToCenter(circle_g))
        
        # LAST SECONDS
        self.wait(2)

class test_shrink(Scene):
    def construct(self):
        # Definindo o retângulo inicial com largura w=2 e altura h=1
        rect = Rectangle(width=2, height=1)
        rect.set_fill(BLUE, opacity=0.5)

        # Posicionar o retângulo com o lado esquerdo no ponto (0, 0)
        rect.to_edge(LEFT, buff=0)
        rect.shift(RIGHT * 1)  # Desloca o retângulo para que o lado esquerdo esteja na origem (0, 0)

        self.add(rect)

        # Animar o retângulo para aumentar a largura para w=10, mantendo o lado esquerdo fixo
        self.play(rect.animate.stretch_to_fit_width(10).shift(RIGHT * 4))

        # Pausa para visualização do retângulo aumentado
        self.wait(1)

        # Animar o retângulo para retornar à largura inicial w=2, mantendo o lado esquerdo fixo
        self.play(rect.animate.stretch_to_fit_width(2).shift(LEFT * 4))

        # Pausa para visualização do retângulo retornado ao tamanho original
        self.wait(1)
