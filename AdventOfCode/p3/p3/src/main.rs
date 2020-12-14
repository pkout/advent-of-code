use regex::Regex;
use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

struct Patch {
    id: usize,
    x: usize,
    y: usize,
    w: usize,
    h: usize,
}

fn main() {
    let file_content = load_file();
    let file_lines = str_to_lines(&file_content);
    let patches = file_lines_to_patches(file_lines);
    let mut matrix = build_matrix();
    apply_patches_to_matrix(&patches, &mut matrix);
    let overlapping_area = find_overlapping_area(&matrix);
    let non_overlapping_patch = find_non_overlapping_patch(&patches, &matrix).unwrap();

    println!("Patches overlapping area: {}", overlapping_area);
    println!("Nonoverlapping patch ID: {}", non_overlapping_patch.id)
}

fn load_file() -> String {
    let path = Path::new("../input.txt");
    let display = path.display();

    let mut file = match File::open(&path) {
        Err(why) => panic!("Couldn't open {}: {}", display, why),
        Ok(file) => file,
    };

    let mut s = String::new();
    match file.read_to_string(&mut s) {
        Err(why) => panic!("Couldn't read {}: {}", display, why),
        Ok(_) => return s.trim().to_string(),
    };
}

fn str_to_lines(s: &str) -> Vec<&str> {
    s.split("\n").collect()
}

fn file_lines_to_patches(lines: Vec<&str>) -> Vec<Patch> {
    let mut patches: Vec<Patch> = Vec::new();
    let re = Regex::new(r"^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$").unwrap();

    for line in lines {
        let cap = re.captures(line).unwrap();
        let patch = Patch {
            id: (&cap[1]).parse::<usize>().unwrap(),
            x: (&cap[2]).parse::<usize>().unwrap(),
            y: (&cap[3]).parse::<usize>().unwrap(),
            w: (&cap[4]).parse::<usize>().unwrap(),
            h: (&cap[5]).parse::<usize>().unwrap(),
        };
        patches.push(patch);
    }

    return patches;
}

fn build_matrix() -> Vec<Vec<usize>> {
    const MATRIX_SIZE: usize = 1500;
    let mut matrix = Vec::new();
    for _ in 0..MATRIX_SIZE {
        matrix.push(vec![0; MATRIX_SIZE]);
    }

    return matrix;
}

fn apply_patches_to_matrix(patches: &Vec<Patch>, matrix: &mut Vec<Vec<usize>>) {
    for patch in patches {
        for row_i in patch.y..patch.y + patch.h {
            for col_i in patch.x..patch.x + patch.w {
                matrix[row_i][col_i] += 1;
            }
        }
    }
}

fn find_overlapping_area(matrix: &Vec<Vec<usize>>) -> usize {
    let mut overlapping_area = 0;

    for row_i in 0..matrix.len() {
        for col_i in 0..matrix[0].len() {
            match matrix[row_i][col_i] > 1 {
                true => overlapping_area += 1,
                false => (),
            }
        }
    }

    return overlapping_area;
}

fn find_non_overlapping_patch<'a>(patches: &'a Vec<Patch>, matrix: &'a Vec<Vec<usize>>) -> Option<&'a Patch> {
    for patch in patches {
        let mut overlaps = false;
        for row_i in patch.y..patch.y + patch.h {
            for col_i in patch.x..patch.x + patch.w {
                if matrix[row_i][col_i] > 1 {
                    overlaps = true;
                    break;
                }
            }
            if overlaps == true {
                break;
            }
        }
        if overlaps == false {
            return Some(patch);
        }
    }

    None
}