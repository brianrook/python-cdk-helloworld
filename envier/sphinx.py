import sys

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import Parser
from docutils.utils import new_document


def asbool(argument):
    return argument.lower() in {"yes", "true", "t", "1", "y", "on"}


RST_PARSER = Parser()


class Envier(Directive):
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        "heading": asbool,
        "recursive": asbool,
    }

    def _parse(self, cell):
        doc = new_document("", self.state.document.settings)
        RST_PARSER.parse(cell, doc)
        return doc.children

    def _create_row(self, cells, add_id=True):
        row = nodes.row()

        if add_id:
            _id = cells[0].strip("``").rstrip("``").lower().replace("_", "-")

            target = nodes.target()
            self.state.add_target(_id, "", target, self.state_machine.abs_line_number())
            row["ids"] += [_id]

        for cell in cells:
            entry = nodes.entry()
            entry += self._parse(cell)
            row += entry
        return row

    def run(self):
        module_name, _, config_class = self.arguments[0].partition(":")
        __import__(module_name)
        module = sys.modules[module_name]

        config_spec = None
        for part in config_class.split("."):
            config_spec = getattr(module, part)
        if config_spec is None:
            raise ValueError(
                "Could not find configuration spec class {} from {}".format(
                    config_class, module_name
                )
            )

        has_header = self.options.get("heading", True)
        recursive = self.options.get("recursive", False)

        table = nodes.table()
        table["classes"] += ["colwidths-given"]

        # Column specs
        tgroup = nodes.tgroup(cols=4)
        table += tgroup
        for col_width in (3, 1, 1, 4):  # TODO: make it configurable?
            tgroup += nodes.colspec(colwidth=col_width)

        head = ("Variable Name", "Type", "Default Value", "Description")

        # Table heading
        if has_header:
            thead = nodes.thead()
            thead += self._create_row(head, add_id=False)
            tgroup += thead

        # Table body
        tbody = nodes.tbody()
        tgroup += tbody
        for row in config_spec.help_info(recursive=recursive):
            tbody += self._create_row(row)

        return [table]


def setup(app):
    app.add_directive("envier", Envier)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }