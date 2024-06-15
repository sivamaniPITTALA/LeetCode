#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        int n = profits.size();
        vector<pair<int, int>> projects(n);
        
        // Step 1: Create a list of projects with their capital requirements and profits
        for (int i = 0; i < n; ++i) {
            projects[i] = {capital[i], profits[i]};
        }
        
        // Step 2: Sort the projects based on their capital requirements
        sort(projects.begin(), projects.end());
        
        priority_queue<int> maxHeap;
        int currentIndex = 0;
        
        // Step 3: Select up to k projects
        for (int i = 0; i < k; ++i) {
            // Step 4: Push all projects that can be started with current capital to the max-heap
            while (currentIndex < n && projects[currentIndex].first <= w) {
                maxHeap.push(projects[currentIndex].second);
                ++currentIndex;
            }
            
            // If no more projects can be started, break out of the loop
            if (maxHeap.empty()) {
                break;
            }
            
            // Step 5: Select the most profitable project
            w += maxHeap.top();
            maxHeap.pop();
        }
        
        return w;
    }
};
