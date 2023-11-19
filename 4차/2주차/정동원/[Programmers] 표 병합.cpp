#include <iostream>
#include <vector>
#include <queue>
#include <sstream>

#define MAX_LEN 51
using namespace std;

typedef struct Node Node_t;
typedef struct Node {
	Node_t* parent;
	vector<Node_t*> child;
	string sValue;
}Node_t;

Node_t maps[MAX_LEN][MAX_LEN];

int getInt(string s) {
	int nums = 0;
	if (s.length() > 1) {
		nums = (s[0] - '0') * 10 + (s[1] - '0');
	}
	else {
		nums = (s[0] - '0');
	}
	return nums;
}

void update(string _r, string _c, string _s) {
	int x = getInt(_r);
	int y = getInt(_c);

	Node_t* p = &maps[y][x];

	// 가장 상단이라면 스스로의 값을 설정해준다
	// 가장 상단의 값을 설정해준다.
	while (p->parent != nullptr) {
		p = p->parent;
	}
	p->sValue = _s;
	return;
}

void update_value(string s1, string s2) {
	for (int i = 0; i < MAX_LEN; ++i) {
		for (int j = 0; j < MAX_LEN; ++j) {
			if (maps[i][j].sValue == s1) {
				maps[i][j].sValue = s2;
			}
		}
	}
}

void merge(string _r1, string _c1, string _r2, string _c2) {
	int x1 = getInt(_r1);
	int y1 = getInt(_c1);
	int x2 = getInt(_r2);
	int y2 = getInt(_c2);

	Node_t* p1 = &maps[y1][x1];
	Node_t* p2 = &maps[y2][x2];

	while (p1->parent != nullptr) {
		p1 = p1->parent;
	}

	while (p2->parent != nullptr) {
		p2 = p2->parent;
	}

	// 이미 같은 부모를 갖고 있다면
	if (p1 == p2) { return; }

	// r1, c1으로 값을 갖게되고, r1,c1의 값만 없을 경우에는 r2, c2의 값을 사용한다
	if (p1->sValue == "") {
		p1->sValue = p2->sValue;
	}

	p2->parent = p1;
	p1->child.push_back(p2);
	return;
}

void unmerge(string _r, string _c) {
	int x = getInt(_r);
	int y = getInt(_c);

	Node_t* p = &maps[y][x];

	while (p->parent != nullptr) {
		p = p->parent;
	}

	string origin = p->sValue;

	queue<Node_t*> que;
	que.push(p);

	while (!que.empty()) {
		Node_t* node = que.front();
		que.pop();

		node->parent = nullptr;
		node->sValue = "";
		for (int i = 0; i < node->child.size(); ++i) {
			que.push(node->child[i]);
		}
		node->child.clear();
	}

	maps[y][x].sValue = origin;
	return;
}

void print(string _r, string _c, vector<string>* _vstring) {
	int x = getInt(_r);
	int y = getInt(_c);

	Node_t* p = &maps[y][x];

	while (p->parent != nullptr) {
		p = p->parent;
	}

	if (p->sValue == "") {
		_vstring->push_back("EMPTY");
	}
	else {
		_vstring->push_back(p->sValue);
	}

	return;
}

vector<string> split(string input, char dlim)
{
	vector<string> result;

	stringstream ss;
	string stringBuffer;
	ss.str(input);

	while (getline(ss, stringBuffer, dlim))
	{
		result.push_back(stringBuffer);
	}

	return result;
}

vector<string> solution(vector<string> commands) {
	vector<string> answer;

	for (int i = 0; i < (int)commands.size(); ++i) {
		vector<string> s = split(commands[i], ' ');

		if (s[0] == "UPDATE") {
			if (s.size() == 3) {
				update_value(s[1], s[2]);
			}
			else {
				update(s[2], s[1], s[3]);
			}
		}
		else if (s[0] == "MERGE") {
			merge(s[2], s[1], s[4], s[3]);
		}
		else if (s[0] == "UNMERGE") {
			unmerge(s[2], s[1]);
		}
		else {
			// PRINTF
			print(s[2], s[1], &answer);
		}
	}
	return answer;
}