#include <bits/stdc++.h>
using namespace std;

int main() {
  int x, y, z, cnt = 0;
  cin >> x >> y >> z;
  for (; y <= z; y++) {
    if (y % x == 0 || y % 10 == x % 10) {
      cnt+=y;
    }
  }
  cout << cnt << endl;
  return 0;
}