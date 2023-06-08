/*
SPPU Computer Engineering DSA Lab 
Group B
Experiment Sr. No. - 6

Beginning with an empty binary search tree, Construct binary searchtree by inserting the values
in the order given. After constructing a binary tree –
i. Insert new node
ii. Find number of nodes in longest path
iii. Minimum data value found in the tree
iv. Change a tree so that the roles of the left and right pointers are swapped atevery node
v. Search a value
*/

#include <iostream>
using namespace std;

struct Node
{
    int val;
    Node *left;
    Node *right;
};

Node *createNode(int val)
{
    Node *temp = new Node();
    temp->val = val;
    temp->left = NULL;
    temp->right = NULL;
    return temp;
}

Node *insertNode(Node *root, int val)
{
    if (root == NULL)
        return createNode(val);
    else
    {
        if (val < root->val)
            root->left = insertNode(root->left, val);
        else if (val > root->val)
            root->right = insertNode(root->right, val);
    }
    return root;
}

int longestPath(Node *root)
{
    if (root == NULL)
        return 0;
    return 1 + (max(longestPath(root->left), longestPath(root->right)));
}

int minElement(Node *root)
{
    // Node *temp = NULL;
    while (root->left != NULL)
        root = root->left;
    // cout << temp ->val;
    return root->val;
}

void swapTree(Node *root)
{
    if (root == NULL)
    {
        return;
    }
    swap(root->left, root->right);
    swapTree(root->left);
    swapTree(root->right);
}

bool search(Node *root, int val)
{
    if (root == NULL)
    {
        return false;
    }
    if (root->val == val)
    {
        return true;
    }
    if (val < root->val)
        return search(root->left, val);
    else
        return search(root->right, val);
}

void inorder(Node *root)
{
    if (root == NULL)
        return;
    inorder(root->left);
    cout << root->val << " ";
    inorder(root->right);
}

int main()
{
    int arr[] = {0, 5, 7, 1, 3, 8, 4, 6, 11};
    Node *root = NULL;
    for (int i = 0; i < (sizeof(arr) / sizeof(arr[0])); i++)
    {
        root = insertNode(root, arr[i]);
    }
    inorder(root);
    cout << endl
         << longestPath(root) << endl;
    cout << minElement(root) << endl;
    cout << search(root, 11) << endl;
    inorder(root);

    return 0;
}   