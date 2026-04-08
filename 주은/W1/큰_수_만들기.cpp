#include <string>
#include <vector>

using namespace std;

string solution(string number, int k) {
    string answer = "";
    int len = number.length();
    for (int i = 0; i < len; i++) {
        while(answer.length() != 0 && k > 0 && answer.back() < number[i]) {
            answer.pop_back();
            k--;
        }
        answer += number[i];
    }
    
    while (k > 0) {
        answer.pop_back();
        k--;
    }
    return answer;
}