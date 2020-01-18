import pygame, sys, time
pygame.init()
#good luck !!

#window settings
width = 900
height= 600
win_size = width,height
#game_box settings

box_width = 600
box_height=600

#colors code
gris = ( 179, 182, 183 ) 
light_salmon = ( 255, 160, 122)
gris_feta7 = (93, 109, 126)
blue = (0,0,255)
#
#colors of surfaces
menu_color =  gris_feta7
rect_color = light_salmon
#
#rectangles/grid declaring

rec_width = box_width/3
rec_height = box_height/3

rect1 = pygame.Rect((0,0),(rec_width,rec_height))
rect2 = pygame.Rect((rec_width,0),(rec_width,rec_height))
rect3 = pygame.Rect((2*rec_width,0),(rec_width,rec_height))
rect4 = pygame.Rect((0,rec_height),(rec_width,rec_height))
rect5 = pygame.Rect((rec_width,rec_height),(rec_width,rec_height))
rect6 = pygame.Rect((2*rec_width,rec_height),(rec_width,rec_height))
rect7 = pygame.Rect((0,2*rec_height),(rec_width,rec_height))
rect8 = pygame.Rect((rec_width,2*rec_height),(rec_width,rec_height))
rect9 = pygame.Rect((2*rec_width,2*rec_height),(rec_width,rec_height))
rectangles = [rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9]
#######
#menu declaring
rect_menu = pygame.Rect((600,0),(width-3*rec_width,height))

def draw_x(surface,color,xs,ys,xe,ye,width):
	pygame.draw.line(surface,color,(xs+rec_width/6,ys+rec_height/6),(xe-rec_width/6,ye-rec_height/6),width)
	pygame.draw.line(surface,color,(xs+rec_width/6,ys+rec_height-rec_height/6),(xe-rec_width/6,ys+rec_width/6),width)
	#pygame.draw.line(screen,(255,0,0),(rectang[0],rectang[1]),(rectang[0]+rec_width,rectang[1]+rec_height),10)
	#pygame.draw.line(screen,(255,0,0),(rectang[0],rectang[1]+rec_height),(rectang[0]+rec_width,rectang[1]),10)
def draw_circle(surface,color,xc,yc,r,w):
	pygame.draw.circle(surface,color,(xc,yc),r,w)

global p

####################################################
global tab
tab = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
global winner
winner = ''
def get_row(p):
	if (p // 3 == 0):
		return  0
	elif (p // 3 != 0 ) and (p % 3 == 0):
		return ((p // 3 ) - 1) 
	elif ( p // 3 != 0) and ((p % 3) != 0):
		return (p // 3 )

def get_column(p):
	if (p % 3 == 0):
		return 2
	elif (p % 3 == 1 ):
		return 0
	elif ( p % 3 == 2 ):
		return 1
def check_row(v, l):
	if (tab[l][0] == tab[l][1] == tab[l][2] == v):
		return True
	else:
		return False
def check_column(v, c):
	if (tab[0][c] == tab[1][c] == tab[2][c] == v):
		return True
	else:
		return False
def check_diag1(v ):
	if (tab[0][0] == tab[1][1] == tab[2][2] == v):
		return True
	else:
		return False

def check_diag2(v ):
	if (tab[2][0] == tab[1][1] == tab[0][2] == v):
		return True
	else:
		return False

def printing():
	print("Current State: ")
	for i in range(3):
		print(*tab[i],sep=' | ')

def win_cond(v,position):
	if ( check_row(v, get_row(position)) or check_column(v, get_column(position)) or check_diag1(v) or  check_diag2(v)):
		print(v , "WON!")
		return True

	##########################################
screen = pygame.display.set_mode(win_size)
def grid_layout():

	#game layout no need to be inside loop
	pygame.draw.rect(screen,rect_color,rect1)
	pygame.draw.rect(screen,rect_color,rect2)
	pygame.draw.rect(screen,rect_color,rect3)
	pygame.draw.rect(screen,rect_color,rect4)
	pygame.draw.rect(screen,rect_color,rect5)
	pygame.draw.rect(screen,rect_color,rect6)
	pygame.draw.rect(screen,rect_color,rect7)
	pygame.draw.rect(screen,rect_color,rect8)
	pygame.draw.rect(screen,rect_color,rect9)
	#

		#grid/lines drawing
	pygame.draw.line(screen,(0,0,0),(box_width/3,0),(box_width/3,box_height),5)
	pygame.draw.line(screen,(0,0,0),(2*box_width/3,0),(2*box_width/3,box_height),5)   # line always present unlike the other format , keep pressing to show the line
	pygame.draw.line(screen,(0,0,0),(0,box_height/3),(box_width,box_height/3),5)
	pygame.draw.line(screen,(0,0,0),(0,2*box_height/3),(box_width,2*box_height/3),5)

global running
running = True
global gamestill
gamestill = True

def game():
	global winner
	grid_layout()
	p='O'
	#MENU FOR TEXT
	pygame.draw.rect(screen,gris_feta7,(600,0,width-3*rec_width,height))
	filled_rects = []
	running = True

	while running and game:
		for event in pygame.event.get():
			if (event.type == pygame.QUIT) : 
				sys.exit()
			if (event.type == pygame.MOUSEBUTTONDOWN):
				if (pygame.mouse.get_pressed()[0]):
					mouse_pos = pygame.mouse.get_pos()
					for rectang in rectangles : 
						global pos
						pos = rectangles.index(rectang)+1
						#if win_cond(p,pos):
						#	running = False
						#	break
						if (rectang.collidepoint(mouse_pos) == 1) and (p=='X') and (rectang not in filled_rects) and (len(filled_rects)!=9) : 
							draw_x(screen,(255,0,0),rectang[0],rectang[1],rectang[0]+rec_width,rectang[1]+rec_height,10)
							filled_rects.append(rectang)
							##
							l = get_row(rectangles.index(rectang)+1)
							c = get_column(rectangles.index(rectang)+1)
							tab[l][c]=p
							printing()
							if win_cond(p,pos):
								#if (len(filled_rects)==9):
								#	print(len(filled_rects))
								#	print("its a draw")
								running = False
								winner = 'X'
								break
							#DRAW CONDITION INSIDE EVERY X_FILL AND O_FILL
							if (len(filled_rects)==9) and running :
								print("its a draw")
								running = False
								winner = 'd'
								break
							##
							p='O'
							break	   #weird bug , it worked somehow....				
						elif((rectang.collidepoint(mouse_pos) == 1) and (p=='O') and (rectang not in filled_rects)) and (len(filled_rects)!=9):
							draw_circle(screen,(0,0,255),int(rectang[0]+rec_width//2),int(rectang[1]+rec_height//2),int(rec_height//2-(rec_height/6)),8)
							filled_rects.append(rectang)
							##o
							l = get_row(pos)
							c = get_column(pos)
							tab[l][c]=p
							printing()
							if win_cond(p,pos):
								running = False
								winner = 'O'
								break
							#DRAW CONDITION
							if (len(filled_rects)==9) and running:
								print("its a draw")
								running = False
								winner = 'd'
								break
							###
							p='X'
							break
						#elif (len(filled_rects)==9) and running:
						#	print("its a draw")
						#	running = False
						#	break
		if (winner != '') :
			if (winner == 'X' ) or (winner == 'O'):
				text = str(winner+ '  WINS!')
			elif (winner =='d'):
				text = 'IT \'S A DRAW!!!'

			myfont = pygame.font.SysFont('Comic Sans MS',30)
			result_surface = myfont.render(text,False,(0,0,0))
			screen.blit(result_surface,(box_width+rec_height/3,rec_height))
			print(text)
			pygame.display.flip()
			time.sleep(4)
		pygame.display.flip()


			#screen.blit(result_surface,(0,0))

grid_layout()
game()
pygame.quit()

