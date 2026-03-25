#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    sort(people.begin(), people.end());
    int a = 0; //첫번째 포인터
    int b = people.size() - 1; //두번째 포인터
    while (1)
    {
        if (people[b] + people[a] <= limit) //안넘으면 옮기기
        {
            a++;
        }
        b--;
        answer++;
        if (a >= b) //같거나 a가 추월하면
        {
            break;
        }
    }
    return answer + (a == b);

}