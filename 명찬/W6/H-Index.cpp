#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int solution(vector<int> c)
{
    int maxx = 0; //최대값 저장
    sort(c.begin(), c.end()); //정렬
    int state = -1; //이전 인용횟수를 저장하는 변수
    for (int i = 0; i < c.size(); i++)
        if (state != c[i]) //이전 인용홧수와 다르다면
        {
            //
            maxx = max(min((int)c.size() - i, c[i]), maxx);
            state = c[i];
        }
    return maxx;
}