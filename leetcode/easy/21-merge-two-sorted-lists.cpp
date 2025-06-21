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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (list1 == NULL) return list2;
        if (list2 == NULL) return list1;
        ListNode* sortedList;
        if (list1->val >= list2->val) {
            sortedList = list2;
            list2 = list2->next;
        } else {
            sortedList = list1;
            list1 = list1->next;
        }
        // Pointer to node to loop over the list
        ListNode* p = sortedList;
        while (list1 || list2) {
            if (list1 != NULL && list2 != NULL) {
                if (list1->val >= list2->val) {
                    p->next = list2;
                    list2 = list2->next;
                } else {
                    p->next = list1;
                    list1 = list1->next;
                }
                p = p->next;
            } else if (list1 != NULL && list2 == NULL) {
                p->next = list1;
                break;
            } else if (list1 == NULL && list2 != NULL) {
                p->next = list2;
                break;
            }
        }  
        return sortedList;
    }
};
