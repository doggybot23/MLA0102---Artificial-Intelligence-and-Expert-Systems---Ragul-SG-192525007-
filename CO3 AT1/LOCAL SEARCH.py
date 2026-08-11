{\rtf1\ansi\ansicpg1252\cocoartf2870
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww29200\viewh17740\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Online Search Agent (Dynamic Path Finding)\
\
grid = [\
    [0, 0, 0, 0],\
    [0, 1, 0, 0],   # 1 = Obstacle\
    [0, 0, 0, 0],\
    [0, 0, 1, 0]\
]\
\
start = (0, 0)\
goal = (3, 3)\
\
moves = [(0,1), (1,0), (0,-1), (-1,0)]\
\
def online_search(start, goal):\
    current = start\
    path = [current]\
\
    while current != goal:\
        x, y = current\
        found = False\
\
        for dx, dy in moves:\
            nx, ny = x + dx, y + dy\
\
            if 0 <= nx < 4 and 0 <= ny < 4:\
                if grid[nx][ny] == 0 and (nx, ny) not in path:\
                    current = (nx, ny)\
                    path.append(current)\
                    found = True\
                    break\
\
        if not found:\
            print("No Path Exists")\
            return\
\
    print("Path Found:")\
    print(path)\
\
online_search(start, goal)}