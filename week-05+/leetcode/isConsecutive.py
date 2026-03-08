class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i = 0 # s pointer/index
        j = 0 # t pointer/index

        s_complete = ""

        # print("i: ", i)
        # print("j: ", j)
        if s[i] == t[j]:
            s_complete += s[i]
            i += 1
            j += 1
        else:
            while s[i] != t[j]:
                j += 1
                if j >= len(t):
                    return False

        # print(s_complete)
        if s_complete == s:
            return True
        
        return False


