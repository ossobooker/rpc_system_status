# from typing import Optional
from typing import List
from fastapi import APIRouter, Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from models import Chamber

chambers_router = APIRouter()

# List all chamebr
@chambers_router.get(
    "/", response_model=List[Chamber], response_description="List all chambers"
)
async def get_chambers(request: Request):
    chambers = []
    for chamber in await request.app.mongodb["chambers"].find().to_list(3000):
        chambers.append(chamber)
    return chambers


# Get a single chamber
@chambers_router.get(
    "/{chamber_name}",
    response_model=Chamber,
    response_description="Get a single chamber",
)
async def get_chamber(request: Request, chamber_name: str):
    if (
        chamber := await request.app.mongodb["chambers"].find_one(
            {"name": chamber_name}
        )
    ) is not None:
        return chamber

    raise HTTPException(status_code=404, detail=f"Chamber {chamber_name} not found.")


# Add a chamber
@chambers_router.post(
    "/",
    response_model=Chamber,
    response_description="Add a single chamber",
)
async def add_chamber(
    chamber: Chamber,
    request: Request,
):
    print(chamber)
    chamber = jsonable_encoder(chamber)
    new_chamber = await request.app.mongodb["chambers"].insert_one(chamber)
    created_chamber = await request.app.mongodb["chambers"].find_one(
        {"_id": new_chamber.inserted_id}
    )
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_chamber)


@chambers_router.delete(
    "/delete/{chamber_name}",
    response_model=Chamber,
    response_description="Delete a chamber",
)
async def delete_chamber(request: Request, chamber_name: str):
    delete_result = await request.app.mongodb["chambers"].delete_one(
        {"name": chamber_name}
    )

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Chamber {chamber_name} not found.")


@chambers_router.put(
    "/update/{chamber_name}",
    response_model=Chamber,
    response_description="Update chamber",
)
async def update_chamber(chamber_name: str, request: Request, chamber: Chamber):
    chamber = jsonable_encoder(chamber)
    del chamber["_id"]
    update_result = await request.app.mongodb["chambers"].update_one(
        {"name": chamber_name}, {"$set": chamber}
    )
    if update_result.modified_count == 1:
        if (
            updated_chamber := await request.app.mongodb["chambers"].find_one(
                {"name": chamber_name}
            )
        ) is not None:
            return updated_chamber

    raise HTTPException(status_code=404, detail=f"Chamber {chamber_name} not found.")
