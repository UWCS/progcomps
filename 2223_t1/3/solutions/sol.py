from enum import IntEnum

class RuleType(IntEnum):
    POS = 1
    NEG = 2
    IGNORE = 3

class Rule:
    def __init__(self, num: int, text: str):
        self.num: int = num
        if text.startswith("ignore rule "):
            self.rt = RuleType.IGNORE
            self.text = None
            self.follow = int(text[12:])
        elif text.startswith("don't "):
            self.rt = RuleType.NEG
            self.text = text[6:]
            self.follow = -1
        else:
            self.rt = RuleType.POS
            self.text = text
            self.follow = -1
        self.prev: list[int] = []
        self.mark: bool = False
    
    def __repr__(self) -> str:
        match self.rt:
            case RuleType.POS:
                return f"(#{self.num} [POS] {self.text})"
            case RuleType.NEG:
                return f"(#{self.num} [NEG] {self.text})"
            case RuleType.IGNORE:
                return f"(#{self.num} [IGNORE] #{self.follow})"

n = int(input())
for _ in range(n):
    k = int(input())

    # Initialise rules
    rules = [
        Rule(i+1, " ".join(input().split()[1:]))
        for i in range(k)
    ]

    # Set prev values for determining ignores
    for rule in rules:
        if rule.rt == RuleType.IGNORE:
            followed = rules[rule.follow - 1]
            followed.prev.append(rule.num)
    
    # Find rules affected by ignore chains, mark for deletion
    for rule in rules:
        if rule.rt != RuleType.IGNORE and rule.prev:
            
            stack : list[tuple[Rule, bool]] = [(rule.num, True)]
            while len(stack) > 0:
                num, is_even = stack.pop()
                other_rule = rules[num-1]
                n_prev = len(other_rule.prev)
                if n_prev == 0:
                    if is_even:
                        continue
                    else:
                        rule.mark = True
                        break
                stack += [(p, not is_even) for p in other_rule.prev]

    # Delete marked and ignore nodes (including paradoxes)
    rules = [
        rule for rule in rules 
        if not rule.mark and rule.rt != RuleType.IGNORE
    ]

    # Merge rules and cancel positive/negative
    rules = sorted(rules, key=lambda x: (x.text, x.num))

    i = 0
    merged_rules : list[Rule] = []
    l = len(rules)
    while i < l:
        candidates = [rules[i]]
        has_pos = rules[i].rt == RuleType.POS
        has_neg = not has_pos
        while i < l - 1 and rules[i].text == rules[i+1].text:
            i += 1
            candidates.append(rules[i])
            is_pos = rules[i].rt == RuleType.POS
            has_pos = has_pos or is_pos
            has_neg = has_neg or not is_pos
        if not (has_pos and has_neg):
            merged_rules.append(min(candidates, key=lambda x: x.num))
        i += 1

    # Get the rule numbers as output    
    nums = [str(rule.num) for rule in merged_rules]
    print(" ".join(nums)) if len(nums) > 0 else print("No Rules")
