---
layout: post
title: Codechef July Challenge 2014部分题解
categories: 
    - Tech
tags: 
    - C++
    - Codechef
date: 2014-07-14 17:31:52
---

# Dish Owner（并查集）

链接：[http://www.codechef.com/JULY14/problems/DISHOWN/](http://www.codechef.com/JULY14/problems/DISHOWN/)

题意分析：本题主要操作就是给出0 x y时，拥有第x道菜的厨师与拥有第y道菜的厨师pk，谁拥有的所有菜的其中一道菜（不一定是x或y）的分值比较高谁就获胜，并赢得loser的所有菜。即比较的是每个人分值最高的菜，所以对于非loser的人来说，他的分值最高的菜是不变的。综合题意用并查集易解。

```C++
#include <cstdio>

const int Maxn=10004;
int To[Maxn];
int val[Maxn];

int _find(int x){
    if(To[x]!=x)
        To[x]=_find(To[x]);     //路径压缩
    return To[x];
}

void _merge(int x,int y){
    int fx=_find(x);
    int fy=_find(y);
    To[fy]=fx;
}

int main()
{
    int T;
    scanf("%d",&T);
    while(T--){
        int n;
        scanf("%d",&n);
        for(int i=1;i<=n;i++){
            scanf("%d",&val[i]);
            To[i]=i;
        }
        int query;
        scanf("%d",&query);
        while(query--){
            int op;
            scanf("%d",&op);
            if(op==0){
                int x,y;
                scanf("%d%d",&x,&y);
                int fx=_find(x);    //获得x，y的父节点
                int fy=_find(y);
                if(fx==fy)
                    puts("Invalid query!");
                else{
                    if(val[fx]>val[fy]){
                        _merge(x,y);
                    }
                    else if(val[fx]<val[fy]){
                        _merge(y,x);
                    }
                }
            }
            else{
                int x;
                scanf("%d",&x);
                printf("%d\n",_find(x));
            }
        }
    }
    return 0;
}
```

# Garden Game

链接：[http://www.codechef.com/JULY14/problems/SGARDEN](http://www.codechef.com/JULY14/problems/SGARDEN)

题意分析：每响哨一次，处在位置i的人就移动到位置A[i]，其中A[i]是不重复的。易知经过有限次响哨后，必定能够恢复到初始态；其中会出现多个互不相关的循环，求出每个循环的人数，计算其最小公倍数即可。注意结果会超过int的范围。

Python版：

```python
#coding:utf8
def gcd(a, b):  #计算a，b的最大公约数
    if(b == 0):
        return a
    return int(gcd(b, a%b))

def fun(a, b):
    _gcd=gcd(a, b)
    product=a//_gcd*b   #用//运算符保证结果是整数
    return int(product)

T = int(input())
while(T > 0):
    n = int(input())
    num = [0]
    vis = [0]
    x = input()
    for i in x.split():
        num.append(int(i))
        vis.append(0)
    div = []
    st = 1
    #计算每个循环的人数
    while(st <= n):
        if(vis[st] == 0):
            mark=st
            vis[st]=1
            cnt=1
            nx=num[st]
            while(mark != nx):
                vis[nx] = 1
                nx = num[nx]
                cnt += 1
            if(cnt not in div): 
                div.append(cnt)
        st += 1
    ans = 1
    for each in div:
        ans = fun(ans,each)
    print(int(ans%1000000007))
    T -= 1
```

C++版：

由于中间运算结果甚至会超出64位整形的范围，于是我采用了因数分解的方法。

```C++
#include <cstdio>
#include <cstring>
#include <set>
using namespace std;

const int Maxn=100005;
const int MOD=1000000007;
int num[Maxn];
bool vis[Maxn];
int prime[10000],primecount=0;
int totalcount[10000];

void getprime(){
    memset(vis,0,sizeof(vis));
    int i,j;
    for(i=2;i<100000;i++){
        if(!vis[i]){
            prime[primecount++]=i;
            for(j=i+i;j<100000;j+=i){
                vis[j]=1;
            }
        }
    }
}
void getdivsor(int param){
    int i;
    int num=param;
    int cnt;
    for(i=0;prime[i]<=num&&i<primecount;i++){
        if(num%prime[i]==0){
            cnt=0;
            while(num%prime[i]==0){
                cnt++;
                num/=prime[i];
            }
            if(totalcount[i]<cnt)
                totalcount[i]=cnt;
        }
    }
}
int main()
{
    getprime();//计算出10万内的所有质数
    int T;
    scanf("%d",&T);
    while(T--){
        int n;
        scanf("%d",&n);
        for(int i=1;i<=n;i++){
            scanf("%d",&num[i]);
        }
        memset(vis,0,sizeof(vis));
        int st=1,nx,cnt,mark;
        set<int> div;
        while(st<=n){
            if(vis[st]==0){
                mark=st;
                vis[st]=1;
                cnt=1;
                nx=num[st];
                while(mark!=nx){
                    vis[nx]=1;
                    nx=num[nx];
                    ++cnt;
                }
                div.insert(cnt);
            }
            ++st;
        }
        long long ans=1;
        set<int>::iterator it;
        for(it=div.begin();it!=div.end();it++){
            getdivsor(*it);
        }
        for(int i=0;i<primecount;i++){
            long long temp=1;
            while(totalcount[i]>0){
                temp=(temp*prime[i])%MOD;
                totalcount[i]--;
            }
            ans=(ans*temp)%MOD;
        }
        printf("%lld\n",ans);
    }
    return 0;
}
```
