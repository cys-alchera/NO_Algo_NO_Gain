class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        for i in sandwiches:
            if i in students:
                students.remove(i)
            else:
                break
        return len(students)
    # def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
    #     while sandwiches[0] in students:
    #         if students[0] == sandwiches[0]:
    #             sandwiches.pop(0)
    #         else:
    #             students.append(students[0])
    #         students.pop(0)

    #         if len(students) == 0:
    #             return len(students)

    #     return len(students)