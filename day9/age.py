age = int(input("Enter your age: "))

if 0 <= age <= 12:
    group = "Kids"
elif 13 <= age <= 19:
    group = "Teenage"
elif 20 <= age <= 40:
    group = "Young"
elif 41 <= age <= 59:
    group = "Prime"
elif age >= 60:
    group = "Senior"
else:
    group = "enter the correct age"

print(f"you belong to the '{group}' group.")
