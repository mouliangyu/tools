import gdb

class Offsets(gdb.Command):
    def __init__(self):
        super (Offsets, self).__init__ ('offsets-of', gdb.COMMAND_DATA)

    def invoke(self, arg, from_tty):
        argv = gdb.string_to_argv(arg)
        if len(argv) != 1:
            raise gdb.GdbError('offsets-of takes exactly 1 argument.')

        stype = gdb.lookup_type(argv[0])

        print argv[0], '{'
        for field in stype.fields():
            if hasattr(field, 'bitpos'):
                print '    [0x%x] %s (%s)' % (field.bitpos//8, field.name, field.type)
        print '}'

Offsets()
