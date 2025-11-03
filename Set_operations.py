developer_1 = {"Python", "SQL", "Git", "Flask"}
developer_2 = {"Python", "Java", "Git", "Django"}

print("Common Skills:", developer_1 & developer_2)        # intersection
print("Unique to Dev 1:", developer_1 - developer_2)      # difference
print("All Skills:", developer_1 | developer_2)           # union
