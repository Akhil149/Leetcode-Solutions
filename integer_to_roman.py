'''
12. Integer to Roman

Seven different symbols represent Roman numerals with the following values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
Given an integer, convert it to a Roman numeral.

 

Example 1:

Input: num = 3749

Output: "MMMDCCXLIX"

Explanation:

3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
Example 2:

Input: num = 58

Output: "LVIII"

Explanation:

50 = L
 8 = VIII
Example 3:

Input: num = 1994

Output: "MCMXCIV"

Explanation:

1000 = M
 900 = CM
  90 = XC
   4 = IV
 

Constraints:

1 <= num <= 3999
'''

class Solution:
    def intToRoman(self, num: int) -> str:
        int_to_roman = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}

        roman_res = ""

        for value, symbol in int_to_roman.items():
            temp = num // value

            roman_res += (symbol * temp)

            num -= value * temp

            if num == 0:
                break

        return roman_res
    
'''
Another solution I got 

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        int_to_roman = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}

        roman_res = ""

        temp = num

        while temp>0:
            if temp >= 1 and temp < 4:
                temp -= 1
                roman_res += int_to_roman[1]
            elif temp == 4:
                temp -= 4
                roman_res += int_to_roman[4]
            elif temp >= 5 and temp <9:
                temp -= 5
                roman_res += int_to_roman[5]
            elif temp == 9:
                temp -= 9
                roman_res += int_to_roman[9]
            elif temp >= 10 and temp < 40:
                temp -= 10
                roman_res += int_to_roman[10]
            elif temp >= 40 and temp < 50:
                temp -= 40
                roman_res += int_to_roman[40]
            elif temp >= 50 and temp < 90:
                temp -= 50
                roman_res += int_to_roman[50]
            elif temp >= 90 and temp < 100:
                temp -= 90
                roman_res += int_to_roman[90]
            elif temp >= 100 and temp < 400:
                temp -= 100
                roman_res += int_to_roman[100]
            elif temp >= 400 and temp < 500:
                temp -= 400
                roman_res += int_to_roman[400]
            elif temp >= 500 and temp < 900:
                temp -= 500
                roman_res += int_to_roman[500]
            elif temp >= 900 and temp < 1000:
                temp -= 900
                roman_res += int_to_roman[900]
            else:
                temp -= 1000
                roman_res += int_to_roman[1000]
        return roman_res
'''