class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        eaten = 0
        last_served = 0
        while last_served < len(students):
            if students[0] == sandwiches[0]:
                # if student prefers sandwhich, take it and leave queue
                students.pop(0)
                sandwiches.pop(0)
                eaten += 1
                last_served = 0
            else:
                # if they don't prefer, go to queue's end
                students.append(students[0])
                students.pop(0)
                last_served += 1
        return len(students)