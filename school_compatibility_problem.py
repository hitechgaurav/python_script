class StudentGrouper:
    def __init__(self, vals):
        self.student_compatibility_factor = vals
        self.max_group_count = 0

    def get_max_group_count(self):
        cache = []
        for data in self.student_compatibility_factor:
            if not len(cache):
                cache.append(data)
                continue
            if data not in cache:
                cache.append(data)
            else:
                cache = []
                self.max_group_count += 1
        return self.max_group_count


if __name__ == '__main__':
    """Test Cases :- Just uncomment the variable and call method to check the answer"""
    # compatibility_factor = [1, 2, 1, 1, 1, 1, 1, 1]
    # compatibility_factor = [1,1]
    # compatibility_factor = [1,2]
    # compatibility_factor = [1, 2, 3]
    # compatibility_factor = [1, 2, 3, 4, 1]
    # compatibility_factor = [1, 2, 3, 4, 1, 5, 6, 5, 7, 8, 8, 8]
    compatibility_factor = [1, 2, 3, 8, 8, 1, 5, 6, 7, 8, 5]
    students = StudentGrouper(compatibility_factor)
    count = students.get_max_group_count()
    print(count)
