#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>
using namespace std;
map <string, vector<pair<int, int>>> m; // 각 장르의 {재생수, 고유번호}들을 저장하는 딕셔너리
map <string, int> counting; //각 장르의 총 곡수를 세는 딕셔너리

vector<int> solution(vector<string> g, vector<int> p)
{
    vector<int> answer;
    int size = g.size();
    for (int i = 0; i < size; i++)
    {
        counting[g[i]] += p[i]; //총 곡 횟수 더하기
        m[g[i]].push_back({ p[i],-i }); //해당 곡 삽입 {장르, 곡 번호 (오름차순을 위해 -로)}
    }
    map <int, string> t; //임시 딕셔너리
    for (auto i = counting.begin(); i != counting.end(); i++)
    {
        t[-(*i).second] = (*i).first; //장르명과 총 곡수를 반대로 키와 값으로 가지는 딕셔너리 생성. 이렇게 하면 장르가 많이 재생된 횟수로 정렬됨.
    }

    for (auto i = t.begin(); i != t.end(); i++)
    {
        string genre = (*i).second; //장르 불러오기
        sort(m[genre].begin(), m[genre].end()); //정렬 이후 뒤집기. (오름차순을 내림차순으로)
        reverse(m[genre].begin(), m[genre].end());

        answer.push_back(-m[genre][0].second);//음수로 오름차순화 시켰으니 정상화
        if (m[genre].size() > 1) //2개인지아닌지
            answer.push_back(-m[genre][1].second);
    }
    return answer;
}