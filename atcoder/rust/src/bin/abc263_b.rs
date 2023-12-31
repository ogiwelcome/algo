use proconio::input;

fn main() {
    input! {
        n: usize,
        p: [usize; n-1],
    }
    let mut ans = 1;
    let mut k = n - 1;
    loop {
        if p[k - 1] == 1 {
            println!("{}", ans);
            return;
        }
        k = p[k - 1] - 1;
        ans += 1;
    }
}
