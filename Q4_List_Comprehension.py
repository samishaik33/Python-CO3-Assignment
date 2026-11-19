# Students registered in electives
elective_a = {"S101", "S102", "S103", "S104"}
elective_b = {"S103", "S104", "S105"}

# All registered students
all_students = {
    "S101", "S102", "S103", "S104",
    "S105", "S106", "S107"
}

# Students in both electives
both = elective_a & elective_b

# Students in exactly one elective
exactly_one = elective_a ^ elective_b

# Students in at least one elective
at_least_one = elective_a | elective_b

# Students in neither elective
neither = all_students - at_least_one

# Students only in elective A
only_a = elective_a - elective_b

# Students only in elective B
only_b = elective_b - elective_a

print("Both:", sorted(both))
print("Exactly One:", sorted(exactly_one))
print("At Least One:", sorted(at_least_one))
print("Neither:", sorted(neither))
print("Only A:", sorted(only_a))
print("Only B:", sorted(only_b))