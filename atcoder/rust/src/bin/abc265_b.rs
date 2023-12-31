use proconio::input;

fn main() {
    input! {
        n: usize,
        m: usize,
        mut t: isize,
        mut a: [isize; n-1],
        xy: [(usize, usize); m],
    }

    for i in 0..m {
        a[xy[i].0 - 1] -= xy[i].1 as isize;
    }
    for i in 0..(n - 1) {
        if t - a[i] > 0 {
            t -= a[i];
        } else {
            println!("No");
            return;
        }
    }
    println!("Yes");
}
