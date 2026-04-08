#include <string>
#include <vector>
#include <climits>
#include <cstdlib>

using namespace std;
int check[110];
int line[110][110];
int cnt = 0, cnt_a, cnt_b;
int minn = INT_MAX;

void dfs(int n, int x, int y)
{
    check[x] = 1;
    cnt++;
    
    for (int i = 1; i <= n; i++) {
        if (line[x][i] == 1 && check[i] == 0 && i != y) {
            dfs(n, i, y);
        }
    }
}

int solution(int n, vector<vector<int>> wires) {
    int answer = -1;
    int a, b;
    for (int i = 0; i < wires.size(); i++) {
        line[wires[i][0]][wires[i][1]] = 1;
        line[wires[i][1]][wires[i][0]] = 1;
    }
    
    for (int i = 0; i < wires.size(); i++) {
        a = wires[i][0];
        b = wires[i][1];
        for (int j = 1; j <= n; j++) check[j] = 0;
        cnt = 0;
        dfs(n, a, b);
        cnt_a = cnt;
        cnt = 0;
        dfs(n, b, a);
        cnt_b = cnt;
        if (minn > abs(cnt_a-cnt_b)) minn = abs(cnt_a-cnt_b);
    }
    
    answer = minn;
    return answer;
}