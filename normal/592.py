class Solution:
    def fractionAddition(self, expression: str) -> str:
        def gcd(a,b):   #最大公约数
            return b if a%b==0 else gcd(b,a%b)      

        def lcm(a,b):     #最小公倍数
            return int(a*b/gcd(a,b))
        
        if expression.count('/')==1:return expression
        expression=expression.replace('-','+-')
        tmp=expression.split('+')
        tmp1=[]
        for x in tmp:
            if len(x):
                y=x.split('/')
                tmp1.append((int(y[0]),int(y[1])))                
        fm,fz=1,0
        for x in tmp1:
            fm=lcm(fm,x[1])
        for x in tmp1:
            fz+=x[0]*(fm//x[1])
        if fz==0:return '0/1'
        gys=gcd(fm,abs(fz))
        return str(fz//gys)+'/'+str(fm//gys)
