def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    scores = [0, 0, 0]

  
    for i, ans in enumerate(answers):
        for idx, pattern in enumerate(patterns):
            if ans == pattern[i % len(pattern)]:
                scores[idx] += 1

    max_score = max(scores)
    return [i for i, score in enumerate(scores, 1) if score == max_score]
