#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

typedef struct kruskal {
    int from;
    int to;
    int val;
}KS;

vector<KS> edge;

int parent[10002];
int res;

bool comp(KS d1, KS d2)
{
    return d1.val < d2.val;
}

int find(int num)
{
    if (num == parent[num])
        return num;
    return parent[num] = find(parent[num]);
}

int main()
{
    int V, E;

    cout << "test" << endl;
    scanf("%d %d", &V, &E);

    for(int i = 1; i<= V; i++ )
        parent[i] = i;

    for (int i = 0 ; i<E; i++ ) 
    {
        KS ks;
        scanf("%d %d %d", &ks.from, &ks.to, &ks.val);
        edge.push_back(ks);
    }

    sort(edge.begin(), edge.end(), comp);

    for(int i = 0 ; i < E; i++)
    {
        int nv = find(edge[i].from);
        int nw = find(edge[i].to);

        if (nv == nw)
            continue;
        
        parent[nv] = nw;

        res += edge[i].val;
    }

    printf("%d", res);

    return 0;
}
































