---
layout: page
title: Photography
permalink: /photography/
---

{% assign photo_files = site.static_files | where_exp: "file", "file.path contains '/assets/photography/'" | sort: "path" %}

<section class="photography-intro">
  <p class="photography-eyebrow">Outside Engineering</p>
  <p class="photography-lede">
    A small gallery for the hobby side of things. If you couldn't tell already - I'm a <em>slight</em> fan of planes! But apart from that, I like to travel, hike, and explore. Mixed in with the plane photos, there should be some pictures from my trips. 
  </p>
</section>

<section class="photography-gallery">
  {% assign photo_count = 0 %}
  {% for photo in photo_files %}
    {% assign photo_path = photo.path | downcase %}
    {% if photo_path contains '.jpg' or photo_path contains '.jpeg' or photo_path contains '.png' or photo_path contains '.webp' or photo_path contains '.gif' %}
      {% assign photo_count = photo_count | plus: 1 %}
      <figure class="photo-card">
        <a href="{{ photo.path | relative_url }}" target="_blank" rel="noopener noreferrer">
          <img
            src="{{ photo.path | relative_url }}"
            alt="{{ photo.basename | replace: '-', ' ' | replace: '_', ' ' }}"
            loading="lazy"
          >
        </a>
      </figure>
    {% endif %}
  {% endfor %}

  {% if photo_count == 0 %}
    <div class="photography-empty">
      <p>No photos in the gallery yet.</p>
      <p>Start by dropping a few images into <code>assets/photography/</code>.</p>
    </div>
  {% endif %}
</section>
