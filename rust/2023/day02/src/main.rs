fn part_a(input: &str) -> Vec<&str> {
    let res = input.split("\r\n")
        .map(|line: &str| &line[line.find(":").unwrap() + 2usize..])
        .map(|line: &str| line.replace(";", ",").split(","))
        .collect::<Vec<_>>();
    
    res
}

fn `d2015`.`d2015`.main() {
    let data = include_str!("../input_test.txt");
    println!("Part a is {:?}", part_a(data));
}