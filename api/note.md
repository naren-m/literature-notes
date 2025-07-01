---
layout: null
---
{%- assign file_path = page.file_path | default: "" -%}
{%- if file_path != "" -%}
  {%- assign notes = site.static_files | where: "path", file_path -%}
  {%- if notes.size > 0 -%}
    {%- assign note = notes[0] -%}
    {{ note.content }}
  {%- else -%}
    {%- comment %} Try to find the file in site pages {%- endcomment -%}
    {%- assign pages = site.pages | where: "path", file_path -%}
    {%- if pages.size > 0 -%}
      {{ pages[0].content | markdownify }}
    {%- else -%}
      File not found: {{ file_path }}
    {%- endif -%}
  {%- endif -%}
{%- else -%}
  No file path specified
{%- endif -%}