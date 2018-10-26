import re
r = 0
wordlist = []
endlist = []


def edits(initial, end):
    global r
    global wordlist
    global endlist
    word = re.sub(" ", "_", initial)
    end = re.sub(" ", "_", end)
    wordlist.append(word)
    endlist.append(end)
    word = re.sub("\W", "", word)
    end = re.sub("\W", "", end)
    word = word.lower()
    end = end.lower()
    regex1 = ".*"
    for i in range(0, len(end)):
        regex = end[i] + ".*"
        regex1 += regex
    regex1 = str(regex1)
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789_?"
    if end == word:
        print("\"{}\" to \"{}\" has edit distance {} {}".format(wordlist[0], endlist[0], r, wordlist))
        return
    delete = []
    for i in range(0, len(word)):
        delete.append(word[:i] +word[i + 1:])
    insert = []
    for i in range(0, len(word) + 1):
        for letter in alphabet:
            insert.append(word[:i] + letter + word[i:])
    replace = []
    for i in range(0, len(word)):
        for letter in alphabet:
                replace.append(word[:i] + letter + word[i + 1:])
    word = delete + insert + replace
    points = []
    for m in range(0, len(word)):
        points.append(0)
        temp = word[m]
        if len(temp) == len(end):
            points[m] += 10000000
        else:
            if re.search(regex1, str(temp)) is not None:
                points[m] += 100000
            points[m] += abs(1000 * (1 / (len(end) - len(temp))))
        for t in range(0, len(end)):
            if t < len(temp):
                if end[t] == temp[t]:
                    points[m] += 100
                else:
                    if end[t] in temp:
                        points[m] += 1
                    else:
                        points[m] += 0
    scores = {word[m]: points[m] for m in range(0, len(word))}
    word = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    word = word[:1]
    word = re.search("\'\w+\'", str(word))
    word = word.group(0)
    mid = re.sub("\'", "", word)
    r += 1
    edits(mid, end)


edits("Nick", "Reduce, Reuse, Recycle")
