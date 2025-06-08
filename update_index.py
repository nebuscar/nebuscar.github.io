import glob
from pathlib import Path

# 获取所有文章（按修改时间倒序）
posts = sorted(glob.glob("posts/*.md"), key=lambda x: Path(x).stat().st_mtime, reverse=True)

# 生成 Markdown 列表
markdown_links = [f"- [{Path(p).stem}](/{p})" for p in posts]
content = f"# 我的博客\n\n## 最新文章\n" + "\n".join(markdown_links)

# 写入 index.md
with open("index.md", "w") as f:
    f.write(content)