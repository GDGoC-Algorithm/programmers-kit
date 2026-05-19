def solution(files):
    def split_file(file):
        head, number, tail = "", "", ""
        
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                number_start = file[i:]
                break
                
        for j in range(len(number_start)):
            if not number_start[j].isdigit():
                number = number_start[:j]
                tail = number_start[j:]
                break
        else:
            number = number_start

        return head.lower(), int(number)

    files.sort(key=split_file)
    return files
