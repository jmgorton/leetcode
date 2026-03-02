import sys
sys.path.insert(0, '/Users/jaredgorton/Documents/GitHub/leetcode')
from typing import List
from TestRunner import TestRunner

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # let's use backtracking 
        result = []
        def format(hours: int, mins: int) -> str:
            return f"{hours}:{mins:02}"

        def backtrack(hours: int, mins: int, rem: int):
            if rem < 0: return
            if not rem: 
                if hours < 12 and mins < 60: result.append(format(hours, mins))
                return

            mask = 1
            while mask < 16: # 2 ** 4
                if not hours & mask: backtrack(hours | mask, mins, rem - 1)
                mask <<= 1
            mask = 1
            while mask < 64: # 2 ** 6
                if not mins & mask: backtrack(hours, mins | mask, rem - 1)
                mask <<= 1

        backtrack(0, 0, turnedOn)
        return sorted(result)


TEST_CASES = [
    {"id": 1, "turnedOn": 1, "expected": ["0:01", "0:02", "0:04", "0:08", "0:16", "0:32", "1:00", "2:00", "4:00", "8:00"]},
    {"id": 2, "turnedOn": 9, "expected": []},
    {"id": 3, "turnedOn": 2, "expected": ["0:03","0:05","0:06","0:09","0:10","0:12","0:17","0:18","0:20","0:24","0:33","0:34","0:36","0:40","0:48","1:01","1:02","1:04","1:08","1:16","1:32","2:01","2:02","2:04","2:08","2:16","2:32","3:00","4:01","4:02","4:04","4:08","4:16","4:32","5:00","6:00","8:01","8:02","8:04","8:08","8:16","8:32","9:00","10:00"]}
]

if __name__ == "__main__":
    runner = TestRunner(
        test_cases=TEST_CASES,
        solution_cls=Solution,
        method_name="readBinaryWatch",
        input_keys=["turnedOn"],
    )
    runner.run_tests()