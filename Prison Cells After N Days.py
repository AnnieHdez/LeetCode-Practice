class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        N = (N - 1) % 14 + 1;
        temp = [0]*8
        for j in range(1,7):
            if cells[j-1] == cells[j+1]:
                temp[j] = 1
            else:
                temp[j] = 0

        cells = temp[0:8]

        for i in range(N-1):
            for j in range(1,7):
                if cells[j-1] == cells[j+1]:
                    temp[j] = 1
                else:
                    temp[j] = 0
            cells = temp[0:8]     

        return cells