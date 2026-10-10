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
    bool hasCycle(ListNode* head) {
        ListNode * haare = head;
        ListNode * tortoise = head;

        while (haare and haare->next) {
            haare = haare->next->next;
            tortoise = tortoise->next;

            if (haare == tortoise) return true;
        }

        return false;

    }
};
