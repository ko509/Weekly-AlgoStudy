#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
#define ll long long
#define MAX 260
ll Union[MAX];
typedef struct Tree {
    ll parent;
    ll sibling;
}Tree;
ll U(ll& cur, Tree* tree)
{
    if (tree[cur].parent == cur)
    {
        return cur;
    }
    else
    {
        Union[cur] = U(tree[cur].parent, tree);
        return Union[cur];
    }

}
vector<int> solution(vector<long long> numbers) {
    vector<int> answer;
    for (auto number : numbers)
    {

        if (number == 1) {
            answer.push_back(1);
            continue;
        }

        Tree tree[MAX];
        for (int z = 0; z < MAX; z++)
            tree[z].parent = tree[z].sibling = 0;

        ll x = 1, bin[MAX], num = number;
        int t = 0, cnt = 1, sum = 0;
        fill(Union, Union + MAX, 0);
        fill(bin, bin + MAX, 0);
        while (x <= number)
        {
            x <<= 1;
            t++;
        }
        while (cnt <= t)
        {
            cnt <<= 1;
        }
        cnt--;

        int root = (cnt + 1) / 2, first = 1, mul = 4;
        for (int j = cnt; j > 0; j--)
        {
            bin[j] = num & 1;
            num >>= 1;
        }

        for (auto j : bin)
        {
            sum += j;
        }

        if (sum == 1 || sum == cnt)
        {
            answer.push_back(1);
            continue;
        }

        while (first != root)
        {
            for (ll i = first; i <= cnt; i += mul)
            {
                ll left = i;
                ll right = i + mul / 2;
                ll parent = (left + right) / 2;
                if (right <= cnt && bin[right])
                {
                    if (bin[parent])
                        tree[right].parent = parent;
                    else
                        tree[right].parent = right;
                    tree[left].sibling = right;
                }if (bin[left])
                {
                    if (bin[parent])
                        tree[left].parent = parent;
                    else
                        tree[left].parent = left;
                    if (right <= cnt)
                        tree[right].sibling = left;
                }
            }
            first *= 2;
            mul *= 2;
        }
        if (bin[root])
            tree[root].parent = root;
        else
        {
            answer.push_back(0);
            continue;
        }
        for (int i = 1; i <= cnt; i++)
        {
            if (bin[i])
                Union[i] = i;
        }

        for (ll i = 1; i <= cnt; i++)
        {
            if (Union[i])
                U(i, tree);
        }
        int cnts = 0;

        for (int i = 1; i <= cnt; i++)
        {
            if (Union[i] == i)
                cnts++;
        }
        int res = 1;

        if (cnts != 1)
            res = 0;
        answer.push_back(res);
    }
    return answer;
}