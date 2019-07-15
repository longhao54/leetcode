#!/usr/bin/env python
#_*_coding:utf-8_*_

import re

def is_symbol(element):  #判断格式化后的数学表达式 是运算符 还是数字
    res=False
    symbol=['+','-','*','/','(',')']
    if element in symbol:
        res=True
    return res


def priority(top_sym,wait_sym):  #优先级比较  栈顶元素，待入栈元素
    '''
    判断传入的 栈顶元素 和 待入栈元素
    > 取出运算符栈的栈顶，取出两次数字栈的栈顶 进行运算
    < 加入符号栈栈顶
    = 取出符号栈栈顶
    :param top_sym:
    :param wait_sym:
    :return:
    '''
    # print('from the priotry : ',ltop_sym,wait_sym)
    level1=['+','-']
    level2=['*','/']
    level3=['(']
    level4=[')']
    #运算符栈顶元素为 + -
    if top_sym in level1:
        if wait_sym in level2 or wait_sym in level3:
            return '<'
        else:
            return '>'

    #运算符栈顶元素为 * /
    elif top_sym in level2:
        if wait_sym in level3:
            return '<'
        else:
            return '>'

    #运算符栈栈顶元素为 (
    elif top_sym in level3:
        if wait_sym in level4: #右括号)碰到了(，那么左括号应该弹出栈顶
            return '='
        else:  #例如 top_sym='(' wait_sym=‘+’，‘-’，‘*’，‘/’
            return '<'  #只要栈顶元素为 ( ,等待入栈的元素都应该无条件入栈

    # 运算符栈栈顶元素为 ）,没有这种情况


def calculale(num1,symbol,num2):  #计算最小化的数学表达式  数字 运算符 数字
    res=0
    if symbol == '+':
        res=num1+num2
    elif symbol == '-':
        res=num1-num2
    elif symbol == '*':
        res=num1*num2
    elif symbol == '/':
        res=num1/num2
    print('from calculate res is [%s|%s|%s|%s]' %(num1,symbol,num2,res))
    return res

def main(expression_l):  #主函数
    # print('from in the main',expression_l)
    number_stack=[]
    symbol_stack=[]
    for ele in expression_l:
        ret=is_symbol(ele)  #传给 is_symbol函数 判断 是运算符 还是数字
        # 如果是数字 返回False
        if not ret:
            #压入数字栈
            ele=float(ele)
            number_stack.append(ele)
        # 如果是运算符 返回True
        else:
            #压入运算符栈
            while True:
                if len(symbol_stack) == 0:  #如果
                    symbol_stack.append(ele)
                    break
                res=priority(symbol_stack[-1],ele)

                if res == '<':  #加入符号栈栈顶  进行下一次判断
                    symbol_stack.append(ele)
                    break
                if res == '=':  #取出符号栈栈顶  进行下一次判断 此时会有 一个左括号.内容.右括号
                    symbol_stack.pop()
                    break
                if res == '>':  #取出运算符栈的栈顶，取出两次数字栈的栈顶，传给给calculale函数 运算出结果
                    symbol=symbol_stack.pop()
                    num2=number_stack.pop()
                    num1=number_stack.pop()
                    number_stack.append(calculale(num1,symbol,num2))
    else: #当循环结束时，数字栈底 和 运算符栈底 还有待入栈底的运算符  需要循结束后，取出该3个元素 运算出最终结果
        symbol = symbol_stack.pop()
        num2 = number_stack.pop()
        num1 = number_stack.pop()
        number_stack.append(calculale(num1, symbol, num2))

    return number_stack,symbol_stack


if __name__ == '__main__':
    print('您可以输入这个数学表达式或者自写数学表达式：-1 - 2 *((-60+30+(-40/5)*(-9-2*-5/30-7/3*99/4*2998+10/-568/14))-(-4*-3)/(16-3*2))+3')
    expression = input('==>>: ').strip() # 一个字符串
    expression_l=list(expression)
    l=main(expression_l)  #把格式化后的列表 传入main主函数
    print('您的最终结果是:\033[31;1m%s\033[0m' %l[0][0])