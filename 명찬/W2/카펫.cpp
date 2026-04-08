#include <string>
#include <vector>
#include <math.h>


using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    int sum = brown + yellow;
    for (int i = 3; i < sum; i++)
    {
        if (sum % i == 0)
        {
            if (2 * (i + sum / i) - 4 == brown) //테두리 타일 개수 구하고 비교
            {
                answer = { sum / i,i };//작은숫자가 먼저 오므로
                break;
            }
        }
    }



    return answer;
}