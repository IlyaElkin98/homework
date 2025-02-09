def filter_by_state(filt_logs: list[dict], key_default: str = "EXECUTED") -> list[dict]:
    """Функция принимающая список словарей и возвращающая новый список словарей, содержащие параметр 'EXECUTED'"""

    filt_dict = []

    for i in filt_logs:
        if i["state"] == key_default:
            filt_dict.append(i)
        else:
            continue

    return filt_dict


def sort_by_date(sort_logs: list[dict], arg_sort: bool = True) -> list:
    """
    Функция принимающая список словарей и возвращающая список словарей,
    отсортированных по параметру 'arg_sort', в порядке убывания
    """

    return sorted(sort_logs, key=lambda x: x["date"], reverse=arg_sort)


print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
