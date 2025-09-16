from collections import defaultdict


def diff_days(today, privacy):
    split_today = today.split(".")
    split_privacy = privacy.split(".")
    year = (int(split_today[0]) - int(split_privacy[0])) * 12 * 28
    month = (int(split_today[1]) - int(split_privacy[1])) * 28
    day = int(split_today[2]) - int(split_privacy[2])
    diff_day = year + month + day

    return diff_day

def solution(today, terms, privacies):
    type_dict = defaultdict(int)

    for term in terms:
        privacy_type, privacy_month = term.split(" ")
        type_dict[privacy_type] = int(privacy_month)

    to_discard = []

    for idx, privacy in enumerate(privacies, start=1):
        priv, typ = privacy.split(" ")
        diff_day = diff_days(today, priv)
        if diff_day >= type_dict[typ] * 28:
            to_discard.append(idx)

    return to_discard