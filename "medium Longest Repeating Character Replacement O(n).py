def characterReplacement(self, s: str, k: int) -> int:
    left, freq, count = 0, 1, defaultdict(int)

    for right in range(len(s)):
        count[s[right]] += 1
        freq = max(freq, count[s[right]])

        if left + k + freq <= right:
            count[s[left]] -= 1
            left += 1

    return right - left + 1
