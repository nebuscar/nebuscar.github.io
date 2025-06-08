---
title: "VSCode-Markdown自动配置开头说明"
author: "Zhu Ni"
date: "2025-01-19 01:15:18"
---

如果你没有找到 "首选项" 或 "用户代码片段" 的选项，可能是 VSCode 的界面或版本不同。让我提供一种更直接的方式来访问 **用户代码片段** 配置。

### 步骤：如何创建并编辑 VSCode 的用户代码片段

1. **打开命令面板**：
   - 按下 `Ctrl + Shift + P`（Windows/Linux）或 `Cmd + Shift + P`（Mac）以打开命令面板。

2. **打开用户代码片段设置**：
   - 在命令面板中输入 `Snippets` 或 `User Snippets`，然后选择 **"Preferences: Configure User Snippets"**。

3. **选择语言或创建全局片段**：
   - 你将看到一个选项，让你选择要为哪个语言创建代码片段。如果你要为 Markdown 文件创建片段，选择 **`markdown.json`**。
   - 如果你没有看到 `markdown.json`，可以选择 **"新建全局代码片段"** 来为所有语言创建片段，或者选择 **"新建文件"** 创建一个新的代码片段文件。

4. **添加代码片段内容**：
   - 在打开的 `markdown.json` 文件中，添加你需要的代码片段。例如：

     ```json
     {
         "Markdown Header Template": {
             "prefix": "markdownheader", 
             "body": [
                 "---",
                 "title: \"$1\"",
                 "author: \"$2\"",
                 "date: \"$3\"",
                 "---",
                 "",
                 "$0"
             ],
             "description": "Insert markdown header template"
         }
     }
     ```

5. **保存文件**：
   - 完成编辑---
title: ""
author: "Zhu Ni"
date: ""
---

后，保存 `markdown.json` 文件（`Ctrl + S` 或 `Cmd + S`）。

### 使用代码片段：

1. 打开一个新的 Markdown 文件（`.md` 文件）。
2. 输入触发片段的前缀（例如：`markdownheader`）。
3. 按 `Tab` 键，VSCode 会自动扩展并插入你定义的模板。

这样，你就能轻松地为新建的 Markdown 文件添加头部信息。

### 其他方式：手动编辑代码片段文件

如果你无法通过命令面板直接打开用户代码片段设置，也可以直接打开并编辑用户代码片段文件。通常这些文件位于以下路径：

- **Windows**:
  ```
  C:\Users\<your-username>\AppData\Roaming\Code\User\snippets
  ```

- **Mac/Linux**:
  ```
  ~/.config/Code/User/snippets
  ```

你可以直接在这些文件夹中找到并编辑对应的代码片段文件。

希望这次的说明能帮助你顺利配置代码片段！

如果你在新建 `.md` 文件时输入片段前缀并按 `Tab` 键没有插入模板，可能是代码片段没有正确配置，或者未按预期触发。下面我会帮你排查问题并确保设置正确。

### 排查步骤：

1. **确认是否已创建了正确的代码片段**：
   - 在 VSCode 中，确保你按照步骤正确创建了 `markdown.json` 代码片段文件。
   - 代码片段的配置文件 `markdown.json` 应该包含类似以下内容：

     ```json
     {
         "Markdown Header Template": {
             "prefix": "markdownheader", 
             "body": [
                 "---",
                 "title: \"$1\"",
                 "author: \"$2\"",
                 "date: \"$3\"",
                 "---",
                 "",
                 "$0"
             ],
             "description": "Insert markdown header template"
         }
     }
     ```

2. **确认代码片段是否已保存**：
   - 检查代码片段是否已经正确保存，文件名应为 `markdown.json`，而且你编辑的内容已经保存（`Ctrl + S` 或 `Cmd + S`）。

3. **确认代码片段在 Markdown 文件中生效**：
   - 确保你正在编辑的是 **`.md`** 文件，而不是其他文件类型（如 `.txt`）。
   - 你可以在文件顶部添加 `---` 来测试是否属于 Markdown 文件，VSCode 会自动检测文件类型。
   
4. **手动触发片段**：
   - 在新建 `.md` 文件时，输入 `markdownheader` 然后按 `Tab` 键。
   - 如果依然不起作用，可以尝试使用 `Ctrl + Space`（Windows/Linux）或 `Cmd + Space`（Mac）手动触发代码片段补全。输入 `markdownheader` 后，按 `Tab` 键看是否能展开为你定义的模板。

### 代码片段配置说明：

- `prefix`: 你在 Markdown 文件中输入的触发前缀。
- `body`: 插入的内容，其中 `$1`, `$2`, `$3` 是占位符，你可以快速跳转并修改。
- `$0`: 插入后光标将跳转到的位置。

### 示例：

```json
{
    "Markdown Header Template": {
        "prefix": "markdownheader", 
        "body": [
            "---",
            "title: \"$1\"",
            "author: \"$2\"",
            "date: \"$3\"",
            "---",
            "",
            "$0"
        ],
        "description": "Insert markdown header template"
    }
}
```

### 验证代码片段是否已启用：

1. 打开一个新的 `.md` 文件。
2. 输入 `markdownheader`，然后按 `Tab` 键。
   - 如果没有发生任何变化，试着按 `Ctrl + Space`（Windows/Linux）或 `Cmd + Space`（Mac），看看代码片段是否显示在补全列表中。
   - 如果仍然没有显示，检查是否有其他插件或配置干扰了代码片段的功能。

### 如果还是无法正常工作：

1. **重启 VSCode**：有时需要重启 VSCode 使新的代码片段生效。
2. **检查 VSCode 版本**：确认你的 VSCode 是最新版本，部分问题可能与旧版本的 VSCode 相关。

希望这些步骤能帮助你解决问题，让 Markdown 模板顺利插入！如果仍有问题，请告诉我更多细节，我们一起进一步排查。

要使 `date` 字段自动填充为当前系统时间，你需要在代码片段中使用一些动态值。然而，VSCode 的代码片段本身不支持动态时间填充。为此，我们可以考虑其他方法，例如使用扩展或脚本来自动填充当前时间。

### 方法 1: 使用 VSCode 的 **`Date` Snippet** 扩展

VSCode 并不原生支持动态获取当前日期作为代码片段的一部分，但你可以使用扩展来实现此功能。以下是使用扩展的步骤：

1. **安装 `Insert Date String` 扩展**：
   - 打开 VSCode，点击左侧的 **扩展**（Extensions）图标。
   - 搜索并安装 **`Insert Date String`** 插件。这个插件允许你插入当前日期和时间。

2. **修改代码片段**：
   一旦安装了扩展，虽然无法直接通过代码片段获取当前日期，但你可以通过扩展的命令来快速插入日期。你可以手动调用该命令，也可以修改你的代码片段来提供一个快捷方式。

### 方法 2: 使用外部脚本来生成日期

你可以考虑通过外部脚本来自动生成包含当前日期和时间的 Markdown 文件。

#### 1. 编写一个 Bash 脚本

假设你在 Linux 或 macOS 上，可以通过以下脚本来自动生成带有当前日期的 Markdown 文件。

```bash
#!/bin/bash
TITLE=$1
AUTHOR="Zhu Ni"
DATE=$(date "+%Y-%m-%d %H:%M")
FILENAME="${TITLE// /_}.md"

echo -e "---\ntitle: \"$TITLE\"\nauthor: \"$AUTHOR\"\ndate: \"$DATE\"\n---\n" > "$FILENAME"
code "$FILENAME"
```

这个脚本会：
- 获取传入的标题参数。
- 获取当前系统时间并格式化为 `YYYY-MM-DD HH:MM`。
- 创建一个新的 Markdown 文件，并写入头部信息。
- 自动打开该文件。

#### 2. 使用脚本生成文件

你可以将该脚本保存为 `create_markdown.sh`，然后使用如下命令生成带有当前日期的 Markdown 文件：

```bash
./create_markdown.sh "理解PDB文件中seqres记录类型"
```

这将创建一个名为 `理解PDB文件中seqres记录类型.md` 的文件，并自动写入头部信息。

### 方法 3: 使用 JavaScript 或 Node.js 脚本

如果你使用 Windows 或希望使用更跨平台的方法，可以使用 Node.js 脚本来实现动态日期插入。

#### Node.js 脚本：

```javascript
const fs = require('fs');
const path = require('path');

// 获取当前日期
const date = new Date().toISOString().split('T')[0]; // 格式化为 yyyy-mm-dd

// 获取命令行传入的标题
const title = process.argv[2];
const author = 'Zhu Ni';

// 文件名转换空格为下划线
const filename = title.replace(/\s+/g, '_') + '.md';

// Markdown 文件内容
const content = `---
title: "${title}"
author: "${author}"
date: "${date}"
---

`;

// 将内容写入文件
fs.writeFileSync(path.join(__dirname, filename), content);

console.log(`Markdown file "${filename}" created successfully.`);
```

#### 使用 Node.js 脚本：

1. 将以上代码保存为 `create_markdown.js`。
2. 使用命令行运行脚本，传入标题参数：

```bash
node create_markdown.js "理解PDB文件中seqres记录类型"
```

这个脚本将创建一个包含当前日期的 Markdown 文件。

### 总结

- **方法 1**：通过安装扩展插件（如 `Insert Date String`）来动态插入当前日期。
- **方法 2**：使用外部脚本（Bash 或 Node.js）生成包含当前日期的 Markdown 文件。
- **方法 3**：如果只需要在某些编辑时插入日期，使用插件来动态插入日期。

虽然 VSCode 的内置代码片段无法动态填充日期，但通过外部脚本和插件，你可以很容易地实现这一功能。