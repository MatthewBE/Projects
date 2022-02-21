import random

def get_valid_moves(point):
  up = maze[point[0]][point[1]]
  dwn = maze[point[0]][point[1]]
  left = maze[point[0]][point[1]]
  right = maze[point[0]][point[1]]

  if maze[point[0]][point[1]] != 1:
    
    
    
pos = (0,0)
seen_moves = []

while valid: 
  new_pos = pos 
  move_list = get_valid_moves(new_pos) 
  # select first move, add rest to list to keep track
  
  pos = move_list[0]
  move_list.pop(0)
  
  class Maze():
    def __init__(self, maze_size):
      self.size = maze_size
      
      
      
    
