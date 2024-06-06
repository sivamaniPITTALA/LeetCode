class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
    if (hand.size() % groupSize != 0) {
        return false; 
    }

    map<int, int> count;
    for (int card : hand) {
        count[card]++;
    }

    priority_queue<int, vector<int>, greater<int>> minHeap;
    for (const auto& entry : count) {
        minHeap.push(entry.first);
    }

    while (!minHeap.empty()) {
        int first = minHeap.top();
        for (int i = 0; i < groupSize; i++) {
            if (count[first + i] > 0) {
                count[first + i]--;
                if (count[first + i] == 0) {
                    if (minHeap.top() == first + i) {
                        minHeap.pop();
                    }
                }
            } else {
                return false;
            }
        }
    }

    return true;
}

};