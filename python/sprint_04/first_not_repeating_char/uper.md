# First Non-Repeated Character

## Prompt
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

Example 1 
- For `s = "abacabad"`, the output should be 
  `first_not_repeating_character(s) = 'c'`.
- There are 2 non-repeating characters in the string: `"c"` and `"d"`. Return `"c"` since it appears in the string first.

Example 2
- For `s = "abacabaabacaba"`, the output should be
- `first_not_repeating_character(s) = '_'`.

There are no characters in this string that do not repeat.

[execution time limit] 4 seconds (py3)

[input] string s

A string that contains only lowercase English letters.

[output] char

The first non-repeating character in s of '_' if there are no characters that do not repeat.

