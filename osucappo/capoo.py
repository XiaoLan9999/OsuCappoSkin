import sys
import tkinter as tk
from tkinter import messagebox, filedialog
import os
import json
import shutil

CONFIG_FILE = "config.json"
SKIN_FOLDER_NAME = "Capoo Skin Edit Ver (All Mode) 1.5"
current_lang = "zh"

# 多语言词典
lang_text = {
    "zh": {
        "title": "osu! 皮肤分辨率切换器",
        "select_label": "请选择你的分辨率：",
        "skin_label": f"皮肤目录：{SKIN_FOLDER_NAME}",
        "resolutions": {
            "1080p / 2K / 4K 显示器适用": "1920x1080",
            "WQXGA (2560x1600) 显示器适用": "2560x1600"
        },
        "success": "已切换为 {res} 分辨率素材\n别忘记 Ctrl+Alt+Shift+D 刷新皮肤！",
        "error": "未找到分辨率资源：{res}",
        "choose_osu": "请选择你的 osu! 安装目录（应包含 Skins 文件夹）",
        "invalid_dir": "该目录下未找到 Skins 文件夹，请重新选择 osu! 安装目录。",
        "cancel_exit": "未选择有效的 osu! 目录，程序已退出。",
        "reselect": "重新选择 osu! 路径"
    },
    "en": {
        "title": "osu! Skin Resolution Switcher",
        "select_label": "Please select your screen resolution:",
        "skin_label": f"Skin Folder: {SKIN_FOLDER_NAME}",
        "resolutions": {
            "1080p / 2K / 4K Display": "1920x1080",
            "WQXGA (2560x1600) Display": "2560x1600"
        },
        "success": "Switched to {res} resolution skin.\nDon’t forget Ctrl+Alt+Shift+D to refresh skin!",
        "error": "Resolution resource not found: {res}",
        "choose_osu": "Please select your osu! install folder (should contain Skins/)",
        "invalid_dir": "Selected folder does not contain Skins/. Please reselect osu! folder.",
        "cancel_exit": "No valid osu! folder selected. Program will exit.",
        "reselect": "Reselect osu! Folder"
    }
}

# 资源路径处理
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def lang(key):
    return lang_text[current_lang].get(key, key)

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def select_osu_path():
    while True:
        path = filedialog.askdirectory(title=lang("choose_osu"))
        if not path:
            return None
        if not os.path.exists(os.path.join(path, "Skins")):
            retry = messagebox.askretrycancel("Invalid", lang("invalid_dir"))
            if not retry:
                return None
        else:
            config = {"osu_path": path}
            with open(CONFIG_FILE, "w", encoding="utf-8") as f:
                json.dump(config, f)
            return config

def switch_resolution(res):
    skin_main_path = os.path.join(config["osu_path"], "Skins", SKIN_FOLDER_NAME)
    src_path = os.path.join(skin_main_path, "_resolutions", res)

    if not os.path.exists(src_path):
        messagebox.showerror("Error", lang("error").format(res=res))
        return

    try:
        for item in os.listdir(src_path):
            s = os.path.join(src_path, item)
            d = os.path.join(skin_main_path, item)
            if os.path.isdir(s):
                if os.path.exists(d):
                    shutil.rmtree(d)
                shutil.copytree(s, d)
            else:
                shutil.copy2(s, d)
        messagebox.showinfo("Success", lang("success").format(res=res))
    except Exception as e:
        messagebox.showerror("Exception", str(e))

def render_ui():
    for widget in root.winfo_children():
        widget.destroy()

    root.title(lang("title"))
    tk.Label(root, text=lang("skin_label")).pack(pady=5)
    tk.Label(root, text=lang("select_label")).pack(pady=5)

    for label, folder in lang_text[current_lang]["resolutions"].items():
        tk.Button(root, text=label, width=34, command=lambda r=folder: switch_resolution(r)).pack(pady=4)

    tk.Button(root, text=lang("reselect"), command=lambda: select_and_reload()).pack(pady=8)

def select_and_reload():
    global config
    config = select_osu_path()
    if not config or not os.path.exists(config["osu_path"]):
        messagebox.showinfo("已取消", lang("cancel_exit"))
        sys.exit(0)
    render_ui()

# 语言选择
def select_language():
    lang_win = tk.Tk()
    lang_win.title("语言选择 / Language Select")
    lang_win.geometry("300x160")
    lang_win.resizable(False, False)

    tk.Label(lang_win, text="请选择语言 / Please select your language", font=("Arial", 11)).pack(pady=20)

    def choose(language):
        global current_lang
        current_lang = language
        lang_win.destroy()
        start_main_program()

    tk.Button(lang_win, text="中文", width=15, command=lambda: choose("zh")).pack(pady=5)
    tk.Button(lang_win, text="English", width=15, command=lambda: choose("en")).pack(pady=5)

    lang_win.mainloop()

# 主程序
def start_main_program():
    global config, root
    config = load_config()
    if not config.get("osu_path") or not os.path.exists(config["osu_path"]):
        config = select_osu_path()
        if not config or not os.path.exists(config["osu_path"]):
            messagebox.showinfo("已取消", lang("cancel_exit"))
            sys.exit(0)

    root = tk.Tk()
    root.geometry("420x260")

    icon_path = resource_path("favicon.ico")
    if os.path.exists(icon_path):
        try:
            root.iconbitmap(icon_path)
        except:
            pass

    render_ui()
    root.mainloop()

select_language()
