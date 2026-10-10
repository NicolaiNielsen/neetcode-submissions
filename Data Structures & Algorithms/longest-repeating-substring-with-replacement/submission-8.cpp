class Solution {
public:
    int characterReplacement(string s, int k) {
        int greatest = 0;
        int l = 0;
        unordered_map<char, int> mp;
        int res = 0;
        for (int r = 0; r < s.size(); r ++) {
            
            if (mp.contains(s[r])) {
                mp[s[r]] += 1;
            } else {
                mp[s[r]] = 1;
            }

            greatest = max(greatest, mp[s[r]]);

            if (greatest < (r - l + 1) - k) {
                mp[s[l]] -= 1;
                l += 1;
            }

            cout << l;
            res = max(res, r - l + 1);

        }
        return res;
    }
};
