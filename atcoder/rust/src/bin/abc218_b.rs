use proconio::input;

fn main() {
    input! {
        p: [usize; 26],
    }
    let alphabet = "abcdefghijklmnopqrstuvwxyz";
    let arr: Vec<char> = alphabet.chars().collect();
    let mut ans = String::from("");
    for i in 0..26 {
        ans.push_str(&arr[p[i] - 1].to_string());
    }
    println!("{}", ans);
}
