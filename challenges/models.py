from django.db import models

from datetime import datetime
from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, BinaryAttribute, BooleanAttribute, UnicodeSetAttribute, UTCDateTimeAttribute, NumberAttribute
)


class Challenge(Model):
    class Meta:
        table_name = "Challenge"
        region = 'us-east-2'

    challenge_month = UnicodeAttribute(attr_name="month", hash_key=True)
    challenge_text = UnicodeSetAttribute(attr_name="challenge")
    completed = BooleanAttribute(default=False)
    created_at = UTCDateTimeAttribute(null=True)

if not Challenge.exists():
    Challenge.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
    print("Table created")

def make_challenge():
    June_challenge = Challenge('July', challenge_text=["This is my 1st July challenge","This is my 2nd July challenge"], completed=True, created_at=datetime.now())
    June_challenge.save()
    print("Saved the challenge")


class Thread(Model):
    class Meta:
        table_name = 'Thread'
        region = 'us-east-2'

    forum_name = UnicodeAttribute(hash_key=True)
    subject = UnicodeAttribute(range_key=True)
    views = NumberAttribute(default=0)
    replies = NumberAttribute(default=0)
    answered = NumberAttribute(default=0)
    tags = UnicodeSetAttribute()
    last_post_datetime = UTCDateTimeAttribute(null=True)
