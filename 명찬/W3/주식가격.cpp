#include <string>
#include <vector>
#include <stack>
#include <iostream>
using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer(prices.size(), 0);
    stack <pair<int, int>> s; //값과 위치를 담은 pair stack 생성
    for (int i = 0; i < prices.size(); i++)
    {
        pair<int, int> ts;
        while (!s.empty())
        {
            ts = s.top();
            if (ts.first > prices[i]) //스택의 맨 윗값보다 크다면
            {
                s.pop();
                int t = i - ts.second;
                answer[ts.second] = t; //없에고 입력
            }
            else
                break;

        }
        s.push({ prices[i],i }); //현재 값 삽입
    }
    while (!s.empty()) //마지막까지 남은 주식들 계산
    {
        pair<int, int> ts = s.top();
        int t = prices.size() - ts.second;
        answer[ts.second] = t - 1;
        s.pop();
    }
    return answer;
}