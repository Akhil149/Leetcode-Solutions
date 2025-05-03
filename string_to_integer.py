class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip()
        res_s = ""
        if s == "" or s == "+" or s == '-':
            return 0
        for i in range(len(s)):
            if (s[i] == '-' or s[i] == "+") and res_s == "":
                if not s[i+1].isdigit():
                    res_s += "0"
                    break
                res_s += s[i]
            elif s[i].isdigit():
                res_s += s[i]
            else:
                if res_s == "":
                    res_s += "0"
                break
        res = int(res_s)
        if res < pow(-2, 31):
            res = pow(-2,31)
        elif res > (pow(2, 31) - 1):
            res = pow(2,31)-1
        return res
    

'''
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        res_s = ""
        if s == "" or len(s) == 1:
            if s.isdigit():
                return int(s)
            return 0
        for i in range(len(s)):
            if (s[i] == " " and res_s == "" ):
                pass
            elif ((s[i] == "-" or s[i] == "+") and res_s == "" ):
                if not s[i+1].isdigit():
                    res_s += "0"
                    break
                res_s +=s[i]
                
            elif(s[i].isdigit()):
                res_s +=s[i]
            else:
                if res_s == "":
                    res_s += "0"
                break
        if res_s == "":
            return 0
        res = int(res_s)
        if res < pow(-2, 31):
            res = pow(-2,31)
        elif res > (pow(2, 31) - 1):
            res = pow(2,31)-1
        return res
'''