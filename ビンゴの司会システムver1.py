import tkinter as tk
import random

class BingoSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("ビンゴの司会システム Ver.1")
        self.numbers = list(range(1, 76))  # 1から75までの数字のリスト
        self.called_numbers = []  # 呼ばれた数字の履歴

        # メインフレーム
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        # ランダムに選ばれた数字を表示するラベル
        self.label = tk.Label(self.frame, text="数字を選んでください", font=("Helvetica", 32))
        self.label.pack(pady=20)

        # ボタンを作成
        self.button = tk.Button(self.frame, text="数字を選ぶ", font=("Helvetica", 20), command=self.draw_number)
        self.button.pack(pady=10)

        # 履歴表示用のリストボックス
        self.history_label = tk.Label(self.frame, text="履歴", font=("Helvetica", 20))
        self.history_label.pack(pady=10)
        self.history_box = tk.Listbox(self.frame, font=("Helvetica", 16), height=10)
        self.history_box.pack(pady=10)

    def draw_number(self):
        if self.numbers:
            # リストからランダムに数字を選んで削除
            number = random.choice(self.numbers)
            self.numbers.remove(number)
            self.called_numbers.append(number)
            
            # ラベルに数字を表示
            self.label.config(text=str(number))
            
            # 履歴に数字を追加
            self.history_box.insert(tk.END, str(number))
        else:
            self.label.config(text="全ての数字が呼ばれました")

# Tkinterウィンドウを作成してアプリケーションを起動
if __name__ == "__main__":
    root = tk.Tk()
    app = BingoSystem(root)
    root.mainloop()
