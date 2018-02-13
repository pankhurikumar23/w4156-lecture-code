class FrontierCalculator:

    def calculateEfficientFrontier(self, inp: list) -> list:
        output = []
        # Found here: https://stackoverflow.com/questions/3121979/how-to-sort-list-tuple-of-lists-tuples
        inp.sort(key=lambda tup: tup[1])
        min = inp[0]
        i = 0
        flag = 0
        while i < len(inp):
            j = i
            while (inp[j][1] == min[1]):
                if (inp[j][0] > min[0]):
                    min = inp[j]
                if (j+1) == len(inp):
                    flag = 1
                    break
                else: j += 1
            output.append(min)
            if flag == 1:
                break
            min = inp[j]
            i = j

        output.sort(key=lambda tup: tup[0])
        return output