import pandas as pd

  # ここでダウンロードしてきたCSVファイルを読み込む
df = pd.read_csv('twins.csv')


# A以上の単位数の合計を求める
sum_of_a = df[(df['総合評価'] == 'A') | (df['総合評価'] == 'A+')]['単位数'].sum()

print(f"A以上の単位数の合計: {sum_of_a}")

# 取得単位数の合計を求める
sum_of_all = df[(df['総合評価'] != 'D') & (df['総合評価'] != 'P') & (df['総合評価'] != 'F') &  (df['総合評価'] != '履修中')]['単位数'].sum()

print(f"取得単位数: {sum_of_all}")

# 割合を求める
ratio = sum_of_a / sum_of_all
print(f"A以上の割合: {ratio}")


