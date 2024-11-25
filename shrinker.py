from fastapi import FastAPI
from pydantic import BaseModel
import link
import firestoreDB

app = FastAPI()


class LinkRequest(BaseModel):
    link: str


@app.get("/api/get/link")
async def get_data_by_short_link(link_req: LinkRequest):
    data = await firestoreDB.get_firestore_where("links", "short_link", link_req.link)
    return data


@app.post("/api/post/link")
async def post_data_by_long_link(link_req: LinkRequest):
    data = await firestoreDB.get_firestore_where("links", "long_link", link_req.link)
    if len(data) > 0:
        return data[0]

    short_link_data = await link.generate_short_link()
    if not short_link_data["ok"]:
        return short_link_data

    res = await link.post_data(link_req.link, short_link_data["short_link"])
    return res
