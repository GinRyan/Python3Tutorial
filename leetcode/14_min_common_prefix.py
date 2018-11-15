"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"

示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:

所有输入只包含小写字母 a-z 。
"""
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 最小字符串长度，只搜索这么长
        min_len = -1

        for str0 in strs:
            strlen = len(str0)
            # 如果遇到0长度，直接停止返回空字符串
            if strlen == 0:
                return ""
            # 初始化
            if min_len == -1:
                min_len = strlen
            # 比对最小值并且赋值
            min_len = min(min_len, strlen)

        offset = 0
        stt =  ""
  
        while offset < min_len:
             
            
            temp = ""
            for i, stt in enumerate(strs):
                if i == 0:
                    temp = stt[offset]
                if temp != stt[offset]:
                    return stt[0: offset]

            offset += 1

        return stt[0:offset]

print(Solution().longestCommonPrefix(["flower","flow","flight"]))