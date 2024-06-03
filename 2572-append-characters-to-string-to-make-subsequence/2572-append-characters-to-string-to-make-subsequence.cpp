class Solution {
public:
    int appendCharacters(string s, string t) {
        int k=t.length(),j=0;
        for(int i=0;i<s.length() && j<k;i++){
            if(s[i]==t[j]){
                j++;
            }
        }
        return k-j;
    }
};