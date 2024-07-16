def minWindow(self, s: str, t: str) -> str:
    find, d = Counter(t), Counter(s[:len(t)])

    if d == find:
        return s[:len(t)]

    l, have, win = 0, 0, [0, len(s)]

    for char in find:
        have += int(find[char] <= d[char])

    for r in range(len(t), len(s)):
        d[s[r]] += 1
        have += int(d[s[r]] == find[s[r]])

        while l < len(s) and find[s[l]] < d[s[l]]:
            d[s[l]] -= 1
            l += 1

        if have == len(find):
            if r + win[0] < l + win[1]:
                win = l, r

            d[s[l]] -= 1
            l += 1
            have -= 1

    return '' if win[1] == len(s) else s[win[0] : win[1] + 1]
