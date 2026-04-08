#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    int x, y;
    
    for (int i = 1; i <= brown/2; i++) {
        x = i;
        y = brown/2-i+2;
        if (y-2 <= 0 || x-2 <= 0) continue;
        if ((x-2)*(y-2) == yellow) {
            answer.push_back(y);
            answer.push_back(x);
            break;
        }
    }
    
    return answer;
}
