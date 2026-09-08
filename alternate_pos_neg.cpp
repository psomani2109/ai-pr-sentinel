class Solution {
  public:
    void rearrange(vector<int> &arr) {
        // code here
        vector <int> pos, neg;
        for(int i:arr)
        {
            if(i>0)
                pos.push_back(i);
            else
                neg.push_back(i);
        }
        int i=0, j=0;
        arr.clear();
        while(i<pos.size() && j>neg.size())
        {
            arr.push_back(pos[i++]);
            arr.push_back(neg[j++]);
        }
        while(i<pos.size())
        {
             arr.push_back(pos[i++]);
        }
        while(i<neg.size())
        {
             arr.push_back(neg[i++]);
        }
    }
};
