/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummyNode = new ListNode;
        ListNode* t1 = l1;
        ListNode* t2 = l2;
        int carry = 0;
        ListNode* currNode = dummyNode;
        while (t1 || t2) {
            ListNode* newNode = new ListNode;
            if (t1 && t2) {
                newNode->val = t1->val + t2->val + carry;
                carry = 0;
                if (newNode->val >= 10) {
                    carry = 1;
                    newNode->val -= 10;
                }
                currNode->next = newNode;
                currNode = currNode->next;
                t1 = t1->next;
                t2 = t2->next;
            } else if (t1) {
                newNode->val = t1->val + carry;
                carry = 0;
                if (newNode->val >= 10) {
                    carry = 1;
                    newNode->val -= 10;
                }
                currNode->next = newNode;
                currNode = currNode->next;
                t1 = t1->next;
            } else {
                newNode->val = t2->val + carry;
                carry = 0;
                if (newNode->val >= 10) {
                    carry = 1;
                    newNode->val -= 10;
                }
                currNode->next = newNode;
                currNode = currNode->next;
                t2 = t2->next;
            }
        }
        if (carry) {
            ListNode* LastcarryNode = new ListNode(carry);
            currNode->next = LastcarryNode;
        } 
        return dummyNode->next;
    }
};
