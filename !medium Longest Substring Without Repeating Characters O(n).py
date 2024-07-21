def lengthOfLongestSubstring(self, s: str) -> int:
    longest, start, explored = 0, 0, set()

    for char in s:
        longest = max(longest, len(explored))

        while char in explored:
            explored.remove(s[start])
            start += 1

        explored.add(char)

    return max(longest, len(explored))
