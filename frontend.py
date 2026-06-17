import pygame, random, time
from backend import bfs, dfs, astar, hamiltonian_cycle, save_result, show_graph

pygame.init()

WIDTH, HEIGHT = 900, 600
GRID = 20
ROWS = 25

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Snake Dashboard")

WHITE=(245,245,245); BLACK=(30,30,30)
GREEN=(0,200,0); RED=(200,0,0)
BLUE=(50,150,255); GRAY=(220,220,220)

font = pygame.font.SysFont("Arial",20)
big_font = pygame.font.SysFont("Arial",35)
clock = pygame.time.Clock()

def draw_text(t,x,y,c=BLACK):
    screen.blit(font.render(t,True,c),(x,y))

def random_food(snake):
    while True:
        f=(random.randint(0,ROWS-1),random.randint(0,ROWS-1))
        if f not in snake: return f

# ---------- MENU ----------
def menu():
    options=["START","GRAPH","CLEAR","EXIT"]

    while True:
        screen.fill(WHITE)
        draw_text("AI SNAKE LAB",300,100)

        rects=[]
        for i,opt in enumerate(options):
            r=pygame.Rect(350,220+i*80,220,60)
            rects.append((r,opt))

            pygame.draw.rect(screen,BLUE if r.collidepoint(pygame.mouse.get_pos()) else GRAY,r)
            draw_text(opt,r.x+60,r.y+20,WHITE if r.collidepoint(pygame.mouse.get_pos()) else BLACK)

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type==pygame.QUIT: pygame.quit(); exit()
            if e.type==pygame.MOUSEBUTTONDOWN:
                for r,opt in rects:
                    if r.collidepoint(pygame.mouse.get_pos()):
                        return opt

# ---------- SELECT ----------
def select_mode():
    modes=["HUMAN","BFS","DFS","A*","HAMILTONIAN"]

    while True:
        screen.fill(WHITE)
        draw_text("SELECT MODE",300,100)

        rects=[]
        for i,m in enumerate(modes):
            r=pygame.Rect(350,200+i*70,220,55)
            rects.append((r,m))

            pygame.draw.rect(screen,BLUE if r.collidepoint(pygame.mouse.get_pos()) else GRAY,r)
            draw_text(m,r.x+60,r.y+15,WHITE if r.collidepoint(pygame.mouse.get_pos()) else BLACK)

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type==pygame.QUIT: pygame.quit(); exit()
            if e.type==pygame.MOUSEBUTTONDOWN:
                for r,m in rects:
                    if r.collidepoint(pygame.mouse.get_pos()):
                        return m

# ---------- GAME ----------
def game(mode):
    snake=[(5,5)]
    direction=(0,1)
    food=random_food(snake)

    score=0; steps=0
    start=time.time()
    path=[]; paused=False

    cycle=hamiltonian_cycle(); idx=0

    while True:
        clock.tick(10)
        screen.fill(WHITE)

        stop_btn=pygame.Rect(620,320,150,50)

        for e in pygame.event.get():
            if e.type==pygame.QUIT: pygame.quit(); exit()

            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_SPACE: paused=not paused

                # HUMAN CONTROL
                if mode=="HUMAN":
                    if e.key==pygame.K_UP: direction=(0,-1)
                    if e.key==pygame.K_DOWN: direction=(0,1)
                    if e.key==pygame.K_LEFT: direction=(-1,0)
                    if e.key==pygame.K_RIGHT: direction=(1,0)

            if e.type==pygame.MOUSEBUTTONDOWN:
                if stop_btn.collidepoint(pygame.mouse.get_pos()):
                    save_result(mode,score,steps,start)
                    return

        if paused:
            draw_text("PAUSED",350,250,RED)
            pygame.display.flip()
            continue

        # AI
        if mode!="HUMAN":
            if mode=="HAMILTONIAN":
                idx=(idx+1)%len(cycle)
                nxt=cycle[idx]
                direction=(nxt[0]-snake[0][0], nxt[1]-snake[0][1])
            else:
                if not path:
                    if mode=="BFS": path=bfs(snake[0],food,snake)
                    if mode=="DFS": path=dfs(snake[0],food,snake)
                    if mode=="A*": path=astar(snake[0],food,snake)
                if path: direction=path.pop(0)

        new=(snake[0][0]+direction[0], snake[0][1]+direction[1])

        if new in snake or not(0<=new[0]<ROWS and 0<=new[1]<ROWS):
            break

        snake.insert(0,new)

        if new==food:
            score+=1
            food=random_food(snake)
            path=[]
        else:
            snake.pop()

        steps+=1

        for s in snake:
            pygame.draw.rect(screen,GREEN,(s[0]*20,s[1]*20,20,20))
        pygame.draw.rect(screen,RED,(food[0]*20,food[1]*20,20,20))

        pygame.draw.rect(screen,GRAY,(600,0,300,600))
        draw_text(f"Mode: {mode}",620,50)
        draw_text(f"Score: {score}",620,100)

        pygame.draw.rect(screen,RED,stop_btn)
        draw_text("STOP",650,335,WHITE)

        pygame.display.flip()

    save_result(mode,score,steps,start)

# ---------- MAIN ----------
while True:
    action=menu()

    if action=="START":
        m=select_mode()
        game(m)

    elif action=="GRAPH":
        show_graph()

    elif action=="CLEAR":
        open("results.csv","w").close()

    elif action=="EXIT":
        break