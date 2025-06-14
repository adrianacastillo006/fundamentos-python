
def load_file():
    filepath=input("Enter the path of the file to load:")
    file=open(filepath,'r',encoding='utf-8')
    lines=file.readlines()
    file.close()
    return lines 

my_file=load_file()
print(my_file)
def set_enviroment(raw_file):
    env=[]
    for line in raw_file:
        line=line.strip()
        env.append(int(c) for c in line)
    return env     

def print_env(env):
    for row in env:
        for cell in row:
            if cell==1:
                print('█', end="")
            else:
                print(' ', end="")
        print()

def count_neighbors(env, x, y):
    rows = len(env)
    cols = len(env[0])
    count = 0
    
    for i in [x-1, x, x+1]:
        for j in [y-1, y, y+1]:
            if i == x and j == y:
                continue  # no contamos la celda central
            if 0 <= i < rows and 0 <= j < cols:
                if env[i][j] == 1:
                    count += 1
    return count
