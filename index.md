---
layout: home
title: Home
pagination:
  enabled: true
---

# Welcome to my blog!

## Recent Posts
{% for post in paginator.posts %}
- [{{ post.title }}]({{ post.url }})  
  <small>{{ post.date | date: "%b %d, %Y" }}</small>
{% endfor %}

<!-- 分页导航 -->
<div class="pagination">
  {% if paginator.previous_page %}
    <a href="{{ paginator.previous_page_path }}">← Newer</a>
  {% endif %}
  <span>Page {{ paginator.page }} of {{ paginator.total_pages }}</span>
  {% if paginator.next_page %}
    <a href="{{ paginator.next_page_path }}">Older →</a>
  {% endif %}
</div>