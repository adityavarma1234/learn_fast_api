from typing import Annotated
from fastapi import FastAPI, Query

import random
from pydantic import AfterValidator

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(min_length=3, max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/none_but_required")
async def read_items_none_but_required(q: Annotated[str | None, Query(min_length=3)]):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/multiple_query_parameter_values")
async def read_items_multiple_query_parameter_values(q: Annotated[list[str] | None, Query()] = None):
    query_items = {"q": q}
    return query_items

@app.get("/items/title_in_query")
async def read_items_title_in_query(q: Annotated[str | None, Query(title="Query string", description="Query string for the items to search in the database that have a good match", min_length=3)]= None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items/item_with_query_parameters_alias")
async def read_items_query_parameters_alias(q: Annotated[str | None, Query(alias="item-query")] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items/deprecated_true")
async def read_items_depreacted_true(
    q: Annotated[
        str | None,
        Query(
            alias = "item-query",
            title= "Query String",
            description="Query string for the items to search in the database",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items/hidden_query")
async def read_items_hidden_query(
    hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None,
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}


data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}

def check_valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id

@app.get("/items/custom_validation")
async def read_items_custom_validation(id: Annotated[str|None, AfterValidator(check_valid_id)] = None):
    if id:
        item = data.get(id)

    else:
        id, item = random.choice(list(data.items()))
    return {"id": id, "name": item}