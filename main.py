from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import link
import firestoreDB

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)


def get_response(data):
    link_id = data["link_id"]
    return {
        "ok": True,
        "link_id": link_id,
        "short_link": f"https://keskn.uz/{link_id}",
        "original_link": data["original_link"],
    }


@app.get("/link/{link_id}")
async def get_link(link_id):
    data = await firestoreDB.get_firestore_where("links", "link_id", link_id)
    if len(data) == 0:
        return {"ok": False, "message": "Link not found"}

    return get_response(data[0])


class CreateLink(BaseModel):
    link: str


@app.post("/link/create")
async def create_link(link_req: CreateLink):
    data = await firestoreDB.get_firestore_where(
        "links", "original_link", link_req.link
    )
    if len(data) > 0:
        return get_response(data[0])

    link_id_data = await link.generate_link_id()
    if not link_id_data["ok"]:
        return link_id_data

    data = await link.post_data(link_req.link, link_id_data["link_id"])
    return get_response(data)
