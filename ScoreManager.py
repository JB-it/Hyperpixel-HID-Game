def writeScore(name, score):
    #reads all lines of the file score.ini
    with open('score.ini', 'r') as file:
        lines = file.readlines()

    #splits all lines 

    with open("score.ini", 'w') as f:
        f.write(name + ":" + str(score))

