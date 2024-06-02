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
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head || k == 0) return head;
        int size =1;
        ListNode* temp = head;
        while(temp->next){
            temp = temp->next;
            size++;
        }
        k = k%size;
        if (k == 0) return head;
        temp->next =head;
        ListNode* p = head,*prev;
        for (int i = 0; i < size - k - 1; i++) 
            p = p->next;
        prev = p->next;
        p->next = NULL;
        return prev;
    }

};