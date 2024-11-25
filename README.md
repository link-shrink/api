# AJ-Linkshrink

AJ-Linkshrink makes your URL simpler.

## Overview

AJ-Linkshrink is a simple URL shortening API that allows you to convert long URLs into shorter, more manageable links. It uses FastAPI for the backend and integrates with Firebase Firestore for storage. The API is deployed on Render for reliable hosting and scalability.

## Endpoints

### `GET /api/get/link`
Fetch the data for a short link.

#### Request
- **Body**: A JSON object containing the short URL ID.
    ```json
    {
        "link_id": "link-id"
    }
    ```

#### Response
- Example response:
    ```json
    {
        "link_id": "link-id",
        "short_link": "short-link",
        "original_link": "original-link"
    }
    ```

---

### `POST /api/post/link`
Create a short link for a given long URL.

#### Request
- **Body**: A JSON object containing the long URL.
    ```json
    {
        "link": "original-link"
    }
    ```

#### Response
- Example response:
    ```json
    {
        "link_id": "link-id",
        "short_link": "short-link",
        "original_link": "original-link"
    }
    ```
