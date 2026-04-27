#include <string>
#include <vector>
#include <queue>

using namespace std;
queue<pair<int, int>> q;
priority_queue<int> pq;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    for (int i = 0; i < priorities.size(); i++) {
        q.push({priorities[i], i});
        pq.push(priorities[i]);
    }
    while(!q.empty()) {
        auto[p, th] = q.front();
        q.pop();
        if (pq.top() <= p) {
            answer++;
            pq.pop();
            if (th == location) break;
        }
        else {
            q.push({p, th});
        }
    }
    return answer;
}