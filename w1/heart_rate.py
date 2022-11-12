"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""


age = float(input('How old are you? '))

max_hr = 220 - age
eighty_five = max_hr * .85
sixty_five = max_hr * .65

print(f'\nWhen you exercise to strengthen your heart, you should keep your heart rate between {sixty_five:.0f} and {eighty_five:.0f} beats per minute.')