# TASK:

# Clock hands
# Write a function that returns the acute angle between two clock hands, with two integers for the number of hours and number of minutes.
# E.g. For 3:00, the acute angle would be 90°. For 6:00, it would be 180°.

# SOLUTION:

def find_angle(hour, minute):
    if hour > 12:
        hour = hour % 12

    h_angle = 360 / 12 * hour
    m_angle = 360 / 60 * minute
    hm_angle = abs(h_angle - m_angle)

    return hm_angle if hm_angle < 180 else 360 - hm_angle

if __name__ == "__main__":

    hour, minute = map(int, input().strip().split(":"))
    angle = find_angle(hour, minute)
    print(int(angle))
    