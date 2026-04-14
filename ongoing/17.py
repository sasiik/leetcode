class Solution:

    def reduce(self, array: list[str]):
        # reduce function
        res = 1
        for elem in array:
            res *= len(elem)
        return res

    def letterCombinations(self, digits: str) -> list[str]:
        from functools import reduce

        # initial mapping and filtered letters we need
        mapping = ['', 'abc', 'def', 'ghi',
                   'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        letters = [mapping[int(dig)-1]
                   for dig in digits]

        # first step: compute complexity, create a res array, subtract 1 iteration cycle
        complexity = self.reduce(letters)
        res = ['' for _ in range(complexity)]

        # getting current working letters, then assigning the letter computed with complexity to the right list index, changing complexity
        for i in range(len(letters)):
            current_letters = letters[i]
            complexity //= len(current_letters)
            c = 0
            while c < len(res):
                current_letter = current_letters[c //
                                                 complexity % len(current_letters)]
                res[c] += current_letter
                c += 1

        return res


sol = Solution()
print(sol.letterCombinations("23"))
print(sol.letterCombinations("2"))
print(sol.letterCombinations("8"))
print(sol.letterCombinations("22"))
