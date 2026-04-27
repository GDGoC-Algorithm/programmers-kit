#include<string>
#include<stack>
#include <iostream>

using namespace std;

stack<int> st;

bool solution(string s)
{
    bool answer = true;
    int len = s.length();

    for (int i = 0; i < len; i++) {
        if (s[i] == '(') {
            st.push(1);
        }
        else {
            if (st.empty()) {
                answer = false;
            }
            else st.pop();
        }
    }

    if (!st.empty()) answer = false;
    return answer;
}