def solution(files):
    def parse(file):
        i = 0
        
        # HEAD 숫자가 나오기 전까지
        while i < len(file) and not file[i].isdigit():
            i += 1
        
        head = file[:i].lower()
        
        # NUMBER 숫자가 연속되는 부분, 최대 5자리
        j = i
        while j < len(file) and file[j].isdigit() and j - i < 5:
            j += 1
        
        number = int(file[i:j])
        
        return (head, number)
    
    files.sort(key=parse)
    return files
