class Fraction():
    def __init__(self,fz,fm):
        self.__fz = fz
        if fm == 0:
            raise ValueError('分母不能为0')
        else:
            self.__fm =fm
    @property   # 装饰器
    def fz(self):
        return self.__fz
    @property   # 装饰器
    def fm(self):
        return self.__fm

    
    # 将分子和分母转换成分数格式
    def transform(self):
        min_value = min(self.__fz,self.__fm)
        max_value = max(self.__fz,self.__fm)
        while max_value % min_value != 0:
            temp = max_value % min_value
            max_value = min_value
            min_value = temp
        self.__fz //= min_value
        self.__fm //= min_value
        if self.__fm == 1:
            str = "{fz}".format(fz=self.__fz)
        else:
            str ="{fz}/{fm}".format(fz=self.__fz, fm=self.__fm)
        return str

#  定义一个计算类，这个类专门进行分数的加，减，乘，除
class Calculater():
    def adjust(self,f1,f2,sign):    #  定义函数，函数的参数为分数一，分数二，运算符
        sign = sign.strip(' ')
        if sign == '+':
            fz = f1.fz * f2.fm + f1.fm * f2.fz
        elif sign == "-":
            fz = f1.fz * f2.fm - f1.fm * f2.fz
        elif sign == '*':
            fz = f1.fz * f2.fz
        elif sign == "/":
            fz = f1.fz * f2.fm
        else:
            print("当前只支持加减乘除四则运算")
            return 0
        if sign =="/":
            fm = f1.fm*f2.fz
        else:
            fm = f1.fm*f2.fm
        
    # 创建分数
        fs = Fraction(fz,fm)
        return fs.transform()
    
fz1 = int(input("请输入第一个分数的分子: "))#  强制类型转换，将输入的字符型转换成能运算的整形
fm1 = int(input("请输入第一个分数的分母: "))

fz2 = int(input("请输入第二个分数的分子: "))
fm2 = int(input("请输入第二个分数的分母: "))
sign = input("请输入要进行的运算: ")

f1 = Fraction(fz1,fm1)
f2 = Fraction(fz2,fm2)
mf = Calculater()
result = mf.adjust(f1, f2,sign)
print(result)


