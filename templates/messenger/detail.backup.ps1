{% extends "base.html" %}
{% block title %}{{ message.subject }}{% endblock %}
{% block content %}
<h2>📩 {{ message.subject }}</h2>
<p><strong>De:</strong> {{ message.sender.username }}</p>
<p><strong>Para:</strong> {{ message.recipient.username }}</p>
<p><strong>Fecha:</strong> {{ message.created_at|date:"d/m/Y H:i" }}</p>
<pre style="white-space:pre-wrap">{{ message.body }}</pre>
<p>
  <a href="{% url 'messenger_inbox' %}">📥 Bandeja</a> |
  <a href="{% url 'messenger_sent' %}">📤 Enviados</a> |
  <a href="{% url 'messenger_reply' message.id %}">↩️ Responder</a>
</p>
{% endblock %}
