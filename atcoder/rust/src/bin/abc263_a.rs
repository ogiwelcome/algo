use proconio::input;

fn main() {
    input! {
        a: [usize; 5]
    }
    let mut cnt = vec![0; 15];
    for &a in a.iter() {
        cnt[a] += 1;
    }
    if cnt.contains(&2) && cnt.contains(&3) {
        println!("Yes");
    } else {
        println!("No")
    }
}
