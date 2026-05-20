#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <tuple>
using namespace std;

int type_check(char a) // 숫자 0, 소문자 1, 대문자 2, 기호 3
{
    if ('0' <= a && a <= '9')
    {
        return 0;
    }
    else if ('a' <= a && a <= 'z')
    {
        return 1;
    }
    else if ('A' <= a && a <= 'Z')
    {
        return 2;
    }
    else
    {
        return 3;
    }
}

vector<string> solution(vector<string> files) {
    vector<string> answer;
    vector<tuple<string, int, int>> v; //헤드와 숫자를 분리하여 저장해놓을 배열
    for (int i = 0; i < files.size(); i++) //파일 순회
    {
        string name = files[i];
        string head = ""; //헤드쪽 저장
        string number = ""; //숫자 저장
        int state = 0; //현재 상태. 헤드 수집중이면 0, 숫자 수집중이면 1
        for (int j = 0; j < name.size(); j++)
        {
            char t = name[j]; //파일명의 한 글자
            int type_num = type_check(t); //타입체크. 숫자 0, 소문자 1, 대문자 2, 기호 3
            if (state == 0) //head 수집단계
            {
                if (type_num == 1 || type_num == 3) //소문자나 기호라면
                    head.push_back(t);
                else if (type_num == 2) //대문자라면
                    head.push_back(t - 'A' + 'a'); //대소문자 통합
                else if (type_num == 0) //숫자라면
                {
                    state = 1; //number 수집 단계로 이동
                    number.push_back(t);
                }
            }
            else if (state == 1) //number 수집 단계
                if (type_num == 1 || type_num == 2 || type_num == 3) //숫자 이외의 것이라면
                    break; //탈출
                else if (type_num == 0)
                    number.push_back(t);
        }
        v.push_back({ head,stoi(number),i }); //헤드, 숫자, 순서
    }
    sort(v.begin(), v.end());
    for (int i = 0; i < v.size(); i++)
        answer.push_back(files[get<2>(v[i])]); //순서를 읽어서 파일 인덱스로 텍스트 가져와 push_back
    return answer;
}