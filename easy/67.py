'''

二进制求和

'''


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """


        '''
        用现成的方法  是最快的 
        return bin(int(a, 2) + int(b, 2))[2:]
        '''
        new = list(str(int(a) + int(b)))
        check = True
        temp_list = ""
        for i in range(len(new)-1,-1,-1):

            if int(new[i]) <= 1:
                temp_list = new[i] + temp_list
                check = True
            else:
                if new[i] == "2":
                    temp_list = "0" + temp_list
                else:
                    temp_list = "1" + temp_list
                check = False
                new[i-1] = str(int(new[i-1])+1)
        if not check :
            temp_list = "1" + temp_list
        return temp_list
a = Solution()
print(a.addBinary("1111","1111"))