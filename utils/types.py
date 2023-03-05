class Generator:
    def __init__(self):
        if __name__ == "__main__":
            print("Generator activate")

    @staticmethod
    def generate(type, auto_increment, not_null, default):
        if auto_increment:
            auto_increment = " PRIMARY KEY AUTOINCREMENT"
        else:
            auto_increment = ""
        if default is not None:
            if type == "TEXT":
                default = f" DEFAULT ('{default}')"
            else:
                default = f" DEFAULT ({default})"
        else:
            default = ""
        if not_null:
            not_null = " NOT NULL"
        else:
            not_null = ""
        return f"{type}{not_null}{auto_increment}{default}"


class Types:
    def __init__(self):
        if __name__ == "__main__":
            print("Types activate")

    @staticmethod
    def integer_field(auto_increment: bool = False, not_null: bool = False, default: object = None) -> str:
        g = Generator()
        return g.generate(type="INTEGER", auto_increment=auto_increment, not_null=not_null, default=default)

    @staticmethod
    def text_field(not_null: bool = False, default=None) -> str:
        g = Generator()
        return g.generate(type="TEXT", auto_increment=False, not_null=not_null, default=default)
