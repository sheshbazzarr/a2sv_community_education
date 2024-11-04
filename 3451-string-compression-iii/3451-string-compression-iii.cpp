class Solution {
public:
    string compressedString(string word) {
        string s = "";
        int i = 0, n = (int)word.length();
        stack<char> stk;
        while (i < n) {
            stk.push(word[i]);
            int j = i + 1;
            while (j < n && stk.top() == word[j] && (int)stk.size() < 9) stk.push(word[j]), ++j;
            s.push_back('0' + (int)stk.size());
            s.push_back(stk.top());
            while (!stk.empty()) stk.pop();
            i = j;
        }
        return s;
    }
};