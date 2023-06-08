/*
SPPU Computer Engineering DSA Lab 
Group C
Experiment Sr. No. - 13

Represent a given graph using adjacency matrix/list to perform DFS and using adjacency list to perform BFS:
Use the map of the area around the college as the graph. Identify the prominent land marks as nodes 
and perform DFS and BFS on that.
*/

#include <iostream>
#include <queue>
#include <stack>
using namespace std;

int adjacencyMatrix[5][5] = {
    {0, 1, 1, 0, 1},
    {1, 1, 0, 1, 0},
    {1, 1, 0, 0, 1},
    {0, 1, 0, 0, 1},
    {0, 0, 1, 1, 0}
};

void BFS(int startVertex, int n)
{
    bool visited[n] = {false};
    queue<int> q;

    visited[startVertex] = true;
    q.push(startVertex);

    cout << "BFS traversal starting from vertex " << startVertex << ": ";

    while (!q.empty())
    {
        int currentVertex = q.front();
        q.pop();

        cout << currentVertex << " ";

        for (int i = 0; i < n; i++)
        {
            if (adjacencyMatrix[currentVertex][i] == 1 && !visited[i])
            {
                visited[i] = true;
                q.push(i);
            }
        }
    }

    cout << endl;
}

void DFS(int startVertex, int n)
{
    bool visited[n] = {false};
    stack<int> stk;

    visited[startVertex] = true;
    stk.push(startVertex);

    cout << "DFS traversal starting from vertex " << startVertex << ": ";

    while (!stk.empty())
    {
        int currentVertex = stk.top();
        stk.pop();

        cout << currentVertex << " ";

        for (int i = 0; i < n; i++)
        {
            if (adjacencyMatrix[currentVertex][i] == 1 && !visited[i])
            {
                visited[i] = true;
                stk.push(i);
            }
        }
    }

    cout << endl;
}

int main()
{
    int n = 5; // Number of vertices

    int startVertex;
    cout << "Enter the starting vertex for BFS and DFS: ";
    cin >> startVertex;

    BFS(startVertex, n); // BFS traversal
    DFS(startVertex, n); // DFS traversal

    return 0;
}
