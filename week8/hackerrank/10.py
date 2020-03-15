n = int(input())
info = {}
for _ in range(n):
    line = input().split()
    name, scores = line[0], line[1:]
    scores = map(float, scores)
    info[name] = list(scores)
query = input()
query_scores = info[query]
print("{0:.2f}".format(sum(query_scores)/(len(query_scores))))