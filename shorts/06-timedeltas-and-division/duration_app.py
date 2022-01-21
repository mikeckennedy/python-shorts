import datetime


def main():
    go_time = get_event_time('performance')
    start_time = get_event_time('arrival')

    dt: datetime.timedelta = go_time - start_time

    print(f"We're on stage in {dt.total_seconds()} seconds.")

    days = int(dt / datetime.timedelta(days=1)) % 7
    weeks = int(dt / datetime.timedelta(days=7))
    print(f"We're on stage in {weeks} weeks and {days} day.")


def get_event_time(name: str) -> datetime.datetime:
    if name == 'arrival':
        return datetime.datetime(year=2022, month=2, day=1, hour=8, minute=31)
    elif name == 'performance':
        return datetime.datetime(year=2022, month=2, day=16, hour=20, minute=00)


if __name__ == '__main__':
    main()
