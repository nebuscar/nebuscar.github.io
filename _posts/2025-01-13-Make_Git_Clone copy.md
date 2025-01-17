---
layout: post
title:  "Git Clone"
date:   2025-01-13 13:20:30 +0800
---
你遇到的错误是因为 GitHub 从 2021 年 8 月 13 日起取消了对密码认证的支持。现在，GitHub 只允许使用 **个人访问令牌（Personal Access Token，PAT）** 或 **SSH 密钥** 来进行 HTTPS 认证。

下面是如何通过 **个人访问令牌（PAT）** 解决这个问题的步骤：

### 1. **生成个人访问令牌（PAT）**

1. 打开 GitHub 网站并登录到你的账户。
2. 点击右上角的头像，选择 **Settings**（设置）。
3. 在左侧菜单中，选择 **Developer settings**（开发者设置）。
4. 然后点击 **Personal access tokens**（个人访问令牌） > **Tokens (classic)**（经典令牌）。
5. 点击 **Generate new token**（生成新令牌）。
6. 选择你需要的权限（例如：`repo`，`workflow` 等，表示访问仓库的权限）。
7. 滚动到底部，点击 **Generate token**（生成令牌）。
8. 复制生成的令牌，并妥善保存。这个令牌只会显示一次，之后无法再次查看。

### 2. **使用个人访问令牌（PAT）进行认证**

现在，你已经有了个人访问令牌，在克隆 GitHub 仓库时，可以使用这个令牌代替密码进行认证。

1. 当你执行 `git clone` 命令时，Git 会提示你输入用户名和密码。
2. 输入 GitHub 用户名（比如 `nebuscar`），然后输入你刚刚生成的 **个人访问令牌（PAT）** 作为密码。

举个例子，执行时会像这样提示：

```bash
Username for 'https://github.com': nebuscar
Password for 'https://nebuscar@github.com': <Your-PAT>
```

注意：**不要再使用 GitHub 账户的密码**，而是使用刚才生成的 **Personal Access Token**。

### 3. **或者：使用 SSH 密钥认证（如果你更喜欢）**

如果你不想每次都输入 PAT，可以选择使用 SSH 密钥，这样认证会更加方便。

#### 设置 SSH 密钥并关联到 GitHub：

1. 打开终端，运行以下命令生成一个新的 SSH 密钥：
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```
   （记得替换成你自己的邮箱）

2. 按照提示完成生成过程，默认位置即可。

3. 运行下面的命令，确保 SSH 代理正在运行，并将 SSH 密钥添加到代理中：
   ```bash
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_ed25519
   ```

4. 将公钥内容复制到剪贴板：
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```

5. 登录到 GitHub，进入 **Settings**（设置）> **SSH and GPG keys**（SSH 和 GPG 密钥）> **New SSH key**（新增 SSH 密钥）。
6. 粘贴你刚才复制的公钥，并为它起个名字（比如 `MyLaptop`）。

7. 测试 SSH 连接：
   ```bash
   ssh -T git@github.com
   ```
   如果一切正常，GitHub 会显示类似以下的信息：
   ```
   Hi nebuscar! You've successfully authenticated, but GitHub does not provide shell access.
   ```

8. 现在你就可以使用 SSH URL 来克隆仓库了，命令如下：
   ```bash
   git clone git@github.com:nebuscar/Machine-Learning.git /home/nebuscar/Projects/Machine-Learning
   ```

通过以上两种方法之一（使用 **个人访问令牌** 或 **SSH 密钥**），你就能成功克隆 GitHub 仓库了。
