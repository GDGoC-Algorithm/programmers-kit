#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#define ll long long
using namespace std;
bool compare(ll a, ll b)
{
    int a_plus_b = stol(to_string(a) + to_string(b));
    int b_plus_a = stol(to_string(b) + to_string(a));
    return a_plus_b > b_plus_a;
}

string solution(vector<int> n) {
    string answer = "";
    vector <ll> s;
    for (int i = 0; i < n.size(); i++)
    {
        s.push_back(n[i]);
    }
    sort(s.begin(), s.end(), compare);
    for (int i = 0; i < n.size(); i++)
    {
        if (!(s[i] == 0 && answer.size() == 0))
            answer += to_string(s[i]);
    }
    if (answer == "")
        answer = "0";
    return answer;
}