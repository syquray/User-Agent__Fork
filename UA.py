#最近流行ってるUA(User Agent)取得です。python初心者なので、お手柔らかにお願いします()
pip install requests
import requests
import json

id = input("作品のURLを入力してください。")

length = len(id) #URLの長さ取得
count = 33
number = "" #なんかバグったって思ってたら先に変数を代入しないといけなかったらしい
for i in range(length - 34):
 number = number + id[count]
 count = count + 1

url = "https://projects.scratch.mit.edu/" + number
r = requests.get(url, timeout=5)
r = r.json()
r = r['meta']['agent']
print("UAはこちらです : " + r)
