import random
pepple=random.choice(["красивоя","ужасноя"])
peppleludoed=random.choice(["голодный","не голодный"])
wether=random.choice(["плохая ","ясноя"])
print("погода была",wether ,"и принцесса была",pepple)
if wether=="ясноя" and pepple=="красивоя" or pepple=="ужасноя":
    print("принцесса пошла гулять")