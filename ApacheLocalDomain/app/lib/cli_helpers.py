import click


class RequiredIF(click.Option):
    def __init__(self, *args, **kwargs):
        self.required_if = kwargs.pop('required_if')
        assert self.required_if, "'required_if' parameter required"
        kwargs['help'] = (kwargs.get('help', '') +
                          ' {} [required with {}]'.format(self.help if hasattr(self, 'help') else '', self.required_if)
                          ).strip()
        super(RequiredIF, self).__init__(*args, **kwargs)

    def handle_parse_result(self, ctx, opts, args):
        we_are_present = self.name in opts
        other_present = self.required_if in opts

        if other_present:
            if not we_are_present:
                raise click.UsageError(
                    "Illegal usage: `%s` requires for `%s`" % (
                        self.name, self.required_if))
            else:
                self.prompt = None
        return super(RequiredIF, self).handle_parse_result(
            ctx, opts, args)
