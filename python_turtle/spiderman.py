import turtle

# Função para desenhar um quadrado de uma cor específica
def draw_square(color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):  # Tamanho do quadrado
        turtle.forward(20)
        turtle.right(90)
    turtle.end_fill()

# Função para desenhar a imagem pixelada
def draw_spiderman():
    turtle.speed(0)  # Velocidade máxima
    turtle.penup()
    turtle.goto(-80, 400)  # Ajuste a posição inicial para cima e para a esquerda
    turtle.pendown()

    # Matriz representando a imagem pixelada
    spiderman_pixels = [
        ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'W', 'W', 'W', 'k', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'k', 'W', 'W', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'W', 'W', 'k', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'k', 'W', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'W', 'k', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'k', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'k', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'k', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'k', 'R', 'k', 'k', 'k', 'R', 'R', 'R', 'R', 'R', 'k', 'k', 'k', 'R', 'k', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'k', 'R', 'k', 'W', 'W', 'k', 'R', 'R', 'R', 'k', 'W', 'W', 'k', 'R', 'k', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'k', 'R', 'k', 'W', 'W', 'k', 'R', 'R', 'R', 'k', 'W', 'W', 'k', 'R', 'k', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'k', 'R', 'k', 'W', 'W', 'W', 'k', 'R', 'k', 'W', 'W', 'W', 'k', 'R', 'k', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'k', 'R', 'R', 'k', 'W', 'W', 'k', 'R', 'k', 'W', 'W', 'k', 'R', 'R', 'k', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'k', 'R', 'R', 'k', 'k', 'k', 'k', 'R', 'k', 'k', 'k', 'k', 'R', 'R', 'k', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'k', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'k', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'W', 'k', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'k', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'W', 'W', 'k', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'k', 'W', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'W', 'W', 'W', 'k', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'k', 'W', 'W', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'W', 'W', 'k', 'k', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'k', 'k', 'W', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'W', 'k', 'R', 'R', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'R', 'R', 'k', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'k', 'k', 'k', 'R', 'k', 'R', 'R', 'k', 'R', 'R', 'k', 'R', 'k', 'k', 'k', 'W', 'W', 'W'],
        ['W', 'W', 'k', 'k', 'B', 'k', 'R', 'R', 'k', 'R', 'k', 'R', 'k', 'R', 'R', 'k', 'B', 'k', 'k', 'W', 'W'],
        ['W', 'W', 'k', 'B', 'B', 'k', 'R', 'R', 'R', 'k', 'k', 'k', 'R', 'R', 'R', 'k', 'B', 'B', 'k', 'W', 'W'],
        ['W', 'W', 'k', 'B', 'B', 'k', 'R', 'R', 'k', 'k', 'k', 'k', 'k', 'R', 'R', 'k', 'B', 'B', 'k', 'W', 'W'],
        ['W', 'W', 'k', 'B', 'B', 'k', 'R', 'k', 'R', 'k', 'R', 'k', 'R', 'k', 'R', 'k', 'B', 'B', 'k', 'W', 'W'],
        ['W', 'W', 'k', 'B', 'B', 'k', 'R', 'R', 'R', 'k', 'R', 'k', 'R', 'R', 'R', 'k', 'B', 'B', 'k', 'W', 'W'],
        ['W', 'W', 'k', 'B', 'R', 'k', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'k', 'R', 'B', 'k', 'W', 'W'],
        ['W', 'W', 'k', 'R', 'R', 'k', 'R', 'R', 'k', 'R', 'R', 'R', 'k', 'R', 'R', 'k', 'R', 'R', 'k', 'W', 'W'],
        ['W', 'W', 'k', 'R', 'R', 'k', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'k', 'R', 'R', 'k', 'W', 'W'],
        ['W', 'W', 'W', 'k', 'k', 'k', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'k', 'k', 'k', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'W', 'W', 'k', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'k', 'W', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'W', 'W', 'k', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'k', 'W', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'W', 'W', 'k', 'B', 'B', 'B', 'k', 'k', 'k', 'B', 'B', 'B', 'k', 'W', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'W', 'W', 'k', 'B', 'B', 'B', 'k', 'W', 'k', 'B', 'B', 'B', 'k', 'W', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'W', 'W', 'k', 'B', 'B', 'B', 'k', 'W', 'k', 'B', 'B', 'B', 'k', 'W', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'W', 'W', 'k', 'k', 'k', 'k', 'W', 'W', 'W', 'k', 'k', 'k', 'k', 'W', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'W', 'W', 'k', 'R', 'R', 'k', 'W', 'W', 'W', 'k', 'R', 'R', 'k', 'W', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'W', 'W', 'k', 'R', 'R', 'k', 'W', 'W', 'W', 'k', 'R', 'R', 'k', 'W', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'W', 'k', 'R', 'R', 'R', 'k', 'W', 'W', 'W', 'k', 'R', 'R', 'R', 'k', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'W', 'k', 'k', 'k', 'k', 'k', 'W', 'W', 'W', 'k', 'k', 'k', 'k', 'k', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],

    ]

    # Cores
    colors = {
        'R': 'red',    # Vermelho
        'B': 'blue',   # Azul
        'W': 'white',  # Espaço em branco
        'k': 'black'   # Preto
    }

    # Desenhar a matriz
    for row in spiderman_pixels:
        for pixel in row:
            draw_square(colors[pixel])
            turtle.forward(20)  # Mover para a direita
        turtle.penup()
        turtle.goto(turtle.xcor(), turtle.ycor() - 20)  # Mover para a linha abaixo
        turtle.pendown()
        turtle.goto(-80, turtle.ycor())  # Voltar para a esquerda

    turtle.hideturtle()
    turtle.done()

# Configurações iniciais
turtle.title("Desenho Pixelado do Homem-Aranha")
turtle.bgcolor("white")

draw_spiderman()
