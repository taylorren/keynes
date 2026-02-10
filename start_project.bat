@echo off
rem Keynes General Theory Project Startup Script
rem 用于启动项目的虚拟环境

echo Starting Keynes General Theory Math Code Environment...

rem 检查虚拟环境是否存在
if not exist .venv (
    echo Creating virtual environment...
    python -m uv venv .venv
)

rem 激活虚拟环境
call .venv\Scripts\activate.bat

rem 安装必要的包（如果尚未安装）
python -c "import sympy, numpy, matplotlib" 2>nul || (
    echo Installing required packages...
    python -m pip install --target .venv\Lib\site-packages sympy numpy matplotlib
)

echo Virtual environment activated.
echo Available commands:
echo   - jupyter notebook          : Start Jupyter Notebook
echo   - python code/chapter_1_setup_updated.py : Run chapter 1 code
echo   - python -m pip install [package] : Install additional packages
echo.
echo To start Jupyter Notebook, run: jupyter notebook
pause