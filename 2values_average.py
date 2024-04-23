# Video created and uploaded in my youtube channel
# my channel: https://www.youtube.com/@guilhermwn
# video: https://youtu.be/iQdJdXA3EDg?si=i835D40JhjXHS5xP
from manim import *

class CodeTutorial(Scene):
    
    def construct(self):
        font_jetbrains = 'JetBrains Mono'
        
        # INTRODUÇÃO 
        text1 = Text("Hello World com", font=font_jetbrains)
        text2 = Text("Guilhermwn", font=font_jetbrains)
        text2.next_to(text1, DOWN)
        t_group1 = VGroup(text1, text2)
        # INTRODUÇÃO 

        # ANIMAÇÃO DA INTRODUÇÃO 
        self.wait(1.5)
        self.play(Write(t_group1)) 
        self.wait(2)
        self.play(Unwrite(t_group1))
        self.wait(1.5)
        # ANIMAÇÃO DA INTRODUÇÃO 

        # QUESTÃO 
        quest = Text("1º) Faça um programa para calcular a média\naritmética entre duas notas de um aluno.\nApresente o resultado com duas casas decimais.", width=12)
        quest.to_edge(UP)
        # QUESTÃO 

        # ANIMAÇÃO DA QUESTÃO 
        self.play(Write(quest))
        self.wait(2.5)
        self.play(FadeOut(quest))
        # ANIMAÇÃO DA QUESTÃO

        # EXPLICAÇÃO PRIMEIRA PARTE
        exp1 = Text("Temos que criar variaveis que\nvão receber as notas dos alunos")  
        exp1.to_edge(UP)

        code_1 = """nota1 = 5
nota2 = 7

print(nota1)
"""

        show_code1 = Code(
            code=code_1, 
            tab_width=4, 
            background="rectangle",
            language="Python", 
            font=font_jetbrains,
            insert_line_no=False
        )
        # EXPLICAÇÃO PRIMEIRA PARTE

        # ANIMAÇÃO EXPLICAÇÃO PRIMEIRA PARTE
        self.wait(1)
        self.play(Write(exp1))
        self.wait(1.5)
        self.play(
            Create(show_code1[0]),
            Create(show_code1[1]),
            Create(show_code1[2][0]))
        self.play(Create(show_code1[2][1]))
        self.play(FadeOut(exp1))
        # ANIMAÇÃO EXPLICAÇÃO PRIMEIRA PARTE

        # EXPLICAÇÃO SEGUNDA PARTE
        exp2 = Text("Quando usamos o comando print() nas\nvariáveis, será exibido seu valor")
        exp2.to_edge(UP)

        console_code = """5"""
        show_console = Code(
            code=console_code, 
            tab_width=4, 
            background="rectangle",
            language="Python", 
            font=font_jetbrains,
            insert_line_no=False
        )
        

        show_console.next_to(show_code1, DOWN)
        # EXPLICAÇÃO SEGUNDA PARTE

        # ANIMAÇÃO EXPLICAÇÃO SEGUNDA PARTE
        self.play(Write(exp2))
        self.wait(1)
        self.play(Create(show_code1[2][3]))
        self.play(Create(show_console))
        self.wait(1)


        self.play(
            FadeOut(show_code1[2][3]),
            FadeOut(show_console)
        )

        code_2 = """nota1 = 5
nota2 = 7

print(nota2)
"""
        show_code2 = Code(
            code=code_2, 
            tab_width=4, 
            background="rectangle",
            language="Python", 
            font=font_jetbrains,
            insert_line_no=False
        )
        console_code = """7"""
        show_console = Code(
            code=console_code, 
            tab_width=4, 
            background="rectangle",
            language="Python", 
            font=font_jetbrains,
            insert_line_no=False
        )
        show_console.next_to(show_code2, DOWN)
        self.play(Create(show_code2[2][3]))
        self.play(Create(show_console))
        self.wait(1)
        self.play(
            FadeOut(show_console),
            FadeOut(show_code1),
            FadeOut(show_code2),
            FadeOut(exp2))
        self.wait(2)
        # ANIMAÇÃO EXPLICAÇÃO SEGUNDA PARTE

        # EXPLICAÇÃO TERCEIRA PARTE
        exp3 = Text("Após declarar as variáveis, temos que\nrealizar a operação de média")
        exp3_1 = Text("Criamos uma variável\nque fará a operação")

        exp3.to_edge(UP)
        exp3_1.to_edge(UP)

        code_3 = """nota1 = 5
nota2 = 7

media = nota1 + nota2 / 2
"""
        show_code3 = Code(
            code=code_3, 
            tab_width=4, 
            background="rectangle",
            language="Python", 
            font=font_jetbrains,
            insert_line_no=False
        )

        exp3_2 = Text("Temos que lembrar a ordem\nde prioridade dos termos da operação")
        exp3_2.to_edge(UP)

        code_4 = """nota1 = 5
nota2 = 7

media = (nota1 + nota2) / 2
"""
        show_code4 = Code(
            code=code_4, 
            tab_width=4, 
            background="rectangle",
            language="Python", 
            font=font_jetbrains,
            insert_line_no=False
        )
        # EXPLICAÇÃO TERCEIRA PARTE

        # ANIMAÇÃO EXPLICAÇÃO TERCEIRA PARTE
        self.play(Write(exp3))
        self.play(
            Create(show_code3[0]),
            Create(show_code3[1]),
            Create(show_code3[2][0]),
            Create(show_code3[2][1])
        )
        self.wait(1)
        self.play(FadeOut(exp3))
        self.play(Write(exp3_1))
        self.wait(0.5)
        self.play(Create(show_code3[2][3]))
        self.wait(1)
        self.play(FadeOut(exp3_1))
        self.play(Write(exp3_2))
        self.play(
            FadeOut(show_code3[2][3]),
            ReplacementTransform(show_code3[0],show_code4[0]),
            ReplacementTransform(show_code3[1],show_code4[1]),
            ReplacementTransform(show_code3[2][0],show_code4[2][0]),
            ReplacementTransform(show_code3[2][1],show_code4[2][1])
        )        
        self.play(Create(show_code4[2][3]))        
        self.wait(2)
        # ANIMAÇÃO EXPLICAÇÃO TERCEIRA PARTE

        # EXPLICAÇÃO QUARTA PARTE
        exp4 = Text("Quando usamos o comando print() na\nmedia teremos o resultado da operação")
        exp4.to_edge(UP)

        code_5 = """nota1 = 4
nota2 = 5.5

media = (nota1 + nota2) / 2

print(media)
"""
        show_code5 = Code(
            code=code_5, 
            tab_width=4, 
            background="rectangle",
            language="Python", 
            font=font_jetbrains,
            insert_line_no=False
        )
        console_code2 = """6"""
        show_console2 = Code(
            code=console_code2, 
            tab_width=4, 
            background="rectangle",
            language="Python", 
            font=font_jetbrains,
            insert_line_no=False
        )
        show_console2.next_to(show_code5, DOWN)
        # EXPLICAÇÃO QUARTA PARTE

        # ANIMAÇÃO EXPLICAÇÃO QUARTA PARTE
        self.play(FadeOut(exp3_2))
        self.play(Write(exp4))

        self.play(
            ReplacementTransform(show_code4[0], show_code5[0]),
            # ReplacementTransform(show_code4[2][0], show_code5[2][0])
            Create(show_code5[2][5])
        )
        self.wait(0.5)
        self.play(Create(show_console2))
        self.wait(1)

        console_code3 = """4.75"""
        show_console3 = Code(
            code=console_code3, 
            tab_width=4, 
            background="rectangle",
            language="Python", 
            font=font_jetbrains,
            insert_line_no=False
        )
        show_console3.next_to(show_code5, DOWN)
        self.play(
            ReplacementTransform(show_code4[2][0],show_code5[2][0]),
            ReplacementTransform(show_code4[2][1],show_code5[2][1]),
            ReplacementTransform(show_code4[2][3],show_code5[2][3]),
        )
        self.wait(0.5)
        self.play(FadeOut(show_console2))
        self.play(Create(show_console3))
        self.wait(2)
        
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        # ANIMAÇÃO EXPLICAÇÃO QUARTA PARTE
        
        # EXPLICAÇÃO 1 QUINTA PARTE
        exp5 = Text("Precisamos agora receber os dados\nque o usuário quiser escrever")
        exp6 = Text("Para isso usar o comando input()\nque recebe dados pelo console")
        # EXPLICAÇÃO 1 QUINTA PARTE

        # ANIMAÇÃO EXPLICAÇÃO 1 QUINTA PARTE
        self.play(Write(exp5))
        self.wait(2)
        self.play(FadeOut(exp5))
        self.play(Write(exp6))
        self.wait(2)
        self.play(FadeOut(exp6))
        self.wait(0.5)
        # ANIMAÇÃO EXPLICAÇÃO 1 QUINTA PARTE
        
        #EXPLICAÇÃO 2 QUINTA PARTE
        

        codigo_input = """nota1 = int(input('Nota 1:'))
nota1 = int(input('Nota 2:'))

media = (nota1 + nota2) / 2

print(media)
"""

        show_code_input = Code(
            code=codigo_input, 
            tab_width=4, 
            background="rectangle",
            language="Python", 
            font=font_jetbrains,
            insert_line_no=False
        )
        console_input = """Nota 1: 4
Nota 2: 7
5.5
"""

        show_console_input = Code(
            code=console_input, 
            tab_width=4, 
            background="rectangle",
            language="Python", 
            font=font_jetbrains,
            insert_line_no=False
        )
        show_console_input.move_to(DOWN*0.5)
        bar = Text("|")

        self.play(
            Create(show_code_input[0]),
            Create(show_code_input[1]),
            Create(show_code_input[2][0]),
        )
        self.wait(0.5)
        self.play(Create(show_code_input[2][1]))
        self.play(Create(show_code_input[2][2]))
        self.play(Create(show_code_input[2][3]))
        self.play(Create(show_code_input[2][4]))
        self.play(Create(show_code_input[2][5]))
        self.wait(1.5)
        self.play(
            show_code_input.animate.move_to(UP*2)
        )
        self.play(
            Create(show_console_input[0]),
        )
        self.play(
            Create(bar.next_to(show_console_input[2][0],LEFT))
        )
        self.play(
            Create(show_console_input[2][0]),
            bar.animate.next_to(show_console_input[2][0],RIGHT)
        )
        self.play(bar.animate.next_to(show_console_input[2][1],LEFT))
        self.play(
            Create(show_console_input[2][1]),
            bar.animate.next_to(show_console_input[2][1],RIGHT)
        )
        self.wait(0.5)
        self.play(bar.animate.next_to(show_console_input[2][2],LEFT))
        self.play(
            Create(show_console_input[2][2]),
            bar.animate.next_to(show_console_input[2][2],RIGHT)
        )
        self.play(Uncreate(bar))
        self.wait(1)
        self.play(FadeOut(show_console_input))

        console_input = """Nota 1: 7.3
Nota 2: 5.8
6.55
"""

        show_console_input = Code(
            code=console_input, 
            tab_width=4, 
            background="rectangle",
            language="Python", 
            font=font_jetbrains,
            insert_line_no=False
        )
        show_console_input.move_to(DOWN*0.5)
        bar = Text("|")
        self.play(
            Create(show_console_input[0]),
        )
        self.play(
            Create(bar.next_to(show_console_input[2][0],LEFT))
        )
        self.play(
            Create(show_console_input[2][0]),
            bar.animate.next_to(show_console_input[2][0],RIGHT)
        )
        self.play(bar.animate.next_to(show_console_input[2][1],LEFT))
        self.play(
            Create(show_console_input[2][1]),
            bar.animate.next_to(show_console_input[2][1],RIGHT)
        )
        self.wait(0.5)
        self.play(bar.animate.next_to(show_console_input[2][2],LEFT))
        self.play(
            Create(show_console_input[2][2]),
            bar.animate.next_to(show_console_input[2][2],RIGHT)
        )
        self.play(Uncreate(bar))
        self.wait(2)
