use proconio::input;

fn main() {
    input! {
        n: usize,
        a: [usize; n],
    }
    let mut copied = a.clone();
    copied.sort();
    let num = copied[copied.len() - 2];
    println!("{}", a.iter().position(|i| { *i == num }).unwrap() + 1)
}
