use proconio::input;

fn main() {
    input! {
        s: usize,
        t: usize,
    }
    let mut cnt = 0;
    for a in 0..s + 1 {
        for b in 0..s + 1 {
            for c in 0..s + 1 {
                if a + b + c <= s && a * b * c <= t {
                    cnt += 1;
                }
            }
        }
    }
    println!("{}", cnt);
}
