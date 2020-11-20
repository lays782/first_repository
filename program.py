file = open("C:\\Users\\jirik\\Documents\\Moje dokumenty\\Cancelled flights\\Email_templates\\affected_passengers.txt", "r")
text = file.readlines()


for i in text:
    print(i)
    


file.close()
