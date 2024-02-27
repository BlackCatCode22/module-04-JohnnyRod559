
text_file = open("C:\\Users\\Johnny\\PycharmProjects\\pythonProject10\\module-04-JohnnyRod559\\mbox-short.txt")

for line in text_file:
    line = line.rstrip()
    wrds = line.split()
    # Guardian pattern
    #if len(wrds) < 3 :
        #continue
    if len(wrds) < 3 or wrds[0] != 'From' :
        continue
    print(wrds[2])