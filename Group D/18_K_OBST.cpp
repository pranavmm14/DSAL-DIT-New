/*
SPPU Computer Engineering DSA Lab 
Group D
Experiment Sr. No. - 18

Given sequence k = k1 <k2 <... <kn of n sorted keys, with a search probability pi for each key ki. 
Build the Binary search tree that has the least search cost given the access probability for each key?
*/

#include <iostream>
using namespace std;

const int MAX = 100;
void printOptimalBST(float keys[], int root[][MAX], int i, int j, int level);

void constructOBST(float keys[], float searchProbs[], int n) {
    float c[MAX][MAX] = {0};
    float w[MAX][MAX] = {0};
    int root[MAX][MAX] = {0};

    for (int i = 0; i < n; i++) {
        w[i][i] = searchProbs[i];
        c[i][i] = 0;
        root[i][i] = i;
    }

    for (int d = 1; d < n; d++) {
        for (int i = 0; i < n - d; i++) {
            int j = i + d;
            w[i][j] = w[i][j - 1] + searchProbs[j] + keys[j];
            c[i][j] = INT_MAX;

            for (int r = i; r <= j; r++) {
                float cost = ((r > i) ? c[i][r - 1] : 0) + ((r < j) ? c[r + 1][j] : 0) + w[i][j];
                if (cost < c[i][j]) {
                    c[i][j] = cost;
                    root[i][j] = r;
                }
            }
        }
    }

    cout << "Optimal BST:\n";
    printOptimalBST(keys, root, 0, n - 1, 0);
}

void printOptimalBST(float keys[], int root[][MAX], int i, int j, int level) {
    if (i > j) return;

    int r = root[i][j];
    cout << "(" << keys[r] << " Level: " << level << ") ";

    printOptimalBST(keys, root, i, r - 1, level + 1);
    printOptimalBST(keys, root, r + 1, j, level + 1);
}

int main() {
    int n;
    cout << "Enter the number of keys: ";
    cin >> n;

    float keys[MAX], searchProbs[MAX];
    cout << "Enter the keys:\n";
    for (int i = 0; i < n; i++) {
        cin >> keys[i];
    }

    cout << "Enter the search probabilities:\n";
    for (int i = 0; i < n; i++) {
        cin >> searchProbs[i];
    }

    constructOBST(keys, searchProbs, n);

    return 0;
}
