from faker import Factory
import random

from hashids import Hashids

from .models import Short, Click

fake = Factory.create()


def get_hash_id(rand_int):
    hashids = Hashids(salt='tiyd python 2015-08', alphabet='abcdefghijklmnopqrstuvwxyz0123456789')
    return hashids.encode(Short.objects.last().id)


def load_bookmarks():
    for _ in range(1000):
        short = Short(
                bookmark=fake.url(),
                short_url=get_hash_id(Short.objects.last().id),
                click_count=random.randint(0, 1000)
            )
        short.save()


def load_clicks():
    for _ in range(10000):
        click = Click(short_id=random.randint(5, 1000))
        click.save()
