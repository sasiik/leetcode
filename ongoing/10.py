class Solution:
    def checkPattern(self, st: str, pat: str) -> None | int:
        # GOTTA FIND THE MOST RIGHT PATTERN
        # SHOULD RETURN THE ENDING INDEX
        # checks only for the patterns without *, gotta clean first
        cur = None
        for i in range(len(st)):
            for j in range(len(pat)):
                if pat[j] != st[i]:
                    break  # pattern doesn't satisfy
            else:
                if cur == None:
                    # initial cur setup if pattern exists
                    cur = i + len(pat) - 1
                if i > cur:
                    # pattern satisfies, return its starting index in the string
                    cur = i + len(pat) - 1
        return cur  # returns None if no pattern found

    def cleanAsteriskLetters(self, p: str) -> list[str] | None:
        p_len = len(p)
        res = []
        cur_block = ""
        for i in range(p_len):
            if i+1 >= p_len and p[i] != "*":  # if reached the end of the string
                cur_block += p[i]
                res.append(cur_block)
            else:  # if not reached yet
                if p[i] == '*':  # if asterisk, just skip it
                    continue
                if p[i+1] == "*":  # if asterisk comes in 1 iteration, save and clean current block
                    res.append(cur_block)
                    cur_block = ""
                else:  # if just a letter or a dot, save into the block
                    cur_block += p[i]
        if not res:
            return None
        if len(res) > 0 and all(len(item) == 0 for item in res):
            return None
        return res

    def isMatch(self, s: str, p: str) -> bool:
        blocks = self.cleanAsteriskLetters(p)
        if not blocks:
            return True  # no blocks -> each symbol is asterisk -> any string suits
        cur = 0  # cursor
        for pat_block in blocks:
            if not pat_block:
                continue
            ending_index = self.checkPattern(s, pat_block)
            if not ending_index:
                # could find any pattern in the string matching for the block
                # therefore useless to continue
                return False
            if cur > ending_index:
                cur = ending_index
            else:
                return False  # means that there is no pattern block following the previous one, the whole chain breaks
        return True  # if none of block has thrown an error, we return True


sol = Solution()
print(sol.isMatch('aa', 'a'))
print(sol.isMatch('aa', 'a*'))
print(sol.isMatch('ab', '.*'))
print(sol.isMatch('aab', 'c*a*b'))  # wrong case: i have false, should be true
# print(sol.cleanAsteriskLetters("a*bc.c*ba*a"))
# print(sol.cleanAsteriskLetters("a*c*a*"))
# print(sol.cleanAsteriskLetters('a*bc.f*.*hahn*ac*'))
