from random import *
import discord

def randomizer(tableau):
	for i in range(len(tableau)):
		a = randint(0, len(tableau))
		b = tableau[0]
	
		tableau.insert(a, b)
		tableau.pop(0)
	
	return tableau

def display(grid):

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pass

async def minesweeper(self, message):
    channel = message.channel
    sender = message.author.id
    size = [int(message.content.split()[1]), int(message.content.split()[2])]
    mines = int(message.content.split()[3])

    grid = [[0 for i in range(size[0])] for j in range(size[1])]
    already_placed = []
    x, y = [randint(0, size[1]-1) for i in range(mines)], [randint(0, size[0]-1) for i in range(mines)]
    x = randomizer(x)
    y = randomizer(y)

    for i in range(len(x)):
        print(x[0], y[0])
        grid[x[0]][y[0]] = "M"
        x.pop(0)
        y.pop(0)
    
    embed=discord.Embed(title="Minesweeper",  
    description="This is an embed that will show how to build an embed and the different components", 
    color=0xFF5733)