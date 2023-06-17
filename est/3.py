def solution(noti_time, do_not_disturb):
    answer = ''
    time = [0 for i in range(23*60+60)]

    for dis in do_not_disturb:
        split_dis = list(map(str, dis.split("~")))

        start = split_dis[0]
        end = split_dis[1]

        (start_hh, start_mm) = map(int, start.split(":"))
        (end_hh, end_mm) = map(int, end.split(":"))

        if start > end:
            start_idx = start_hh*60+start_mm
            end_idx = 23*60+60
            time[start_idx:] = [-1]*(end_idx - start_idx)

            end_idx = end_hh*60+end_mm
            time[ : end_idx] = [-1]*end_idx

        else:
            start_idx = start_hh*60+start_mm
            end_idx = end_hh*60+end_mm
            time[start_idx : end_idx] = [-1]*(end_idx-start_idx)

    (hh,mm) = map(int, noti_time.split(":"))
    noti_idx = hh*60 + mm
    if time[noti_idx] == 0:
        answer = noti_time
    else:
        if 0 in time[noti_idx: ]:
            _idx = time[noti_idx: ].index(0)
            r = (noti_idx+_idx)//60
            c = (noti_idx+_idx)%60

            tmptime = str(r) + ":" + str(c)
            hour,minute = tmptime.split(":")
            formattime = "{:02d}:{:02d}".format(int(hour), int(minute))
            answer = formattime
        elif 0 in time[ : noti_idx]:
            _idx = time[ : noti_idx].index(0)
            r = _idx//60
            c = _idx%60

            tmptime = str(r) + ":" + str(c)
            hour,minute = tmptime.split(":")
            formattime = "{:02d}:{:02d}".format(int(hour), int(minute))
            answer = formattime
        else:
            answer = "impossible"

    return answer

print(solution("23:00", ["22:30~23:40", "23:05~00:45"]))
print(solution("09:55", ["09:55~13:25", "13:25~14:01"]))
print(solution("00:00", ["11:00~01:00", "23:00~13:00"]))
print(solution("23:59", ["00:00~23:59", "11:35~23:59"]))

