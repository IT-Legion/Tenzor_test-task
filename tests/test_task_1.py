import pytest


def test_url(url):
    if "tensor.ru" in url:
        print("Первая ссылка ведет на сайт tensor.ru")
    else:
        print("Первая ссылка не ведет на сайт tensor.ru")
