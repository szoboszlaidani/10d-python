with open("ekiras/forras.txt","r",encoding="UTF-8") as ds:
    text,spec=[ds.read(),[",",";",".",":","-","!","?","%","!","„","()",")","="]]
    text2=text
    for c in spec:text=text.replace(c,' ')
    textlist=text.lower().split()
    sentencelist=text2.replace("!",".").replace("?",".").split(".")


beg=[w for w in textlist if w[0] in "bcd"]

lessthan5=[x for x in textlist if len(x)<5]

print(*beg, sep=" // ")
print(f"elemek száma - | {len(beg)} |")
print(f"5-nél rövidebb - | {lessthan5} |")
print(*sentencelist, sep=f"\n")