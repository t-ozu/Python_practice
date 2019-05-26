answer = input("好きな動物は?")
with open("ansewer.txt", "w", encoding="utf-8")as f:
    f.write(answer)
    
