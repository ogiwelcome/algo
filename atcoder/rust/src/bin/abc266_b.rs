use proconio::input;

fn main() {
    input! {
        n: i128,
    }
    let ans = n % 998244353;
    if ans >= 0 {
        println!("{}", ans);
    } else {
        println!("{}", ans + 998244353);
    }
}
