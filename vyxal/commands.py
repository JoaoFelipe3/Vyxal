codepage = "λƛ¬∧⟑∨⟇÷×«\n»°•ß†€"
codepage += "½∆ø↔¢⌐æʀʁɾɽÞƈ∞¨ "
codepage += "!\"#$%&'()*+,-./01"
codepage += "23456789:;<=>?@A"
codepage += "BCDEFGHIJKLMNOPQ"
codepage += "RSTUVWXYZ[\\]`^_abc"
codepage += "defghijklmnopqrs"
codepage += "tuvwxyz{|}~↑↓∴∵›"
codepage += "‹∷¤ð→←βτȧḃċḋėḟġḣ"
codepage += "ḭŀṁṅȯṗṙṡṫẇẋẏż√⟨⟩"
codepage += "‛₀₁₂₃₄₅₆₇₈¶⁋§ε¡"
codepage += "∑¦≈µȦḂĊḊĖḞĠḢİĿṀṄ"
codepage += "ȮṖṘṠṪẆẊẎŻ₌₍⁰¹²∇⌈"
codepage += "⌊¯±₴…□↳↲⋏⋎꘍ꜝ℅≤≥"
codepage += "≠⁼ƒɖ∪∩⊍£¥⇧⇩ǍǎǏǐǑ"
codepage += "ǒǓǔ⁽‡≬⁺↵⅛¼¾Π„‟"

assert len(codepage) == 256

command_dict = {
    "¬": ("stack.append(int(not pop(stack)))", 1),
    "∧": ("rhs, lhs = pop(stack, 2); stack.append(lhs and rhs)", 2),
    "⟑": ("rhs, lhs = pop(stack, 2); stack.append(rhs and lhs)", 2),
    "∨": ("rhs, lhs = pop(stack, 2); stack.append(lhs or rhs)", 2),
    "⟇": ("rhs, lhs = pop(stack, 2); stack.append(rhs or lhs)", 2),
    "÷": ("for item in iterable(pop(stack)): stack.append(item)", 1),
    "•": ("rhs, lhs = pop(stack, 2); stack.append(log(lhs, rhs))", 2),
    "†": ("fn = pop(stack); stack += function_call(fn, stack)", 1),
    "€": ("rhs, lhs = pop(stack, 2); stack.append(split(lhs, rhs))", 2),
    "½": ("stack.append(halve(pop(stack)))", 1),
    "↔": (
        "rhs, lhs = pop(stack, 2); stack.append(combinations_replace_generate(lhs, rhs))",
        2,
    ),
    "⌐": ("stack.append(complement(pop(stack)))", 1),
    "æ": ("stack.append(is_prime(pop(stack)))", 1),
    "ʀ": ("stack.append(orderless_range(0, add(pop(stack), 1)))", 1),
    "ʁ": ("stack.append(orderless_range(0, pop(stack)))", 1),
    "ɾ": ("stack.append(orderless_range(1, add(pop(stack), 1)))", 1),
    "ɽ": ("stack.append(orderless_range(1, pop(stack)))", 1),
    "ƈ": ("rhs, lhs = pop(stack, 2); stack.append(ncr(lhs, rhs))", 2),
    "∞": ("stack.append(Generator(lambda x: x))", 0),
    "!": ("stack.append(len(stack))", 0),
    '"': ("rhs, lhs = pop(stack, 2); stack.append([lhs, rhs])", 2),
    "$": ("top, over = pop(stack, 2); stack.append(top); stack.append(over)", 2),
    "%": ("rhs, lhs = pop(stack, 2); stack.append(modulo(lhs, rhs))", 2),
    "*": ("rhs, lhs = pop(stack, 2); stack.append(multiply(lhs, rhs))", 2),
    "+": ("rhs, lhs = pop(stack, 2); stack.append(add(lhs, rhs))", 2),
    ",": ("VY_print(pop(stack))", 1),
    "-": ("rhs, lhs = pop(stack, 2); stack.append(subtract(lhs, rhs))", 2),
    "/": ("rhs, lhs = pop(stack, 2); stack.append(divide(lhs, rhs))", 2),
    ":": ("temp = pop(stack); stack.append(temp); stack.append(deref(temp))", 1),
    "^": ("stack = stack[::-1]", 0),
    "_": ("pop(stack)", 1),
    "<": (
        "rhs, lhs = pop(stack, 2); stack.append(compare(lhs, rhs, Comparitors.LESS_THAN))",
        2,
    ),
    ">": (
        "rhs, lhs = pop(stack, 2); stack.append(compare(lhs, rhs, Comparitors.GREATER_THAN))",
        2,
    ),
    "=": (
        "rhs, lhs = pop(stack, 2); stack.append(compare(lhs, rhs, Comparitors.EQUALS))",
        2,
    ),
    "?": ("stack.append(get_input(0))", 0),
    "A": ("stack.append(int(all(iterable(pop(stack)))))", 1),
    "B": ("stack.append(VY_int(pop(stack), 2))", 1),
    "C": ("stack.append(chrord(pop(stack)))", 1),
    "D": (
        "temp = pop(stack); stack.append(temp); stack.append(deref(temp)); stack.append(deref(stack[-1]))",
        1,
    ),
    "E": ("stack.append(VY_eval(pop(stack)))", 1),
    "F": ("fn, vector = pop(stack, 2); stack.append(VY_filter(fn, vector))", 2),
    "G": ("stack.append(VY_max(iterable(pop(stack))))", 1),
    "H": ("stack.append(VY_int(pop(stack), 16))", 1),
    "I": ("stack.append(VY_int(pop(stack)))", 1),
    "J": ("rhs, lhs = pop(stack, 2); stack.append(join(lhs, rhs))", 2),
    "K": ("stack.append(divisors_of(pop(stack)))", 1),
    "L": ("top = pop(stack); stack.append(len(iterable(top)))", 1),
    "M": ("fn, vector = pop(stack, 2); stack.append(VY_map(fn, vector))", 2),
    "N": ("stack.append(negate(pop(stack)))", 1),
    "O": (
        "needle, haystack = pop(stack, 2); stack.append(iterable(haystack).count(needle))",
        2,
    ),
    "P": ("rhs, lhs = pop(stack, 2); stack.append(VY_str(lhs).strip(VY_str(rhs)))", 2),
    "Q": ("exit()", 0),
    "R": ("fn, vector = pop(stack, 2); stack += VY_reduce(fn, vector)", 2),
    "S": ("stack.append(VY_str(pop(stack)))", 1),
    "T": ("stack.append([i for (i, x) in enumerate(pop(stack)) if bool(x)])", 1),
    "U": ("stack.append(Generator(uniquify(pop(stack))))", 1),
    "V": (
        "replacement, needle, haystack = pop(stack, 3); stack.append(replace(haystack, needle, replacement))",
        3,
    ),
    "W": ("stack = [deref(stack)]", 0),
    "X": ("context_level += 1", 0),
    "Y": ("rhs, lhs = pop(stack, 2); stack.append(interleave(lhs, rhs))", 2),
    "Z": (
        "rhs, lhs = pop(stack, 2); stack.append(Generator(VY_zip(iterable(lhs), iterable(rhs))))",
        2,
    ),
    "a": ("stack.append(int(any(iterable(pop(stack)))))", 1),
    "b": ("stack.append(VY_bin(pop(stack)))", 1),
    "c": (
        "needle, haystack = pop(stack, 2); haystack = iterable(haystack, str)\nif type(haystack) is str: needle = VY_str(needle)\nstack.append(int(needle in iterable(haystack, str)))",
        2,
    ),
    "d": ("stack.append(multiply(pop(stack), 2))", 1),
    "e": ("rhs, lhs = pop(stack, 2); stack.append(exponate(lhs, rhs))", 2),
    "f": ("stack.append(flatten(iterable(pop(stack))))", 1),
    "g": ("stack.append(VY_min(iterable(pop(stack))))", 1),
    "h": ("stack.append(iterable(pop(stack))[0])", 1),
    "i": ("rhs, lhs = pop(stack, 2)\nstack.append(index(lhs, rhs))", 2),
    "j": ("rhs, lhs = pop(stack, 2); stack.append(join_on(lhs, rhs))", 2),
    "l": ("rhs, lhs = pop(stack, 2); stack.append(nwise_pair(lhs, rhs))", 2),
    "m": ("item = pop(stack); stack.append(mirror(item))", 1),
    "n": ("stack.append(context_values[context_level % len(context_values)])", 0),
    "o": (
        "needle, haystack = pop(stack, 2); stack.append(remove(haystack, needle))",
        2,
    ),
    "p": ("rhs, lhs = pop(stack, 2); stack.append(prepend(lhs, rhs))", 2),
    "q": ("stack.append(uneval(VY_str(pop(stack))))", 1),
    "r": ("rhs, lhs = pop(stack, 2); stack.append(orderless_range(lhs, rhs))", 2),
    "s": ("stack.append(VY_sorted(pop(stack)))", 1),
    "t": ("stack.append(iterable(pop(stack))[-1])", 1),
    "u": ("stack.append(-1)", 0),
    "w": ("stack.append([pop(stack)])", 1),
    "x": ("stack += this_function(stack)", 0),
    "y": ("stack += uninterleave(pop(stack))", 1),
    "z": ("fn, vector = pop(stack, 2); stack += VY_zipmap(fn, vector)", 2),
    "↑": ("stack.append(max(pop(stack), key=lambda x: x[-1]))", 1),
    "↓": ("stack.append(min(pop(stack), key=lambda x: x[-1]))", 1),
    "∴": ("rhs, lhs = pop(stack, 2); stack.append(VY_max(lhs, rhs))", 2),
    "∵": ("rhs, lhs = pop(stack, 2); stack.append(VY_min(lhs, rhs))", 2),
    "β": (
        "alphabet, number = pop(stack, 2); stack.append(utilities.to_ten(number, alphabet))",
        2,
    ),
    "τ": (
        "alphabet, number = pop(stack, 2); stack.append(utilities.from_ten(number, alphabet))",
        2,
    ),
    "›": ("stack.append(add(pop(stack), 1))", 1),
    "‹": ("stack.append(subtract(pop(stack), 1))", 1),
    "∷": ("stack.append(modulo(pop(stack), 2))", 1),
    "¤": ("stack.append('')", 0),
    "ð": ("stack.append(' ')", 0),
    "ȧ": ("stack.append(VY_abs(pop(stack)))", 1),
    "ḃ": ("stack.append(int(not compare(pop(stack), 0, Comparitors.EQUALS)))", 1),
    "ċ": ("stack.append(compare(pop(stack), 1, Comparitors.NOT_EQUALS))", 1),
    "ḋ": (
        "rhs, lhs = pop(stack, 2); stack.append(VY_divmod(lhs, rhs))",
        2,
    ),  # Dereference because generators could accidentally get exhausted.
    "ė": ("stack.append(Generator(enumerate(iterable(pop(stack)))))", 1),
    "ḟ": ("rhs, lhs = pop(stack, 2); stack.append(find(lhs, rhs))", 2),
    "ġ": (
        "rhs = pop(stack)\nif VY_type(rhs) in [list, Generator]: stack.append(gcd(rhs))\nelse: stack.append(gcd(pop(stack), rhs))",
        2,
    ),
    "ḣ": ("top = iterable(pop(stack)); stack.append(top[0]); stack.append(top[1:])", 1),
    "ḭ": ("rhs, lhs = pop(stack, 2); stack.append(integer_divide(lhs, rhs))", 2),
    "ŀ": (
        "start, needle, haystack = pop(stack, 3); stack.append(find(haystack, needle, start))",
        3,
    ),
    "ṁ": (
        "top = iterable(pop(stack)); stack.append(divide(summate(top), len(top)))",
        1,
    ),
    "ṅ": ("stack.append(first_n(pop(stack)))", 1),
    "ȯ": ("n, fn = pop(stack, 2); stack.append(first_n(fn, n))", 2),
    "ṗ": ("stack.append(powerset(iterable(pop(stack))))", 1),
    "ṙ": ("stack.append(VY_round(pop(stack)))", 1),
    "ṡ": ("fn , vector = pop(stack, 2); stack.append(VY_sorted(vector, fn))", 2),
    "ṫ": (
        "vector = iterable(pop(stack)); stack.append(vector[:-1]); stack.append(vector[-1])",
        1,
    ),
    "ẇ": ("rhs, lhs = pop(stack, 2); stack.append(wrap(lhs, rhs))", 2),
    "ẋ": (
        "rhs, lhs = pop(stack, 2); main = None;\nif VY_type(lhs) is Function: main = pop(stack)\nstack.append(repeat(lhs, rhs, main))",
        2,
    ),
    "ẏ": ("obj = iterable(pop(stack)); stack.append(Generator(range(0, len(obj))))", 1),
    "ż": (
        "obj = iterable(pop(stack)); stack.append(Generator(range(1, len(obj) + 1)))",
        1,
    ),
    "√": ("stack.append(exponate(pop(stack), 0.5))", 1),
    "₀": ("stack.append(10)", 0),
    "₁": ("stack.append(100)", 0),
    "₂": (
        "stack.append(const_divisibility(pop(stack), 2, lambda item: len(item) % 2 == 0))",
        1,
    ),
    "₃": (
        "stack.append(const_divisibility(pop(stack), 3, lambda item: len(item) == 1))",
        1,
    ),
    "₄": ("stack.append(26)", 0),
    "₅": (
        "top = pop(stack); res = const_divisibility(top, 5, lambda item: (top, len(item)))\nif type(res) is tuple: stack += list(res)\nelse: stack.append(res)",
        1,
    ),
    "₆": ("stack.append(64)", 0),
    "₇": ("stack.append(128)", 0),
    "₈": ("stack.append(256)", 0),
    "¶": ("stack.append('\\n')", 0),
    "⁋": ("stack.append(osabie_newline_join(pop(stack)))", 1),
    "§": ("stack.append(vertical_join(pop(stack)))", 1),
    "ε": (
        "padding, vector = pop(stack, 2); stack.append(vertical_join(vector, padding))",
        2,
    ),
    "¡": ("stack.append(factorial(pop(stack)))", 1),
    "∑": ("stack.append(summate(pop(stack)))", 1),
    "¦": ("stack.append(cumulative_sum(iterable(pop(stack))))", 1),
    "≈": ("stack.append(int(len(set(iterable(pop(stack)))) == 1))", 1),
    "Ȧ": (
        "value, lst_index, vector = pop(stack, 3); stack.append(assigned(iterable(vector), lst_index, value))",
        3,
    ),
    "Ḃ": ("stack += bifurcate(pop(stack))", 1),
    "Ċ": ("stack.append(counts(pop(stack)))", 1),
    "Ḋ": (
        "rhs, lhs = pop(stack, 2); ret = is_divisble(lhs, rhs)\nif type(ret) is tuple: stack += list(ret)\nelse: stack.append(ret)",
        2,
    ),
    "Ė": ("stack += VY_exec(pop(stack))", 1),
    "Ḟ": (
        """top = pop(stack)
if VY_type(top) is Number:
    limit = int(top); vector = pop(stack)
else:
    limit = -1; vector = top
fn = pop(stack)
stack.append(Generator(fn, limit=limit, initial=iterable(vector)))
""",
        2,
    ),
    "Ġ": ("stack.append(group_consecutive(iterable(pop(stack))))", 1),
    "Ḣ": ("stack.append(iterable(pop(stack))[1:])", 1),
    "İ": (
        "indexes, vector = pop(stack, 2); stack.append(indexed_into(vector, indexes))",
        2,
    ),
    "Ŀ": (
        "new, original, value = pop(stack, 3)\nif Function in map(type, (new, original, value)): stack.append(repeat_no_collect(value, original, new))\nelse: stack.append(transliterate(iterable(original, str), iterable(new, str), iterable(value, str)))",
        3,
    ),
    "Ṁ": (
        "item, index, vector = pop(stack, 3);\nif Function in map(type, (item, index, vector)): stack.append(map_every_n(vector, item, index))\nelse: stack.append(inserted(vector, item, index))",
        3,
    ),
    "Ṅ": (
        "top = pop(stack);\nif VY_type(top) == Number:stack.append(Generator(partition(top)))\nelse: stack.append(' '.join([VY_str(x) for x in top]))",
        1,
    ),  # ---------------------------
    "Ȯ": (
        "if len(stack) >= 2: stack.append(stack[-2])\nelse: stack.append(get_input(0))",
        0,
    ),
    "Ṗ": ("stack.append(Generator(permutations(iterable(pop(stack)))))", 1),
    "Ṙ": ("stack.append(reverse(pop(stack)))", 1),
    "Ṡ": ("stack = [summate(stack)]", 0),
    "Ṫ": ("stack.append(iterable(pop(stack), str)[:-1])", 1),
    "Ẇ": ("rhs, lhs = pop(stack, 2); stack.append(split(lhs, rhs, True))", 2),
    "Ẋ": ("rhs, lhs = pop(stack, 2); stack.append(cartesian_product(lhs, rhs))", 2),
    "Ẏ": (
        "index, vector = pop(stack, 2); stack.append(one_argument_tail_index(vector, index, 0))",
        2,
    ),
    "Ż": (
        "index, vector = pop(stack, 2); stack.append(one_argument_tail_index(vector, index, 1))",
        2,
    ),
    "⁰": ("stack.append(input_values[0][0][-1])", 0),
    "¹": ("stack.append(input_values[0][0][-2])", 0),
    "²": ("x = pop(stack); stack.append(square(x))", 1),
    "∇": (
        "c, b, a = pop(stack, 3); stack.append(c); stack.append(a); stack.append(b)",
        3,
    ),
    "⌈": ("stack.append(ceiling(pop(stack)))", 1),
    "⌊": ("stack.append(floor(pop(stack)))", 1),
    "¯": ("stack.append(deltas(pop(stack)))", 1),
    "±": ("stack.append(sign_of(pop(stack)))", 1),
    "₴": ("VY_print(pop(stack), end='')", 1),
    "…": ("top = pop(stack); stack.append(top); VY_print(top)", 0),
    "□": (
        "if inputs: stack.append(inputs)\nelse:\n    s, x = [], input()\n    while x:\n        s.append(Vy_eval(x)); x = input()",
        0,
    ),
    "↳": ("rhs, lhs = pop(stack, 2); stack.append(rshift(lhs, rhs))", 2),
    "↲": ("rhs, lhs = pop(stack, 2); stack.append(lshift(lhs, rhs))", 2),
    "⋏": ("rhs, lhs = pop(stack, 2); stack.append(bit_and(lhs, rhs))", 2),
    "⋎": ("rhs, lhs = pop(stack, 2); stack.append(bit_or(lhs, rhs))", 2),
    "꘍": ("rhs, lhs = pop(stack, 2); stack.append(bit_xor(lhs, rhs))", 2),
    "ꜝ": ("stack.append(bit_not(pop(stack)))", 1),
    "℅": ("stack.append(random.choice(iterable(pop(stack))))", 1),
    "≤": (
        "rhs, lhs = pop(stack, 2); stack.append(compare(lhs, rhs, Comparitors.LESS_THAN_EQUALS))",
        2,
    ),
    "≥": (
        "rhs, lhs = pop(stack, 2); stack.append(compare(lhs, rhs, Comparitors.GREATER_THAN_EQUALS))",
        2,
    ),
    "≠": ("rhs, lhs = pop(stack, 2); stack.append(int(deref(lhs) != deref(rhs)))", 2),
    "⁼": ("rhs, lhs = pop(stack, 2); stack.append(int(deref(lhs) == deref(rhs)))", 2),
    "ƒ": ("stack.append(fractionify(pop(stack)))", 1),
    "ɖ": ("stack.append(decimalify(pop(stack)))", 1),
    "×": ("stack.append('*')", 0),
    "∪": ("rhs, lhs = pop(stack, 2); stack.append(set_union(lhs, rhs))", 2),
    "∩": ("rhs, lhs = pop(stack, 2); stack.append(set_intersection(lhs, rhs))", 2),
    "⊍": ("rhs, lhs = pop(stack, 2); stack.append(set_caret(lhs, rhs))", 2),
    "£": ("register = pop(stack)", 1),
    "¥": ("stack.append(register)", 0),
    "⇧": ("stack.append(graded(pop(stack)))", 1),
    "⇩": ("stack.append(graded_down(pop(stack)))", 1),
    "Ǎ": ("stack.append(two_power(pop(stack)))", 1),
    "ǎ": ("stack.append(nth_prime(pop(stack)))", 1),
    "Ǐ": ("stack.append(prime_factors(pop(stack)))", 1),
    "ǐ": ("stack.append(all_prime_factors(pop(stack)))", 1),
    "Ǒ": ("rhs, lhs = pop(stack, 2); stack.append(order(lhs, rhs))", 2),
    "ǒ": ("stack.append(is_empty(pop(stack)))", 1),
    "Ǔ": (
        "rhs, lhs = pop(stack, 2); stack += overloaded_iterable_shift(lhs, rhs, ShiftDirections.LEFT)",
        2,
    ),
    "ǔ": (
        "rhs, lhs = pop(stack, 2); stack += overloaded_iterable_shift(lhs, rhs, ShiftDirections.RIGHT)",
        2,
    ),
    "¢": (
        "replacement, needle, haystack = pop(stack, 3); stack.append(infinite_replace(haystack, needle, replacement))",
        3,
    ),
    "↵": ("stack.append(split_newlines_or_pow_10(pop(stack)))", 1),
    "⅛": ("global_stack.append(pop(stack))", 1),
    "¼": ("stack.append(pop(global_stack))", 0),
    "¾": ("stack.append(deref(global_stack))", 0),
    "Π": ("stack.append(product(iterable(pop(stack))))", 1),
    "„": ("stack = iterable_shift(stack, ShiftDirections.LEFT)", 0),
    "‟": ("stack = iterable_shift(stack, ShiftDirections.RIGHT)", 0),
    "∆S": ("arg = pop(stack); stack.append(vectorise(math.asin, arg))", 1),
    "∆C": ("arg = pop(stack); stack.append(vectorise(math.acos, arg))", 1),
    "∆T": ("arg = pop(stack); stack.append(math.atan(arg))", 1),
    "∆q": (
        "coeff_a, coeff_b = pop(stack, 2); stack.append(polynomial([coeff_a, coeff_b, 0]))",
        2,
    ),
    "∆Q": (
        "coeff_b, coeff_c = pop(stack, 2); stack.append(polynomial([1, coeff_b, coeff_c]))",
        2,
    ),
    "∆P": ("coeff = iterable(pop(stack)); stack.append(polynomial(coeff));", 1),
    "∆s": ("arg = pop(stack); stack.append(vectorise(math.sin, arg))", 1),
    "∆c": ("arg = pop(stack); stack.append(vectorise(math.cos, arg))", 1),
    "∆t": ("arg = pop(stack); stack.append(vectorise(math.tan, arg))", 1),
    "∆ƈ": (
        "rhs, lhs = pop(stack, 2); stack.append(divide(factorial(lhs), factorial(subtract(lhs, rhs))))",
        2,
    ),
    "∆±": (
        "rhs, lhs = pop(stack, 2); stack.append(vectorise(math.copysign, lhs, rhs))",
        2,
    ),
    "∆K": (
        "arg = pop(stack); stack.append(summate(join(0, divisors_of(arg)[:-1])))",
        1,
    ),
    "∆²": ("arg = pop(stack); stack.append(is_square(arg))", 1),
    "∆e": ("arg = pop(stack); stack.append(vectorise(math.exp, arg))", 1),
    "∆E": ("arg = pop(stack); stack.append(vectorise(math.expm1, arg))", 1),
    "∆L": ("arg = pop(stack); stack.append(vectorise(math.log, arg))", 1),
    "∆l": ("arg = pop(stack); stack.append(vectorise(math.log2, arg))", 1),
    "∆τ": ("arg = pop(stack); stack.append(vectorise(math.log10, arg))", 1),
    "∆d": ("rhs, lhs = pop(stack, 2); stack.append(distance_between(lhs, rhs))", 2),
    "∆D": ("arg = pop(stack); stack.append(vectorise(math.degrees, arg))", 1),
    "∆R": ("arg = pop(stack); stack.append(vectorise(math.radians, arg))", 1),
    "∆≤": (
        "arg = pop(stack); stack.append(compare(VY_abs(arg), 1, Comparitors.LESS_THAN_EQUALS))",
        1,
    ),
    "∆Ṗ": ("stack.append(next_prime(pop(stack)))", 1),
    "∆ṗ": ("stack.append(prev_prime(pop(stack)))", 1),
    "∆p": ("stack.append(closest_prime(pop(stack)))", 1),
    "∆ṙ": (
        "stack.append(unsympy(sympy.prod(map(sympy.poly('x').__sub__, iterable(pop(stack)))).all_coeffs()[::-1]))",
        1,
    ),
    "∆Ṙ": ("stack.append(random.random())", 0),
    "∆W": (
        "rhs, lhs = pop(stack, 2); stack.append(vectorise(round, lhs, rhs))",
        2,
    ),  # if you think I'm making this work with strings, then you can go commit utter go awayance. smh.
    "∆Ŀ": (
        "rhs, lhs = pop(stack, 2); stack.append(vectorise(lambda x, y: int(numpy.lcm(x, y)), lhs, rhs))",
        2,
    ),
    "øo": (
        "needle, haystack = pop(stack, 2); stack.append(infinite_replace(haystack, needle, ''))",
        2,
    ),
    "øV": (
        "replacement, needle, haystack = pop(stack, 3); stack.append(infinite_replace(haystack, needle, replacement))",
        3,
    ),
    "øc": (
        "value = pop(stack); stack.append('«' + utilities.from_ten(utilities.to_ten(value, utilities.base27alphabet), encoding.codepage_string_compress) + '«')",
        1,
    ),
    "øC": (
        "number = pop(stack); stack.append('»' + utilities.from_ten(number, encoding.codepage_number_compress) + '»')",
        1,
    ),
    "øĊ": ("stack.append(centre(pop(stack)))", 1),
    "øm": ("stack.append(palindromise(iterable(pop(stack))))", 1),
    "øe": ("stack.append(run_length_encode(iterable(pop(stack), str)))", 1),
    "ød": ("stack.append(run_length_decode(pop(stack)))", 1),
    "øD": ("stack.append(dictionary_compress(pop(stack)))", 1),
    "øW": ("stack.append(split_on_words(VY_str(pop(stack))))", 1),
    "øṙ": (
        "replacent, pattern, source = pop(stack, 3); stack.append(regex_replace(VY_str(source), VY_str(pattern), replacent))",
        3,
    ),
    "øp": (
        "rhs, lhs = pop(stack, 2); stack.append(int(str(lhs).startswith(str(rhs))))",
        2,
    ),
    "øP": ("rhs, lhs = pop(stack, 2); stack.append(pluralise(lhs, rhs))", 2),
    "øṁ": ("stack.append(vertical_mirror(pop(stack)))", 1),
    "øṀ": (
        "stack.append(vertical_mirror(pop(stack), ['()[]{}<>/\\\\', ')(][}{><\\\\/']))",
        1,
    ),
    "ø¦": ("rhs, lhs = pop(stack, 2); stack.append(vertical_mirror(lhs, rhs))", 2),
    "Þ…": ("value, vector = pop(stack, 2); stack.append(distribute(vector, value))", 2),
    "Þ↓": (
        "fn, vector = pop(stack, 2); stack.append(min(VY_zipmap(fn, vector), key=lambda x: x[-1])[0])",
        2,
    ),
    "Þ↑": (
        "fn, vector = pop(stack, 2); stack.append(max(VY_zipmap(fn, vector), key=lambda x: x[-1])[0])",
        2,
    ),
    "Þ×": ("vector = pop(stack); stack.append(all_combinations(vector));", 1),
    "ÞF": ("stack.append(Generator(fibonacci(), is_numeric_sequence=True))", 0),
    "Þ!": ("stack.append(Generator(factorials(), is_numeric_sequence=True))", 0),
    "ÞU": ("stack.append(nub_sieve(iterable(pop(stack))))", 1),
    "ÞT": ("stack.append(transpose(pop(stack)))", 1),
    "ÞD": ("stack.append(Generator(diagonals(iterable(pop(stack), list))))", 1),
    "ÞS": ("stack.append(Generator(sublists(iterable(pop(stack), list))))", 1),
    "ÞṪ": (
        "rhs, lhs = pop(stack, 2); print(lhs, rhs) ;stack.append(Generator(itertools.zip_longest(*iterable(lhs), fillvalue=rhs)))",
        2,
    ),
    "Þ℅": ("top = iterable(pop(stack)); stack.append(random.sample(top, len(top)))", 1),
    "Þ•": (
        "rhs, lhs = pop(stack, 2); stack.append(dot_product(iterable(lhs), iterable(rhs)))",
        2,
    ),
    "ÞṀ": (
        "rhs, lhs = pop(stack, 2); stack.append(matrix_multiply(iterable(lhs), iterable(rhs)))",
        2,
    ),
    "ÞḊ": ("stack.append(determinant(pop(stack)))", 1),
    "Þ/": ("stack.append(diagonal_main(deref(pop(stack))))", 1),
    "Þ\\": ("stack.append(diagonal_anti(deref(pop(stack))))", 1),
    "ÞR": (
        "fn, vector = pop(stack, 2); stack.append(foldl_rows(fn, deref(vector)))",
        2,
    ),
    "ÞC": (
        "fn, vector = pop(stack, 2); stack.append(foldl_cols(fn, deref(vector)))",
        2,
    ),
    "¨U": ("if not online_version: stack.append(request(pop(stack)))", 1),
    "¨M": (
        "function, indexes, original = pop(stack, 3); stack.append(map_at(function, iterable(original), iterable(indexes)))",
        3,
    ),
    "¨,": ("VY_print(pop(stack), end=' ')", 1),
    "¨…": ("top = pop(stack); stack.append(top); VY_print(top, end=' ')", 1),
    "¨t": ("vectorise(time.sleep, pop(stack))", 1),
    "kA": ("stack.append(string.ascii_uppercase)", 0),
    "ke": ("stack.append(math.e)", 0),
    "kf": ("stack.append('Fizz')", 0),
    "kb": ("stack.append('Buzz')", 0),
    "kF": ("stack.append('FizzBuzz')", 0),
    "kH": ("stack.append('Hello, World!')", 0),
    "kh": ("stack.append('Hello World')", 0),
    "k1": ("stack.append(1000)", 0),
    "k2": ("stack.append(10000)", 0),
    "k3": ("stack.append(100000)", 0),
    "k4": ("stack.append(1000000)", 0),
    "k5": ("stack.append(10000000)", 0),
    "ka": ("stack.append(string.ascii_lowercase)", 0),
    "kL": ("stack.append(string.ascii_letters)", 0),
    "kd": ("stack.append(string.digits)", 0),
    "k6": ("stack.append('0123456789abcdef')", 0),
    "k^": ("stack.append('0123456789ABCDEF')", 0),
    "ko": ("stack.append(string.octdigits)", 0),
    "kp": ("stack.append(string.punctuation)", 0),
    "kP": ("stack.append(string.printable)", 0),
    "kw": ("stack.append(string.whitespace)", 0),
    "kr": ("stack.append(string.digits + string.ascii_letters)", 0),
    "kB": ("stack.append(string.ascii_uppercase + string.ascii_lowercase)", 0),
    "kZ": ("stack.append(string.ascii_uppercase[::-1])", 0),
    "kz": ("stack.append(string.ascii_lowercase[::-1])", 0),
    "kl": ("stack.append(string.ascii_letters[::-1])", 0),
    "ki": ("stack.append(math.pi)", 0),
    "kn": ("stack.append(math.nan)", 0),
    "kt": ("stack.append(math.tau)", 0),
    "kD": ("stack.append(date.today().isoformat())", 0),
    "kN": ("stack.append([dt.now().hour, dt.now().minute, dt.now().second])", 0),
    "kḋ": ("stack.append(date.today().strftime('%d/%m/%Y'))", 0),
    "kḊ": ("stack.append(date.today().strftime('%m/%d/%y'))", 0),
    "kð": (
        "stack.append([date.today().day, date.today().month, date.today().year])",
        0,
    ),
    "kβ": ("stack.append('{}[]<>()')", 0),
    "kḂ": ("stack.append('()[]{}')", 0),
    "kß": ("stack.append('()[]')", 0),
    "kḃ": ("stack.append('([{')", 0),
    "k≥": ("stack.append(')]}')", 0),
    "k≤": ("stack.append('([{<')", 0),
    "kΠ": ("stack.append(')]}>')", 0),
    "kv": ("stack.append('aeiou')", 0),
    "kV": ("stack.append('AEIOU')", 0),
    "k∨": ("stack.append('aeiouAEIOU')", 0),
    "k⟇": ("stack.append(commands.codepage)", 0),
    "k½": ("stack.append([1, 2])", 0),
    "kḭ": ("stack.append(2 ** 32)", 0),
    "k+": ("stack.append([1, -1])", 0),
    "k-": ("stack.append([-1, 1])", 0),
    "k≈": ("stack.append([0, 1])", 0),
    "k/": ("stack.append('/\\\\')", 0),
    "kR": ("stack.append(360)", 0),
    "kW": ("stack.append('https://')", 0),
    "k℅": ("stack.append('http://')", 0),
    "k↳": ("stack.append('https://www.')", 0),
    "k²": ("stack.append('http://www.')", 0),
    "k¶": ("stack.append(512)", 0),
    "k⁋": ("stack.append(1024)", 0),
    "k¦": ("stack.append(2048)", 0),
    "kṄ": ("stack.append(4096)", 0),
    "kṅ": ("stack.append(8192)", 0),
    "k¡": ("stack.append(16384)", 0),
    "kε": ("stack.append(32768)", 0),
    "k₴": ("stack.append(65536)", 0),
    "k×": ("stack.append(2147483648)", 0),
    "k⁰": ("stack.append('bcfghjklmnpqrstvwxyz')", 0),
    "k¹": ("stack.append('bcfghjklmnpqrstvwxz')", 0),
    "k•": ("stack.append(['qwertyuiop', 'asdfghjkl', 'zxcvbnm'])", 0),
    "kṠ": ("stack.append(dt.now().second)", 0),
    "kṀ": ("stack.append(dt.now().minute)", 0),
    "kḢ": ("stack.append(dt.now().hour)", 0),
    "kτ": ("stack.append(int(dt.now().strftime('%j')))", 0),
    "kṡ": ("stack.append(time.time())", 0),
    "k□": ("stack.append([[0,1],[1,0],[0,-1],[-1,0]])", 0),
    "k…": ("stack.append([[0,1],[1,0]])", 0),
    "kɽ": ("stack.append([-1,0,1])", 0),
    "k[": ("stack.append('[]')", 0),
    "k]": ("stack.append('][')", 0),
    "k(": ("stack.append('()')", 0),
    "k)": ("stack.append(')(')", 0),
    "k{": ("stack.append('{}')", 0),
    "k}": ("stack.append('}{')", 0),
    "k/": ("stack.append('/\\\\')", 0),
    "k\\": ("stack.append('\\\\/')", 0),
    "k<": ("stack.append('<>')", 0),
    "k>": ("stack.append('><')", 0),
    "kẇ": ("stack.append(dt.now().weekday())", 0),
    "kẆ": ("stack.append(dt.now().isoweekday())", 0),
    "k§": (
        "stack.append(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])",
        0,
    ),
    "kɖ": (
        "stack.append(['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])",
        0,
    ),
    "kṁ": ("stack.append([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)]", 0),
}

transformers = {
    "⁽": "stack.append(function_A)",
    "v": "stack.append(transformer_vectorise(function_A, stack))",
    "&": "apply_to_register(function_A, stack)",
    "~": "dont_pop(function_A, stack)",
    "ß": "cond = pop(stack)\nif cond: stack += function_call(function_A, stack)",
    "₌": "para_apply(function_A, function_B, stack)",
    "₍": "para_apply(function_A, function_B, stack); rhs, lhs = pop(stack, 2); stack.append([lhs, rhs])",
}
