
s = 'PAYPALISHIRING'
numRows = 3
o = 'PAHNAPLSIIGYIR'
def conversion(s, numRows):

    increament = 2 * (numRows - 1)
    result = ""

    if numRows ==1:
        return s
    else:

        for r in range(numRows):
            for i in range(r, len(s), increament):
                result += s[i]
                if i>0 and i<numRows-1 and i+increament-2*r<len(s):
                    result+=s[i+increament-2*r]

        return result

print(conversion("PAYPALISHIRING", 4))