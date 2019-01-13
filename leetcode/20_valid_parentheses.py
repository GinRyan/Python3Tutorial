"""给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。

注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true

示例 2:

输入: "()[]{}"
输出: true

示例 3:

输入: "(]"
输出: false

示例 4:

输入: "([)]"
输出: false

示例 5:

输入: "{[]}"
输出: true
"""
"""
题解：这个其实跟消消乐很像，其实就是二消游戏，不是三消

有效规则示例: 

{}[]{[()]()}

"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        parDict = {
            "(": ")", 
            "[": "]", 
            "{": "}"}
        nump = 0
        tempCache = []
        while nump < len(s):
            osymb = s[nump]
            #当遇到存在于字典的括号的时候，是存储
            if osymb in parDict:
                tempCache.append(parDict[s[nump]])
            #当遇到不存在于字典的括号的时候，是读取
            elif len(tempCache) > 0 :
                if tempCache[-1] == osymb:
                    del tempCache[-1]
                else:
                    print(tempCache)
                    return False
            else:
                return False
            nump += 1
        print(tempCache)
        return len(tempCache) == 0
        
print(Solution().isValid("{}[]{[()]()}"))#true
# print(Solution().isValid(""))#true
# print(Solution().isValid("]"))#false
# print(Solution().isValid("()"))#true
# print(Solution().isValid("()[]{}"))#true
# print(Solution().isValid("([)]"))#false
# print(Solution().isValid("{[]}"))#true
# print(Solution().isValid("(]"))#false
# print(Solution().isValid("{}[]{[()]()}"))#true
# print(Solution().isValid("{}[]{[(})]()}"))#false