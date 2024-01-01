use proconio::input;

fn main() {
    input! {
        a: u32,
    }
    if a % 1111 == 0 || (a - 123) % 1111 == 0 || a == 9012 || a == 8901 || a == 7890 {
        println!("Weak");
    } else {
        println!("Strong");
    }
}
