"""
The count-and-say sequence is a sequence of digit strings defined by the
recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from
countAndSay(n-1), which is then converted into a different digit string.

To determine how you "say" a digit string,
    1. split it into the minimal number of groups so that each group is a
    contiguous section all of the same character.
    2. Then for each group, say the number of characters, then say the
    character.
    3. To convert the saying into a digit string, replace the counts with a
    number and concatenate every saying.


# 2 pointer
 1 Counter and character pointer set at 0. Counter pointer advances until
   character is not the same as the current char. Character pointer holds the
character itself.
 2 Translate pointer results until end of string into digit.
 3 Redo on the length of the string of digits n times.

"""



class Solution:
    def countAndSay(self, n: int) -> str:


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
