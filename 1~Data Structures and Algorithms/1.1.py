"""unpacking a sequence into separate variables"""
#examples for unpacking a N-element sequence
data = ['AI', 93, 6.14, (2023, 2024, 2025)]
name, mark, tt, year = data
print(name, mark, tt, year) #AI 93 6.14 (2023, 2024, 2025)
_, _, _, (y1, y2, y3) = data
print(y1, y2, y3) #2023 2024 2025