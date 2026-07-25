#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法
def trim(str):
    if str[:1]==' ':
        return trim(str[1:])
    if str[-1:]==' ':
        return trim(str[:-1])
    return str
print(trim('    hallo   '))


