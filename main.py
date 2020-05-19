# coding:utf8

from tkinter import filedialog

import ctypes
import os
import sys
import tkinter as tk


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if __name__ == '__main__':
    if is_admin():
        root = tk.Tk()
        root.withdraw()
        source = filedialog.askdirectory()
        target = filedialog.askdirectory() + source[source.rfind("/"):]
        os.symlink(source, target)
        print("操作成功完成.")
    elif sys.version_info[0] == 3:
        input("请以管理员身份运行.")
        quit()
