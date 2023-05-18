class Solution:
    """
    Given a string s and a dictionary of strings
    wordDict, return true if s can be segmented into
    a space-separated sequence of one or more   dictionary words
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        To solve the problem of determining whether a given string s can be segmented into
        a space-separated sequence of one or more dictionary words from 'wordDict' you can use
        a dynamic programming approach.
        """
        #store the words from wordDict in a set
        wordSet = set(wordDict)

        #stores the length of the string s
        n = len(s)

        #initialized with false values
        #dp[i] represents whether the substring s[0:i] can be segmented into words from wordDict
        dp = [False] * (n+1)

        #dp[0] is initialized as True bc an empty string could be segmented into an empty sequence
        dp[0] = True

        #nested loops iterate over the string indices. 
        #outer loop iterates from first character to the last character of s (inclusive)
        for i in range(1, n+1):

            #inner loop iterates from the start of the string up to the current index (j<1)
            for j in range(i):

                #it checks the substring s[j:i] (from index j to i) is a word in wordDict
                #it checks if dp[j] is True, if both conditions are satisfied it means that
                #s[0:i] can be segmented into words from wordDict
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
            

        #function returns dp[n] which represents whether the entire string s can be 
        #segmented into words from wordDict
        return dp[n]
