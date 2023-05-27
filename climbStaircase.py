class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Input: n   desired number of steps
        Output: Number of distinct ways to climb to top
        When climbing the staircase, you have 2 options at each step, you can either take one step or two steps. For a staircase with only one step, theres only one way to reach the top, take a single step.
        If the staircase has 2 steps, there are 2 ways to reach the top, either by taking two individual steps or by taking a single two-step leap.
        For a staircase with 3 steps, there are the following possibilities:
        1. Start with a single step, and there are 2 steps remaining, you can solve this subproblem by considering the number of distinct ways to climb a 2-way staircase.
        2. Start with a two-step leap then there is one way remaining. 
        3. The number of distinct ways to climb a 3-step staircase is the sum of all the distinct ways to climb a 2-step staircase and a 1-step staircase
        4. By observing this pattern you can see that the number of distinct ways to reach the top of a staircase with n steps can be obtained by summing the number of different ways to reach the (n-1) step and the (n-2) step.
        5. F(i) = F(i-1) + F(i-2)
        We can solve this problem from the base cases. For the first two steps we can directly climb to them in only one way, so we have F(1) = 1 and F(2) = 2
        6. Using the recurrence relation F(i) = F(i-1) + F(i-2) we can find F(n), which represents the number of distinct ways to reach the top of the staircase.

        """
        if n <= 2:
            return n
        
        #create a list to store the number of distinct ways for each step
        dp = [0] * (n+1)
        #only one way to reach the first two steps
        dp[1] = 1
        dp[2] = 2

        #iterate from the 3rd step up to the desired n
        for i in range(3, n+1):
            #the number of distinct ways to reach the current step is the sum of the ways to reach the previous steps
            dp[i] = dp[i-1] + dp[i-2]
        #the value at index n represents the number of distinct ways to reach the top
        return dp[n]


        """
        Example walkthrough:
        If n = 5
        1. Initialize the dp list to store the number of distinct ways for each step.
            dp = [0] * (5+1) = dp[6]
            dp = [0, 0, 0, 0, 0, 0]
        2. Set the base cases: dp[1] = 1 && dp[2] = 2
            dp = [0, 1, 2, 0 0 0]
        3.Iterate from the 3rd step up to the desired  n, its n+1 ceiling because theres no <= or >=, so we need to go up 1 so that number (5) is included.
        4. Calculate the number of distinct ways by summing the ways to reach the previous 2 steps
        for i = 3: dp[3] = dp[2] + dp[1] = 2 + 1 = 3
        dp = [0, 1, 2, 3, 0 , 0]
        for i = 4: dp[4] = dp[3] + dp[2] = 3 + 2 = 5
        dp = [0, 1, 2, 3, 5. 0]
        for i = 5: dp[4] + dp[3] = 5 + 3 = 8 
        dp = [0, 1, 2, 4, 6, 8]
        5. Update dp list: [0, 1, 2, 3, 5, 8]
        6. Return the value at index 'n' (5) from the dp list: 8, so there are 8 distinct ways to climb the staircase.



        """
