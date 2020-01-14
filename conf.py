# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "Chichele/Blog-With-GitHub-Boilerplate@gh-pages"
}

# 站点设置
site_name = "Don't ask me why"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "Chichele"
email = ""
author_homepage = "https://chichele.life"
description = "but time has passed us by"
key_words = ['Maverick', 'Chechele', 'Galileo', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "Maverick",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "🏄‍ Go My Own Way."
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "GitHub",
        "url": "https://github.com/Chichele",
        "icon": "gi gi-github"
    }
]
valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "sOrecO94dj6mt3xv8WKJiyRU-gzGzoHsz",
    "appKey": "AMysgqiml5FAJ6zjxUvpGm3N",
    "visitor": True,
    "recordIP": True
}
head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
