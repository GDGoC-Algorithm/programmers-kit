#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string solution(string number, int k) {
    string answer = "";
    int select = number.size() - k; //선택해야하는 갯수
    int limit = -1; //이전에 선택한 인덱스 위치
    for (int i = 0; i < select; i++)
    {
        char max = -1;
        int index = -1;

        for (int j = limit + 1; j < number.size() - select + i + 1; j++) //이전 위치부터 최대값 찾기
        {
            if (number[j] > max)
            {
                max = number[j];
                index = j;
            }
            if (max == '9')
            {
                break;
            }
        }
        limit = index;
        answer.push_back(max);
    }
    return answer;
}