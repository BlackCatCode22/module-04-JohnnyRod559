
text_file = open("C:\\Users\\Johnny\\PycharmProjects\\pythonProject10\\module-04-JohnnyRod559\\mbox-short.txt")

for line in text_file:
    ly = line.rstrip()
    print(ly.upper())