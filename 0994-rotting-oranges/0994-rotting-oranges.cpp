class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();

        vector<vector<bool>> vis(n, vector<bool>(m, false));
        queue <pair <pair<int,int>, int>> q;
        int ans = 0;

        for (int i=0 ; i<n; i++){
            for(int j=0; j<m ; j++){
                if(grid[i][j] == 2){
                    q.push({{i,j}, 0});
                    vis[i][j] = true;
                }
            }
        }

        while(q.size() > 0){
            int i = q.front().first.first;
            int j = q.front().first.second;
            int time = q.front().second;
            q.pop();
            ans  = max(ans, time);

            if(i-1>= 0 && !vis[i-1][j] && grid[i-1][j] == 1){ //top
                q.push({{i-1,j}, time+1});
                vis[i-1][j] = true;
            }
            if(j+1 < m && !vis[i][j+1] && grid[i][j+1] == 1){ //right
                q.push({{i,j+1}, time+1});
                vis[i][j+1] = true;
            }
            if(i+1 <n  && !vis[i+1][j] && grid[i+1][j] == 1){ //bottom
                q.push({{i+1,j}, time+1});
                vis[i+1][j] = true;
            }
            if(j-1 >= 0  && !vis[i][j-1] && grid[i][j-1] == 1){ //bottom
                q.push({{i,j-1}, time+1});
                vis[i][j-1] = true;
            }
        }


        // check fresh orange exist or not
        for (int i = 0; i< n ; i++){
            for(int j =0; j<m; j++){
                if (grid[i][j] == 1 && !vis[i][j]){
                    return -1;
                }
            }
        }

        return ans;
        
    }
};