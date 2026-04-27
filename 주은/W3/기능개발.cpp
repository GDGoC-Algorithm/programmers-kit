#include <string>
#include <vector>
#include <queue>

using namespace std;
queue<pair<int, int>> q;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int>::iterator it;
    for (int i = 0; i < progresses.size(); i++) {
        q.push({progresses[i], i});
    }
    int day = 1;
    int cnt = 1;
    while(!q.empty()) {
        auto[p, th] = q.front();
        if (p+speeds[th]*day >= 100) {
            q.pop();
            cnt++;
        }
        else {
            if (day != 1) {
                answer.push_back(cnt);
                cnt = 1;
            }
            if ((100-p)%speeds[th] == 0) day = (100-p)/speeds[th];
            else day = (100-p)/speeds[th] + 1;
            q.pop();
        }
    }
    answer.push_back(cnt);
    return answer;
}