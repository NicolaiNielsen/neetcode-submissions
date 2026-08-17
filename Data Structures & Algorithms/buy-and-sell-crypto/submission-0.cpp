class Solution {
public:
    int maxProfit(vector<int>& prices) {
        //Kardanes algorithm
        int min_value = prices[0];
        int result = 0;
        for (int i = 0; i < prices.size(); i++) {
            min_value = min(min_value, prices[i]);
            result = max(prices[i] - min_value, result);
        }

        return result;

    }
};
