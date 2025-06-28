# 猫猫虫咖波皮肤替换器 / Capoo Skin Resolution Switcher

一个用于 [osu!](https://osu.ppy.sh) 的皮肤分辨率切换器，适用于“猫猫虫咖波”主题皮肤。

This is a simple resolution switcher for the **Capoo-themed osu! skin**, designed to make skin usage on different screen sizes more convenient.

---

## 获取皮肤原始文件 / Get the skin file

>  下载 `.osk` 文件请前往博客页面：  
> [https://blog.xiaolan9999.net/index.php/archives/18/](https://blog.xiaolan9999.net/index.php/archives/18/)

You can get the original `.osk` skin file from the link above.

---

## 项目内容 / Project Contents

此项目 **仅包含皮肤切换器的源代码**，不包含完整皮肤资源。  
This repo **only contains the source code** of the resolution switcher, not the full skin.

---

## 使用方式 / How to Use

1. 打开 `.osk` 文件，osu! 会自动安装皮肤
2. 如果你的屏幕为 WQXGA（如 2560×1600）或使用 4K 导致轨道偏移，请使用本工具
3. 运行 `revo.exe`（切换器）
4. 选择对应分辨率即可一键替换皮肤资源
5. 回到 osu! 并按 `Ctrl + Shift + Alt + S` 刷新皮肤

---

## 兼容性 / Compatibility

- 系统：Windows 10/11
- 分辨率切换器由 Python 编写，可执行文件通过 PyInstaller 打包

---

## ⚠️ 注意事项 / Notes

- **请勿更改皮肤文件夹名称**，否则切换器将无法定位目标
- 若你未选择正确的 `osu!` 安装路径，程序将提示并终止
- 支持的分辨率：
  - `1920×1080`（适用于常见 1080p / 2K / 4K 屏幕）
  - `2560×1600`（适用于 WQXGA 屏幕）

---

## License

MIT License  
© XiaoLanツ / XiaoLan9999
