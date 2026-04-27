#include <string>
#include <vector>
#include <queue>

using namespace std;
queue<pair<int, int>> q;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;
    int now_weight = 0;
    int time = 0;
    int i = 0;

    while(i < truck_weights.size()) {
        time++;
        while(!q.empty() && q.front().second == time) {
            now_weight -= q.front().first;
            q.pop();
        }
        if (q.size() < bridge_length && now_weight + truck_weights[i] <= weight) {
            now_weight += truck_weights[i];
            q.push({truck_weights[i], time+bridge_length});
            i++;
        }
    }
    while(!q.empty()) {
        auto[w, t] = q.front();
        q.pop();
        time = t;
    }
    answer = time;
    return answer;
}