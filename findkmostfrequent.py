from collections import Counter
class Solution:
    """
    Given an integer array nums and an integer k, return the k most frequent elements, you may return the answer in any order
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
    """
    use a dictionary to count the frequency of each element and then sorting the dictionary by frequency to find the k most frequent elements
    sort the dictionary by frequency in descending order
    frequency.items() returns a list of key-value pairs from the frequency dictionary
    each key-value pair is represented as a tuple: key,value
    sorted() returns a new sorted list from the items in the given iterable.
    in this case it takes the list of key-value pairs from frequency.items() as the input
    the key parameter of the sorted() function is set to 'lambda x: x[1]', this means
    that the second element of each tuple x[1] which represents the frequency value
    should be used as the basis for sorting, this means that the sorting will be
    based on the frequencies of the elements
    The reverse=true parameter is set to sort the list in descending order from 
    highest to lowest frequency
    after executing the line, the sorted_Frequency variable will contain a list of 
    key,value pairs from the frequency dictionary sorted based on the values
    (frequencies) in descending order
    """
        sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

        """
        get the k most freq elements
        sorted_frequency[:k] is a list slicing operation that retrieves the first k 
        elements from the sorted_frequency list, since its already sorted in
        descending order, it gives us the k most frequent elements
        the list comprehension iterates over the selected elements from the list
        and extracts only the num value from each key-value pair, it creates a new list 
        called top_k that contains these num values

        """
        top_k = [num for num, freq in sorted_frequency[:k]]
        return top_k
