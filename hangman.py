# ハングマン
# 文字あてゲーム
def hangman(word):
    wrong = 0       # 間違えた回数を記録
    stages = [
        "",
        "-----------------------",
        "|                      ",
        "|              |       ",
        "|              0       ",
        "|            ／|＼     ",
        "|            ／ ＼     ",
        "|                      "
    ]
    rletters = list(word)           # 残りの文字を記憶
    board = ["_"] * len(word)      # ヒントを記録
    win = False
    print("ハングマンへようこそ")

    # 間違えた回数が絵が出来上がる回数になるまでループを行う
    while wrong < len(stages) - 1:
        print("\n")
        msg = "一文字を予想してね："
        char = input(msg)
        # 入力した文字がリストに含まれている場合
        if char in rletters:
            # 対象文字の位置を取得
            cind  = rletters.index(char)
            # ヒントの文字列を更新する
            board[cind] = char
            rletters[cind] = '$'
        # 含まれていない場合
        else:
            # 間違えた回数を増やす
            wrong += 1
            print(" ".join(board))
        print("\n".join(stages[0:wrong + 1]))
        if "_" not in board:
            print("あなたの勝ち")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong + 1]))
        print("あなたの負け!正解は{}".format(word))


hangman("cat")
