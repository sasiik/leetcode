class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        l = 0
        r = len(s) - 1
        for i in range(len(p)):
            if i+1 < len(p) and p[i+1] == "*":  # if we catch an asterisk pattern
                if p[i] == '.':  # if we have a ".*" case
                    if i+2 < len(p):  # if we have a ".*a" case
                        # we should move the right cursor towards left until "a" is met
                        while s[r] != p[i+2]:
                            print("R cycle, R:", r)
                            r -= 1
                            if r < 0:
                                break  # if we reach the left end, we break, but we dont return false yet
                            # maybe "a" is an asterisk, then it shouldn't return false yet
                    else:
                        return True  # else, we just return true
                else:  # if we have a "a*" case
                    # we should move the left cursor until the other letter than "a" is met
                    while s[l] == p[i]:
                        print("L cycle, L:",
                              l)
                        l += 1
                        if l >= len(s):
                            # again, we only break here. other checks later
                            break
            elif p[i] == '.':  # if we catch a dot
                if i >= len(s):  # here, only if i is bigger than length of the string, we return false
                    # it doesn't matter if the cursors are at the edges in the dot's case
                    return False
            else:  # if we catch a normal letter
                # here, cursorc do actually matter
                if i >= len(s) or p[i] != s[i] or r < 0 or l >= len(s):
                    # here we catch the cursors being at the edges case
                    return False
        # if all the checks have passed, return True
        return True


sol = Solution()
print(sol.isMatch('aa', 'a'))
print(sol.isMatch('aa', 'a*'))
print(sol.isMatch('ab', '.*'))
print(sol.isMatch('aab', 'c*a*b'))  # wrong case: i have false, should be true
