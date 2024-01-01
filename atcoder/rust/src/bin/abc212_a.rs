use proconio::input;

fn main() {
    input! {
        a: i32,
        b: i32,
    }
    if a == 0 {
        println!("Silver");
    } else if b == 0 {
        println!("Gold");
    } else {
        println!("Alloy");
    }
}
