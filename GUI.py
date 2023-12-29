import tkinter as tk
from tkinter import simpledialog


# 默认按英文逗号分割，输入出发地点，到达地点和出发时间
# 注意车站打中文名，如北京南；出发时间要是yyyy-mm-dd格式，时间在今天到预售期结束附近

def get_list_from_gui():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    # 使用simpledialog弹出对话框获取用户输入
    user_input = simpledialog.askstring("Input", "Enter a list with depart, arrival and start_time (comma-separated):")

    # 将用户输入的字符串转换为列表,按逗号分割即可
    input_list = user_input.split(',')

    # 移除空格
    input_list = [item.strip() for item in input_list]

    # 输出获取的列表
    print("Input List:", input_list)

    return input_list
