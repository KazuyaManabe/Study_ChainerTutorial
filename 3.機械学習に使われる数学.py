
# 3.2
# 未知のデータに対しても精度良く予測が行えることを汎化性能(generalizability)と言う
# 与えられたデータの特徴や関係性を、パラメータで表すものを、モデルという

# 3.3 目的関数
# 3.3.1二乗誤差関数
n = int(input())  # サンプル数
t = list(input().split())  # 2次元上の点の座標

a = 2  # 1次関数の傾き
b = 1  # 1次関数の切片
s = 0  # 二乗誤差の和

for i in t:
    y = a * int(i[1]) + b  # 予測値 =　出力値 = パラメータ×入力値 + パラメータ
    s += (int(i[3]) - y) ** 2  # 二乗誤差の和 += (目標値-予測値)**2

L = s / n  # 二乗誤差の和/サンプル数
print(L)

# 3.4目的関数の最適化
