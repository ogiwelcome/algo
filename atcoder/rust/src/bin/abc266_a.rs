use proconio::input;

fn main() {
    input! {
        s: String,
    }
    let count = s.chars().count() / 2;
    println!("{}", s.chars().nth(count).unwrap());
}
