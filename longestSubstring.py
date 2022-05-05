# s = "abcabcbb"
#Output: 3
s = 'pwweku'
# s = "au"
def lengthOfLongestSubstring(s: str) -> int:
    temp_list = []
    if len(s)==0:
        return 0
    else:
        for i in range(len(s)):
            temp_string = s[i]
            temp_alpha = []
            temp_alpha.append(s[i])
            for j in range(i+1, len(s)):
                if s[j] not in temp_alpha:
                    temp_string += s[j]
                    temp_alpha.append(s[j])
                    if j == len(s) - 1:
                        temp_list.append(len(temp_string))
                else:
                    print(temp_string)
                    temp_list.append(len(temp_string))
                    break
        print("temp_list ", temp_list)
        if len(temp_list)!=0:
            return max(temp_list)
        else:
            return 1

print(lengthOfLongestSubstring(s))
