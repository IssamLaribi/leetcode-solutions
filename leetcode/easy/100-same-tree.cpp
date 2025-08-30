/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {

        // If both are null, they are the same
        if (!q && !p) return true;

        // If only one is null, they are not the same
        if (!q || !p) return false;

        // If the values are different, they are not the same
        if (q->val != p->val) return false;

        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};
