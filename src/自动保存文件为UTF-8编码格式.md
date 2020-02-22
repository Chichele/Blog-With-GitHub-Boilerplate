---
layout: post
title: 自动保存文件为UTF-8编码格式
categories: 
  - Tech
tags: 
  - 瞎折腾
date: 2020-02-23 00:36:12
---

# 写在前面


最近在琢磨跨平台开发，需要把代码文件都统一保存为`UTF8 no bom`的格式，但找了很久也没找到将文件编码格式自动保存为`UTF8 no bom`的方法。尝试过VS的插件`Force UTF-8(No BOM)`，但可能因为版本问题，在我的`VS2019（16.3.7）`上并未生效。

然后偶然发现了`EditorConfig`可以搞定，VS以及很多其它编辑器都支持它。

# 解决办法
在项目根目录新建一个文件`.editorconfig`，然后输入内容并保存，重启编辑器/IDE后生效：
```
# EditorConfig is awesome: https://EditorConfig.org
# top-most EditorConfig file
root = true
# Unix-style newlines with a newline ending every file
[*]
charset = utf-8
# Matches multiple files with brace expansion notation
# Set default charset
[*.{js,py}]
charset = utf-8
```
可以从上面的注释内容看出，EditorConfig 支持针对不同文件后缀使用不同配置方案。除了设置文件编码外，EditorConfig还支持代码缩进等配置，具体使用方法到[https://EditorConfig.org](https://EditorConfig.org)查看。