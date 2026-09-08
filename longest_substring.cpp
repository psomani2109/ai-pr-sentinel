#include <iostream>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> charIndex;
        int maxLength = 0;
        int left = 0;

        for (int right = 0; right <= s.length(); right++) {
            char currentChar = s[right];

            if (charIndex.find(currentChar) != charIndex.end()) {
                left = charIndex[currentChar] + 1;
            }

            charIndex[currentChar] = right;
            maxLength = max(maxLength, right - left + 1);
        }

        return maxLength;
    }
};

int main() {
    Solution sol;
    string test = "pwwkew";
    cout << "Max Length: " << sol.lengthOfLongestSubstring(test) << endl;
    return 0;
}
