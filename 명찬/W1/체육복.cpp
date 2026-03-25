#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    vector <int> v(n + 2, 1);
    for (int i = 0; i < lost.size(); i++)
    {
        v[lost[i]] = 0;
    }
    for (int i = 0; i < reserve.size(); i++)
    {
        v[reserve[i]] += 1;
    }

    for (int j = 0; j < n / 2; j++) //전달후 다시 검토 n/2번 수행.
    {
        for (int i = 1; i < n + 1; i++) //한쪽에만 도난당한 친구가 있으면 전달.
        {
            if (v[i] == 2)
            {
                if (v[i - 1] == 0 && v[i + 1] != 0)
                {
                    v[i - 1] = 1;
                    v[i] = 1;
                }
                if (v[i - 1] != 0 && v[i + 1] == 0)
                {
                    v[i + 1] = 1;
                    v[i] = 1;
                }
            }
        }
    }
    for (int i = 1; i < n + 1; i++) //이후 양쪽에 둘다 체육복이 없는 경우와 있는 경우 처리
    {

        if (v[i] == 1)
        {
            answer++;
        }
        else if (v[i] == 2 && v[i - 1] == 0 && v[i + 1] == 0) //양쪽에 있으면 한쪽에 전달.
        {
            answer += 2;
        }
        else if (v[i] == 2)
        {
            answer++;
        }
    }
    return answer;
}