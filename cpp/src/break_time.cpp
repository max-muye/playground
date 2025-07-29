#include <bits/stdc++.h>
using namespace std;

int main() {
    int h,s,m,t;
    cin>>h>>s>>m>>t;
    s+=t;
    m+=s/60;
    s%=60;
    h+=m/60;
    h%=24;
    printf("%02d %02d %02d",h,m,s);
    return 0;
}