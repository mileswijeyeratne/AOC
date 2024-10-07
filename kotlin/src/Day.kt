abstract class Day<T>(val year: Int, val day: Int, filterEmpty: Boolean = true) {
    private val testInputRaw: List<String> = readInput("$year/${day.toString().padStart(2, '0')}_test").filter { if (filterEmpty) it != "" else true}
    private val inputRaw: List<String> = readInput("$year/${day.toString().padStart(2, '0')}").filter { if (filterEmpty) it != "" else true }

    protected abstract fun parse(line: String): T

    protected abstract fun part1(inp: List<T>): Any
    protected abstract fun part2(inp: List<T>): Any

    fun part1(test: Boolean = false): Any {
        val input = if (test) testInputRaw.map { parse(it) } else inputRaw.map { parse(it) }
        return part1(input)
    }

    fun part2(test: Boolean = false): Any {
        val input = if (test) testInputRaw.map { parse(it) } else inputRaw.map { parse(it) }
        return part2(input)
    }
}