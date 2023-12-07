fn calc(times: &Vec<u32>, dists: &Vec<u32>) -> u32 {
    let mut res = 1;

    for i in 0..times.len() {
        let t = times[i];
        let d = dists[i];

        let mut count = 0;

        for charge_time in 0..t {
            if d < charge_time * (t - charge_time) {
                count += 1;
            }
        }
        res *= count;

    }

    res
}

fn part_a(data: &str) -> u32 {
    let data = data.split("\r\n")
        .map(|line| line.split(":").collect::<Vec<_>>()[1])
        .map(|line| line.split(" ").map(|c| c.parse::<u32>().unwrap()).collect::<Vec<u32>>())
        .collect::<Vec<Vec<u32>>>();
    let times = &data[0];
    let dists = &data[1];

    calc(times, dists)
}

fn part_b(data: &str) -> u32 {
    println!("{:?}", data.trim());
    let data = data.split("\r\n")
        .map(|line| line.chars().filter(|c| !c.is_whitespace()).collect::<String>())
        .map(|line| (&line).split(":").collect::<Vec<_>>()[1])
        .map(|line|line.parse::<u32>().unwrap())
        .collect::<Vec<u32>>();
    let times = vec![data[0].clone()];
    let dists = vec![data[0].clone()];

    calc(&times, &dists)
}

fn main() {
    let data = include_str!("../input.txt");
    println!("Part a is {:?}", part_a(data));
    println!("Part b is {:?}", part_b(data));
}