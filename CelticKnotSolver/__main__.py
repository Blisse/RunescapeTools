import collections

def main():
    knot1 = collections.deque(["Cs", "Ds", "F", "St", "As", "Bl", "M", "De", "So", "Bl", "Ai", "W", "St", "Lw", "Bl", "Du"])
    knot2 = collections.deque(["Ms", "Bl", "M", "Co", "Lv", "Du", "Bd", "Bl", "De", "Ms", "So", "Bl", "Ai", "Na", "Bl", "W"])
    knot3 = collections.deque(["Ai", "Na", "F", "Ms", "St", "Du", "Ai", "Lw", "M", "So", "E", "Co", "Bl", "So", "Lv", "Bl"])

    knot1_to_2 = [5, 11]
    knot2_to_1 = [3, 13]
    knot1_to_3 = [6, 10]
    knot3_to_1 = [2, 14]
    knot2_to_3 = [5, 11]
    knot3_to_2 = [3, 13]

    for i in range(1, len(knot1)):
        knot1.rotate(1)

        for j in range(1, len(knot2)):  
            knot2.rotate(1)

            for k in range(1, len(knot3)):
                knot3.rotate(1)

                if (knot1[knot1_to_2[0]] == knot2[knot2_to_1[0]] and
                    knot1[knot1_to_2[1]] == knot2[knot2_to_1[1]] and
                    knot1[knot1_to_3[0]] == knot3[knot3_to_1[0]] and
                    knot1[knot1_to_3[1]] == knot3[knot3_to_1[1]] and
                    knot2[knot2_to_3[0]] == knot3[knot3_to_2[0]] and
                    knot2[knot2_to_3[1]] == knot3[knot3_to_2[1]]):

                    print("Solution found")
                    print(knot1)
                    print(knot2)
                    print(knot3)

if __name__ == "__main__":
    main()
