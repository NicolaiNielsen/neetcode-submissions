class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> array(nums.size() * 2);
        int pointer = 0;
        for (int i = 0; i < array.size(); i++) {
            cout << i % nums.size();
            array[i] = nums[i % nums.size()];
        }
        return array;
    }
};