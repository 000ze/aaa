#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re


string = '''
    abcD12343
    ab134cD
'''

# 相当于
# 1. 编译正则表达式
# (.*)      贪婪匹配，尽可能多匹配直到无法匹配
# (.*?)     非贪婪匹配，只要匹配到就返回
#  . 符号默认不包含换行符，DOTALL模式表示让 . 符号匹配任何字符包括换行符
# re.DOTALL == re.S == re.RegexFlag.DOTALL == re.RegexFlag.S
# 忽略大小写
# re.IGNORECASE == re.I == re.RegexFlag.IGNORECASE == re.RegexFlag.I
# 忽略大小写并且支持 DOTALL模式 使用 |
pattern = re.compile(r"\w(.?)\d",re.RegexFlag.IGNORECASE )

# 2. 提取数据
result = pattern.findall(string)
a=" ".join(result)
print(a)
string = r"abc\nd"
print(string)
string = "a;dj jkl,jj; j;sd"
# split 分组
pattern = re.compile(r'[^; ,]+')
result = pattern.findall(string)
print(result)
# sub 交换
string = "hello world;sjd;ssd jkls;sd jk;crise lyj"
# 带空格的词组替换成 #
pattern = re.compile(r'(.*) (.*)')

# 把 空格的词组 进行交换
result = pattern.sub(r"\2 \1",string)

print(result)

string = '<input type="submit" id="su" value="百度一下" class="bg s_btn">'

pattern = re.compile(r'<input type="submit" id="(.*?)" value="(.*?)" class="bg s_btn">')

result = pattern.findall(string)
print(result)
res=" ".join(result)
print(res)