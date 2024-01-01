fn part_a(input: &str) -> u32 {
    input.split("\n")
        .map(|line| line.chars().filter(|c| c.is_numeric()).map(|c| c as u32 - '0' as u32).collect::<Vec<_>>())
        .map(|line| line[0]*10 + line[line.len()-1])
        .sum()
}

fn main() {
    let data = include_str!("../input.txt");
    println!("Part a is {:?}", part_a(data));
}