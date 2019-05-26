while True:
    correct_num = [4, 8]
    num = input("数字を当ててください。")
    if num == "q":
        break
    try:
        if int(num) in correct_num:
            print("正解\n")
        else:
            print("不正解\n")
    except:
        print("数字を入力するか、qで終了します\n")

    
