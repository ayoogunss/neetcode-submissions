class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size())
            return false;
        std:: unordered_map<char,int> in1;
        std:: unordered_map<char, int> in2;
        for(int i = 0; i < s.size(); i++){
            in1[s[i]]++;
            in2[t[i]]++;
        }
        // check if char in word1 exists in word2
        for(auto it : in1){
            if(in2.find(it.first) == in2.end() || in2[it.first] != it.second)
                return false;
        }
        return true;
    }
};
