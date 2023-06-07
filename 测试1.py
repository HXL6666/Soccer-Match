def abc(s: str) -> str:
    # 接收一个长度为n的字符串
    n = len(s)
    # 如果字符串只有1个或0个字符，其本身就是回文串
    if n < 2:
        return s
    # 用0初始化一个nxn的动态数组
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    maxlen = 0
    begin = 0

    for j in range(1, n):
        for i in range(0, j):
            if (s[i] == s[j]) and dp[i + 1][j - 1]:
                dp[i][j] = 1
                # 判断是否为最长回文字串
                if j - i > maxlen:
                    maxlen = j - i
                    begin = i

    return s[begin:begin + maxlen]


print(abc("asdfgdfgfd"))
