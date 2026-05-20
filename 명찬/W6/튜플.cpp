#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

vector<int> solution(string s) {
    vector<vector<int>> tuple_list; //튜플을 표현하는 집합을 2차원 백터로 표현
    vector<int> t;
    vector<int> answer;
    string number = "";

    int tuple_size = 0;
    t.push_back(0); //첫 앞자리 비워놓기. 이후 사이즈 정보로 갱신하여 정렬할때 크기순으로.

    for (int i = 1; i < s.size() - 1; i++) //문자열을 2차원 백터로 변환
    {
        char text = s[i];
        if (text == '}')
        {
            t.push_back(stoi(number));
            number = "";

            t[0] = tuple_size + 1; //이번 숫자까지 포함해야하므로 +1 한후 0번째 자리 갱신
            tuple_list.push_back(t);
            t.clear();

            tuple_size = 0;
            t.push_back(0);
        }
        else if (text == ',' && number != "")
        {
            t.push_back(stoi(number)); //숫자 push_back
            tuple_size++; //크기 갱신
            number = "";
        }
        else if (text >= '0' && text <= '9')
        {
            number.push_back(text);
        }
    }
    sort(tuple_list.begin(), tuple_list.end()); //크기 오름차 순으로 정렬

    vector<int> check_list(200000, 0); //기록해나갈 백터
    vector<int> tmp; //기록 백터를 복사해서 이전 기록과 대조할 백터

    for (int i = 0; i < tuple_list.size(); i++)
    {
        tmp = check_list; //이전 기록

        for (int j = 1; j < tuple_list[i].size(); j++)
        {
            tmp[tuple_list[i][j]]--; //1씩 빼주어 대조
            if (tmp[tuple_list[i][j]] == -1) //-1이라는것은 이전 기록에서 저장하지 않은 값이므로
            {
                check_list[tuple_list[i][j]]++; //추가
                answer.push_back(tuple_list[i][j]);
                break;
            }
        }
    }

    return answer;
}