---
layout: page
title: Projects
permalink: /projects/
---

Here are some of the projects I've worked on! Click on any project to learn more.

{% assign sorted_projects = site.projects | sort: "date" | reverse %}
{% assign starred_projects = sorted_projects | where: "starred", true %}
{% assign other_projects = sorted_projects | where_exp: "project", "project.starred != true" %}

{% if starred_projects.size > 0 %}
  <section class="project-section">
    <h2>Starred Projects</h2>
    <div class="project-gallery">
      {% for project in starred_projects %}
        {% include project-card.html project=project %}
      {% endfor %}
    </div>
  </section>
{% endif %}

<section class="project-section">
  <h2>{% if starred_projects.size > 0 %}Other Projects{% else %}All Projects{% endif %}</h2>
  <div class="project-gallery">
    {% for project in other_projects %}
      {% include project-card.html project=project %}
    {% endfor %}
  </div>
</section>
