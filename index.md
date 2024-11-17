---
title: "The Finished Book"
layout: splash
permalink: /
date: 2021-10-29
last_modified_at: 2024-11-16
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

Welcome to The Finished Book! This site contains posts analyzing the mechanics of D&D 5th edition. My interest is in understanding the math behind how the game functions, and in communicating that understanding in a way others, hopefully, find useful. 

The majority of these posts were written with the 2014 5th edition rules in mind, but many remain applicable to the 2024 rules as well. And, for those that aren't, I will undoubtedly be updating them to be compatible in the future as time permits. 

{% include feature_row  %}

# Recent Posts

{% assign sorted = site.documents | sort: 'date' | reverse %}
{% for post in sorted limit:10 %}
  {% include archive-single.html %}
{% endfor %}