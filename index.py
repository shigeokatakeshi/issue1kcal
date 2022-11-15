from database import Kcal
import datetime

# データベースから引っ張ってきて表示させる

now = datetime.datetime.now()

Kcal.select()
kcal = Kcal.select()
t_kcal = 0
# print(kcal[0].kcal)

for i in range(0, 4):
    k = kcal[i].kcal
    k = int(k)
    t_kcal = t_kcal + k


print(f"「{now:%Y/%m/%d}の摂取カロリーは{t_kcal}kcalです。」")
