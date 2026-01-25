"""
Find common available meeting slot from everyone's calendar
Sample input:
calendars = [
    [(9, 10), (12, 13), (16, 18)],  # Employee 1
    [(10, 11), (12, 14), (16, 17)],  # Employee 2
    [(9, 10), (13, 14), (15, 16)]  # Employee 3
]
Sample output:
O / P: [(11, 12), (14, 15)]
"""
calendars = [
    [(9, 10), (12, 13), (16, 18)],  # Employee 1
    [(10, 11), (12, 14), (16, 17)],  # Employee 2
    [(9, 10), (13, 14), (15, 16)]  # Employee 3
]
start_of_day = 9
end_of_day = 18
duration = 1

"""Approach 1"""

# Approach 1:
def create_available_slots(start, end, duration, meetings):
    slots = []
    # for hour in range(start, end - duration + 1):
    #     slot = (hour, hour + duration)
    #     # check overlap with any meeting
    #     if any(not (slot[1] <= m[0] or slot[0] >= m[1]) for m in meetings):
    #         continue
    #     slots.append(slot)

    # More readable form
    for hour in range(start, end - duration + 1):
        slot = (hour, hour + duration)
        overlap = False
        for m in meetings:
            if slot[0] < m[1] and slot[1] > m[0]:
                overlap = True
                break

        if not overlap:
            slots.append(slot)

    return slots


def common_available_slot(start, end, duration, calendars):
    all_availability = []

    for calendar in calendars:
        all_availability.append(
            set(create_available_slots(start, end, duration, calendar))
        )

    # intersection of all employees' availability
    common_slots = set.intersection(*all_availability)

    return sorted(common_slots)


# Approach 2
# def get_busy_hours(calendars):
#     busy = set()
#     for calendar in calendars:
#         for start, end in calendar:
#             for h in range(start, end):
#                 busy.add(h)
#     return busy
#
# def common_available_slot(start, end, duration, calendars):
#     busy_hours = get_busy_hours(calendars)
#
#     result = []
#
#     hour = start
#     while hour + duration <= end:
#         # check if entire duration is free
#         if all(h not in busy_hours for h in range(hour, hour + duration)):
#             result.append((hour, hour + duration))
#         hour += 1
#
#     return result



if __name__ == '__main__':
    print(common_available_slot(start_of_day, end_of_day, duration, calendars))
