import y2015.Day07

fun <T> run(day: Day<T>) {
    println("${day.year} Day ${day.day}")
    println("[Part 1] Test answer: ${day.part1(true)}")
    println("[Part 1] Answer: ${day.part1()}")
    println("[Part 2] Test answer: ${day.part2(true)}")
    println("[Part 2] Answer: ${day.part2()}")
}

fun main() {
    val day06 = Day07()
    run(day06)
}