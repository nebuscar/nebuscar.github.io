---
layout: home
title: Home
---

# Welcome to my blog!

## Latest Posts
{% for post in site.posts %}
- [{{ post.title }}]({{ post.url }})  
  <small>{{ post.date | date: "%Y-%m-%d" }}</small>
{% endfor %}