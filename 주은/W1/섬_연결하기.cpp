#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int parent[101];


void init(int N)
{
	int i;
	for (i = 0; i < N; i++) parent[i] = i;
}

int find(int x)
{
	if (parent[x] == x) return x;
	return parent[x] = find(parent[x]);
}

void uni(int a, int b)
{
	int ka, kb;
	ka = find(a); kb = find(b);
	parent[ka] = kb;
}

bool cmp(vector<int> a, vector<int> b) {
    return a[2] < b[2];
}
int solution(int n, vector<vector<int>> costs) {
    int answer = 0;
    init(n);
    sort(costs.begin(), costs.end(), cmp);
    
    for (int i = 0; i < costs.size(); i++) {
        if (find(costs[i][0]) != find(costs[i][1])) {
            answer += costs[i][2];
            uni(costs[i][0], costs[i][1]);
        }
    }
    
    return answer;
}