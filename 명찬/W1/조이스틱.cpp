#include <string>
#include <vector>
#include <math.h>
using namespace std;

int solution(string name) {
    int answer = 0;
    int A_size = 0;
    int MAX_A_size = 0;
    vector <pair<int, int>> v;

    name.push_back('0');
    bool is_A = 0;
    int start_A = -1;
    for (int i = 1; i < name.size(); i++) //연속된 A 검출
    {
        if (name[i] == 'A')
        {
            if (!is_A == 1)
            {
                start_A = i;
                is_A = 1;
            }
            A_size++;
        }
        else
        {
            if (is_A == 1)
            {
                if (MAX_A_size < A_size)
                {
                    MAX_A_size = A_size;
                }
                is_A = 0;
                A_size = 0;
                v.push_back({ start_A,i - 1 });
            }
        }

    }
    int move_min = name.size() - 2; //최대 크기를 문자열 크기로 설정.
    for (int i = 0; i < v.size(); i++)
    {
        int t1 = (v[i].first - 1) * 2 + (name.size() - 2) - v[i].second; //시작점에서 특정 A시작점 전까지 갔다가 A끝점 도달하기. 우 -> 좌
        int t2 = (v[i].first - 1) + ((name.size() - 2) - v[i].second) * 2; //시작점에서 특정 A끝점 전까지 갔다가 A시작점 도달하기. 좌 -> 우
        if (move_min > min(t1, t2))
        {
            move_min = min(t1, t2);
        }
    }
    for (int i = 0; i < name.size() - 1; i++)
    {
        int t1 = 'Z' - name[i] + 1;
        int t2 = name[i] - 'A';
        answer += min(t1, t2);
    }
    return answer + move_min;
}