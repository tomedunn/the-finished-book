---
title: "The Finished Book"
layout: splash
permalink: /
date: 2021-10-29
last_modified_at: 2023-03-27
show_date: false
feature_row:
  - image_path: /assets/images/classes-image1.jpg
    image_url: "/classes/"
    image_caption: "Classes"
    alt: "cool character mini"
    excerpt: "Posts about player character and class related content."
  - image_path: /assets/images/monsters-image1.jpg
    image_url: "/monsters/"
    image_caption: "Monsters"
    alt: "scary monster mini"
    excerpt: "Posts about monsters and such."
  - image_path: /assets/images/theory-image1.jpg
    image_url: "/theory/"
    image_caption: "Theory"
    alt: "dice and diagrams"
    excerpt: "Posts about the mechanics and theories behind the game."
---

Welcome! These posts are a collection of my thoughts and analysis on D&D 5th edition. As One D&D is fleshed out more I will likely make posts about that as well, but for the most part I will be posting about 5th edition D&D.

I like to think of this as more of a living text book than a blog. When I find something worth sharing, I'll make a post about it. And if I find something new related to something I've already written about, or discover I've made and error somewhere, I'll update those post with new information.

{% include feature_row  %}

# Recent Posts

{% assign sorted = site.documents | sort: 'date' | reverse %}
{% for post in sorted limit:10 %}
  {% include archive-single.html %}
{% endfor %}