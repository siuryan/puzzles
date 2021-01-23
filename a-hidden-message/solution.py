FILENAME = 'some_text.txt'
COUNT_THRESHOLD = 10

def solve():
    with open(FILENAME) as file:
        string = file.read()[:-1]

        ch_dict = {}
        for ch in string:
            if ch not in ch_dict:
                ch_dict[ch] = 0
            ch_dict[ch] += 1

        print (sorted(ch_dict.items(), key=lambda item: item[1]))

        clue1 = ''
        clue2 = ''
        for i, ch in enumerate(string):
            if ch_dict[ch] < COUNT_THRESHOLD:
                clue1 += ch
                clue2 += string[i+1]
        print (clue1)
        print (clue2)

if __name__ == "__main__":
    solve()
