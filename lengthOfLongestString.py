class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        To find the length of the longest substring without repeating characters in a given string s, we can use the sliding window technique with a set to track the characters in the current window.
        :type s: str
        :rtype: int
        """
        #initialize max_length to 0, it'll store the length of the longest substring
        max_length = 0
        #initialize left to 0, it'll keep track of the left boundary of the current window
        left = 0
        #initialize an empty set, 'seen', to track the characters in the current window.
        seen = set()

        #iterate through each character, 'c', in the string 's'. 
        for i in range(len(s)):
            #while c is already in the seen set
            while s[i] in seen:
                #remove the character at the left boundary s[left] from the seen set
                seen.remove(s[left])
                #increment left by 1 to slide the window to the right
                left += 1
            #add c to the seen set
            seen.add(s[i])
            #update max_length if the length of the current window , i - left + 1 is greater than max_length 
            max_length = max(max_length, i - left + 1)
            #return max_len which represents the length of the longest substring without repeating characters.
        
        return max_length



        """
        Example input s = "abcabcbb"
        1. Initialize max_len to 0 and left to 0
        2. Initialize empty set seen
        3. Iterate through every character in 's':
            a. for i = 0 and s[i] = 'a': add a to the seen set and update max_length to 1 (0 - 0 + 1)
            b. for i = 1 and s[i] = 'b': add b to the seen set and update max_length to 2(1-0+1)
            c. for i = 2 and s[i] = 'c': add c to the seen set and update max_length to 3(3-0+1)
            d. for i = 3 and s[i] = 'a': 'a' is in the seen set so remove 'a' from the seen set and increment 'left' by 1. Then add a to the seen set. Update max_length to 3(3-1+1).
            e. for i = 4 and s[i] = 'b': 'b' is in the seen set so remove 'b' from the seen set and increment 'left' by 1. Then add b to the seen set. Update max_length to 3(4-2+1)
            f. for i = 5 and s[i] = 'c': 'c' is in the seen set so remove 'c' from the seen set and increment left by 1 and add c to the seen set and update max_len to 3(5-3+1)
            e. for i = 6 and s[i] = 'b': 'b' is not in the seen set (sliding window) so add b to the seen set, and update max_length to 4( 6-3+1).
            f. Return max_length which is 4 in this case.
            Therefore the length of the longest substring w/o repeating characters in the input string "abcabcbb" is 4.
            

        """
