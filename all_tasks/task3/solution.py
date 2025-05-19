def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals['lesson']
    pupil_intervals = intervals['pupil']
    tutor_intervals = intervals['tutor']
    events = []

    for i in range(0, len(pupil_intervals), 2):
        start = max(pupil_intervals[i], lesson_start)
        end = min(pupil_intervals[i + 1], lesson_end)
        if start < end:
            events.append((start, 1, 'pupil'))
            events.append((end, -1, 'pupil'))

    for i in range(0, len(tutor_intervals), 2):
        start = max(tutor_intervals[i], lesson_start)
        end = min(tutor_intervals[i + 1], lesson_end)
        if start < end:
            events.append((start, 1, 'tutor'))
            events.append((end, -1, 'tutor'))

    events.sort()
    total_time = 0
    pupil_count = 0
    tutor_count = 0
    prev_time = lesson_start

    for time, delta, role in events:
        if time > lesson_end:
            break
        if pupil_count > 0 and tutor_count > 0:
            total_time += time - prev_time
        if role == 'pupil':
            pupil_count += delta
        else:
            tutor_count += delta

        prev_time = time

    return total_time

tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

additional_tests = [
    {
        'intervals': {
            'lesson': [1000, 2000],
            'pupil': [1000, 1200],
            'tutor': [1300, 2000]
        },
        'answer': 0
    },
    {
        'intervals': {
            'lesson': [1000, 2000],
            'pupil': [1000, 2000],
            'tutor': [1000, 2000]
        },
        'answer': 1000
    },
    {
        'intervals': {
            'lesson': [1000, 2000],
            'pupil': [900, 1500, 1800, 2100],
            'tutor': [950, 1900]
        },
        'answer': 600
    },
    {
        'intervals': {
            'lesson': [1000, 2000],
            'pupil': [500, 900, 2100, 2200],
            'tutor': [400, 950, 2050, 2300]
        },
        'answer': 0
    },
    {
        'intervals': {
            'lesson': [1000, 2000],
            'pupil': [1100, 1900],
            'tutor': [1000, 1200, 1300, 1500, 1600, 2000]
        },
        'answer': 700
    }
]

all_tests = tests + additional_tests


if __name__ == '__main__':
    for i, test in enumerate(all_tests):
        test_answer = appearance(test['intervals'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
    print("Все тесты пройдены успешно!")