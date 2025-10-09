"""unpacking element from iterables of arbitrary length"""
#using * xpression, examples:
record = ('Sam', 'sam@sam.com', '000-111-222', '333-444-555')
name, emai, *phone_number = record
print(name, emai, phone_number) #Sam sam@sam.com ['000-111-222', '333-444-555']

a, *var, b = [1, 2, 3, 4, 5]
print(a)    # 1
print(var)  # [2, 3, 4]
print(b)    # 5

"""
| 用法位置  | 作用      | 示例                     |
| ----- | ------- | ---------------------- |
| 函数定义  | 接收多个参数  | `def f(*args):`        |
| 函数调用  | 解包参数    | `f(*[1,2,3])`          |
| 解包赋值  | 收集中间变量  | `a, *b, c = [1,2,3,4]` |
| 构造新序列 | 展开列表、元组 | `[1, *[2, 3], 4]`      |
"""
