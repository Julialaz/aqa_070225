# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record to the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

# Task 1: Adding my new record to the beginning of the given list

people_records.insert(0, ('Ostap', 'Ukrainets', 25, 'Singer', 'Lviv'))

# print(f'Old list: {people_records}')

# Task 2: In modified list swap elements with indexes 1 and 5 (1<->5). Print result

# Get records that are assigned to indexes 1 and 5
# print(f'Record with index 1: {people_records[1]}') # ('John', 'Doe', 28, 'Engineer', 'New York')
# print(f'Record with index 5: {people_records[5]}') # ('Michael', 'Brown', 22, 'Student', 'Seattle')

popped_element_5_new1 = people_records.pop(5) # ('Michael', 'Brown', 22, 'Student', 'Seattle') - deleted it first, as in case deleting item with '1' index ordering for original original item with '5' index is changed 
popped_element_1_new5 = people_records.pop(1) # ('John', 'Doe', 28, 'Engineer', 'New York')

people_records.insert(1, popped_element_5_new1) # ('Michael', 'Brown', 22, 'Student', 'Seattle') - must be with index 1 - inserted it first, so index for 5 will be correct
people_records.insert(5, popped_element_1_new5) # ('John', 'Doe', 28, 'Engineer', 'New York') - must be with index 5

# Check if indexes switched correctly
# print(f'Switched record with index 1 (must be previous 5): {people_records[1]}') # ('Michael', 'Brown', 22, 'Student', 'Seattle')
# print(f'Switched record with index 5 (must be previous 1): {people_records[5]}')  # ('John', 'Doe', 28, 'Engineer', 'New York')

print('----------------------------------------------------------------------------------')

# New list is printed
print(f'New list with inserted new element to the beginning and swapped elements with indexes 1 and 5 (1<->5) provided: {people_records}')

print('----------------------------------------------------------------------------------')

# Task 3: Check that all people in modified list with records indexes 6, 10, 13 have age >=30. Print condition check result

# Get records that are assigned to indexes 6, 10, 13
# print(f'Record with index 6: {people_records[6]}') # ('Sophia', 'Davis', 40, 'Lawyer', 'Boston')
# print(f'Record with index 10: {people_records[10]}') # ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami')
# print(f'Record with index 13: {people_records[13]}') # ('William', 'Clark', 29, 'Financial Analyst', 'Houston')

age_check_value = 30
age_check_index_6 = people_records[6][2] >= age_check_value
age_check_index_10 = people_records[10][2] >= age_check_value
age_check_index_13 = people_records[13][2] >= age_check_value
general_age_check = age_check_index_6 and age_check_index_10 and age_check_index_13

print(f'Age of person with index 6 is >= 30 ? Response: {age_check_index_6}')
print(f'Age of person with index 10 is >= 30 ? Response: {age_check_index_10}')
print(f'Age of person with index 13 is >= 30 ? Response: {age_check_index_13}')
print(f'Age of all people with indexes 6, 10, 13 is >= 30 ? Response: {general_age_check}')

print('----------------------------------------------------------------------------------')
