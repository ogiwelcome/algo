use proconio::input;

fn main() {
    input! {
        s: [String; 3],
    }
    let candi = ["ABC", "ARC", "AGC", "AHC"];
    let ans = candi.iter().find(|x| !s.contains(&x.to_string())).unwrap();
    println!("{}", ans)
}
