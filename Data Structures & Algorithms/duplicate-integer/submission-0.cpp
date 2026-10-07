class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std:: unordered_map<int,int> dup;
        for(auto num: nums){
            if(dup.find(num) == dup.end()){
                dup.insert({num,1});
            }
            else
                return true;
        }
        return false;
    }
};