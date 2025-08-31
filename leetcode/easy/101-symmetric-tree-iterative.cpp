class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (!root) return true; // If tree is empty, it is symmetric

        queue <TreeNode *> q;
        q.push(root->left);
        q.push(root->right);

        while (!q.empty()) {
            // Take two nodes at a time to compare
            TreeNode *t1 = q.front();
            q.pop();
            TreeNode *t2 = q.front();
            q.pop();

            if (!t1 && !t2) continue; // If both are null, symmetric so far
            if (!t1 || !t2) return false; // If only one is null, not symmetric
            if (t1->val != t2->val) return false; // If values are different, not symmetric

            // push the next nodes to the queue
            // And ensure comparing t1 right with t2 left, t1 left with t2 right 
            q.push(t1->left);
            q.push(t2->right);
            q.push(t1->right);
            q.push(t2->left);
        }
        return true; // If the loop finish, then no assymetry was found
        }
    }
};
