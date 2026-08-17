class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> array(nums.size() * 2);
        int pointer = 0;
        for (int i = 0; i < array.size(); i++) {
            array[i] = nums[pointer];

            if (pointer < nums.size() - 1) {
                pointer ++;
            }
            else {
                pointer = 0;
            }


        }
        return array;
    }
};