use proconio::input;

fn main() {
    input! {
        s: f32,
    }
    let y = (s * 10.0) as usize % 10;
    let x = s as usize;
    if y <= 2 {
        println!("{}-", x);
    } else if y <= 6 {
        println!("{}", x);
    } else {
        println!("{}+", x);
    }
}
