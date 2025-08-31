class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (!root) return true; // If the tree is empty, it is symmetric
        return isMirror(root->left, root->right); // Left and right subtrees comparison
    }

private:
    // Recursive helper
    bool isMirror(TreeNode* t1, TreeNode* t2) {
        if (!t1 && !t2) return true; // If both are null, it is symmetric
        if (!t1 || !t2) return false; // If only one is null, it is not symmetric
        
        return (t1->val == t2->val) // Values must match
            && isMirror(t1->left, t2->right) // t1 left and t2 right comparison
            && isMirror(t1->right, t2->left); // t1 right and t2 left comparison
    }
};

