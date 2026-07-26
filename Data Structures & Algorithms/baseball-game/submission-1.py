class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for operation in operations:
            if operation.isdigit() or "-" in operation:
                record.append(int(operation))
            elif operation == "+":
                record.append(record[-1] + record[-2])
            elif operation == "D":
                record.append(record[-1] * 2)
            elif operation == "C":
                record.pop(-1)
        return sum(record)