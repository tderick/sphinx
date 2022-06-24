{% if not obj.display %}
:orphan:

{% endif %}

{% set name_length = obj.name.split('.') | length %}
{% if name_length > 1 %}

:py:mod:`{{ obj.name.split('.')[1] }}`
=========={{ "=" * obj.name|length }}


.. py:module:: {{ obj.name }}

{% endif %}

{% block submodules %}
{% set visible_submodules = obj.submodules|selectattr("display")|list %}
{% if visible_submodules %}


.. toctree::
   :titlesonly:
   :maxdepth: 1

{% for submodule in visible_submodules %}
   {{ submodule.short_name }}/index.rst
{% endfor %}


{% endif %}
{% endblock %}
{% block content %}
{% if obj.all is not none %}
{% set visible_children = obj.children|selectattr("short_name", "in", obj.all)|list %}
{% elif obj.type is equalto("package") %}
{% set visible_children = obj.children|selectattr("display")|list %}
{% else %}
{% set visible_children = obj.children|selectattr("display")|rejectattr("imported")|list %}
{% endif %}
{% if visible_children %}

{{ "-" * obj.type|length }}---------

{% set visible_classes = visible_children|selectattr("type", "equalto", "class")|list %}
{% set visible_attributes = visible_children|selectattr("type", "equalto", "data")|list %}
{% if "show-module-summary" in autoapi_options and (visible_classes or visible_functions) %}


{% block functions scoped %}
{% if visible_functions %}
Functions
~~~~~~~~~

.. autoapisummary::

{% for function in visible_functions %}
   {{ function.id }}
{% endfor %}


{% endif %}
{% endblock %}

{% block attributes scoped %}
{% if visible_attributes %}
Attributes
~~~~~~~~~~

.. autoapisummary::

{% for attribute in visible_attributes %}
   {{ attribute.id }}
{% endfor %}


{% endif %}
{% endblock %}
{% endif %}
{% for obj_item in visible_children %}
{{ obj_item.render()|indent(0) }}
{% endfor %}
{% endif %}
{% endblock %}
