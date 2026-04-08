#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    int x, y;
    
    for (int i = 1; i <= brown/2; i++) {
        x = i;
        y = brown/2-i;
        if (y-2 <= 0) continue;
        if (x*(y-2) == yellow) {
            answer.push_back(y);
            answer.push_back(x+2);
            break;
        }
    }
    
    return answer;
}

