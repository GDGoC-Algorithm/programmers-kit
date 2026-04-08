#include <string>
#include <vector>
#include <set>
#include <cmath>

using namespace std;
set<int> num;
int check[10];
string curr;

void dfs(int now, string &numbers)
{
    if (now > numbers.length()) return;
    
    for (int i = 0; i < numbers.length(); i++) {
        if (check[i] == 1) continue;
        check[i] = 1;
        curr += numbers[i];
        num.insert(stoi(curr));
        dfs(now+1, numbers);
        curr.pop_back();
        check[i] = 0;
    }
}

bool check_prime(int x)
{
    if (x < 2) return false;
    for (int i = 2; i <= sqrt(x); i++) {
        if (x % i == 0) return false;
    }
    return true;
}

int solution(string numbers) {
    int answer = 0;
    dfs(1, numbers);
    for (int it : num) {
        if (check_prime(it) == true) answer++;
    }
    return answer;
}