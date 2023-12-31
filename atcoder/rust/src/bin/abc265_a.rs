use proconio::input;
use std::cmp::min;

fn main() {
    input! {
        x: i32,
        y: i32,
        n: i32,
    }
    let yy = min(x * 3, y);
    let ans = yy * (n / 3) + x * (n - (n / 3) * 3);
    println!("{}", ans);
}
