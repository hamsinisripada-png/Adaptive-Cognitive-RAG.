from typing import Any

type JSONScalar = str | int | float | bool | None
type JSONDict = dict[str, Any]
type JSONList = list[Any]
type JSONValue = JSONScalar | JSONDict | JSONList
