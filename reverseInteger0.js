function reverse(x) {
    // Define the limit for a 32-bit signed integer.
    const limit = 2147483648; // 2^31

    // Check if x is negative or positive, store it in k.
    // This is done so that we can multiply the reversed number by k later to restore its original sign.
    const k = x < 0 ? -1 : 1;

    // Reverse the absolute value of the number.
    // First, get the absolute value of x, then turn it into a string.
    // After that, split the string into an array of characters, reverse the array, and join it back into a string.
    // Finally, turn the string back into a number.
    const n = Number(String(Math.abs(x)).split('').reverse().join(''));

    // If the reversed number exceeds the limit for a 32-bit signed integer, return 0.
    // Otherwise, return the reversed number multiplied by k to restore its original sign.
    return n > limit ? 0 : n * k;
}
