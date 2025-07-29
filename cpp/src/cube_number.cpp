#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  for (int i = 1; i < n; i++) {
    if (i * i * i == n) {
      printf("Yes\n");
      return 0;
    }
  }
  printf("No\n");
  return 0;
}