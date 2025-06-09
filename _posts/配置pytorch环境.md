```markdown
# PyTorch GPU环境配置指南（避坑版）

> 本教程适用于Windows系统，无需安装Anaconda，直接使用原生Python环境配置PyTorch GPU版

## 🔍 前置检查
### 1. 确认显卡CUDA版本
1. 右键桌面 → 打开 `NVIDIA 控制面板`
2. 点击 `帮助` → `系统信息` → `组件`
3. 查看 `NVCUDA.DLL` 对应的CUDA版本（例如11.1）

![查看CUDA版本](https://i.imgur.com/EXAMPLE.png)

### 2. 安装对应CUDA Toolkit
- 官方下载地址：[https://developer.nvidia.com/cuda-toolkit-archive](https://developer.nvidia.com/cuda-toolkit-archive)
- 选择与显卡匹配的版本（如CUDA 11.1）

## ⚡ 两种安装方式

### 方法1：在线安装（简单但慢）
```bash
pip3 install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
```

### 方法2：本地安装（推荐快速）
1. **下载whl文件**：
   - 访问 [PyTorch预编译包列表](https://download.pytorch.org/whl/torch_stable.html)
   - 搜索对应版本（例如：`cu111/torch-1.9.0%2Bcu111-cp36-cp36m-win_amd64.whl`）

2. **本地安装**：
```bash
# 进入下载目录
cd C:\Users\YourName\Downloads

# 安装本地whl文件
pip install torch-1.9.0+cu111-cp36-cp36m-win_amd64.whl

# 补充安装其他组件
pip install torchvision==0.10.0+cu111 torchaudio==0.9.0
```

## ⚠️ 重要注意事项
1. **不要使用国内镜像源**：可能导致安装CPU版本
2. **Python版本匹配**：whl文件中的`cp36`表示需要Python 3.6
3. **安装后必须验证**：

```python
import torch
print(torch.rand(5, 3))  # 测试基础功能
print(torch.cuda.is_available())  # 必须返回True
```

## 🐞 常见问题排查
| 问题现象 | 解决方案 |
|---------|----------|
| `torch.cuda.is_available()`返回False | 1. 检查CUDA与PyTorch版本匹配<br>2. 重新安装NVIDIA驱动 |
| 安装时提示版本冲突 | 使用`pip install --force-reinstall` |
| 出现DLL加载错误 | 安装VC++ 2015-2022可再发行组件 |

## 💡 优化建议
1. 使用虚拟环境（推荐）：
```bash
python -m venv pytorch_env
.\pytorch_env\Scripts\activate
```
2. 安装轻量版Python（如官方3.6/3.7版本）

> 如果遇到问题，可在评论区留言显卡型号+错误信息获取帮助
```

---

### 文章优化建议：
1. 添加实际截图（CUDA版本查看界面/安装成功验证界面）
2. 补充各版本对应关系表格（PyTorch vs CUDA vs Python）
3. 增加「如何彻底卸载重装」章节
4. 添加性能测试代码示例（如GPU矩阵运算对比）

需要我补充上述任何部分吗？