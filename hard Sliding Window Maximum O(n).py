def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    slide = deque([k - 1])

    for i in range(k - 2, -1, -1):
        if nums[slide[0]] < nums[i]:
            slide.appendleft(i)

    window = [nums[slide[0]]]

    for i in range(len(nums) - k):
        if slide[0] == i:
            slide.popleft()

        while slide and nums[slide[-1]] < nums[i + k]:
            slide.pop()

        slide.append(i + k)
        window.append(nums[slide[0]])

    return window
