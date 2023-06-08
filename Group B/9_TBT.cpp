/*
SPPU Computer Engineering DSA Lab
Group B
Experiment Sr. No. - 9

Convert given binary tree into threaded binary tree.
Analyze time and space complexity of the algorithm.
*/

#include <iostream>
using namespace std;

struct Node
{
    //Node structure:
    // |lbit|left|data|right|rbit|

    int data;
    bool lbit, rbit;
    Node *left;
    Node *right;
};

Node *createNode(int data)
{
    Node *temp = new Node();
    temp->data = data;
    temp->lbit = 0;
    temp->rbit = 0;
    temp->left = NULL;
    temp->right = NULL;
    // temp is |0|NULL|data|NULL|0|
    return temp;
}

void insertNode(Node *root, int data)
{
    Node *node = createNode(data);
    if (node->data < root->data)    //if node is less than root
    {
        if (root->lbit == 0)    //if root has no left child
        {
            node->left = root->left;
            node->right = root;
            root->left = node;
            root->lbit = 1;
        }
        else
        {
            insertNode(root->left, data);   //insertion to be done in left child of root 
        }
    }
    else
    {
        if (root->rbit == 0)    //if root has no right child
        {
            node->right = root->right;
            node->left = root;
            root->right = node;
            root->rbit = 1;
        }
        else
        {
            insertNode(root->right, data);  //insertion to be done in right child of root
        }
    }
}

void printTBT(Node *root)       //Inorder Traversing is done
{
    if (root == NULL)
    {
        return;
    }

    if (root->lbit == 1)
    {
        cout << "(";
        printTBT(root->left);
        cout << ")";
    }

    cout << "<--" << root->data << "-->";

    if (root->rbit == 1)
    {
        cout << "(";
        printTBT(root->right);
        cout << ")";
    }
}

int main()
{
    // creating root
    Node *root = createNode(5);
    Node *dummy = createNode(99999); //important to maintain threaded structure 
    dummy->right = dummy;
    dummy->rbit = true;
    dummy->left = root;
    dummy->lbit = true;
    root->left = dummy;
    root->right = dummy;
    // dummy looks like |1|root|99999|dummy|1|

    // node insertion
    int node_arr[] = {12, 3, 16, 2, 1, 20, 7, 4};
    for (int i = 0; i < (sizeof(node_arr) / sizeof(node_arr[0])); i++)
    {
        insertNode(root, node_arr[i]);
    }

    if (root != NULL)
    {
        printTBT(root);
    }

    return 0;
}