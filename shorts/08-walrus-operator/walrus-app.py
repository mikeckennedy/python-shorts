import datetime
import re
from typing import Optional

# PEP 572 – Assignment Expressions (aka walrus operator)

# What is it?
creator = "Professor Falken"

name = input("What is your name? ")
if name == creator:
    print(f"Greetings {name}, would you like to play a game?")

# Using the walrus:
# Mistake in the video: Forgot to add the () here and name = True rather than input.
if (name := input("What is your name? ")) == creator:
    print(f"Greetings {name}, would you like to play a game?")

# ****************************************************************************
r = re.compile(pattern=".* ([0-9]+)x([0-9]+) .*")
text = 'This video has a resolution of 2560x1440 pixels.'

match = r.match(text)
if match and len(match.groups()) >= 2:
    w = match.groups()[0]
    h = match.groups()[1]
    print(f'The new resolution is width: {w} x {h}')

# Using the walrus:


if match := r.match(text) and len(g := match.groups()) >= 2:
    print(f'The new resolution is width: {g[0]} x {g[1]}')





# ****************************************************************************
class User:
    id_: int
    created_date: datetime.datetime

    def __init__(self, id_: int, date):
        self.id_ = id_
        self.created_date = date

    def __str__(self):
        return f'User: id={self.id_}, created={self.created_date.date().isoformat()}'

    def __repr__(self):
        return str(self)


def get_user_by_id(user_id: int) -> Optional[User]:
    now = datetime.datetime.now()
    rand_users = dict()
    rand_users[2] = User(2, now - datetime.timedelta(days=1))
    rand_users[7] = User(7, now - datetime.timedelta(days=100))
    rand_users[11] = User(11, now - datetime.timedelta(days=2))

    return rand_users.get(user_id)


user_ids = [
    1, 2, 7, 11, ]
cutoff_date = datetime.datetime.now() - datetime.timedelta(days=7)

active_users = [
    get_user_by_id(uid)
    for uid in user_ids
    if get_user_by_id(uid) and get_user_by_id(uid).created_date > cutoff_date
]

print(active_users)

# Using the walrus:
active_users = [
    user
    for uid in user_ids
    if (user := get_user_by_id(uid)) and user.created_date > cutoff_date
]

print(active_users)

# ****************************************************************************

prompt_text = "Which action? [a], [b], or [c] (ENTER to exit)? "
command = input(prompt_text)

while command.strip() != '':
    print(f"You chose to perform action '{command}'!")
    command = input(prompt_text)

print("Bye now!")

# Using the walrus:


while (command := input(prompt_text)).strip() != '':
    print(f"You chose to perform action '{command}'!")

print("Bye now!")

# ****************************************************************************
# What value matched any() or the all()?
values = [55, 7, 22, 200, 15, -5, 75, -20, -10]
if any(v < 0 for v in values):
    print("We have negatives!")
else:
    print("Only non-negative numbers for us.")

if all(v < 0 for v in values):
    print("ALL numbers are negatives!")
else:
    print("At least one non-negative number exists.")

# Using the walrus:
if any((first := v) < 0 for v in values):
    print(f"We have negatives, the first is {first}!")
else:
    print("Only non-negative numbers for us.")

if all((counterpoint := v) < 0 for v in values):
    print("ALL numbers are negatives!")
else:
    print(f"At least one non-negative number exists, for example: {counterpoint}")
