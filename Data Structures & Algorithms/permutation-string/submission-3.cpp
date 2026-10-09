class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        array<int, 26> a{}, b{};

        int l = 0;
        int r = s2.size() - 1;

        for (char c: s1) {
            a[c - 'a'] += 1;
        }

        for (int r = 0; r < s2.size(); r++) {

            b[s2[r] - 'a'] += 1;

            while (r - l + 1> s1.size()) {
                b[s2[l] - 'a'] -= 1;
                l += 1;
            }

            if (a == b) {
                return 1;
            }

        }
        return 0;
    }
};
