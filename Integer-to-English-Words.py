class Solution:
    def numberToWords(self, num: int) -> str:
        # max num = 2 147 483 647
        if num == 0:
            return 'Zero'
        idx = 0 
        billions = 0
        millions = 0
        thousands = 0
        ones = 0
        if num // 1e9 != 0:
            billions += num // 1e9
            num = num % 1e9
        if num // 1e6 != 0:
            millions += num // 1e6
            num = num % 1e6
        if num // 1e3 != 0:
            thousands += num // 1e3
            num = num % 1e3
        ones += num
    
        def printHundred(num):
            my_set = {  10: 'Ten',
                        20: 'Twenty',
                        30: 'Thirty',
                        40: 'Forty',
                        50: 'Fifty',
                        60: 'Sixty',
                        70: 'Seventy',
                        80: 'Eighty',
                        90: 'Ninety'    }
            my_set2 = { 11: 'Eleven',
                        12: 'Twelve',
                        13: 'Thirteen',
                        14: 'Fourteen',
                        15: 'Fifteen', 
                        16: 'Sixteen', 
                        17: 'Seventeen',
                        18: 'Eighteen',
                        19: 'Nineteen', }
            my_set3 = { 1: 'One',
                        2: 'Two',
                        3: 'Three',
                        4: 'Four',
                        5: 'Five',
                        6: 'Six',
                        7: 'Seven',
                        8: 'Eight',
                        9: 'Nine'   }
            my_str = ""
            if num // 100 != 0:
                my_str += my_set3[num//100] + " Hundred "
                num = num % 100
            if num in my_set2:
                my_str += my_set2[num] + " "
                return my_str
            if num // 10 != 0:
                my_str += my_set[(num//10)*10] + " "
                num = num % 10
            if num != 0:
                my_str += my_set3[int(num)] + " "
            return my_str

        ret_str = ""
        if billions != 0:
            ret_str += printHundred(billions) + "Billion "
        if millions != 0:
            ret_str += printHundred(millions) + "Million " 
        if thousands != 0:
            ret_str += printHundred(thousands) + "Thousand " 
        if ones != 0:
            ret_str += printHundred(ones)
        return ret_str.strip()