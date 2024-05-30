#include <stdio.h>
#include <queue>
#include <algorithm>

using namespace std;

struct Position {
    int x;
    int y;

    Position(int _x = 0, int _y = 0) {
        this->x = _x;
        this->y = _y;
    }
};


int n, m, minimum = 0, wall_cnt = 3;
int map[9][9];

int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

void infection() {
    queue<Position> q;
    int copied_map[9][9] = {};
    
    for (int i = 0; i < n; i ++) {
        for(int j = 0; j < m; j ++) {
            copied_map[i][j] = map[i][j];
            if (map[i][j] == 2) q.push(Position(i, j));
        }
    }

    while (!q.empty()) {
        Position p = q.front();
        q.pop();

        for (int i = 0; i < 4; i ++) {
            int new_x = p.x + dx[i];
            int new_y = p.y + dy[i];
            
            if (new_x < 0 || new_y < 0 || new_x >= n || new_y >= m) continue;
            if (copied_map[new_x][new_y] == 0) {
                copied_map[new_x][new_y] = 2;
                q.push(Position(new_x, new_y));
            }
        }
    }

    int cnt = 0;
    for (int i = 0; i < n; i ++) {
        for(int j = 0; j < m; j ++) {
            if (copied_map[i][j] == 0) cnt ++;
        }
    }

    minimum = max(cnt, minimum);
}

void set_wall(int count, int index_i, int index_j) {
    if (wall_cnt == 0) {
        infection();
        return;
    }

    for (int i = index_i; i < n; i ++) {
        for(int j = index_j; j < m; j ++) {
            if (map[i][j] == 0) {
                map[i][j] = 1;
                wall_cnt -= 1;
                set_wall(count + 1, i, 0);
                wall_cnt += 1;
                map[i][j] = 0;
            }
        }
    }
}

int main() {
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i ++) {
        for(int j = 0; j < m; j ++) {
            scanf("%d", &map[i][j]);
        }
    }
    set_wall(0, 0, 0);

    printf("%d", minimum);
}