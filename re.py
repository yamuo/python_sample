import re

"""
l = "Beautiful is better than ugly."
matches = re.findall("beautiful", l, re.IGNORECASE)

print(matches)
"""

zen = """Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

m = re.findall("^If", zen, re.MULTILINE)
#print(m)

"""
string = "Two too."
m = re.findall("t[ow]o", string, re.IGNORECASE)
print(m)
"""
"""
line = "123 hi 34 hello."
m = re.findall("\d", line, re.IGNORECASE)
print(m)
"""
"""
t = "__pne __ __two__ __three__"
found = re.findall("__.*?__", t)
for match in found:
    print(match)
"""

text = """キリンは大昔から __複数名刺__の興味の対象でした。
キリンは__複数名刺__の中で一番背が高いですが、科学者たちはそのような長い__体の一部__をどうやって獲得したのか説明できません。
キリンの身長は__数値____単位__近くあり、その高さのほとんどは脚と__体の一部__によるものです。
"""
"""
def mad_libs(mls):
    hints = re.findall("__.*?__", mls)
    if hints is not None:
        for word in hints:
            q = "{}を入力:".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
        print('\n')
        mls = mls.replace("\n","")
        print(mls)
    else:
        print("引数mlsが無効です")

mad_libs(text)
"""
"""
line = "I love $"
m = re.findall("\\$", line, re.IGNORECASE)
print(m)
"""

cha = "The ghost that says boo haunts the loo"

match = re.findall(".oo" , cha, re.IGNORECASE)
print(match)










