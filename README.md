[![Forks][forks-shield]][forks-url] [![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
<a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangoproject120x25.gif" border="0" alt="A Django project." title="A Django project." height="28" /></a>
<a href="https://golang.org/"><img src="https://img.shields.io/badge/Golang-1.16.7-blue?style=for-the-badge" border="0" alt="A Django project." title="A Django project." height="28" /></a>

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/themir8/blog-bot/">
    <img src="./readme/img/blog-bot.jpg" alt="Header">
  </a>

<h1 align="center">📜🤖 Blog Bot</h1>

<p align="center">
    Telegram bot for blogging
    <br />
    <a href="https://github.com/themir8/blog-bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/themir8/blog-bot/issues">Request Feature</a>
    ·
    <a href="https://github.com/themir8/blog-bot/pulls">Send a Pull Request</a>
  </p>
</p>

### Development requires

- [Python 3.9.0](https://www.python.org/downloads/release/python-390/)
- [Golang 1.16.7](https://golang.org/dl/)
- [Django 3](https://www.djangoproject.com/)

### Installation

```sh
# make sure that the virtual environment with python 3.9 is activated

git clone https://gitlab.com/themir8/blog-bot.git

mkdir blog-bot-telegram
git clone https://gitlab.com/themir8/blog-bot.git --branch telegram-bot-go ./blog-bot-telegram

pip install -r blog-bot/requirements.txt  # installing python dependencies
python blog-bot/manage.py migrate # database migration (preparation)
```

### Launch server

```sh
cd blog-bot
python manage.py runserver
```

### Launch telegram bot

```sh
cd blog-bot-telegram
make run
```

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[forks-shield]: https://img.shields.io/github/forks/themir8/blog-bot?style=for-the-badge
[forks-url]: https://github.com/themir8/blog-bot/network/members
[stars-shield]: https://img.shields.io/github/stars/themir8/blog-bot?style=for-the-badge
[stars-url]: https://github.com/themir8/blog-bot/stargazers
[issues-shield]: https://img.shields.io/github/issues/themir8/blog-bot?style=for-the-badge
[issues-url]: https://github.com/themir8/blog-bot/issues
