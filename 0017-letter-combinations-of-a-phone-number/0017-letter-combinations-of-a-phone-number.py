class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
        '2' : 'abc', '3' : 'def', '4': 'ghi', '5':'jkl',
        '6':'mno', '7':'pqrs', '8':'tuv' , '9':'wxyz'
        }  

        result = []
        def solve(index=0,current_string=''):
            if index == len(digits):
                result.append(current_string)
                return

            current_digit = digits[index]
            letters = mapping[current_digit]

            for letter in letters:
                solve(index+1,current_string+letter)

        solve(0,"")
        return result

        