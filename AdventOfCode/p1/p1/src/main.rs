use std::fs::File;
use std::io::prelude::*;
use std::collections::HashSet;

fn main() {
    let file_content = load_file();
    let freqs = find_frequencies(&file_content);
    let total_freq = sum_frequencies(&freqs);
    let repeating_freq = find_repeating_freq(&freqs);
    println!("{}", total_freq);
    println!("{}", repeating_freq);
}

fn load_file() -> String {
    let mut file = File::open("../input.txt").unwrap();
    let mut s = String::new();
    file.read_to_string(&mut s).unwrap();

    return s.trim().to_string();
}

fn find_frequencies(s: &str) -> Vec<isize> {
    let freqs:Vec<&str> = s.split("\n").collect();
    let freqs_usize = freqs.iter().map(|x| x.parse::<isize>().unwrap()).collect();
    return freqs_usize;
}

fn find_repeating_freq(freqs: &Vec<isize>) -> isize {
    let mut existing_freqs: HashSet<isize> = vec![0].into_iter().collect();
    let mut total = 0;

    loop {
        for freq in freqs {
            total += freq;
            match existing_freqs.insert(total) {
                false => return total,
                true => ()
            }
        }
    }
}

fn sum_frequencies(freqs: &Vec<isize>) -> isize {
    let mut total = 0;

    for freq in freqs {
        total += freq;
    }

    return total;
}