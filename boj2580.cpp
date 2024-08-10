#include<stdio.h>
#include<queue>
using namespace std;

struct Position {
    int x;
    int y;

    Position(int _x = 0, int _y = 0) {
        this->x = _x;
        this->y = _y;
    }
};

int m[9][9], cnt = 0, fin = 0;
Position a[81];

bool chk(int x, int y, int v) {
    for(int i = 0; i < 9; i ++) {
        if (
            m[i][x] == v
            || m[y][i] == v
            || m[(int)(y / 3) * 3 + i / 3][(int)(x / 3) * 3 + i % 3] == v
        ) return false;
    }
    return true;
}

void backtracking(int c) {
    if (c >= cnt) {
        fin = 1;
        return;
    }
    for(int i = 0; i < 9; i ++) {
        int nx = a[c].x, ny = a[c].y;
        // printf("%d %d %d %d\n", nx, ny, i + 1, chk(nx, ny, i + 1));
        if (chk(nx, ny, i + 1)) {
            m[ny][nx] = i + 1;
            backtracking(c+1);
            if (fin) return;
            m[ny][nx] = 0;
        }
    }
}

int main() {
    for(int i = 0; i < 9; i ++) {
        for(int j = 0; j < 9; j ++) {
            scanf("%d", &m[i][j]);
            if(m[i][j] == 0) {
                a[cnt++] = Position(j, i);
            }
        }
    }

    backtracking(0);


    for(int i = 0; i < 9; i ++) {
        for(int j = 0; j < 9; j ++) {
            printf("%d ", m[i][j]);
        }
        printf("\n");
    }
}
