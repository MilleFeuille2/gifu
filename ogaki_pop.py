import os
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tick

today = datetime.today()
today = str(today.year) + str(today.month).zfill(2) + str(today.day).zfill(2)
INPATH = r'./input'
OUTPATH = r'./output/{}'.format(today)

if not os.path.exists(OUTPATH):
    os.makedirs(OUTPATH)

# データを読み込む
df = pd.read_excel(os.path.join(INPATH, 'ogaki_population.xlsx'), index_col=0)

fig1 = plt.figure()
# 余白を挿入
fig1.subplots_adjust(bottom=0.2, left=0.3)

ax1 = fig1.add_subplot(1, 1, 1)

ax1.plot(df.index, df['pop'].values)
ax1.set_title('1918〜2016年の大垣市の人口', fontsize=18)

ax1.set_xlabel('西暦（年）', fontsize=16)
ax1.set_ylabel('人口（人）', fontsize=16)
ax1.tick_params(labelsize=16)
# 縦軸の数値を３桁カンマ区切りに
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda i, loc: "{:,}".format(int(i))))

# 25年ごとの目盛線
ax1.grid(which="major", axis="x", color="black", alpha=0.5, linestyle="-", linewidth=0.5)
# 5年ごとの補助目盛線
ax1.xaxis.set_minor_locator(tick.MultipleLocator(5))
ax1.grid(which="minor", axis="x", color="black", alpha=0.5, linestyle="-", linewidth=0.3)

# 図を保存する
plt.savefig(os.path.join(OUTPATH, 'plot_ogaki_pop.png'))
