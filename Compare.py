class Compare:
    def __init__(self):
        c = "c"

def compare(a, b):
    print (a is b)

comp = Compare()
same_comp = comp
another_comp = Compare()

compare(comp,same_comp)
compare(comp,another_comp)
