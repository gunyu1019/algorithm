#include<stdio.h>
using namespace std;

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
int mx, my, cnt = 0;
char m[20][20];
bool visited[32] = {};

void backtracking(int x, int y, int c) {
    if (c > cnt) cnt = c;
    for (int i = 0; i < 4; i ++) {
        int nx = x + dx[i], ny = y + dy[i];
        if (nx >= mx || ny >= my || nx < 0 || ny < 0)
            continue;
        if (visited[(int)(m[nx][ny])-65])
            continue;
        visited[(int)(m[nx][ny])-65] = true;    
        backtracking(x + dx[i], y + dy[i], c + 1);
        visited[(int)(m[nx][ny])-65] = false;
    }
}

int main() {
    scanf("%d %d\n", &mx, &my);
    for(int i = 0; i < mx; i ++) {
        for(int j = 0; j < my; j ++) {
            scanf("%c", &m[i][j]);
            if ((int)m[i][j] == 10) scanf("%c", &m[i][j]);
            // scanf %c는 \n도 먹어버린다. 맛있냐?
        }
    }
    visited[(int)(m[0][0])-65] = true;   
    backtracking(0, 0, 1);
    
    printf("%d", cnt);
}
