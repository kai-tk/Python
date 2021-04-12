#include <stdio.h>
#define MAX 10001
#define mod 1000000007

long fac[MAX], finv[MAX], inv[MAX];
long P[MAX][MAX];

void initCOM(){
    fac[0]=fac[1]=1;
    finv[0]=finv[1]=1;
    inv[1]=1;
    for(int i=2;i<MAX;i++){
        fac[i]=fac[i-1]*i%mod;
        inv[i]=mod-inv[mod%i]*(mod/i)%mod;
        finv[i]=finv[i-1]*inv[i]%mod;
    }
}

long nCk(int n,int k){
    if(n<k || n<0 || k<0) return 0;
    return fac[n]*(finv[k]*finv[n-k]%mod)%mod;
}

long nPk(int n,int k){
    long ans=1;
    while(k-->0){
        ans=ans*n%mod;
        n--;
    }
    return ans;
}

//k種類のものから重複を許してn個
//n個の区別できない玉をk個の区別できる箱に分ける
long nHk(int n,int k){
    return nCk(k+n-1,k);
}

//n!
long fact(int n){
    long ans=1;
    while(n>1){
        ans=ans*n%mod;
        n--;
    }
    return ans;
}

//x^n
long m_pow(int x,int n){
    long ans=1;
    long y=x;
    while(n>0){
        if(n&1){
            ans=ans*y%mod;
        }
        y=y*y%mod;
        n>>=1;
    }
    return ans;
}

//n個の区別できる玉をk個の区別できない箱に空箱なく分ける
long Stirling2(int n,int k){
    long ans=0;
    int flag=k%2;
    for(int i=0;i<=k;i++){
        if(flag==0){
            ans=(ans+nCk(k,i)*m_pow(i,n)%mod)%mod;
            flag=1;
        }else{
            ans=(ans+(mod-nCk(k,i)*m_pow(i,n)%mod))%mod;
            flag=0;
        }
    }
    ans=ans*finv[k]%mod;
    return ans;
}

//n個の区別できる玉をk個の区別できない箱に分ける
long Bell(int n,int k){
    long ans=0;
    for(int i=0;i<=k;i++){
        ans=(ans+Stirling2(n,i))%mod;
    }
    return ans;
}

long partition(int n,int k){
    if(n==0 || k==1) return 1;
    if(n<0 || k<1) return 0;
    if(P[n][k]!=0) return P[n][k];
    else return P[n][k]=(partition(n,k-1)+partition(n-k,k))%mod;
}

int main(void){
    int n,k;

    scanf("%d %d",&n,&k);
    P[0][0]=1;

    initCOM();
    printf("%ld\n",partition(n-k,k));

    return 0;
}
