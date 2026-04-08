#include <string>
#include <vector>

using namespace std;

int solution(string name) {
    int answer = 0;
    int len = name.length();
    for (int i = 0; i < len; i++) {
        answer += min(name[i]-'A', 'Z'-name[i]+1);
    }
    
    int minn = len-1;
    
    for (int i = 0; i < len; i++) {
        int a = i+1;
        while (name[a] == 'A' && i < len) a++;
        if (minn > 2*i+(len-a)) minn = 2*i+(len-a);
        if (minn > i+2*(len-a)) minn = i+2*(len-a);
    }
    answer += minn;
    return answer;
}