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

## 章节进展

本项目的章节进展与每日工作记录不在本 README 中维护，所有进度、临时笔记与当日变更请查看 `daily_progress/` 目录下的每日记录文件（例如 `daily_progress/2026-02-10.md`）。

具体分析内容、交互 Notebook、图表与临时输出均保存在 `code/` 与 `results/`（生成文件通常被忽略，不纳入版本控制）中。