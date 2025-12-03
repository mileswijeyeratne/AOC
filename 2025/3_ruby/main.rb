SAMPLE_INPUT = "987654321111111
811111111111119
234234234234278
818181911112111"

AOCAnswer = Struct.new(:a, :b)

def load_input(test)
    if test
        return SAMPLE_INPUT
    end

    return File.read("../../data/2025/3")
end

def parse_input(input)
    return input.split("\n").map do |line|
        line.chars.map(&:to_i)      
    end
end

def find_max_in_range(array, left, right)
    max = 0
    ind = -1
    (left..right).each do |i|
        if array[i] > max
            max = array[i]
            ind = i
        end
    end
    return ind
end

def greedy(line, n)
    l = line.length()
    res = 0
    place_value = 10 ** n
    prev = -1

    (1..n).each do |i|
        ind = find_max_in_range(line,prev+1, l-n+i-1)
        prev = ind
        place_value /= 10
        res += place_value * line[ind]
    end

    return res
end

def run(input)
    a = 0
    b = 0 

    input.each do |line|
        a += greedy(line, 2)
        b += greedy(line, 12)
    end

    return AOCAnswer.new(a, b)
end

input = parse_input(load_input(false))
res = run(input)
print "Part a:", res.a, "\n"
print "Part b:", res.b, "\n"