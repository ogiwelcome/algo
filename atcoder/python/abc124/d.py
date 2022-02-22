n,k=map(int,input().split())
s=list(input())
for i in range(n):
    s[i]=int(s[i])
# 111111 {00000} 1111111
# ここがまとめて一回の操作で置換される

# 1 0 1 00 1 0 1 0 1
# 0の連続する個数4に対して、1と0の入れ替わりの回数が8回

# 似たようなことが一般化できて
# (1連続)(0連続)(1連続)(0連続)(1連続)とする...
# この時k回の操作で2*k+1の長さまで取れることになる

# 端の挙動に注意(両端が0の場合少し困る)
# 尺取りでもいい
ans=0
arr=[]
# (0連続)が最初(最後)に来ると困るから(場合分けが面倒なので)最初と最後には0を詰めておく(imos法とかでも使うテク)
if s[0]==0:
    arr.append(0)
pre=s[0]
cnt=0
# 連続する数を管理しておく
for i in range(n):
    if pre==s[i]:
        cnt+=1
    else:
        arr.append(cnt)
        pre=s[i]
        cnt=1
# 末尾の処理もちゃんとやること
if cnt:
    arr.append(cnt)
# ここの0のことを「番人」とかって言ったりする
# 本当はいらないが端での処理で場合分けをしないようにするため
if s[-1]==0:
    arr.append(0)
# debugしたりして挙動通りか見る
# print(arr)
ans=sum(arr[:2*k+1])
sc=ans
idx=2*k+1
while idx<len(arr):
    sc+=arr[idx]+arr[idx+1]-arr[idx-(2*k+1)]-arr[idx-(2*k)]
    ans=max(ans,sc)
    idx+=2
print(ans)