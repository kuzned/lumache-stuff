---
html_theme.sidebar_secondary.remove: true
myst:
  html_meta:
    description: "Jeremy's Blog"
    keywords: "Electronics, Raspberry Pi, Python, Django"
    property_og_locale: "en_US"
    property_og_description: "Jeremy's Blog"
---


<!-- # Welcome to Jeremy's Notebook -->
# Welcome to Electronics & Progs
**by Jeremy H. Boob**


::::{grid}
:::{grid-item-card}
:link: about.html
👨‍💻 About me
:::
:::{grid-item-card}
:link: blog.html
📗 My blog
:::
:::{grid-item-card}
:link: handbook.html
📊 Handbook 
:::
::::

You can find here some posts and other useful stuff about electronic devices, Python and C programming and web development. This could be helpful if you are dabbled in these topics.

Check the [Blog](#blog) and then to handbook section for further information.

```{note}
This project is under active development.
```
<!-- ## Recent blog posts -->

```{postlist}
:date: "%Y-%m-%d"
:format: "{title} - {date}"
:excerpts:
```

```{toctree}
:maxdepth: 2
:hidden:
about
blog
handbook
# ablog
# lumache
# clang
# mystmd
```