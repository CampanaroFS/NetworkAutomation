from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from rich import print
import json

app = FastAPI()


class Interface(BaseModel):
    id: str = Field(..., title="The ID of the interface")
    name: str
    description: str
    ip_address: str
    subnet_mask: str
    enabled: bool
    speed: str


@app.get("/")
def read_root():
    return {"Network": "Automation World"}


@app.get("/interfaces")
def read_item():
    with open("interfaces.json", "r") as file:
        interfaces = json.load(file)
    return interfaces


@app.get("/interfaces/{int_id}")
def read_item(int_id: str):
    with open("interfaces.json", "r") as file:
        interfaces = json.load(file)
    for interface in interfaces:
        if interface.get('id') == int_id:
            return interface
    return {"error": "Interface not found"}


@app.post("/interfaces/post")
def create_item(interface: Interface):
    with open("interfaces.json", "r") as file:
        interfaces = json.load(file)

    interfaces.append(interface.model_dump())

    with open("interfaces.json", "w") as file:
        json.dump(interfaces, file, indent=4)

    return interface


@app.put("/interfaces/{int_id}")  # TODO by Felipe
def replace_item(int_id: str, interface: Interface):
    with open("interfaces.json", "r") as file:
        interfaces = json.load(file)

    for i, inter in enumerate(interfaces):
        if inter["id"] == int_id:
            interfaces[i] = interface
            break

    with open("interfaces.json", "w") as file:
        json.dump(interfaces, file)
    
    return {"message": "Interface replaced successfully"}


@app.delete("/interfaces/{int_id}")
def delete_item(int_id: str):
    with open("interfaces.json", "r") as file:
        interfaces = json.load(file)

    for interface in interfaces:
        if interface.get('id') == int_id:
            interfaces.remove(interface)
            with open("interfaces.json", "w") as file:
                json.dump(interfaces, file, indent=4)
            return {"message": "Interface deleted"}

    raise HTTPException(status_code=404, detail="Interface not found")
