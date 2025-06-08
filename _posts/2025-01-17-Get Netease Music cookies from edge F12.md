---
title: "从Edge浏览器中获取网易云音乐Cookies，以便登录VSCode-网易云插件"
author: "Zhu Ni"
date: "2025-01-17 23:42"
---

# Cookie获取步骤

## 1.打开Edge浏览器，搜索网易云音乐网页版，登录  
（不限制浏览器，本人使用Edge浏览器，没有测试其他浏览器）

## 2.按F12进入开发者模式，选择Application选项卡  
![Edge-开发者模式示意图](/images/image-8.png)

## 3.找到页面左侧边栏Cookies选项卡，展开

找到MUSIC_U，复制其Value值

## 4.进入VSCode，输入`ctrl+shift+p`，输入`netease music log in(cookie)`





[参考1-CSDN](https://blog.csdn.net/weixin_46677913/article/details/107893959)
[参考2-MicroSoftware](https://learn.microsoft.com/zh-cn/microsoft-edge/devtools-guide-chromium/storage/cookies)
[参考3-OpenAI_ChatGPT]

# 参考3-OpenAI_ChatGPT查询所得内容（略有助益）

如果你在开发者工具中没有找到 **Cookies** 选项，可以尝试以下不同的方法来获取和查看 Cookies。下面分别提供针对 **Google Chrome** 和 **Firefox** 的详细操作步骤：

---

### **1. 在 Google Chrome 中获取 Cookies**

1. **打开网易云音乐网页版：**
   - 访问 [网易云音乐官网](https://music.163.com) 并登录你的账户。

2. **打开开发者工具：**
   - 右键点击网页上的任意地方，选择 **“检查”**（Inspect），或者按 `F12` 打开开发者工具。

3. **切换到 Network 标签：**
   - 在开发者工具界面，切换到 **“Network”** 标签页（如果你没有看到这个标签，可以点击顶部的双箭头并找到它）。

4. **刷新页面：**
   - 刷新页面（按 `F5` 或点击浏览器的刷新按钮）。确保浏览器的 **Network** 标签已经加载了所有网络请求。

5. **查看 Cookies：**
   - 在 **Network** 标签中，点击左侧的 **“Cookies”**（可以在左侧菜单的 “Headers” 或 “Preview” 下找到，通常是一个下拉菜单）。
   - 选择 `music.163.com` 域名下的 Cookies，你将看到登录相关的 Cookie 数据。

6. **复制 Cookie 信息：**
   - 找到如下 Cookie 信息并复制它们：
     - `MUSIC_U`
     - `__remember_me`
     - `__csrf_token`（如果有的话）

---

### **2. 在 Firefox 中获取 Cookies**

1. **打开网易云音乐网页版：**
   - 访问 [网易云音乐官网](https://music.163.com) 并登录你的账户。

2. **打开开发者工具：**
   - 右键点击网页上的任意地方，选择 **“检查元素”**（Inspect Element），或者按 `F12` 打开开发者工具。

3. **切换到 Storage 标签：**
   - 在开发者工具中，点击 **“Storage”**（存储）标签。**Storage** 标签和 **Network** 标签的作用类似，但它专门显示存储在浏览器中的信息。

4. **查看 Cookies：**
   - 在 **Storage** 标签的左侧菜单中，找到 **Cookies** 选项，并选择 `music.163.com` 域名。
   - 你将看到一个表格，其中列出了所有存储在这个域下的 Cookie。

5. **复制 Cookie 信息：**
   - 复制如下 Cookie 信息：
     - `MUSIC_U`
     - `__remember_me`
     - `__csrf_token`（如果有的话）

---

### **3. 使用扩展插件（如 EditThisCookie）**

如果你还是无法找到 Cookies，使用一个浏览器扩展插件来帮助你导出 Cookies 也是一种不错的选择。**EditThisCookie** 是一个流行的 Chrome 插件，可以方便地查看、编辑和导出 Cookies。

#### **安装 EditThisCookie 插件：**
1. **Chrome 浏览器**：
   - 打开 [Chrome 网上应用店](https://chrome.google.com/webstore)。
   - 搜索 **EditThisCookie** 插件并安装。
   - 安装完成后，插件会出现在浏览器工具栏中。

2. **导出 Cookie：**
   - 在你登录网易云音乐的页面，点击浏览器工具栏上的 **EditThisCookie** 图标。
   - 在弹出的插件界面中，你可以查看并导出所有相关的 Cookies。
   - 找到 `MUSIC_U` 和 `__remember_me` 等相关 Cookies，并复制它们。

---

### **4. 使用浏览器开发者工具的 "Application" 标签（如果可以找到）**

在某些版本的 Chrome 或 Firefox 中，Cookies 选项可能在 **Application** 或 **Storage** 标签下：

1. **在 Chrome 中**：
   - 打开开发者工具，切换到 **Application** 标签。
   - 在左侧栏中找到 **Cookies** 选项，点击并选择 `music.163.com` 域名，查看登录相关的 Cookies。

2. **在 Firefox 中**：
   - 打开开发者工具，切换到 **Storage** 标签。
   - 在左侧栏中找到 **Cookies**，然后选择 `music.163.com`，查看 Cookies。

---

### 5. 额外方法：通过浏览器的 Cookies 页面查看

如果你使用的是 **Chrome**，你也可以通过浏览器的 **设置** 页面来查看和导出 Cookies：

1. **打开 Chrome 设置页面：**
   - 在浏览器地址栏输入 `chrome://settings/cookies`，按回车。
   
2. **查找网易云音乐 Cookies：**
   - 在 Cookies 页面中，找到 `music.163.com`，点击查看。

3. **复制 Cookies：**
   - 复制所需的 Cookies 信息。

---

### 总结：
- **在 Chrome 和 Firefox 中，通常你可以在 Network 或 Storage/Application 标签中找到 Cookies。**
- **如果使用开发者工具仍然无法找到，可以通过安装 EditThisCookie 插件来简化操作。**

希望这些步骤能够帮助你获取到所需的 Cookies。如果你仍然遇到问题，欢迎告诉我你使用的具体浏览器和版本，我可以给出更具体的建议。