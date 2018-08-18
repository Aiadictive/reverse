class Solution:
    def reverse(self, x):
        """
        :type x: int(32位 python并没有限制int的大小，不会溢出自动变成长型整数)
        :rtype: int
        """
        maxsize=0
        i=0
        
        while i<31:
            maxsize=maxsize+pow(2,i)
            i=i+1
        minsize=-maxsize-1
        rev = 0
        if x<0:
            while (x != 0):
                pop = -((-x) % 10)
                x = -((-x)//10)
                if (rev < -((-minsize)//10) or (rev == -((-minsize)//10) and pop < -8)):
                    return 0
                rev = rev * 10 + pop
            return rev            
        else:
            while (x != 0):
                pop = x % 10
                x = x//10
                if (rev > maxsize//10 or (rev == maxsize // 10 and pop > 7)):
                    return 0
                rev = rev * 10 + pop
            return rev

def main():
    sol=Solution()
    print(sol.reverse(-3563847413))
if __name__=='__main__':
    main()