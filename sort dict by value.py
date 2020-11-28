sorted_x = dict(sorted(items.items(), key=lambda kv: kv[1]))
print(sorted_x)
for i in sorted_x:
    print(i,":",sorted_x[i])
