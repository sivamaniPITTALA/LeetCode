from collections import Counter

MAX_BASKETS = 2

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        return self.ensure_first_that_fruit_can_be_added(fruits)

    @staticmethod
    def ensure_first_that_fruit_can_be_added(fruits: list[int]) -> int:
        cnt = Counter()
        output, w_start = 0, 0

        for w_end, t in enumerate(fruits):
            if cnt[t] == 0:
                while len(cnt) == MAX_BASKETS:
                    cnt[x := fruits[w_start]] -= 1

                    if cnt[x] == 0:
                        cnt.pop(x)

                    w_start += 1
            cnt[t] += 1
            output = max(output, w_end - w_start + 1)

        return output

    @staticmethod
    def ensure_later_that_fruit_can_be_added(fruits: list[int]) -> int:
        cnt = Counter()
        output, w_start = 0, 0

        for w_end, t in enumerate(fruits):
            cnt[t] += 1
            while len(cnt) > MAX_BASKETS:
                cnt[x := fruits[w_start]] -= 1

                if cnt[x] == 0:
                    cnt.pop(x)

                w_start += 1

            output = max(output, w_end - w_start + 1)

        return output