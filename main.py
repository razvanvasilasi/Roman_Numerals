class RomanNumerals:

    def to_roman(number):
        num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12
        result = ''
        while number:
            div = number // num[i]
            number %= num[i]
  
            while div:
                result+=sym[i]
                div -= 1
            i -= 1
        return result
    
    def from_roman(n):
        values = {'I': 1,'IV':4, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'Z':0}
        n+='Z'
        result = 0
        for i in range(len(n)-1):
            if values[n[i]]<values[n[i+1]]:
                result-=values[n[i]]
            else:
                result+=values[n[i]]
        return result
