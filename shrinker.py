from fastapi import FastAPI
from pydantic import BaseModel
import link
import firestoreDB

app = FastAPI()


class LinkRequest(BaseModel):
    link: str


class LinkIDRequest(BaseModel):
    link_id: str


def get_response(data):
    link_id = data["link_id"]
    return {
        "link_id": link_id,
        "short_link": f"aj-linkshrink.web.app/l/{link_id}",
        "original_link": data["original_link"],
    }


@app.get("/api/get/link")
async def get_data_by_short_link(link_id_req: LinkIDRequest):
    data = (
        await firestoreDB.get_firestore_where("links", "link_id", link_id_req.link_id)
    )[0]

    return get_response(data)


@app.post("/api/post/link")
async def post_data_by_long_link(link_req: LinkRequest):
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
