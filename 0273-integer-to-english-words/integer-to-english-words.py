# -*- coding:utf-8 -*-


# Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
#
# Example 1:
#
#
# Input: 123
# Output: "One Hundred Twenty Three"
#
#
# Example 2:
#
#
# Input: 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
#
# Example 3:
#
#
# Input: 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
#
#
# Example 4:
#
#
# Input: 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
#
#


class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return 'Zero'
        nums=[]
        while num>999:
            nums.append(str(num)[-3:])
            num/=1000
        if num>99:
            nums.append(str(num))
        elif num>9:
            nums.append('0'+str(num))
        else:
            nums.append('00'+str(num))
        ans = ''
        for i in range (len(nums)-1,-1,-1):
            for ii in range (0,3):
                if ii!=1:
                    if nums[i][ii]=='1':
                        ans+='One '
                    elif nums[i][ii]=='2':
                        ans+='Two '
                    elif nums[i][ii]=='3':
                        ans+='Three '
                    elif nums[i][ii]=='4':
                        ans+='Four '
                    elif nums[i][ii]=='5':
                        ans+='Five '
                    elif nums[i][ii]=='6':
                        ans+='Six '
                    elif nums[i][ii]=='7':
                        ans+='Seven '
                    elif nums[i][ii]=='8':
                        ans+='Eight '
                    elif nums[i][ii]=='9':
                        ans+='Nine '
                    if ii==0 and nums[i][ii]!='0':
                        ans+='Hundred '
                if ii==1:
                    if nums[i][ii]=='2':
                        ans+='Twenty '
                    elif nums[i][ii]=='3':
                        ans+='Thirty '
                    elif nums[i][ii]=='4':
                        ans+='Forty '
                    elif nums[i][ii]=='5':
                        ans+='Fifty '
                    elif nums[i][ii]=='6':
                        ans+='Sixty '
                    elif nums[i][ii]=='7':
                        ans+='Seventy '
                    elif nums[i][ii]=='8':
                        ans+='Eighty '
                    elif nums[i][ii]=='9':
                        ans+='Ninety '
                    elif nums[i][ii]=='1':
                        if nums[i][2]=='0':
                            ans+='Ten '
                        elif nums[i][2]=='1':
                            ans+='Eleven '
                        elif nums[i][2]=='2':
                            ans+='Twelve '
                        elif nums[i][2]=='3':
                            ans+='Thirteen '
                        elif nums[i][2]=='4':
                            ans+='Fourteen '
                        elif nums[i][2]=='5':
                            ans+='Fifteen '
                        elif nums[i][2]=='6':
                            ans+='Sixteen '
                        elif nums[i][2]=='7':
                            ans+='Seventeen '
                        elif nums[i][2]=='8':
                            ans+='Eighteen '
                        elif nums[i][2]=='9':
                            ans+='Nineteen '
                        break
            if i==1 and nums[i]!='000':
                ans+='Thousand '
            elif i==2 and nums[i]!='000':
                ans+='Million '
            elif i==3 and nums[i]!='000':
                ans+='Billion '
        return ans[:-1]
