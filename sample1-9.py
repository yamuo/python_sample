"""
import os
path = os.path.join("Users","s-yamashita","work","python")
print(path)
"""
"""
st = open("st.txt","w",encoding="utf-8")
st.write("Hi from Python!")
st.close()
"""
"""
with open("st.txt","w", encoding="utf-8") as f:
    f.write("Hi from Python!")

with open("st.txt","r", encoding="utf-8") as f:
    print(f.read())
"""
"""
my_list = []

with open("st.txt","r",encoding="utf-8") as f:
    my_list.append(f.read())

    print(my_list)
"""
"""
import csv

with open("st.csv","w",encoding="utf-8") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["one","two","three"])
    w.writerow(["four","five","six"])

with open("st.csv","r",encoding="utf-8") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
"""
"""
i = input("please input any comment");

with open("challenge.txt","w", encoding="utf-8") as f:
    f.write(i)
"""

import csv

my_list = [["トップガン","riskey","minoruty"],["titanic","revenant","inception"],["training","man of fire","flight"]]

with open("challenge.csv","w",encoding="utf-8") as f:
    w = csv.writer(f, delimiter=",")
    for row in my_list:
        w.writerow(row)

