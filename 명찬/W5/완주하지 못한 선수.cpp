#include <string>
#include <vector>
#include <unordered_map>

using namespace std;
unordered_map <string, int> m; //시간복잡도상 map으로는 시간초과 발생
string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    for (int i = 0; i < participant.size(); i++) //참가자 삽입
    {
        m[participant[i]]++;
    }
    for (int i = 0; i < completion.size(); i++) //완주자 삭제
    {
        m[completion[i]]--;
    }
    for (int i = 0; i < participant.size(); i++)
    {
        if (m[participant[i]] == 1) //남아있으면
        {
            return participant[i];
        }
    }
}