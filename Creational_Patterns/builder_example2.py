class SQLBuilder:
    def __init__(self):
        self._select = []
        self._where = []
        self._order_by = None
        self._limit = None

    def select(self, *columns):
        self._select.extend(columns)
        return self

    def where(self, condition):
        self._where.append(condition)
        return self

    def order_by(self, column):
        self._order_by = column
        return self

    def limit(self, n):
        self._limit = n
        return self

    def build(self):
        query = "SELECT " + ", ".join(self._select) + " FROM users"

        if self._where:
            query += " WHERE " + " AND ".join(self._where)

        if self._order_by:
            query += " ORDER BY " + self._order_by

        if self._limit is not None:
            query += f" LIMIT {self._limit}"

        return query + ";"


if __name__=="__main__":
    query = (
        SQLBuilder()
        .select("id", "name")
        .where("age > 30")
        .order_by("created_at")
        .limit(10)
        .build()
    )
    print(query)