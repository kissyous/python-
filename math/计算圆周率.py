import mpmath

# 设置精度为 32 位，因为还包含整数部分的 3
mpmath.mp.dps = 3000

# 计算圆周率
pi = mpmath.pi

# 转换为字符串并截取小数点后 30 位
pi_str = str(pi)
decimal_part = pi_str.split('.')[1][:3000]

# 输出结果
print(f"圆周率小数点后 3000 位是: {decimal_part}")