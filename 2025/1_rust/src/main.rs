use std::fs;

const TEST_INPUT: &str = "L68
L30
R48
L5
R60
L55
L1
L99
R14
L82";

fn load_input(test: bool) -> String {
    match test {
        true => TEST_INPUT.to_string(),
        false => fs::read_to_string("../../data/2025/1").unwrap(),
    }
}

fn parse_input(input: String) -> Vec<i32> {
    input
        .lines()
        .map(|rot| {
            let dir = &rot[0..1];
            let val = &rot[1..].parse::<i32>().unwrap();

            match dir {
                "R" => *val,
                "L" => -val,
                _ => unreachable!(),
            }
        })
        .collect()
}

fn run(input: Vec<i32>) -> (i32, i32) {
    let mut pos = 50;
    let mut a = 0;
    let mut b = 0;

    for rot in input {
        // defo a better way to do part b
        // ts solution sm worse than O(n)
        let steps = rot.abs();
        let step = if rot < 0 { -1 } else { 1 };

        for _ in 0..steps {
            pos += step;
            pos %= 100;
            if pos == 0 {
                b += 1
            }
        }

        if pos == 0 {
            a += 1;
        }
    }

    (a, b)
}

fn main() {
    let input = parse_input(load_input(false));

    let (a, b) = run(input);

    println!("Part a: {}", a);
    println!("Part b: {}", b);
}
