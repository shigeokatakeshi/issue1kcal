from database import Kcal
import datetime

# データベースから引っ張ってきて表示させる

now = datetime.datetime.now()

Kcal.select()
kcal = Kcal.select()
t_kcal = 0
# print(kcal[0].kcal)


string1 = kcal
# print(len(string1))
line = len(string1)


for i in range(line):
    k = kcal[i].kcal
    k = int(k)
    t_kcal = t_kcal + k


print(f"「{now:%Y/%m/%d}の摂取カロリーは{t_kcal}kcalです。」")
