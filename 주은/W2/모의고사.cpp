#include <string>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

int two[6] = {1, 3, 4, 5};
int three[6] = {3, 1, 2, 4, 5};
vector<pair<int, int>> cnt;

void cnt_answer(vector<int> answers)
{   
    int cnt1, cnt2, cnt3;
    cnt1 = cnt2 = cnt3 = 0;
    for (int i = 0; i < answers.size(); i++) {
        if (answers[i] == (i%5)+1) cnt1++;
        
        if (i%2 == 0) {
            if (answers[i] == 2) cnt2++;
        }
        else {
            if (two[(i/2)%4] == answers[i]) cnt2++;
        }
        
        if (three[(i/2)%5] == answers[i]) cnt3++;   
    }
    
    cnt.push_back({cnt1, 1});
    cnt.push_back({cnt2, 2});
    cnt.push_back({cnt3, 3});
}

bool cmp(pair<int, int> a, pair<int, int> b)
{
    if (a.first == b.first) return a.second < b.second;
    return a.first > b.first;
}

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    cnt_answer(answers);
    sort(cnt.begin(), cnt.end(), cmp);
    
    for (int i = 0; i < cnt.size(); i++) {
        if (i == 0 || cnt[i-1].first == cnt[i].first) answer.push_back(cnt[i].second);
        else break;
    }
    
    return answer;
}