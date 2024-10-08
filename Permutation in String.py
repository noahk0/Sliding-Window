def checkInclusion(self, s1: str, s2: str) -> bool:
    same, find, have = 0, Counter(s1), Counter(s2[:len(s1)])

    for c in find:
        same += find[c] == have[c]

    for i in range(len(s2) - len(s1)):
        if same == len(find):
            return True

        same -= find[s2[i]] == have[s2[i]]
        have[s2[i]] -= 1

        same += (find[s2[i]] and find[s2[i]] == have[s2[i]]) - (find[s2[i + len(s1)]] and find[s2[i + len(s1)]] == have[s2[i + len(s1)]])

        have[s2[i + len(s1)]] += 1
        same += find[s2[i + len(s1)]] == have[s2[i + len(s1)]]

    return same == len(find)
