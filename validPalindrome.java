/*
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
*/


class Solution {
    public boolean isPalindrome(String s)   {
        // convert the string to lowercase using toLowerCase() method
        String lowerCaseString = s.toLowerCase();

        // remove the non-alphanumeric characters using replaceAll() method
        // and the regular expression "[^a-ZA-Z0-9]"
        String alphaNumericString = lowerCaseString.replaceAll("[^a-zA-Z0-9]", "");

        // check if the resulting string is equal to its reverse
        // using the StringBuilder class 
        String reversedString = new StringBuilder(alphaNumericString).reverse().toString();
        return alphaNumericString.equals(reversedString);

    }
}
