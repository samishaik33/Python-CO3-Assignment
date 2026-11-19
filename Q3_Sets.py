from collections import Counter, defaultdict
import re

complaints = [
    "seeds not received",
    "seeds delayed",
    "fertiliser price high",
    "seeds price high",
    "subsidy not received",
]

stop_words = {"not", "high"}

word_count = {}

for complaint in complaints:
    words = re.findall(r"\b[a-z]+\b", complaint.lower())
    for word in words:
        if word not in stop_words:
            word_count[word] = word_count.get(word, 0) + 1

print("Word Frequencies:", word_count)

# Find top three words
top_three_words = sorted(
    word_count.items(),
    key=lambda x: (-x[1], x[0]),
)[:3]

print("Top Three Words:", top_three_words)

# Group complaints by districts
district_complaints = defaultdict(list)
district_complaints["Kurnool"].append("seeds not received")
district_complaints["Anantapur"].append("fertiliser price high")
district_complaints["Kurnool"].append("seeds price high")

print("District Complaints:", dict(district_complaints))

# Using Counter
counter = Counter()

for complaint in complaints:
    for word in re.findall(r"\b[a-z]+\b", complaint.lower()):
        if word not in stop_words:
            counter[word] += 1

print("Counter Result:", counter)