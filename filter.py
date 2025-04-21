
# def filter_students_by_year(year):
#     start_date = datetime(year, 1, 1)
#     end_date = datetime(year + 1, 1, 1)

#     students = student_collection.find({
#         "join_date": {
#             "$gte": start_date,
#             "$lt": end_date  # strictly less than Jan 1 of next year
#         }
#     })

#     for student in students:
#         print(student)

# # Example usage
# filter_students_by_year(2020)


