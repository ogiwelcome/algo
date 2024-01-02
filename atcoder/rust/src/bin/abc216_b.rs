use itertools::Itertools;
use proconio::input;

fn main() {
    input! {
        n: usize,
        st: [(String, String); n],
    }
    if st.iter().all_unique() {
        println!("No");
    } else {
        println!("Yes");
    }
}
