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

A tech [blog](https://en.wikipedia.org/wiki/Blog) is a website that focuses on publishing articles, news, and other content related to a specific area of technology. A technical [handbook](https://en.wikipedia.org/wiki/Handbook) is a reference work that provides practical information on a selected subject, such as web development.

You can find here some posts and other useful stuff about microcontroller devices, web development, Python and C programming. This could be helpful if you are dabbled in these topics.

Check the [Blog](#blog) and then to [Handbook](#handbook) section for further information.<br>

<hr class="border border-secondary border-2 opacity-75">

<!-- ## Recent blog posts -->
## Featured Blog Post

<!-- ```{postlist}
:date: "%Y-%m-%d"
:format: "{title} - {date}"
:excerpts:
``` -->

```{postlist} 1
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