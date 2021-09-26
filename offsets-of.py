import gdb

class Offsets(gdb.Command):
    def __init__(self):
        super (Offsets, self).__init__ ('offsets-of', gdb.COMMAND_DATA)

    def show_struct_fields(self, struct, prefix):
        for field in struct.fields():
            self.show_field(field, prefix)

    def show_struct_field(self, field, prefix):
        print '%s[0x%x] %s {' % (prefix, field.bitpos//8, field.type)
        self.show_struct_fields(field.type, prefix + '  ')
        print '%s} %s' % (prefix, field.name)

    def show_field(self, field, prefix):
        if (str(field.type).startswith('struct')) :
            self.show_struct_field(field, prefix)
        elif hasattr(field, 'bitpos'):
            print prefix + '[0x%x] %s %s' % (field.bitpos//8, field.type, field.name)

    def invoke(self, arg, from_tty):
        argv = gdb.string_to_argv(arg)
        if len(argv) != 1:
            raise gdb.GdbError('offsets-of takes exactly 1 argument.')

        stype = gdb.lookup_type(argv[0])

        print '%s {' % stype
        self.show_struct_fields(stype, '  ')
        print '}'

Offsets()
