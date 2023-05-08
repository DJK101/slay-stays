# called when mutmut starts
def init():
    pass


# called before each mutation is applied and tested
def pre_mutation(context):
    context.config.test_command = 'python -m mutmut'

    # to run mutmut type this command in the terminal: python -m mutmut run --paths-to-mutate tests
    # make sure the file you mutate is committed before you apply mutmut
