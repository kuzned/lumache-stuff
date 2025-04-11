---
html_theme.sidebar_secondary.remove: true
myst:
  html_meta:
    description: "Blog & Handbook"
    keywords: "Electronics, Raspberry Pi, Python, Django"
---

<!-- # Welcome to Jeremy's Notebook -->
# Welcome to Blog & Handbook
**by Jeremy H. Boob**

You can find here some posts and other useful stuff about electronic devices, Python and C programming and web development. This could be helpful if you are dabbled in these topics.

Check the [Blog](#blog) and then to [Handbook](#handbook) section for further information.<br>

<hr class="border border-secondary border-2 opacity-75">

## Recent blog posts

<!-- ```{postlist}
:date: "%Y-%m-%d"
:format: "{title} - {date}"
:excerpts:
``` -->

```{postlist} 3
:date: "%Y-%m-%d"
:format: "{title} - {date}"
:expand: Read more ...
:excerpts:
```

```{toctree}
:maxdepth: 2
:hidden:
blog
handbook
about
```