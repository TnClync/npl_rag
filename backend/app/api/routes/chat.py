from pydantic import BaseModel

class QueryRequest(BaseModel):
    question: str
    context: str | None = None


from fastapi import APIRouter

router = APIRouter(tags =["Chat Bot"])

@router.post("/ask_base_model")
def ask(req: QueryRequest):
    # answer = generate_answer(
    #     model=model,
    #     tokenizer=tokenizer,
    #     question=req.question,
    #     context=req.context
    # )

    return {
        "question": req.question
    }


@router.post("/ask_tunned_model")
def asking(req:QueryRequest):
    return {
        "question": req.question
    }