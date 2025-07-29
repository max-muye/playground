#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, m, odd = 0, even = 0;
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> m;
    if (m % 2 == 0) {
      even++;
    } else {
      odd++;
    }
  }
  cout << odd << " " << even << endl;
  return 0;
}