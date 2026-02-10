# 《就业、利息和货币通论》数理与编程解析

本项目旨在通过数学推导和 Python 编程，深入理解约翰·梅纳德·凯恩斯的《就业、利息和货币通论》(The General Theory of Employment, Interest and Money)。

## 目录结构

- `code/`: Jupyter Notebooks (主要分析文件)
- `references/`: 参考文献
- `daily_progress/`: 每日进度记录

## 环境设置

本项目使用 uv 作为 Python 包管理器。要设置开发环境，请执行以下步骤：

1. 安装 uv: `pip install uv`
2. 创建虚拟环境: `uv venv .venv`
3. 激活虚拟环境: `.venv\Scripts\activate` (Windows) 或 `.venv/bin/activate` (Linux/Mac)
4. 安装依赖: `uv pip install numpy pandas matplotlib sympy jupyter`

## 使用方法

要开始分析，请运行:
```
jupyter notebook
```
然后在浏览器中打开相应的 `.ipynb` 文件。

## 计划

我们将按照《通论》的章节顺序，逐步进行数理建模和编程验证，所有内容都将集中在 Jupyter Notebooks 中，整合代码、数学公式、解释和可视化。

## 第一章：前言和性质的探讨

### 核心概念

1.  **古典经济学假设：** 自由市场能自动实现充分就业（萨伊定律）。
2.  **凯恩斯的挑战：** 市场可能长期处于非充分就业均衡，非自愿失业是可能的。
3.  **总需求的重要性：** 强调有效需求是决定就业和产出的关键。

### 初步工作

本章通过 Jupyter Notebook 实现了古典经济学与凯恩斯经济学的基础模型对比，包括：
- 核心经济变量的符号定义
- 萨伊定律与有效需求原理的数学表达
- 消费函数和总需求函数的建立
- 凯恩斯交叉模型的可视化
- 乘数效应的数学推导

见 `code/chapter_1_keynes_model.ipynb` 文件。