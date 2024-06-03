class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int n=arr.size();
        int m=arr[n-1];
        arr[n-1]=-1;
        for(int i=n-2; i>=0; i--)
        {
            int c=m;
               m=max(arr[i],m);
            arr[i]=c;
        }
        return arr;
    }
};