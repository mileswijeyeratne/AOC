package y2015

import Day

class Day06 : Day<Day06.Command>(2015, 6) {

    data class Command(val cmd: String, val a: Int, val b: Int, val x: Int, val y: Int)

    override fun parse(line: String): Command {
        val (cmd, a, b, x, y) = "(\\D+) (\\d+),(\\d+) through (\\d+),(\\d+)".toRegex().find(line)!!.destructured
        return Command(cmd, a.toInt(), b.toInt(), x.toInt(), y.toInt())
    }

    override fun part1(inp: List<Command>): Any {
        val lights = BooleanArray(1000 * 1000)
        inp.forEach {
            for (i in it.a..it.x) {
                for (j in it.b..it.y) {
                    val ind = i * 1000 + j
                    when (it.cmd) {
                        "turn on" -> lights[ind] = true
                        "turn off" -> lights[ind] = false
                        "toggle" -> lights[ind] = !lights[ind]
                    }
                }
            }
        }
        return lights.count { it }
    }

    override fun part2(inp: List<Command>): Any {
        val lights = IntArray(1000 * 1000)
        inp.forEach {
            for (i in it.a..it.x) {
                for (j in it.b..it.y) {
                    val ind = i * 1000 + j
                    when (it.cmd) {
                        "turn on" -> lights[ind]++
                        "turn off" -> {
                            if (lights[ind] > 0) {
                                lights[ind]--
                            }
                        }

                        "toggle" -> lights[ind] += 2
                    }
                }
            }
        }
        return lights.sum()
    }

}

