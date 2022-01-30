---
title: "The Finished Book"
layout: splash
permalink: /
author_profile: false
date: 2021-10-29T12:00:00-04:00
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/images/site-header.jpg
  caption: "Photo credit: **tomedunn**"
feature_row:
  - image_path: /assets/images/classes-image1.png
    image_url: "/classes/"
    image_caption: "Classes"
    alt: "cool character mini"
    excerpt: "Posts about player character and class related content."
  - image_path: /assets/images/monsters-image1.png
    image_url: "/monsters/"
    image_caption: "Monsters"
    alt: "scary monster mini"
    excerpt: "Posts about monsters and such."
  - image_path: /assets/images/theory-image1.png
    image_url: "/theory/"
    image_caption: "Theory"
    alt: "dice and diagrams"
    excerpt: "Posts about the mechanics and theories behind the game."
---

Welcome! These posts are a collection of my thoughts and analysis on D&D 5th edition. It's possible I will expand this to other games or topics in the future, but for now my focus will be exclusively on D&D.

This is not a blog, and I will not be sticking to any kind of regular posting schedule. I like to do these sorts of analysis in my spare time. When I find something worth sharing I'll post about it.

{% include feature_row  %}

# Recent Posts

{% assign sorted = site.documents | sort: 'date' | reverse %}
{% for post in sorted limit:5 %}
  {% include archive-single.html %}
{% endfor %}