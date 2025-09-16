def min_sec_to_second(video):
    time = video.split(":")
    min = int(time[0])
    sec = int(time[1])
    return min * 60 + sec


def second_to_mm_ss(time):
    min = time // 60
    sec = time % 60
    return f"{min:02}:{sec:02}"


def solution(video_len, pos, op_start, op_end, commands):
    video_len_second = min_sec_to_second(video_len)
    pos_second = min_sec_to_second(pos)
    op_start_second = min_sec_to_second(op_start)
    op_end_second = min_sec_to_second(op_end)

    if op_start_second <= pos_second <= op_end_second:
        pos_second = op_end_second

    for command in commands:
        if command == "next":
            pos_second = min(video_len_second, pos_second + 10)
        elif command == "prev":
            pos_second = max(0, pos_second - 10)

        if op_start_second <= pos_second <= op_end_second:
            pos_second = op_end_second

    return second_to_mm_ss(pos_second)