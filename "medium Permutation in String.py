def checkInclusion(self, s1: str, s2: str) -> bool:
    find, have = Counter(s1), Counter(s2[:len(s1)])
    same = sum([int(find[c] == have[c]) for c in find])

    for i in range(len(s2) - len(s1)):
        if same == len(find):
            return True

        same -= int(find[s2[i]] == have[s2[i]])
        have[s2[i]] -= 1

        same += int(find[s2[i]] and find[s2[i]] == have[s2[i]]) - int(find[s2[i + len(s1)]] and find[s2[i + len(s1)]] == have[s2[i + len(s1)]])

        have[s2[i + len(s1)]] += 1
        same += int(find[s2[i + len(s1)]] == have[s2[i + len(s1)]])

    return same == len(find)
