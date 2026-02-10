"""
《通论》第一章：前言和性质的探讨
Python 初步设置与符号定义
"""

# 导入 SymPy 库用于符号计算
# 请在命令行运行: pip install sympy
try:
    import sympy as sp
    print("SymPy library imported successfully.")
except ImportError:
    print("SymPy library is not installed. Please install it using 'pip install sympy'")
    exit()

# 定义核心经济变量符号
# Y: 总产出 (Income/GDP)
# C: 总消费 (Consumption)
# I: 总投资 (Investment)
# L: 流动性偏好 (Liquidity Preference / Demand for Money)
# M: 名义货币供给 (Nominal Money Supply)
# r: 利率 (Interest Rate)
# N: 就业量 (Level of Employment)
# P: 物价水平 (Price Level)
# Z: 总供给价格 (Aggregate Supply Price)
# D: 总需求价格 (Aggregate Demand Price)

Y = sp.Symbol('Y', real=True, positive=True) # 总产出/收入
C = sp.Symbol('C', real=True, positive=True) # 消费
I = sp.Symbol('I', real=True, positive=True) # 投资
L = sp.Symbol('L', real=True, positive=True) # 货币需求
M = sp.Symbol('M', real=True, positive=True) # 货币供给
r = sp.Symbol('r', real=True)               # 利率
N = sp.Symbol('N', real=True, positive=True) # 就业量
P = sp.Symbol('P', real=True, positive=True) # 物价水平
Z = sp.Symbol('Z', real=True, positive=True) # 总供给价格
D = sp.Symbol('D', real=True, positive=True) # 总需求价格

print("\n--- 定义的核心经济变量符号 ---")
print(f"总产出/收入 (Y): {Y}")
print(f"消费 (C): {C}")
print(f"投资 (I): {I}")
print(f"货币需求 (L): {L}")
print(f"货币供给 (M): {M}")
print(f"利率 (r): {r}")
print(f"就业量 (N): {N}")
print(f"物价水平 (P): {P}")
print(f"总供给价格 (Z): {Z}")
print(f"总需求价格 (D): {D}")

# 示例：表达总需求等于消费加投资 (简化版)
# D = C + I (这是一个非常简化的模型，实际关系更复杂)
# 这里只是展示如何用符号表示概念
simple_aggregate_demand = C + I
print(f"\n--- 示例：简化总需求 (D = C + I) ---")
print(f"Symbolic Expression: D = {simple_aggregate_demand}")

# 提示用户下一步
print("\n--- 下一步 ---")
print("请在命令行中安装 SymPy (pip install sympy)，然后运行此脚本以查看符号定义。")
print("后续章节将基于这些符号进行更复杂的数学推导和建模。")
