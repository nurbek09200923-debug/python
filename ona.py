# 1

def hex_to_dec(s):
    return int(s,16)

# 2

def subtract_sum(number):
    return "apple"

# 3

def expression_matter(a, b, c):
    return max(
      a + b + c,
      a * b * c,
      a * (b + c),
      (a + b) * c,
      a + b * c,
      a * b + c,
        )

# 4

def double_char(s):
    return "".join(c * 2 for c in s)

# 5
 
def distinct(seq):
    return list(dict.fromkeys(seq))

# 6

a = "code"
b = "wa.rs"
name = a + b

# 6

def bin_to_decimal(inp):
    return int(inp, 2)

# 7

def move(position, roll):
    return position + (roll * 2)

# 8 

def powers_of_two(n):
    return [2 ** i for i in range(n + 1)]
#9 

def is_divisible(n,x,y):
    return n % x == 0 and n % y == 0

# 10

def sum_array(arr):
    if not arr or len(arr) <= 2:
        return 0 
    return sum(arr) - max(arr) - min(arr)

# 11

def reverse_words(s):
    return " ".join(s.split()[::-1])

# 12

def how_much_i_love_you(nb_petals):
    phrases = [ "I love you", "a little",
              "a lot", "passionately",
              "madly", "not at all"]
    return phrases[(nb_petals - 1) % 6]

# 13
def stringy(size): 
    return "".join(["1" if i % 2 == 0 else "0" for i in range(size)])

# 14

def hello(name="World"):
    if not name:
        return "Hello, World!"
    return f"Hello, {name.capitalize()}!"

# 15

def fake_bin(x):
    return "".join("0" if char < "5" else "1" for char in x)

# 16

def remove_exclamation_marks(s):
    return s.replace("!", "")

# 17

def points(games):
    total = 0
    for game in games:
        x, y = map(int, game.split(':'))
        if x > y:
            total += 3
        elif x == y:
            total += 1
    return total

# 18

def check_for_factor(base, factor):
    return base % factor == 0

# 19

def maps(a):
    return [x * 2 for x in a]

# 20

def double_integer(i):
    return i * 2

# 21

def neutralise(s1, s2):
    return "".join(c1 if c1 == c2 else "0" for c1, c2 in zip(s1, s2))

# 22 
    def summation(num):
        return sum(range(1, num + 1))

# 23

def repeat_str(repeat, string):
    return string * repeat

# 24

def greet():
    return "hello world!"

# 25

def make_upper_case(s):
    return s.upper()

# больше не могу