#include <string>
#include <vector>
#include <climits>

using namespace std;

int choiced[10] = {0};
int caled[10] = {0};
int life;
int maxx = INT_MIN;

void order_cal(int time, int total_choice, vector<vector<int>> &dungeons)
{
    if (time > total_choice) {
        if (life >= 0) {
            if (maxx < total_choice) maxx = total_choice;
        }
        return;
    }
    for (int i = 0; i < dungeons.size(); i++) {
        if (choiced[i] == 0 || caled[i] == 1) continue;
        if (dungeons[i][0] > life) continue;
        caled[i] = 1;
        life -= dungeons[i][1];
        order_cal(time+1, total_choice, dungeons);
        life += dungeons[i][1];
        caled[i] = 0;
    }
}

void choice(int curr, int total_choice, vector<vector<int>> &dungeons)
{
    if (curr >= dungeons.size()) {
        order_cal(1, total_choice, dungeons);
        return;
    }
    choiced[curr] = 1;
    choice(curr+1, total_choice+1, dungeons);
    choiced[curr] = 0;
    choice(curr+1, total_choice, dungeons);
}

int solution(int k, vector<vector<int>> dungeons) {
    int answer = -1;
    life = k;
    choice(0, 0, dungeons);
    answer = maxx;
    return answer;
}