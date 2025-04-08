class Config:
    MUTATORS = [
        'colon_mutator.ColonMutator',
        'bracket_mutator.BracketMutator',
        'indent_mutator.IndentMutator',
        'quote_mutator.QuoteMutator',
        'comparison_mutator.ComparisonMutator',
        'decorator_mutator.DecoratorMutator',
        # 添加其他变异器...
    ]
    ERROR_RATES = {
        'colon': 0.3,
        'bracket': 0.2,
        'indent': 0.15,
        'quote': 0.1,
        'comparison': 0.25,
        'decorator': 0.1
    }