"""
    数据类型转换
"""

if __name__ == '__main__':
    int1 = 1000
    float1 = 13.14
    str1 = '131.132'
    print(f'int -> float {float(int1)}')
    print(f'float -> int {int(float1)}')
    print(f'int -> str {str(int1)}')
    print(f'float -> str {str(float1)}')
    print(f'str -> float {float(str1)}')
    print(f'str -> int {int(str1[0:3])}')
