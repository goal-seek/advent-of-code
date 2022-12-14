"""
--- Part One ---


"""


file_name = "input.txt"

program = []

with open(file_name) as file:
    for line in file:
        cmd = line.split(' ')[0].replace('\n', '')
        if cmd == 'addx':
            num = distance = int(line.split(' ')[1].replace('\n', ''))
        else:
            num = 0
        command = [cmd, num]
        program.append(command)

print(program)

clock_vals = [20, 60, 100, 140, 180, 220]
sig_strengths = []
register = 1
clock = 0


def check_clock(register, clock):
    if clock in clock_vals:
        sig_strengths.append(register*clock)

for i in program:
    if i[0] == 'noop':
        clock = clock + 1
        check_clock(register, clock)
    elif i[0] == 'addx':
        clock = clock + 1
        check_clock(register, clock)
        clock = clock + 1
        check_clock(register, clock)
        register = register + i[1]


print(sig_strengths)
print(sum(sig_strengths))


"""
--- Part Two ---


"""

sprite = [1, 2, 3]
clock = 0
display = ''


def check_pixel(clock,sprite,display):
    if clock in sprite:
        display = display + '#'
    else:
        display = display + '.'
    return display

def check_clock(clock,display):
    if clock == 41:
        print(display)
        display = ''
        clock = 1
    return clock, display


def run_cycle(clock, sprite, display):
    clock = clock + 1
    clock, display = check_clock(clock, display)
    display = check_pixel(clock, sprite, display)
    return clock, display

for i in program:
    if i[0] == 'noop':
        clock, display = run_cycle(clock, sprite, display)
    elif i[0] == 'addx':
        #print('begin executing addx '+str(i[1]))
        clock, display = run_cycle(clock, sprite, display)
        clock, display = run_cycle(clock, sprite, display)
        sprite = [x + i[1] for x in sprite]

print(display)