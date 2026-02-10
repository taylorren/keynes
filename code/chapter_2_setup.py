"""chapter_2_setup.py
工具函数：为第二章的数学推导与数值示例提供符号与简单函数。
"""

import math

try:
    import sympy as sp
    _HAS_SYMPY = True
except Exception:
    sp = None
    _HAS_SYMPY = False

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    _HAS_PLT = True
except Exception:
    plt = None
    _HAS_PLT = False


def create_production_symbols():
    if not _HAS_SYMPY:
        raise RuntimeError('sympy is required for symbolic symbols')
    K, L = sp.symbols('K L', positive=True)
    alpha = sp.symbols('alpha', positive=True)
    return K, L, alpha


def cobb_douglas(K, L, alpha):
    """Cobb-Douglas 生产函数 Y = K^alpha * L^(1-alpha)

    Works for both sympy symbols and numeric floats.
    """
    return K**alpha * L**(1 - alpha)


def marginal_products(K, L, alpha):
    """Return (MPK, MPL). If sympy available returns symbolic expressions."""
    Y = cobb_douglas(K, L, alpha)
    if _HAS_SYMPY:
        MPK = sp.diff(Y, K)
        MPL = sp.diff(Y, L)
        return sp.simplify(MPK), sp.simplify(MPL)
    else:
        # numeric fallback
        MPK = alpha * (K ** (alpha - 1)) * (L ** (1 - alpha))
        MPL = (1 - alpha) * (K ** alpha) * (L ** (-alpha))
        return MPK, MPL


def numeric_evaluate(alpha_val=0.3, K_val=100.0, L_val=50.0):
    """Evaluate MPK and MPL numerically and return (mpk, mpl)."""
    try:
        mpk, mpl = marginal_products(K_val, L_val, alpha_val)
        return float(mpk), float(mpl)
    except Exception:
        # fallback safe numeric computation
        mpk = alpha_val * (K_val ** (alpha_val - 1)) * (L_val ** (1 - alpha_val))
        mpl = (1 - alpha_val) * (K_val ** alpha_val) * (L_val ** (-alpha_val))
        return mpk, mpl


def run_example():
    print('Running chapter 2 numeric example...')
    alpha = 0.3
    K_val = 100.0
    L_val = 50.0
    if _HAS_SYMPY:
        K, L, a = create_production_symbols()
        mpk_sym, mpl_sym = marginal_products(K, L, a)
        print('Symbolic MPK =', mpk_sym)
        print('Symbolic MPL =', mpl_sym)
    mpk, mpl = numeric_evaluate(alpha, K_val, L_val)
    print(f'numeric MPK={mpk:.6f}, numeric MPL={mpl:.6f}')


def plot_marginal_products(alpha_val=0.3, L_val=50.0, K_min=10, K_max=400, n=100, out_prefix='results/marginal'):
    """Plot MPK and MPL as functions of K (for fixed L) and save PNG files.

    Returns list of saved filenames.
    """
    if not _HAS_PLT:
        raise RuntimeError('matplotlib not available')
    import os
    os.makedirs(os.path.dirname(out_prefix), exist_ok=True)
    # 设置中文字体回退（Windows 常见字体），并保证负号正常显示
    try:
        import matplotlib
        matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
        matplotlib.rcParams['axes.unicode_minus'] = False
    except Exception:
        pass

    Ks = [K_min + i * (K_max - K_min) / (n - 1) for i in range(n)]
    MPKs = []
    MPLs = []
    for K in Ks:
        mpk, mpl = numeric_evaluate(alpha_val=alpha_val, K_val=float(K), L_val=float(L_val))
        MPKs.append(mpk)
        MPLs.append(mpl)

    fn1 = f'{out_prefix}_vsK.png'
    plt.figure()
    plt.plot(Ks, MPKs, label='MPK (资本边际产量)')
    plt.plot(Ks, MPLs, label='MPL (劳动边际产量)')
    plt.xlabel('资本 K')
    plt.ylabel('边际产量')
    plt.title(f'MPK 与 MPL 关于 资本 K 的变化 (α={alpha_val}, L={L_val})')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(fn1)
    plt.close()

    # plot MPK/MPL vs K/L ratio
    ratios = [K / float(L_val) for K in Ks]
    fn2 = f'{out_prefix}_vsKtoL.png'
    plt.figure()
    plt.plot(ratios, MPKs, label='MPK (资本边际产量)')
    plt.plot(ratios, MPLs, label='MPL (劳动边际产量)')
    plt.xlabel('资本-劳动比 K/L')
    plt.ylabel('边际产量')
    plt.title(f'MPK 与 MPL 关于 资本-劳动比 K/L 的变化 (α={alpha_val})')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(fn2)
    plt.close()

    print('Saved plots:', fn1, fn2)
    return [fn1, fn2]


def price_tatonnement(demand_params=(200,1.0), supply_params=(20,0.5), p0=10.0, steps=50, gamma=0.1):
    """Simple tatonnement: price_{t+1} = p_t + gamma*(D(p_t)-S(p_t)).

    demand_params = (a, b) for D(p)=a - b*p
    supply_params = (c, d) for S(p)=c + d*p
    Returns (prices, demands, supplies)
    """
    a, b = demand_params
    c, d = supply_params
    prices = [p0]
    demands = []
    supplies = []
    p = p0
    for t in range(steps):
        D = max(a - b * p, 0.0)
        S = max(c + d * p, 0.0)
        demands.append(D)
        supplies.append(S)
        p = p + gamma * (D - S)
        # keep price non-negative
        p = max(p, 0.0)
        prices.append(p)
    return prices, demands, supplies


def plot_price_dynamics(demand_params=(200,1.0), supply_params=(20,0.5), p0=10.0, steps=80, gamma=0.05, out='results/price_dynamics.png'):
    if not _HAS_PLT:
        raise RuntimeError('matplotlib not available')
    import os
    os.makedirs(os.path.dirname(out), exist_ok=True)
    try:
        import matplotlib
        matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
        matplotlib.rcParams['axes.unicode_minus'] = False
    except Exception:
        pass

    prices, demands, supplies = price_tatonnement(demand_params, supply_params, p0, steps, gamma)
    ts = list(range(len(prices)))
    plt.figure()
    plt.plot(ts, prices, label='价格 p')
    plt.xlabel('迭代步 t')
    plt.ylabel('价格 p')
    plt.title('价格调整过程（调节：泰塔诺姆）')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(out)
    plt.close()
    # also plot demand and supply over price index
    out2 = out.replace('.png', '_DS.png')
    plt.figure()
    plt.plot(ts[:-1], demands, label='需求 D(p)')
    plt.plot(ts[:-1], supplies, label='供给 S(p)')
    plt.xlabel('迭代步 t')
    plt.ylabel('数量')
    plt.title('需求与供给随价格调整的变化')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(out2)
    plt.close()
    print('Saved price dynamics plots:', out, out2)
    return [out, out2]


def savings_investment_plot(s_params=(10,5), i_params=(100,50), r_min=0.0, r_max=0.2, n=200, out='results/S_I.png'):
    """Plot S(r)=s0 + s1*r and I(r)=i0 - i1*r and mark intersection (equilibrium r).

    s_params = (s0, s1) ; i_params = (i0, i1)
    """
    if not _HAS_PLT:
        raise RuntimeError('matplotlib not available')
    import os
    os.makedirs(os.path.dirname(out), exist_ok=True)
    try:
        import matplotlib
        matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
        matplotlib.rcParams['axes.unicode_minus'] = False
    except Exception:
        pass

    s0, s1 = s_params
    i0, i1 = i_params
    rs = [r_min + i * (r_max - r_min) / (n - 1) for i in range(n)]
    Ss = [s0 + s1 * r for r in rs]
    Is = [max(i0 - i1 * r, 0.0) for r in rs]
    # find intersection approximately
    eq_r = None
    for r, S, I in zip(rs, Ss, Is):
        if abs(S - I) < 1e-6 or (S - I) * (s0 + s1 * (r + 1e-6) - max(i0 - i1 * (r + 1e-6), 0)) < 0:
            eq_r = r
            break
    plt.figure()
    plt.plot(rs, Ss, label='储蓄 S(r)')
    plt.plot(rs, Is, label='投资 I(r)')
    if eq_r is not None:
        plt.axvline(eq_r, color='k', linestyle='--')
        plt.text(eq_r, max(max(Ss), max(Is)) * 0.6, f'均衡利率 r≈{eq_r:.4f}', rotation=90)
    plt.xlabel('利率 r')
    plt.ylabel('数量')
    plt.title('储蓄与投资关于利率的函数 S(r) 与 I(r)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(out)
    plt.close()
    print('Saved S-I plot:', out)
    return out


def simulate_sticky_price(demand_params=(200,1.0), supply_params=(20,0.5), p0=10.0, steps=80, gamma=0.05, stickiness=0.9, out='results/sticky_price.png'):
    """Simulate sticky price: p_{t+1} = stickiness*p_t + (1-stickiness)*(p_t + gamma*(D-S))

    Higher stickiness -> slower adjustment.
    """
    if not _HAS_PLT:
        raise RuntimeError('matplotlib not available')
    import os
    os.makedirs(os.path.dirname(out), exist_ok=True)
    try:
        import matplotlib
        matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
        matplotlib.rcParams['axes.unicode_minus'] = False
    except Exception:
        pass

    a, b = demand_params
    c, d = supply_params
    p = p0
    prices = [p]
    for t in range(steps):
        D = max(a - b * p, 0.0)
        S = max(c + d * p, 0.0)
        p_tilde = p + gamma * (D - S)
        p = stickiness * p + (1 - stickiness) * p_tilde
        p = max(p, 0.0)
        prices.append(p)
    ts = list(range(len(prices)))
    plt.figure()
    plt.plot(ts, prices, label=f'黏性系数={stickiness}')
    plt.xlabel('迭代步 t')
    plt.ylabel('价格 p')
    plt.title('黏性价格下的价格动态比较')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(out)
    plt.close()
    print('Saved sticky price plot:', out)
    return out


if __name__ == '__main__':
    run_example()
