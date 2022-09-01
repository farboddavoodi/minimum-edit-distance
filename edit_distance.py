def distance(w1, w2, insertcost, deletecost, replacecost):
    dist = [[0 for j in range(len(w2) + 1)] for i in range(len(w1) + 1)]
    hst = [[0 for j in range(len(w2) + 1)] for i in range(len(w1) + 1)]
    for i in range(1, len(w1) + 1):
        dist[i][0] = dist[i - 1][0] + insertcost
        hst[i][0] = "insert"
    for j in range(1, len(w2) + 1):
        dist[0][j] = dist[0][j - 1] + deletecost
        hst[0][j] = "delete"
    for j in range(1, len(w2) + 1):
        for i in range(1, len(w1) + 1):
            inscost = insertcost + dist[i - 1][j]
            delcost = deletecost + dist[i][j - 1]
            cost = 0 if w1[i - 1] == w2[j - 1] else replacecost
            substcost = cost + dist[i - 1][j - 1]
            dist[i][j] = min(inscost, delcost, substcost)
            if min(inscost, delcost, substcost) == inscost:
                hst[i][j] = "insert"
            elif min(inscost, delcost, substcost) == delcost:
                hst[i][j] = "delete"
            else:
                hst[i][j] = "substitute"
    str = []
    n = len(w1)
    m = len(w2)
    while n > 0 or m > 0:
        if hst[n][m] == "substitute":
            n -= 1
            m -= 1
            str.append("substitute")
            print("substitute   " + w1[m] + ", " + w2[n])
        elif hst[n][m] == "delete":
            m -= 1
            str.append("insert")
            print("insert   " + w1[m])
        elif hst[n][m] == "insert":
            n -= 1
            str.append("delete")
            print("delete   " + w2[n])
    return dist[len(w1)][len(w2)]
print("levenshtein distance =", distance("intention", "execution", 1, 1, 2))