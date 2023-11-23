#include <string>
#include <vector>

#define MAX_LEN 100
#define PLUS 1
#define MINUS 0
#define DIVID 2
using namespace std;

typedef struct Node Node_t;
typedef struct Node {
    Node_t* p;
    long long value;
}Node_t;

long long origin[MAX_LEN];
int prior[MAX_LEN];
Node_t nodes[MAX_LEN];
vector<int> m_vPrior;
int cnt = 0;
long long maxValue = 0;

long long getNum(string _expression, int _s, int _e) {
    long long nums = 0;
    long long ten = 1;

    for (int i = _e; i >= _s; --i) {
        nums += (_expression[i] - '0') * ten;
        ten *= 10;
    }
    return nums;
}

void reset_Nodes(int _idx) {
    for (int i = 0; i < _idx; ++i) {
        nodes[i].value = origin[i];
        nodes[i].p = nullptr;
    }
    return;
}

Node_t* getParent(Node_t* _node) {
    while (_node->p != nullptr) {
        _node = _node->p;
    }
    return _node;
}

void doCal(int _index) {
    long long v = 0;
    Node_t* node1 = getParent(&nodes[_index]);
    Node_t* node2 = getParent(&nodes[_index + 1]);

    switch (prior[_index])
    {
    case 0: v = node1->value - node2->value; break;
    case 1: v = node1->value + node2->value; break;
    case 2: v = node1->value * node2->value; break;
    }
    node2->p = node1;
    node1->value = v;
    return;
}

void forCal(int _nums, int _idx) {
    for (int i = 0; i < _idx - 1; ++i) {
        if (prior[i] == _nums) {
            doCal(i);
        }
    }
    return;
}

void cal(int a, int b, int c, int _idx) {
    reset_Nodes(_idx);

    forCal(a, _idx);
    forCal(b, _idx);
    forCal(c, _idx);

    long long v = getParent(&nodes[0])->value;
    v = v < 0 ? v * (-1) : v;
    if (maxValue < v) {
        maxValue = v;
    }
    return;
}

long long solution(string expression) {
    long long answer = 0;

    int s = 0;
    int e = 0;
    int idx = 0;
    for (int i = 0; i < expression.length(); ++i) {
        // 숫자 값이 아닌 부분을 찾았다면
        if (expression[i] > '9' || expression[i] < '0') {
            switch (expression[i]) {
            case '-': prior[idx] = MINUS; break;
            case '+': prior[idx] = PLUS; break;
            case '*': prior[idx] = DIVID; break;
            }

            origin[idx++] = getNum(expression, s, e - 1);

            s = i + 1;
        }
        ++e;
    }
    // 마지막 숫자 넣어주기
    origin[idx++] = getNum(expression, s, e - 1);

    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            if (i == j) { continue; }
            for (int z = 0; z < 3; ++z) {
                if (i == z || j == z) { continue; }
                cal(i, j, z, idx);
            }
        }
    }

    answer = maxValue;
    return answer;
}