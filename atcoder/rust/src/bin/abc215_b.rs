use proconio::input;

fn main() {
    input! {
        n: u128
    }
    let mut k = 1;
    loop {
        if 2_u128.pow(k) > n {
            println!("{}", k - 1);
            break;
        } else {
            k += 1;
        }
    }
}
