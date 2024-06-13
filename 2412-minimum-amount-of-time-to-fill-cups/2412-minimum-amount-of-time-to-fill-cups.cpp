class Solution {
public:
    int fillCups(vector<int>& amount) 
    {
        priority_queue<int>q;
        for(int a:amount)
            q.push(a);
        bool flag=true;
        int sum=0;
        while(flag)
        {
            int a=q.top();
            q.pop();
            int b=q.top();
            q.pop();
            if(b==0)
            {
                sum=sum+a;
                flag=false;
            }
            else
            {
                sum++;
                a--;b--;
                q.push(a);
                q.push(b);
            }
        }
        return sum;
    }
};